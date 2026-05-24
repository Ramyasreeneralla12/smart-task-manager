const socket = io();

/* SOCKET NOTIFICATIONS */

socket.on("notification", function(data){

    const notificationBox =
        document.getElementById(
            "notification-box"
        );

    notificationBox.innerHTML =
        data.message;

    notificationBox.style.display =
        "block";

    notificationBox.style.opacity =
        "1";

    setTimeout(() => {

        notificationBox.style.opacity =
            "0";

        setTimeout(() => {

            notificationBox.style.display =
                "none";

        }, 500);

    }, 3000);

});


/* AUTO HIDE FLASH MESSAGES */

window.addEventListener("load", () => {

    const flashMessages =
        document.querySelectorAll(
            ".flash-message"
        );

    flashMessages.forEach(msg => {

        setTimeout(() => {

            msg.style.opacity = "0";

            msg.style.transform =
                "translateY(-10px)";

            setTimeout(() => {

                msg.style.display = "none";

            }, 500);

        }, 2500);

    });

});


/* DATE VALIDATION */

const deadlineInput =
    document.getElementById("deadline");

if(deadlineInput){

    const today = new Date();

    const year =
        today.getFullYear();

    const month = String(
        today.getMonth() + 1
    ).padStart(2, "0");

    const day = String(
        today.getDate()
    ).padStart(2, "0");

    const minDate =
        `${year}-${month}-${day}`;

    deadlineInput.setAttribute(
        "min",
        minDate
    );
}


/* BUTTON LOADING EFFECT */

const forms =
    document.querySelectorAll("form");

forms.forEach(form => {

    form.addEventListener(
        "submit",
        () => {

            const button =
                form.querySelector(
                    "button"
                );

            if(button){

                button.innerHTML =
                    "Processing...";

            }

        }
    );

});