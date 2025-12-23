// Select the form
const form = document.querySelector('.test-drive-form');

// Load saved values when the page opens
window.addEventListener('DOMContentLoaded', () => {
    if (!form) return; // if form is not found or exists

    form.fullName.value = localStorage.getItem("fullName") || "";
    form.phone.value = localStorage.getItem("phone") || "";
    form.email.value = localStorage.getItem("email") || "";
    form.vehicleModel.value = localStorage.getItem("vehicleModel") || "";
    form.notes.value = localStorage.getItem("notes") || "";
});

// Save values while the user types
if (form) {
    form.addEventListener('input', () => {
        localStorage.setItem("fullName", form.fullName.value);
        localStorage.setItem("phone", form.phone.value);
        localStorage.setItem("email", form.email.value);
        localStorage.setItem("vehicleModel", form.vehicleModel.value);
        localStorage.setItem("notes", form.notes.value);
    });
}
