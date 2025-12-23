// function updateDateTime() {
//         const now = new Date();
//         const options = {
//             weekday: 'long',
//             year: 'numeric',
//             month: 'long',
//             day: 'numeric',
//             hour: '2-digit',
//             minute: '2-digit'
//         };
//         document.getElementById("date-time").textContent = now.toLocaleDateString("en-US", options);
//     }

//     updateDateTime();

    function updateDateTime() {
        const now = new Date();

        // Format date
        const date = now.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });

        // Format time
        const time = now.toLocaleTimeString('en-US', {
            hour: '2-digit',
            minute: '2-digit'
        });

        document.getElementById("current-date").textContent = date;
        document.getElementById("current-time").textContent = time;
    }

    updateDateTime(); // run immediately

