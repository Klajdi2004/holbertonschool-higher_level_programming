// Function to change the header color to red

function TurnRed() {
    const header = document.querySelector('header')
    header.style.color = "#FF0000" 
};

// Call the TurnRed function when the document is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    TurnRed();
});