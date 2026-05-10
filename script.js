const revealElements = document.querySelectorAll('.reveal');
const metricElements = document.querySelectorAll('.metric');
const progressBar = document.querySelector('.scroll-progress-bar');
const navLinks = Array.from(document.querySelectorAll('.top-nav a'));
const interactiveCards = document.querySelectorAll('.interactive-card');

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.18 }
);

revealElements.forEach((el, index) => {
  el.style.transitionDelay = `${Math.min(index * 40, 260)}ms`;
  revealObserver.observe(el);
});

const animateMetric = (el) => {
  const target = Number(el.dataset.target);
  let current = 0;
  const duration = 1000;
  const tick = 20;
  const increment = Math.max(1, Math.ceil(target / (duration / tick)));

  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      el.textContent = String(target);
      clearInterval(timer);
      return;
    }
    el.textContent = String(current);
  }, tick);
};

const metricObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        animateMetric(entry.target);
        metricObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.45 }
);

metricElements.forEach((el) => metricObserver.observe(el));

const updateScrollProgress = () => {
  if (!progressBar) return;

  const scrollTop = window.scrollY;
  const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
  const progress = maxScroll > 0 ? Math.min(scrollTop / maxScroll, 1) : 0;
  progressBar.style.transform = `scaleX(${progress})`;
};

window.addEventListener('scroll', updateScrollProgress, { passive: true });
window.addEventListener('resize', updateScrollProgress);
updateScrollProgress();

const sectionById = new Map();

navLinks.forEach((link) => {
  const targetId = link.getAttribute('href')?.replace('#', '');
  if (!targetId) return;

  const section = document.getElementById(targetId);
  if (!section) return;
  sectionById.set(targetId, { section, link });

  link.addEventListener('click', (event) => {
    event.preventDefault();
    section.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

const setActiveNav = (targetId) => {
  navLinks.forEach((link) => {
    const isActive = link.getAttribute('href') === `#${targetId}`;
    link.classList.toggle('is-active', isActive);
    if (isActive) {
      link.setAttribute('aria-current', 'page');
    } else {
      link.removeAttribute('aria-current');
    }
  });
};

const sectionObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        setActiveNav(entry.target.id);
      }
    });
  },
  {
    rootMargin: '-45% 0px -45% 0px',
    threshold: 0,
  }
);

sectionById.forEach(({ section }, id) => {
  sectionObserver.observe(section);
  if (id === 'services') {
    setActiveNav(id);
  }
});

interactiveCards.forEach((card) => {
  card.addEventListener('pointermove', (event) => {
    const rect = card.getBoundingClientRect();
    const x = ((event.clientX - rect.left) / rect.width) * 100;
    const y = ((event.clientY - rect.top) / rect.height) * 100;
    card.style.setProperty('--mx', `${x}%`);
    card.style.setProperty('--my', `${y}%`);
  });
});
