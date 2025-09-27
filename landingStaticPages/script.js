document.addEventListener('DOMContentLoaded', function() {
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    menuBtn.addEventListener('click', function() {
        mobileMenu.classList.toggle('hidden');
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Simple form handling if needed (placeholder for Sign Up)
    const signupLink = document.querySelector('a[href="#signup"]');
    if (signupLink) {
        signupLink.addEventListener('click', function(e) {
            e.preventDefault();
            alert('Sign Up functionality would redirect to a registration form. Demo mode.');
        });
    }
});
