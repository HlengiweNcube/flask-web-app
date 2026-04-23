document.addEventListener("DOMContentLoaded", function () {

    console.log("JavaScript loaded");

    // CONTACT FORM VALIDATION
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function (e) {

            const name = document.querySelector("#name");
            const email = document.querySelector("#email");
            const phone = document.querySelector("#phone");

            //  VALIDATION
            if (name.value.trim().length < 2) {
                alert("Name must be at least 2 characters long");
                e.preventDefault();
            }

            if (!email.value.includes("@")) {
                alert("Please enter a valid email address");
                e.preventDefault();
            }

            if (!/^[0-9]+$/.test(phone.value)) {
                alert("Phone must contain only numbers");
                e.preventDefault();
            }
        });
    }

      const links = document.querySelectorAll(".navbar nav a");

    links.forEach(link => {
        link.addEventListener("click", () => {
            link.style.opacity = "0.7";
        });
    });


});