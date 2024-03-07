document.addEventListener('DOMContentLoaded', function () {
    // Now safely add event listeners
   
    const getTextBtn = document.getElementById('getText');

    

    if(getTextBtn) {
        getTextBtn.addEventListener('click', function () {
            // Your code...
        });
    } else {
        console.error('getText button not found');
    }

    // Additional code for the language dropdown if applicable...
});
