document.addEventListener('DOMContentLoaded', () => {
    const roleInputs = document.querySelectorAll('input[name="role"]');
    roleInputs.forEach(input => {
        input.addEventListener('change', () => {
            console.log(`Selected Role: ${input.value}`);
        });
    });
});
function showError(errorMessage) {
    // Check if error exists
    if (errorMessage) {
        alert(errorMessage); // Display error message in a dialog box
    }
}
// function validatePassword(event) {
//     const password = document.getElementById("password").value;
//     const pattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

//     if (!pattern.test(password)) {
//         event.preventDefault(); // Prevent form submission
//         alert("Your password must be at least 8 characters long and include uppercase letters, lowercase letters, numbers, and special characters.");
//     }
// }