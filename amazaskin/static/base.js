let nav = document.getElementsByTagName("nav")[0];
const navMenu = document.getElementById("nav-menu");

navMenu.addEventListener('click', () => {
    nav.classList.toggle("expanded");
});

// collapse nav if open
window.addEventListener('scroll', () => {
    if (nav.classList.contains('expanded')) {
        const scrollThreshold = 400; // Adjust this value as needed
        if (window.scrollY > scrollThreshold) {
            nav.classList.remove('expanded');
        }
    }
});