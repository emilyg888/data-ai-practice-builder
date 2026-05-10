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
    href: 'use-cases/semantic-foundry-business-banking-fraud-layer.md',
  },
  {
    title: 'Governance Certification Gate for Enterprise AI Assets',
    category: 'Governance',
    tag: 'governance',
    summary: 'Applies deterministic validation gates for schema, policy, and SQL quality before semantic assets are promoted.',
    href: 'use-cases/semantic-foundry-governance-certification-gate.md',
  },
  {
    title: 'Analyst-in-the-Loop Controls for Fraud AI Recommendations',
    category: 'Fraud',
    tag: 'fraud',
    summary: 'Ensures human review boundaries, approved/disallowed usage, and audit-ready case handling for high-risk alerts.',
    href: 'use-cases/semantic-foundry-analyst-review-controls.md',
  },
  {
    title: 'Kafka + Lambda Trigger Layer for GenAI Invocation Control',
    category: 'GenAI Ops',
    tag: 'genai',
    summary: 'Introduces invoke/ignore/sample decisions between event streams and GenAI to increase control and reduce waste.',
    href: 'use-cases/kafka-lambda-trigger-layer-for-genai.md',
  },
  {
    title: 'GenAI Cost Optimization Through Signal Filtering',
    category: 'GenAI Ops',
    tag: 'genai',
    summary: 'Routes low-value events away from premium models while preserving high-value signal coverage.',
    href: 'use-cases/genai-inference-cost-optimization-via-signal-filtering.md',
  },
  {
    title: 'Streaming AI Decision Observability and Evaluation',
    category: 'GenAI Ops',
    tag: 'genai',
    summary: 'Captures trigger decisions, outcomes, and metrics to continuously tune policy and runtime behavior.',
    href: 'use-cases/streaming-ai-decision-observability-and-evaluation.md',
  },
  {
    title: 'Fraud Semantic Contracts and Governed Signal Layer',
    category: 'Governance',
    tag: 'governance',
    summary: 'Converts fragmented fraud logic into certified semantic assets that AI systems are allowed to reason over.',
    href: 'use-cases/fraud-semantic-contracts-governed-signal-layer.md',
  },
  {
    title: 'Fraud Agentic Investigation with Human Control Boundaries',
    category: 'Fraud',
    tag: 'fraud',
    summary: 'Orchestrates investigation steps with explicit human checkpoints and auditable evidence synthesis.',
    href: 'use-cases/fraud-agentic-investigation-with-human-control-boundaries.md',
  },
  {
    title: 'Fraud Pattern Experimentation and Promotion Loop',
    category: 'Fraud',
    tag: 'fraud',
    summary: 'Implements a Generate-Detect-Evaluate-Compare-Register-Promote loop for adaptive fraud detection patterns.',
    href: 'use-cases/fraud-pattern-experimentation-and-promotion-loop.md',
  },
];

const renderUseCases = (filter = 'all') => {
  if (!useCaseGrid) return;

  const items = useCases.filter((item) => filter === 'all' || item.tag === filter);

  useCaseGrid.innerHTML = items
    .map(
      (item) => `
      <article class="use-case-card interactive-card reveal is-visible">
        <p class="use-case-category">${item.category}</p>
        <h3>${item.title}</h3>
        <p>${item.summary}</p>
        <a class="use-case-link" href="${item.href}" target="_blank" rel="noopener noreferrer">View Use Case</a>
      </article>
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
