// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Copy to Clipboard
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        alert('Copied to clipboard!');
    });
}

// Input Character Counters
document.querySelectorAll('.stTextInput input, .stTextArea textarea').forEach(input => {
    const counter = document.createElement('div');
    counter.className = 'char-counter';
    input.parentNode.appendChild(counter);
    
    input.addEventListener('input', () => {
        counter.textContent = `${input.value.length}/${
            input.getAttribute('maxlength') || '∞'
        }`;
    });
});

// Initialize Tooltips
tippy('[data-tippy-content]', {
    placement: 'top',
    animation: 'scale',
    theme: 'light-border',
});