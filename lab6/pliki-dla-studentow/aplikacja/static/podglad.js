

window.addEventListener('DOMContentLoaded', () => {
    const hash = decodeURIComponent(window.location.hash.substring(1));
    const el = document.getElementById('podglad');
    if (el) {
        el.textContent = hash;
    }
});
