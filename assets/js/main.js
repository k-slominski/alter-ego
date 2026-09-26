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
