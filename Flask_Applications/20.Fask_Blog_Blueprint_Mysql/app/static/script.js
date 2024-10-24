document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript loaded successfully!');

    // Example: Form validation for the new post form
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', (event) => {
            const title = document.getElementById('title').value.trim();
            const content = document.getElementById('content').value.trim();

            // Simple validation to ensure title and content are not empty
            if (title === '' || content === '') {
                event.preventDefault(); // Prevent form submission
                alert('Title and content cannot be empty!'); // Alert user
            }
        });
    }
});
