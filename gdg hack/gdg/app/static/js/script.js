
        function toggleSidebar() {
            let sidebar = document.getElementById("sidebar");

            if (sidebar.style.left === "0px") {
                sidebar.style.left = "-220px";
            } else {
                sidebar.style.left = "0px";
            }
        }

        function toggleProfileMenu() {
            let menu = document.getElementById("profileMenu");
            menu.classList.toggle("active");
        }

        const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        let currentDate = new Date();
        let currentYear = currentDate.getFullYear();
        let currentMonth = currentDate.getMonth();

        function populateSelectors() {
            const monthSelect = document.getElementById("monthSelect");
            const yearSelect = document.getElementById("yearSelect");

            for (let i = 0; i < 12; i++) {
                let option = document.createElement("option");
                option.value = i;
                option.textContent = monthNames[i];
                if (i === currentMonth) option.selected = true;
                monthSelect.appendChild(option);
            }

            for (let i = currentYear - 5; i <= currentYear + 5; i++) {
                let option = document.createElement("option");
                option.value = i;
                option.textContent = i;
                if (i === currentYear) option.selected = true;
                yearSelect.appendChild(option);
            }
        }

        function generateCalendar(year, month) {
            const calendarDiv = document.getElementById("calendar");
            const monthTitle = document.getElementById("monthTitle");
            calendarDiv.innerHTML = "";
            monthTitle.innerText = ${monthNames[month]} ${year};

            const daysInMonth = new Date(year, month + 1, 0).getDate();
            const firstDay = new Date(year, month, 1).getDay();

            for (let i = 0; i < firstDay; i++) {
                calendarDiv.appendChild(document.createElement("div"));
            }

            for (let day = 1; day <= daysInMonth; day++) {
                let dayDiv = document.createElement("div");
                dayDiv.classList.add("day");
                dayDiv.innerText = day;
                calendarDiv.appendChild(dayDiv);
            }
        }

        populateSelectors();
        generateCalendar(currentYear, currentMonth);
    