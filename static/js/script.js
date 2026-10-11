/**
 * Puja Sharma Portfolio - Interactive Script
 * Handles navigation, case study modals, scroll reveal, mobile drawer, and contact submissions.
 */

document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initScrollReveal();
    initProjectModal();
    initContactForm();
    initPlaceholders();
});

/* --------------------------------------------------------------------------
   1. Navbar & Navigation
   -------------------------------------------------------------------------- */
function initNavbar() {
    const navbar = document.getElementById('navbar');
    const mobileToggle = document.getElementById('mobileToggle');
    const mobileMenu = document.getElementById('mobileMenu');
    const navLinks = document.querySelectorAll('.desktop-nav .nav-link, .mobile-nav-link');
    const sections = document.querySelectorAll('section[id], footer[id]');

    // Sticky shadow on scroll
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        highlightActiveSection();
    }, { passive: true });

    // Mobile Hamburger Toggle
    if (mobileToggle && mobileMenu) {
        mobileToggle.addEventListener('click', () => {
            const isExpanded = mobileToggle.getAttribute('aria-expanded') === 'true';
            mobileToggle.setAttribute('aria-expanded', !isExpanded);
            mobileMenu.classList.toggle('open');
            mobileMenu.setAttribute('aria-hidden', isExpanded);
            document.body.style.overflow = isExpanded ? '' : 'hidden';
        });

        // Close mobile drawer when clicking any link
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileToggle.setAttribute('aria-expanded', 'false');
                mobileMenu.classList.remove('open');
                mobileMenu.setAttribute('aria-hidden', 'true');
                document.body.style.overflow = '';
            });
        });
    }

    // Scroll spy: Highlight active nav link
    function highlightActiveSection() {
        const scrollPosition = window.scrollY + 120;
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }
}

/* --------------------------------------------------------------------------
   2. Scroll Reveal Animations (IntersectionObserver)
   -------------------------------------------------------------------------- */
function initScrollReveal() {
    const revealElements = document.querySelectorAll('[data-reveal]');
    if (!('IntersectionObserver' in window)) {
        revealElements.forEach(el => el.classList.add('revealed'));
        return;
    }

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                obs.unobserve(entry.target);
            }
        });
    }, {
        root: null,
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach(el => observer.observe(el));
}

/* --------------------------------------------------------------------------
   3. Interactive Project Case Study Modal
   -------------------------------------------------------------------------- */
function initProjectModal() {
    const modal = document.getElementById('projectModal');
    if (!modal) return;

    const modalTitle = document.getElementById('modalTitle');
    const modalCategory = document.getElementById('modalCategory');
    const modalBadges = document.getElementById('modalBadges');
    const modalProblem = document.getElementById('modalProblem');
    const modalApproach = document.getElementById('modalApproach');
    const modalTechnologies = document.getElementById('modalTechnologies');
    const modalContribution = document.getElementById('modalContribution');
    const modalOutcome = document.getElementById('modalOutcome');
    const modalRepoType = document.getElementById('modalRepoType');
    const closeBtn = document.getElementById('modalCloseBtn');
    const closeAction = document.getElementById('modalCloseAction');

    let previousActiveElement = null;

    // Open Modal
    document.querySelectorAll('.view-case-study-btn').forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            previousActiveElement = button;
            const projectDataRaw = button.getAttribute('data-project');
            
            if (!projectDataRaw) return;

            try {
                const project = JSON.parse(projectDataRaw);
                populateModal(project);
                openModal();
            } catch (err) {
                console.error("Failed to parse project data:", err);
            }
        });
    });

    function populateModal(project) {
        modalTitle.textContent = project.title || 'Case Study';
        modalCategory.textContent = project.category || 'Engineering';
        modalRepoType.innerHTML = `<i class="fa-solid fa-shield-halved"></i> ${project.repo_type || 'Private / Demonstration'}`;

        // Technologies Pills
        modalTechnologies.innerHTML = '';
        const techList = project.case_study?.technologies || project.technologies || [];
        techList.forEach(tech => {
            const span = document.createElement('span');
            span.className = 'tech-tag';
            span.textContent = tech;
            modalTechnologies.appendChild(span);
        });

        // Badges in header
        modalBadges.innerHTML = '';
        (project.technologies || []).slice(0, 3).forEach(tech => {
            const badge = document.createElement('span');
            badge.className = 'project-category-tag';
            badge.textContent = tech;
            modalBadges.appendChild(badge);
        });

        const cs = project.case_study || {};
        modalProblem.textContent = cs.problem || 'Context and problem specifications are private to company IP.';
        modalApproach.textContent = cs.approach || 'Technical solution built using Python and modern engineering principles.';
        modalContribution.textContent = cs.contribution || 'Direct engineering implementation and validation.';
        modalOutcome.textContent = cs.outcome_learning || 'Core focus on maintainability, reliability, and precision.';
    }

    function openModal() {
        modal.classList.add('active');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        closeBtn.focus();
    }

    function closeModal() {
        modal.classList.remove('active');
        modal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        if (previousActiveElement) {
            previousActiveElement.focus();
        }
    }

    closeBtn.addEventListener('click', closeModal);
    if (closeAction) closeAction.addEventListener('click', closeModal);

    // Close when clicking outside dialog
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
}

