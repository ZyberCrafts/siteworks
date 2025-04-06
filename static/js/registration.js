document.addEventListener('DOMContentLoaded', () => {
    const roleInputs = document.querySelectorAll('input[name="role"]');
    roleInputs.forEach(input => {
        input.addEventListener('change', () => {
            console.log(`Selected Role: ${input.value}`);
        });
    });
});