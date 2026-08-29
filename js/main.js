// Bus Traffic Fever Guide — nav toggle, level jump, scroll reveal
(function () {
  'use strict';

  // Mobile nav toggle
  var navToggle = document.getElementById('navToggle');
  var navLinks = document.getElementById('navLinks');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      navLinks.classList.toggle('open');
    });
  }

  // Level jump search
  var input = document.getElementById('levelInput');
  var goBtn = document.getElementById('levelGo');
  var msg = document.getElementById('levelMsg');
  function jump() {
    var n = parseInt(input.value, 10);
    if (!n || n < 1 || n > 292) {
      if (msg) msg.textContent = 'Please enter a level number between 1 and 292.';
      return;
    }
    window.location.href = '/level/' + n + '/';
  }
  if (goBtn && input) {
    goBtn.addEventListener('click', jump);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') jump();
    });
  }

  // Scroll reveal
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('is-visible'); });
  }
})();

// Range tabs — filter level cards by range so each band shows separately
(function () {
  'use strict';

  var tabs = document.querySelectorAll('.range-tab');
  var cards = document.querySelectorAll('.level-card');
  var empty = document.getElementById('emptyRange');
  if (!tabs.length || !cards.length) return;

  function levelOf(card) {
    var m = card.getAttribute('href').match(/\/level\/(\d+)\//);
    return m ? parseInt(m[1], 10) : 0;
  }

  function applyRange(tab) {
    tabs.forEach(function (t) { t.classList.remove('is-active'); });
    tab.classList.add('is-active');

    var parts = tab.getAttribute('data-range').split('-');
    var min = parseInt(parts[0], 10);
    var max = parseInt(parts[1], 10);
    var shown = 0;

    cards.forEach(function (card) {
      var lv = levelOf(card);
      var show = lv >= min && lv <= max;
      card.style.display = show ? '' : 'none';
      if (show) { card.classList.add('is-visible'); shown++; }
    });

    if (empty) {
      if (shown === 0) {
        empty.style.display = '';
        empty.textContent = 'Levels ' + min + '–' + max + ' walkthroughs are coming soon. Check back, or open a guide from Levels 1–40 above.';
      } else {
        empty.style.display = 'none';
      }
    }
  }

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function (e) {
      e.preventDefault();
      applyRange(tab);
    });
  });

  var active = document.querySelector('.range-tab.is-active');
  if (active) applyRange(active);
})();
