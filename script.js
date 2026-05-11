const revealElements = document.querySelectorAll('.reveal');
const metricElements = document.querySelectorAll('.metric');
const progressBar = document.querySelector('.scroll-progress-bar');
const navLinks = Array.from(document.querySelectorAll('.top-nav a'));
const interactiveCards = document.querySelectorAll('.interactive-card');
const useCaseGrid = document.querySelector('#useCaseGrid');
const filterButtons = Array.from(document.querySelectorAll('.chip[data-filter]'));

const useCases = [
  {
    title: 'Semantic Layer for Business Banking Fraud Detection',
    category: 'Fraud',
    tag: 'fraud',
    summary: 'Defines governed fraud entities, signals, prediction outputs, and metrics as a reusable semantic contract.',
    href: 'https://www.linkedin.com/posts/emily-gao-291177a_reusableaiaccelerators-enterpriseai-semanticlayer-share-7457348849179971585-s5BA',
  },
  {
    title: 'Governance Certification Gate for Enterprise AI Assets',
    category: 'Governance',
    tag: 'governance',
    summary: 'Applies deterministic validation gates for schema, policy, and SQL quality before semantic assets are promoted.',
    href: 'https://www.linkedin.com/posts/emily-gao-291177a_reusableaiaccelerators-enterpriseai-semanticlayer-share-7457348849179971585-s5BA',
  },
  {
    title: 'Analyst-in-the-Loop Controls for Fraud AI Recommendations',
    category: 'Fraud',
    tag: 'fraud',
    summary: 'Ensures human review boundaries, approved/disallowed usage, and audit-ready case handling for high-risk alerts.',
    href: 'https://www.linkedin.com/posts/emily-gao-291177a_reusableaiaccelerators-enterpriseai-semanticlayer-share-7457348849179971585-s5BA',
  },
  {
    title: 'Kafka + Lambda Trigger Layer for GenAI Invocation Control',
    category: 'GenAI Ops',
    tag: 'genai',
    summary: 'Introduces invoke/ignore/sample decisions between event streams and GenAI to increase control and reduce waste.',
    href: 'https://www.linkedin.com/posts/emily-gao-291177a_aiarchitecture-kafka-aws-share-7452644703209967616-jz0k',
  },
  {
    title: 'GenAI Cost Optimization Through Signal Filtering',
    category: 'GenAI Ops',
    tag: 'genai',
    summary: 'Routes low-value events away from premium models while preserving high-value signal coverage.',
    href: 'https://www.linkedin.com/posts/emily-gao-291177a_aiarchitecture-kafka-aws-share-7452644703209967616-jz0k',
  },
  {
    title: 'Streaming AI Decision Observability and Evaluation',
    category: 'GenAI Ops',
    tag: 'genai',
    summary: 'Captures trigger decisions, outcomes, and metrics to continuously tune policy and runtime behavior.',
    href: 'https://www.linkedin.com/posts/emily-gao-291177a_aiarchitecture-kafka-aws-share-7452644703209967616-jz0k',
  },
  {
    title: 'Fraud Semantic Contracts and Governed Signal Layer',
    category: 'Governance',
    tag: 'governance',
    summary: 'Converts fragmented fraud logic into certified semantic assets that AI systems are allowed to reason over.',
    href: 'https://www.linkedin.com/posts/emily-gao-291177a_frauddetection-agenticworkflows-semanticcontracts-share-7457590320050909184-m4We',
  },
  {
    title: 'Fraud Agentic Investigation with Human Control Boundaries',
    category: 'Fraud',
    tag: 'fraud',
    summary: 'Orchestrates investigation steps with explicit human checkpoints and auditable evidence synthesis.',
    href: 'https://www.linkedin.com/posts/emily-gao-291177a_frauddetection-agenticworkflows-semanticcontracts-share-7457590320050909184-m4We',
  },
  {
    title: 'Fraud Pattern Experimentation and Promotion Loop',
    category: 'Fraud',
    tag: 'fraud',
    summary: 'Implements a Generate-Detect-Evaluate-Compare-Register-Promote loop for adaptive fraud detection patterns.',
    href: 'https://www.linkedin.com/posts/emily-gao-291177a_frauddetection-agenticworkflows-semanticcontracts-share-7457590320050909184-m4We',
  },
];

const renderUseCases = (filter = 'all') => {
  if (!useCaseGrid) return;

  const items = useCases.filter((item) => filter === 'all' || item.tag === filter);

  useCaseGrid.innerHTML = items
    .map(
      (item) => `
      <a class="use-case-card interactive-card reveal is-visible" href="${item.href}" target="_blank" rel="noopener noreferrer">
        <p class="use-case-category">${item.category}</p>
        <h3>${item.title}</h3>
        <p>${item.summary}</p>
        <span class="use-case-link">View LinkedIn Post</span>
      </a>
    `
    )
    .join('');

  useCaseGrid.querySelectorAll('.interactive-card').forEach((card) => {
    card.addEventListener('pointermove', (event) => {
      const rect = card.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width) * 100;
      const y = ((event.clientY - rect.top) / rect.height) * 100;
      card.style.setProperty('--mx', `${x}%`);
      card.style.setProperty('--my', `${y}%`);
    });
  });
};

filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const filter = button.dataset.filter || 'all';

    filterButtons.forEach((btn) => {
      const isActive = btn === button;
      btn.classList.toggle('is-active', isActive);
      if (isActive) {
        btn.setAttribute('aria-pressed', 'true');
      } else {
        btn.setAttribute('aria-pressed', 'false');
      }
    });

    renderUseCases(filter);
  });
});

renderUseCases();

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
