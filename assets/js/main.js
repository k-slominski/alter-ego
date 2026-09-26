(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');

  // Expose header height for sticky sub-navigation and anchor offsets
  var header = document.querySelector('.site-header');
  function setHeaderHeight() {
    document.documentElement.style.setProperty('--hdr', header.offsetHeight + 'px');
  }
  setHeaderHeight();
  window.addEventListener('resize', setHeaderHeight);

  // Mobile menu
  toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });

  // Copy bank account number
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var label = btn.querySelector('span');
      function done() {
        btn.classList.add('copied');
        label.textContent = 'Skopiowano';
        setTimeout(function () { btn.classList.remove('copied'); label.textContent = 'Kopiuj'; }, 2000);
      }
      if (navigator.clipboard) {
        navigator.clipboard.writeText(btn.getAttribute('data-copy')).then(done);
      }
    });
  });

  // Google map – loaded only after the visitor agrees (remembered in this browser)
  var MAP_KEY = 'alterego-map-consent';
  function storageGet() { try { return localStorage.getItem(MAP_KEY); } catch (e) { return null; } }
  function storageSet(v) { try { v ? localStorage.setItem(MAP_KEY, v) : localStorage.removeItem(MAP_KEY); } catch (e) {} }
  function loadMap(box) {
    if (box.classList.contains('loaded')) return;
    var f = document.createElement('iframe');
    f.src = box.getAttribute('data-map-src');
    f.title = 'Mapa – ALTER EGO, Szosa Chełmińska 154E, Toruń';
    f.loading = 'lazy';
    f.referrerPolicy = 'no-referrer-when-downgrade';
    f.allowFullscreen = true;
    box.appendChild(f);
    box.classList.add('loaded');
  }
  var maps = document.querySelectorAll('[data-map-src]');
  maps.forEach(function (box) {
    if (storageGet() === '1') loadMap(box);
    box.querySelector('[data-map-load]').addEventListener('click', function () {
      storageSet('1');
      maps.forEach(loadMap);
    });
  });
  document.querySelectorAll('[data-map-revoke]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      storageSet(null);
      btn.textContent = 'Zapisano – mapa nie będzie wyświetlana automatycznie';
      btn.disabled = true;
    });
  });

  // Gentle reveal of sections
  if ('IntersectionObserver' in window) {
    var items = document.querySelectorAll('.section > .container');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08 });
    items.forEach(function (el) {
      el.classList.add('reveal');
      io.observe(el);
    });
  }
})();
