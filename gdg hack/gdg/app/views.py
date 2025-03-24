from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta
from .models import Customer, Task
from .forms import TaskForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Customer.objects.get(email=email, password=password)
            request.session["user_id"] = user.id  # Store user ID in session
            return redirect("home")  # Redirect to home page after login
        except Customer.DoesNotExist:
            return render(request, "login.html", {"error_message": "Invalid email or password!"})

    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        hint_selection = request.POST.get("hint_selection")
        hint_answer = request.POST.get("hint_answer")

        # Save user data in Customer model
        Customer.objects.create(
            name=name,
            email=email,
            password=password,
            hint_selection=hint_selection,
            hint_answer=hint_answer
        )

        return redirect("login")  # Redirect to login page after signup

    return render(request, "signup.html")

def home(request):
    if "user_id" not in request.session:
        return redirect("login")  # Redirect to login if not authenticated

    return render(request, "home.html")

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to task list after saving
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})


def reset_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        new_password = request.POST.get("new_password")

        try:
            user = Customer.objects.get(email=email)
            user.password = make_password(new_password)
            user.save()
            return redirect("login")
        except Customer.DoesNotExist:
            return render(request, "forget_page.html", {"error": "User not found!"})
    return redirect("forget_password")

def forget_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        hint_selection = request.POST.get("hint_selection")
        hint_answer = request.POST.get("hint_answer")

        try:
            user = Customer.objects.get(email=email, hint_selection=hint_selection)
        except Customer.DoesNotExist:
            messages.error(request, "No user found with this email and security question.")
            return render(request, "forget_page.html")

        if user.hint_answer.strip().lower() != hint_answer.strip().lower():
            messages.error(request, "Incorrect security answer. Please try again.")
            return render(request, "forget_page.html")

        if "verify" in request.POST:
            return render(request, "forget_page.html", {
                "show_password_fields": True,
                "email": email,
                "hint_selection": hint_selection,
                "hint_answer": hint_answer
            })

        elif "reset_password" in request.POST:
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")

            if new_password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return render(request, "forget_page.html", {
                    "show_password_fields": True,
                    "email": email,
                    "hint_selection": hint_selection,
                    "hint_answer": hint_answer
                })

            user.password = make_password(new_password)
            user.save()
            messages.success(request, "Password updated successfully! Redirecting to login...")
            return redirect("login")
    return render(request, "forget_page.html")

def help_page(request):
    return render(request, "help.html")

from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = list(Task.objects.all())
    print("Fetched tasks:", tasks)  # Debugging

    tasks = list(Task.objects.all())

    # Ensure deadlines are converted to date only (remove time component)
    for task in tasks:
        if isinstance(task.deadline, datetime):
            task.deadline = task.deadline.date()  # Convert DateTimeField to just a DateField

    # Handle None values for sorting (defaulting to safe values)
    tasks.sort(key=lambda x: (
        x.deadline if x.deadline else datetime.today().date(),  # Use today if deadline is missing
        -x.importance if x.importance is not None else 0,  # Default importance to 0
        -x.number_of_topics if x.number_of_topics is not None else 0,  # Default topics to 0
        -x.time_required if x.time_required is not None else 0  # Default time required to 0
    ))

    available_study_hours = 4  
    today = datetime.today().date()
    schedule = []

    for task in tasks:
        subject, deadline, importance, topics, time_required = (
            task.subject, task.deadline, task.importance, task.number_of_topics, task.time_required
        )
        
        # Ensure values are valid before processing
        time_required = time_required if time_required is not None else 1  # Minimum 1 hour
        days_left = max(1, (deadline - today).days)
        daily_hours = min(available_study_hours, time_required // days_left) if days_left > 0 else available_study_hours

        while time_required > 0 and today <= deadline:
            study_hours = min(daily_hours, time_required)
            schedule.append({"date": today.strftime("%Y-%m-%d"), "subject": subject, "hours": study_hours})
            time_required -= study_hours
            today += timedelta(days=1)
            
    # Ensure the schedule is sorted by date
    schedule.sort(key=lambda x: x["date"])
    print("Final schedule:", schedule)

    return render(request, "task_list.html", {"schedule": schedule})
from django.shortcuts import render

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')