/* --------------------------------------------------------------------------
   4. Contact Form Handling
   -------------------------------------------------------------------------- */
function initContactForm() {
    const form = document.getElementById('contactForm');
    if (!form) return;

    const submitBtn = document.getElementById('formSubmitBtn');
    const btnText = document.getElementById('btnText');
    const formStatus = document.getElementById('formStatus');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const name = form.name.value.trim();
        const email = form.email.value.trim();
        const subject = form.subject.value.trim();
        const message = form.message.value.trim();

        // Basic front-end validation
        if (!name || !email || !message) {
            showStatus('Please fill in all required fields (Name, Email, Message).', 'error');
            return;
        }

        // Email regex
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            showStatus('Please provide a valid email address.', 'error');
            return;
        }

        // Set Loading state
        submitBtn.disabled = true;
        const originalBtnHTML = btnText.innerHTML;
        btnText.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending message...';
        hideStatus();

        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({ name, email, subject, message })
            });

            const result = await response.json();

            if (response.ok && result.success) {
                showStatus(result.message || 'Thank you! Your message was sent successfully.', 'success');
                form.reset();
            } else {
                throw new Error(result.message || 'Server error while sending message.');
            }
        } catch (err) {
            console.warn('Form submission fallback:', err);
            // Graceful fallback offering mailto trigger
            const mailtoUrl = `mailto:pujasharmarps@gmail.com?subject=${encodeURIComponent(subject || 'Portfolio Inquiry')}&body=${encodeURIComponent(`Hi Puja,\n\n${message}\n\nFrom: ${name} (${email})`)}`;
            showStatus(
                `Thank you for your note! If needed, you can also launch your mail client directly: <a href="${mailtoUrl}" style="text-decoration: underline; font-weight: 700; color: inherit;">Click here to send via Email</a>`,
                'success'
            );
        } finally {
            submitBtn.disabled = false;
            btnText.innerHTML = originalBtnHTML;
        }
    });

    function showStatus(msg, type) {
        formStatus.innerHTML = msg;
        formStatus.className = `form-status ${type}`;
        formStatus.style.display = 'block';
    }

    function hideStatus() {
        formStatus.style.display = 'none';
        formStatus.textContent = '';
    }
}

/* --------------------------------------------------------------------------
   5. Graceful Placeholder Notices
   -------------------------------------------------------------------------- */
function initPlaceholders() {
    const githubPlaceholders = document.querySelectorAll('.github-placeholder');
    githubPlaceholders.forEach(el => {
        el.addEventListener('click', (e) => {
            e.preventDefault();
            alert("Puja's public GitHub link will be updated soon. In the meantime, feel free to connect via LinkedIn or email!");
        });
    });
}
