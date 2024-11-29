let nav = document.getElementsByTagName("nav")[0];
const navMenu = document.getElementById("nav-menu");

navMenu.addEventListener('click', () => {
    nav.classList.toggle("expanded");
});