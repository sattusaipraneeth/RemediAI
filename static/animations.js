// Navigation animations
document.addEventListener('DOMContentLoaded', () => {
    // Fade in content
    const content = document.querySelector('.content');
    content.style.opacity = '0';
    setTimeout(() => {
        content.style.opacity = '1';
        content.style.transition = 'opacity 0.8s ease-in-out';
    }, 100);

    // Animate navigation links
    const navLinks = document.querySelectorAll('.nav-links a');
    navLinks.forEach((link, index) => {
        link.style.opacity = '0';
        link.style.transform = 'translateY(-20px)';
        setTimeout(() => {
            link.style.opacity = '1';
            link.style.transform = 'translateY(0)';
            link.style.transition = 'all 0.5s ease-out';
        }, 200 + (index * 100));
    });

    // Card animations
    const cards = document.querySelectorAll('.service-card, .doctor-card, .about-card, .info-card');
    const animateCards = () => {
        cards.forEach(card => {
            const cardPosition = card.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.3;

            if (cardPosition < screenPosition) {
                card.classList.add('card-animate');
            }
        });
    };

    window.addEventListener('scroll', animateCards);
    animateCards();

    // Form animations
    const formGroups = document.querySelectorAll('.form-group');
    formGroups.forEach((group, index) => {
        group.style.opacity = '0';
        group.style.transform = 'translateX(-20px)';
        setTimeout(() => {
            group.style.opacity = '1';
            group.style.transform = 'translateX(0)';
            group.style.transition = 'all 0.5s ease-out';
        }, 300 + (index * 100));
    });
});