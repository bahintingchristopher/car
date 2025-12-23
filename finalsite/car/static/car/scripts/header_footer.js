// for hamburger menu
const hamburger = document.querySelector('.hamburger');
const navigation = document.querySelector('.navigation');
const cta = document.querySelector('.cta');

hamburger.addEventListener('click', () => {
    navigation.classList.toggle('show'); // show/hide nav
    hamburger.classList.toggle('show');   // toggle hamburger X icon
    cta.classList.toggle('nav-open');     // move CTA down
});

const currentYearSpan = document.getElementById("currentYear");
if (currentYearSpan) {
  currentYearSpan.textContent = new Date().getFullYear();
}
