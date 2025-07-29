document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('section');
    const houseCards = document.querySelectorAll('.house-card');
    const heroHome = document.querySelector('.hero-home');

    // Function to check if an element is in viewport
    const isInViewport = (element) => {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    };

    // Scroll-triggered animations for sections
    const handleScroll = () => {
        sections.forEach(section => {
            if (isInViewport(section) && !section.classList.contains('is-visible')) {
                section.classList.add('is-visible');
            }
        });
    };

    // Initial check on load
    handleScroll();

    // Event listener for scroll
    window.addEventListener('scroll', handleScroll);

    // Mousemove parallax effect for hero-home (optional and subtle)
    if (heroHome) {
        heroHome.addEventListener('mousemove', (e) => {
            const speed = 0.02;
            const x = (window.innerWidth - e.pageX * speed) / 100;
            const y = (window.innerHeight - e.pageY * speed) / 100;
            heroHome.style.backgroundPosition = `${x}px ${y}px`;
        });
    }

    // Add a pulsating effect to the "Learn More" button
    const learnMoreBtn = document.querySelector('.hero-home .btn');
    if (learnMoreBtn) {
        learnMoreBtn.classList.add('pulsate');
    }

    // House card hover animation: particle effect (conceptual, requires canvas/libraries for full implementation)
    // For now, we'll just enhance the existing CSS hover
    houseCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            // Can imagine creating small, transient div elements here for a "sparkle" or "dust" effect
            // e.g., createParticle(card);
        });
    });

    // Example of a simple particle creation (CSS-based for demonstration)
    function createParticle(element) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        element.appendChild(particle);

        const size = Math.random() * 5 + 2; // 2-7px
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;
        particle.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 70%)`; // Random color

        // Animate particle
        particle.animate([
            { transform: `translate(-50%, -50%) scale(1)`, opacity: 1 },
            { transform: `translate(${(Math.random() - 0.5) * 200}px, ${(Math.random() - 0.5) * 200}px) scale(0)`, opacity: 0 }
        ], {
            duration: 1000 + Math.random() * 1000,
            easing: 'ease-out',
            fill: 'forwards'
        });

        particle.onanimationend = () => particle.remove();
    }
});
