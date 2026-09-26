#!/usr/bin/env python3
"""Generates the static pages of the ALTER EGO website.

Every page shares the same header, navigation and footer, so they are kept
here in one place. Edit the content below and run:

    python3 tools/build.py

The generated *.html files are written to the repository root and committed,
so the site works without running this script (e.g. on GitHub Pages).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PHONE = "609 88 17 88"
PHONE_HREF = "tel:+48609881788"
EMAIL = "kontakt@alterego-torun.pl"
FACEBOOK = "https://www.facebook.com/alterego.torun/"
SITE_URL = "https://www.alterego-torun.pl/"
ADDRESS_Q = "ALTER%20EGO%20Gabinet%20Psychoterapii%2C%20Szosa%20Che%C5%82mi%C5%84ska%20154E%2C%2087-100%20Toru%C5%84"
MAP_EMBED = "https://www.google.com/maps/embed?origin=mfe&pb=!1m3!2m1!1sSzosa+Che%C5%82mi%C5%84ska+154E,+87-100+Toru%C5%84!6i16"
MAP_OPEN = "https://maps.google.com/maps?cid=1051423359503064108"
MAP_ROUTE = f"https://www.google.com/maps/dir/?api=1&destination={ADDRESS_Q}"
VCARD = "assets/alter-ego-bozena-slominska.vcf"

# (file, label) – order as in the original menu
NAV = [
    ("index.html", "alter ego"),
    ("komu-pomagam.html", "komu pomagam"),
    ("formy-pomocy.html", "formy pomocy"),
    ("oferta-szkoleniowa.html", "oferta szkoleniowa"),
    ("o-mnie.html", "o mnie"),
    ("wspolpracuje.html", "współpracuję"),
    ("orientacja-teoretyczna.html", "orientacja teoretyczna"),
    ("cennik.html", "cennik"),
    ("pierwsza-wizyta.html", "pierwsza wizyta"),
    ("kontakt.html", "kontakt"),
]

ICON = {
    "phone": '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a1 1 0 0 1-1 1A16 16 0 0 1 4 5a1 1 0 0 1 1-1"/></svg>',
    "mail": '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1.5"/><path d="M3 7l9 6 9-6"/></svg>',
    "pin": '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    "fb": '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8z"/></svg>',
    "route": '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h8.5a3.5 3.5 0 0 0 0-7h-9a3.5 3.5 0 0 1 0-7H16"/></svg>',
    "card": '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1.5"/><circle cx="9" cy="11" r="2"/><path d="M5.5 16c.6-1.6 2-2.5 3.5-2.5s2.9.9 3.5 2.5M15 10h3M15 13h3"/></svg>',
    "copy": '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V5.5A1.5 1.5 0 0 0 14.5 4h-9A1.5 1.5 0 0 0 4 5.5v9A1.5 1.5 0 0 0 5.5 16H8"/></svg>',
    "lifebuoy": '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M5.6 5.6l3.6 3.6M14.8 14.8l3.6 3.6M18.4 5.6l-3.6 3.6M9.2 14.8l-3.6 3.6"/></svg>',
    "arrow": '<svg class="i i-arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
}


def nav_html(current):
    items = []
    for href, label in NAV:
        ext = href.startswith("http")
        attrs = ' target="_blank" rel="noopener"' if ext else ""
        cls = ' class="active" aria-current="page"' if href == current else ""
        items.append(f'<a href="{href}"{cls}{attrs}>{label}</a>')
    return "\n        ".join(items)


def map_frame():
    # The Google map is loaded only after the visitor clicks (privacy / RODO).
    return f"""<div class="map" data-map-src="{MAP_EMBED}">
          <div class="map-placeholder">
            <img src="assets/img/drzewo.png" alt="" width="56" height="52">
            <p class="map-address">Szosa Chełmińska 154E/2<br>87-100 Toruń</p>
            <button type="button" class="btn btn-primary" data-map-load>{ICON['pin']} Pokaż mapę Google</button>
            <p class="map-note">Wyświetlenie mapy łączy się z serwerami Google, które mogą zapisać pliki cookies.
              <a href="polityka-prywatnosci.html#mapa">Więcej informacji</a></p>
          </div>
        </div>"""


JSON_LD = f"""<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "MedicalBusiness",
    "name": "ALTER EGO – Gabinet Psychoterapii i Rozwoju Osobistego Bożena Słomińska",
    "url": "{SITE_URL}",
    "image": "{SITE_URL}assets/img/bozena-slominska-portret.jpg",
    "logo": "{SITE_URL}assets/img/drzewo.png",
    "telephone": "+48 609 881 788",
    "email": "{EMAIL}",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Szosa Chełmińska 154E/2",
      "postalCode": "87-100",
      "addressLocality": "Toruń",
      "addressCountry": "PL"
    }},
    "geo": {{ "@type": "GeoCoordinates", "latitude": 53.0302896, "longitude": 18.5903511 }},
    "hasMap": "{MAP_OPEN}",
    "sameAs": ["{FACEBOOK}"],
    "founder": {{ "@type": "Person", "name": "Bożena Słomińska", "jobTitle": "psychoterapeuta" }}
  }}
  </script>"""


def layout(filename, title, description, body, eyebrow=None, heading=None, lead=None):
    page_head = ""
    if heading:
        page_head = f"""
    <section class="page-head">
      <div class="container">
        {f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ''}
        <h1>{heading}</h1>
        {f'<p class="lead">{lead}</p>' if lead else ''}
      </div>
    </section>"""
    full_title = "ALTER EGO – Gabinet Psychoterapii Bożena Słomińska – Toruń"
    if title:
        full_title = f"{title} | {full_title}"
    return f"""<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{SITE_URL}{'' if filename == 'index.html' else filename}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pl_PL">
  <meta property="og:site_name" content="ALTER EGO – Gabinet Psychoterapii">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{SITE_URL}{'' if filename == 'index.html' else filename}">
  <meta property="og:image" content="{SITE_URL}assets/img/bozena-slominska-portret.jpg">
  <meta name="theme-color" content="#f8f7f3">
  <link rel="stylesheet" href="assets/fonts/fonts.css">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="icon" href="assets/img/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
  {JSON_LD if filename in ('index.html', 'kontakt.html') else ''}
</head>
<body>
  <a class="skip" href="#main">Przejdź do treści</a>

  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html" aria-label="ALTER EGO – strona główna">
        <img src="assets/img/drzewo.png" alt="" class="brand-tree" width="52" height="48">
        <span class="brand-text">
          <span class="brand-name">alter ego</span>
          <span class="brand-sub">gabinet psychoterapii i rozwoju osobistego – Bożena Słomińska</span>
        </span>
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu">
        <span></span><span></span>
      </button>
    </div>
    <nav class="nav" id="nav" aria-label="Menu główne">
      <div class="container nav-inner">
        {nav_html(filename)}
      </div>
    </nav>
    <div class="ribbon" aria-hidden="true"></div>
  </header>

  <main id="main">{page_head}
{body}
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <img src="assets/img/drzewo.png" alt="" width="64" height="59">
        <p><strong>ALTER EGO</strong><br>Gabinet Psychoterapii<br>i Rozwoju Osobistego</p>
      </div>
      <div>
        <h2 class="footer-title">Kontakt</h2>
        <p>Bożena Słomińska<br>
          <a href="{PHONE_HREF}">tel. {PHONE}</a><br>
          <span class="muted">Gdy nie mogę odebrać, oddzwaniam.</span><br>
          <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <h2 class="footer-title">Adres</h2>
        <p>Szosa Chełmińska 154E/2<br>87-100 Toruń<br>
          <a href="{MAP_ROUTE}" target="_blank" rel="noopener">Wyznacz trasę</a></p>
        <p><a href="{FACEBOOK}" target="_blank" rel="noopener">facebook.com/alterego.torun</a></p>
      </div>
      <div class="footer-cert">
        <a href="http://www.psychologia.edu.pl/" target="_blank" rel="noopener" title="Instytut Psychologii Zdrowia PTP">
          <img src="assets/img/logo-ipz-ptp.png" alt="Instytut Psychologii Zdrowia PTP" width="150" height="72">
        </a>
      </div>
    </div>
    <div class="container footer-crisis">
      <p>{ICON['lifebuoy']}<span><strong>W sytuacji zagrożenia życia</strong> dzwoń pod <a href="tel:112">112</a>.
        Całodobowe Centrum Wsparcia dla osób w kryzysie psychicznym: <a href="tel:800702222">800 70 2222</a> ·
        <a href="pierwsza-wizyta.html#pomoc-w-kryzysie">więcej telefonów zaufania</a></span></p>
    </div>
    <div class="container footer-bottom">
      <p>© Alter Ego - Toruń Psychoterapia</p>
      <p><a href="polityka-prywatnosci.html">Polityka prywatności</a></p>
    </div>
  </footer>

  <nav class="quickbar" aria-label="Szybki kontakt">
    <a href="{PHONE_HREF}">{ICON['phone']}<span>Zadzwoń</span></a>
    <a href="{MAP_ROUTE}" target="_blank" rel="noopener">{ICON['route']}<span>Dojazd</span></a>
    <a href="mailto:{EMAIL}">{ICON['mail']}<span>E-mail</span></a>
  </nav>

  <script src="assets/js/main.js"></script>
</body>
</html>
"""


def figure(src, alt, cls="photo"):
    return f'<figure class="{cls}"><img src="assets/img/{src}" alt="{alt}"></figure>'


def ul(items, cls="list"):
    lis = "\n".join(f"          <li>{i}</li>" for i in items)
    return f'<ul class="{cls}">\n{lis}\n        </ul>'


# --------------------------------------------------------------------------
# Strona główna – „alter ego”
# --------------------------------------------------------------------------
HOME = f"""
    <section class="hero">
      <div class="container hero-grid">
        <div class="hero-text">
          <p class="eyebrow">Toruń · Szosa Chełmińska 154E/2</p>
          <h1>Gabinet ALTER EGO w Toruniu to miejsce dla ludzi, którzy:</h1>
          <ul class="hero-points">
            <li>szukają pomocy, bo przeżywają trudności osobiste,</li>
            <li>funkcjonują dobrze i szukają możliwości rozwoju.</li>
          </ul>
          <div class="actions">
            <a href="{PHONE_HREF}" class="btn btn-primary">{ICON['phone']} {PHONE}</a>
            <a href="mailto:{EMAIL}" class="btn btn-ghost">{ICON['mail']} Napisz wiadomość</a>
          </div>
          <p class="hero-more"><a href="pierwsza-wizyta.html">Jak wygląda pierwsza wizyta? {ICON['arrow']}</a></p>
        </div>
        <figure class="hero-photo">
          <img src="assets/img/bozena-slominska-portret.jpg" alt="Bożena Słomińska – psychoterapeuta" width="1200" height="1200">
          <figcaption>Bożena Słomińska<span>psychoterapeuta, trener rozwoju osobistego</span></figcaption>
        </figure>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container split">
        <div class="split-text">
          <h2>Psychoterapia i rozwój</h2>
          <p><strong>Tym pierwszym oferuję psychoterapię.</strong> W psychoterapii pomagam klientom znajdować ich własne rozwiązania problemów będących przyczyną dolegliwości lub cierpienia.</p>
          <p><strong>Tym drugim</strong> pomagam rozpoznawać rzeczywiste możliwości i ograniczenia, zwiększać ich możliwości osiągania swoich celów, pokonywać przeszkody i poprawiać jakość życia.</p>
          <p>Oferuję między innymi <a href="formy-pomocy.html#psychoterapia-indywidualna">psychoterapię indywidualną</a>, <a href="formy-pomocy.html#psychoterapia-grupowa">psychoterapię grupową</a>, <a href="formy-pomocy.html#terapia-par">terapię par</a>, poradnictwo małżeńskie, <a href="formy-pomocy.html#poradnictwo-rodzinne">rodzinne i wychowawcze</a>, <a href="formy-pomocy.html#interwencja-kryzysowa">pomoc w kryzysach osobistych</a>, <a href="oferta-szkoleniowa.html#trening-interpersonalny">trening interpersonalny</a>, warsztaty i treningi komunikacji, asertywności, szkolenia dla osób pracujących w obszarze pomagania drugiemu człowiekowi.</p>
          <p class="muted">W trosce o jakość pracy korzystam z superwizji i zawodowych konsultacji.</p>
        </div>
        <div class="split-media">
          {figure('bozena-slominska-gabinet.jpg', 'Bożena Słomińska w gabinecie ALTER EGO', 'photo photo-lg')}
          {figure('gabinet.jpg', 'Gabinet ALTER EGO w Toruniu', 'photo photo-sm')}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <blockquote class="quote">
          <p>Zapraszam do wspólnego rozpoznawania mapy życia – całej lub fragmentu – wybierania celów wędrówki, wytyczania do nich dróg i porzucania szlaków prowadzących na manowce.</p>
          <footer>Rozwój jest możliwy przez całe życie.</footer>
        </blockquote>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Formy pomocy</p>
          <h2>W czym mogę pomóc</h2>
        </div>
        <div class="tiles">
          <a class="tile" href="formy-pomocy.html#psychoterapia-indywidualna">{figure('psychoterapia-indywidualna.jpg', '')}<span>psychoterapia indywidualna</span></a>
          <a class="tile" href="formy-pomocy.html#psychoterapia-grupowa">{figure('psychoterapia-grupowa.jpg', '')}<span>psychoterapia grupowa</span></a>
          <a class="tile" href="formy-pomocy.html#terapia-par">{figure('terapia-par-2.jpg', '')}<span>terapia par</span></a>
          <a class="tile" href="formy-pomocy.html#terapia-dda-ddd">{figure('terapia-dda-ddd.jpg', '')}<span>terapia DDA i DDD</span></a>
          <a class="tile" href="formy-pomocy.html#poradnictwo-rodzinne">{figure('poradnictwo-rodzinne.jpg', '')}<span>poradnictwo rodzinne</span></a>
          <a class="tile" href="formy-pomocy.html#interwencja-kryzysowa">{figure('interwencja-kryzysowa.jpg', '')}<span>interwencja kryzysowa</span></a>
        </div>
        <p class="more"><a href="oferta-szkoleniowa.html">Oferta szkoleniowa {ICON['arrow']}</a></p>
      </div>
    </section>

    <section class="section visit" id="dojazd">
      <div class="container visit-grid">
        <div class="visit-text">
          <p class="eyebrow">Dojazd i kontakt</p>
          <h2>Zapraszam do gabinetu</h2>
          <ul class="contact-list">
            <li>{ICON['pin']}<span><strong>Szosa Chełmińska 154E/2</strong><br>87-100 Toruń</span></li>
            <li>{ICON['phone']}<span><a href="{PHONE_HREF}">tel. {PHONE}</a><br><small class="muted">Gdy nie mogę odebrać, oddzwaniam.</small></span></li>
            <li>{ICON['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          </ul>
          <div class="actions">
            <a href="{MAP_ROUTE}" class="btn btn-primary" target="_blank" rel="noopener">{ICON['route']} Wyznacz trasę</a>
            <a href="{MAP_OPEN}" class="btn btn-ghost" target="_blank" rel="noopener">{ICON['pin']} Otwórz w Mapach Google</a>
          </div>
        </div>
        {map_frame()}
      </div>
    </section>
"""

# --------------------------------------------------------------------------
# Komu pomagam
# --------------------------------------------------------------------------
KOMU = f"""
    <section class="section section-tight">
      <div class="container article">
        <div class="article-body">
          <p>Moimi klientami są osoby dorosłe poszukujące pomocy z powodu trudności osobistych, takich jak:</p>
          {ul(['nadmierne lęki,', 'stany przygnębienia,', 'brak chęci do życia,', 'kryzysy różnego pochodzenia,', 'niskie poczucie własnej wartości,', 'poczucie winy,', 'rozdrażnienie,', 'stres,', 'żałoba,', 'rozstanie z bliską osobą,', 'dylematy decyzyjne,', 'trudności w relacjach z innymi: współmałżonkiem, dziećmi, rodzicami, teściami, współpracownikami, szefem…'], 'list list-cols')}
          <p>Pomagam też osobom określającym swoje trudności jako zaburzenia nerwicowe, depresyjne, adaptacyjne, psychosomatyczne, DDA, DDD.</p>
          <p>Pracuję też z osobami zainteresowanymi własnym rozwojem i poszerzaniem granic swojej wewnętrznej wolności.</p>
          <h2>Pracuję z tymi, którzy pomagają innym i chcą jeszcze lepiej pomagać:</h2>
          {ul(['z rodzicami, którzy chcą lepiej pomagać swoim dzieciom,', 'z lekarzami, którzy chcą lepiej pomagać swoim pacjentom,', 'z nauczycielami, którzy chcą lepiej pomagać swoim uczniom,', 'z pracownikami socjalnymi, którzy chcą lepiej pomagać swoim klientom i podopiecznym.'])}
          <p>Oprócz osób indywidualnych zapraszam też grupy zainteresowane szkoleniami w zakresie psychologicznych umiejętności ważnych w kontaktach społecznych.</p>
        </div>
        <aside class="article-aside">
          {figure('komu-pomagam.jpg', 'Wnętrze gabinetu ALTER EGO')}
        </aside>
      </div>
    </section>
"""

# --------------------------------------------------------------------------
# Formy pomocy
# --------------------------------------------------------------------------
def form_section(anchor, title, img, body, img2=None, alt=False):
    extra = figure(img2[0], img2[1]) if img2 else ""
    return f"""
    <section class="section section-tight{' section-alt' if alt else ''}" id="{anchor}">
      <div class="container article">
        <div class="article-body">
          <h2>{title}</h2>
{body}
        </div>
        <aside class="article-aside">
          {figure(img[0], img[1])}
          {extra}
        </aside>
      </div>
    </section>"""


FORMY = f"""
    <nav class="subnav" aria-label="Formy pomocy">
      <div class="container">
        <a href="#psychoterapia-indywidualna">psychoterapia indywidualna</a>
        <a href="#psychoterapia-grupowa">psychoterapia grupowa</a>
        <a href="#terapia-par">terapia par</a>
        <a href="#terapia-dda-ddd">terapia dda i ddd</a>
        <a href="#poradnictwo-rodzinne">poradnictwo rodzinne</a>
        <a href="#interwencja-kryzysowa">interwencja kryzysowa</a>
      </div>
    </nav>
""" + form_section("psychoterapia-indywidualna", "Psychoterapia indywidualna",
                   ("psychoterapia-indywidualna.jpg", "Figurka – psychoterapia indywidualna"), f"""
          <p>Psychoterapia indywidualna polega na systematycznych spotkaniach klienta/pacjenta z terapeutą odbywanych zwykle raz w tygodniu. Sesja trwa 50 - 60 minut. Liczba sesji zależy od rodzaju problemu i indywidualnych potrzeb pacjenta. Zwykle jest to od dziesięciu do kilkudziesięciu spotkań.</p>
          <p>Psychoterapia jest:</p>
          {ul(['terapią, czyli drogą do zdrowia,', 'głębszym poznawaniem siebie i swojej historii,', 'odkrywaniem swojego potencjału,', 'pokonywaniem wewnętrznych ograniczeń,', 'sposobem przezwyciężania skutków urazowych doświadczeń z przeszłości,'])}
          <p>w rezultacie:</p>
          {ul(['prowadzi do lepszego, dojrzalszego życia w zgodzie ze swoimi wartościami'])}
          <p>Narzędziem pracy jest przede wszystkim rozmowa. Najważniejszym czynnikiem leczącym jest relacja terapeutyczna. Na czas pomiędzy sesjami pacjent może otrzymać zadanie terapeutyczne.</p>
          <p>Psychoterapia jest pracą nad sobą. Pewnych prac nie można jej wykonać w pojedynkę – nawet najlepszy chirurg nie może zoperować sam siebie. Potrzebny bywa drugi człowiek – czasem lekarz, czasem duchowny, czasem psychoterapeuta. Uznaję odrębność sfer oddziaływania poszczególnych specjalistów, współpracuję z dobrymi lekarzami i służę kontaktami do duchownych, którzy mogą pomóc moim klientom.</p>""") \
  + form_section("psychoterapia-grupowa", "Psychoterapia grupowa",
                 ("psychoterapia-grupowa.jpg", "Kolorowe kamienie – psychoterapia grupowa"), f"""
          <p>Psychoterapia grupowa jest formą pomocy, w której terapeuta stosuje techniki terapeutyczne wobec grupy pacjentów oraz dodatkowo korzysta z relacji interpersonalnych jako narzędzia terapeutycznego.</p>
          <h3>Zalety pracy w grupie</h3>
          {ul(['Grupa pozwala przezwyciężyć poczucie osamotnienia wynikające z nieprawdziwego przekonania, że inni nie mają pewnych problemów.', 'Grupa jest źródłem korektywnych doświadczeń emocjonalnych, w szczególności daje możliwość doświadczenia takiej akceptacji, jakiej wcześniej uczestnik nie otrzymał.', 'W grupie terapeutycznej uczestnik występuje w dwóch rolach – zarówno przyjmuje pomoc, jak i udziela pomocy innym.', 'Fakt bycia świadkiem, jak inni pokonują trudności, sprawia, że grupa terapeutyczna jest źródłem dodatkowej nadziei na uzyskanie poprawy w swoim życiu.', 'Grupa terapeutyczna daje okazję do szybszego uczenia się pożądanych umiejętności społecznych.', 'Terapia grupowa jest mniej kosztowna dla klienta.'])}""", alt=True) \
  + form_section("terapia-par", "Terapia par",
                 ("terapia-par-1.jpg", "Lampa w gabinecie – terapia par"), """
          <p>Pary szukają pomocy zarówno wtedy, gdy chcą poprawić swoje relacje lub uporać się z kryzysem, jak i wtedy, gdy zastanawiają się, czy związek kontynuować.</p>
          <p>Terapeuta pomaga im znaleźć ich własne rozwiązanie.</p>
          <p>Pomaga im zrozumieć nawzajem swoje słowa, uczucia i potrzeby, budować realne oczekiwania i klarownie je wyrażać, w sytuacji kryzysowej pomaga szukać sposobu odbudowywania zaufania i poczucia bezpieczeństwa.</p>
          <p>Pomaga także budować odrębność i autonomię w ramach związku.</p>
          <p>Skorzystać z terapii może każda para: małżeństwo, związek nieformalny, znajomi, członkowie rodziny.</p>
          <p>Zdarza się, że tylko jedna strona gotowa jest korzystać z pomocy terapeutycznej. Taka praca też może mieć sens – nie tylko dla tej osoby, ale także dla całego związku.</p>""",
                 img2=("terapia-par-2.jpg", "Rzeźba dwóch postaci – terapia par")) \
  + form_section("terapia-dda-ddd", "Terapia DDA i DDD",
                 ("terapia-dda-ddd.jpg", "Kompozycja roślinna – terapia DDA i DDD"), """
          <p>Terapia DDA oznacza terapię Dorosłych Dzieci Alkoholików. Adresatami tej formy pomocy są osoby dorosłe, które wychowywały się w rodzinach z problemem alkoholowym, a ślady tych doświadczeń są źródłem problemów w życiu dorosłym.</p>
          <p>Terapia DDD oznacza terapię Dorosłych Dzieci z rodzin Dysfunkcyjnych, czyli z takich, w których brakowało bezpieczeństwa, troski, oparcia, szacunku, miłości, a istniała przemoc, strach, poniżanie, zaniedbywanie, osamotnienie.</p>
          <p>Pomoc terapeutyczna może być udzielana zarówno indywidualnie, jak i grupowo.</p>""", alt=True) \
  + form_section("poradnictwo-rodzinne", "Poradnictwo rodzinne",
                 ("poradnictwo-rodzinne.jpg", "Stare radio – poradnictwo rodzinne"), """
          <p>Trudne sytuacje są naturalnym elementem życia rodzinnego. Niektóre z nich są wyzwaniami, którym rodzina nie jest w stanie sama stawić czoła. Mogą to być problemy wychowawcze, sytuacja rozwodowa, zdrada małżeńska, tajemnica rodzinna, przemoc, choroba przewlekła, problemy opieki nad osobą niepełnosprawną, ingerencje rodziców w małżeństwo dorosłych dzieci, przemiany obyczajowe, konflikty międzypokoleniowe – i wszystko, co subiektywnie doświadczane jest jako trudność.</p>
          <p>Częstym rodzajem trudności są wątpliwości związane z wychowywaniem dzieci – jak najlepiej przygotować swoje dziecko do życia? Jak przekazać mu to, co uważamy za najcenniejsze? Jak uchronić przed zagrożeniami? Jak budować relacje z dzieckiem na różnych etapach jego rozwoju, w różnych sytuacjach rodzinnych? Jak mu pomagać tak, by chciało pomoc przyjąć? Co robić, gdy nie sprawdzają się dotychczasowe metody wychowawcze? Jak naprawić swój błąd, gdy się zdarzy? I wiele, wiele innych…</p>
          <p>Terapeuta pomaga klientom korygować błędy w myśleniu, eliminować zachowania nieskuteczne lub destrukcyjne, znaleźć rozwiązanie problemu, podjąć właściwe decyzje i je zrealizować.</p>
          <p>Może okazać się, że skorzystanie z poradnictwa nie wystarcza do tego, by z problemem się uporać, wówczas należy rozważyć inną formę pomocy psychologicznej.</p>""") \
  + form_section("interwencja-kryzysowa", "Interwencja kryzysowa",
                 ("interwencja-kryzysowa.jpg", "Drzewo na ścianie gabinetu – interwencja kryzysowa"), """
          <p>Kryzys jest indywidualną emocjonalną reakcją na szczególnie trudne doświadczenie. Osoba w kryzysie nie potrafi sprostać sytuacji przy pomocy dotychczasowych sposobów radzenia sobie z problemami. Jest bezradna, załamana, zdezorientowana, ma utrudnioną zdolność logicznego myślenia i ma poczucie utraty kontroli nad swoim życiem.</p>
          <p>Pomoc polega na udzieleniu takiej osobie wsparcia, skorygowaniu nieprawdziwych przekonań, zaktywizowaniu, ukierunkowaniu i przywróceniu poczucia sprawczości.</p>
          <p>Celem pomocy osobie w kryzysie jest umożliwienie jej powrotu do równowagi emocjonalnej i do samodzielnego pokonywania trudności.</p>""", alt=True)

# --------------------------------------------------------------------------
# Oferta szkoleniowa
# --------------------------------------------------------------------------
OFERTA = f"""
    <section class="section section-tight">
      <div class="container">
        <ul class="offer-list">
          <li><a href="#trening-interpersonalny">trening interpersonalny</a></li>
          <li>treningi i warsztaty komunikacji</li>
          <li>trening asertywności</li>
          <li>warsztaty umiejętności wychowawczych</li>
          <li>„Szkoła dla rodziców i wychowawców”</li>
          <li>warsztaty „praca z trudnym klientem/pacjentem/petentem”</li>
          <li><a href="#programy-rozwoju-osobistego">programy rozwoju osobistego</a></li>
          <li>szkolenia na zamówienie</li>
        </ul>
      </div>
    </section>
""" + form_section("trening-interpersonalny", "Trening interpersonalny",
                   ("trening-interpersonalny.jpg", "Lampa – trening interpersonalny"), f"""
          <p>Jest to intensywne doświadczenie grupowe, adresowane do ludzi dobrze funkcjonujących.</p>
          <p>Grupa składa się z osób, które dotychczas się nie znały. W centrum uwagi znajdują się relacje uczestników z innymi ludźmi. Podczas treningu kładzie się nacisk na sytuacje „tu i teraz”, wyrażanie uczuć, konstruktywne komunikowanie się. Trening jest okazją do eksperymentowania z nowymi zachowaniami oraz do przejrzenia się w „społecznym lustrze”, czyli uzyskania informacji o tym, jak jest się spostrzeganym przez innych.</p>
          <p>W grupie treningowej wszystkie procesy społeczne zachodzą podobnie, jak w naturalnych warunkach, tylko szybciej, dzięki czemu w krótkim czasie zdobywa się wiele znaczących doświadczeń, które – w odróżnieniu od życia w naturalnych warunkach – są omówione, i to w taki sposób, by uczestnik wyniósł z nich jak najwięcej korzyści.</p>
          <h3>Efektem udziału w treningu jest między innymi:</h3>
          {ul(['wzbogacenie wiedzy o sobie – swoich cechach, typowych zachowaniach, przyjmowanych rolach grupowych', 'lepsze poznanie siebie w kontakcie z drugim człowiekiem (jak jestem odbierany, w jakim stopniu jest to zbieżne z moim przekonaniem na ten temat)', 'urealnienie swojej samooceny', 'skuteczniejsze komunikowanie się – także w trudnych emocjonalnie sytuacjach', 'lepsze zrozumienie innych ludzi,', 'zdobywanie nowych doświadczeń w zakresie relacji interpersonalnych (w bezpiecznej psychologicznie sytuacji mogę próbować innych niż dotąd zachowań),', 'doświadczanie wpływu emocji na funkcjonowanie,', 'identyfikowanie zachowań dyktowanych emocjami', 'konstruktywne radzenie sobie z przykrymi emocjami', 'poprawa skuteczności własnego działania.'])}
          <p class="note"><strong>Czas trwania</strong> – 45 godzin, pięć kolejnych dni, w grupie 10 – 15 osób nie znających się wcześniej.</p>
          <p>Trening interpersonalny szczególnie polecany jest profesjonalistom pracującym z ludźmi (psychologom, nauczycielom, lekarzom, duchownym, menedżerom…). Z uwagi na duże osobiste korzyści może być też interesującą przygodą i ważnym doświadczeniem dla każdego, kto ceni kontakty z ludźmi.</p>""", alt=True) \
  + form_section("programy-rozwoju-osobistego", "Programy rozwoju osobistego",
                 ("programy-rozwoju-osobistego.jpg", "Lampa – programy rozwoju osobistego"), f"""
          <p>To jest propozycja dla osób zainteresowanych swoim rozwojem psychologicznym. Dokładna tematyka jest ustalana z klientem. Forma pracy – 3-godzinne zajęcia grupowe, raz w tygodniu, przez 2 – 9 miesięcy. Czas trwania dostosowany jest do oczekiwań grupy.</p>
          <h3>Korzyści z udziału:</h3>
          {ul(['pogłębiona psychologicznie refleksja nad tym, kim jestem', 'wzrost świadomości swoich granic psychologicznych', 'skuteczniejsze kierowanie sobą zgodnie z przyjętymi wartościami', 'skuteczniejsza komunikacja z drugim człowiekiem', 'poprawa umiejętności radzenia sobie z trudnymi sytuacjami interpersonalnymi.'])}""")

# --------------------------------------------------------------------------
# O mnie
# --------------------------------------------------------------------------
OMNIE = f"""
    <section class="section section-tight">
      <div class="container about">
        <aside class="about-photo">
          {figure('bozena-slominska-portret.jpg', 'Bożena Słomińska')}
        </aside>
        <div class="about-body">
          <p class="lead-text">Psychoterapeuta z certyfikatem Polskiego Stowarzyszenia Psychoterapii Integracyjnej i trener rozwoju osobistego z rekomendacjami I i II stopnia Polskiego Towarzystwa Psychologicznego.</p>

          <h2>Wykształcenie</h2>
          <ul class="timeline">
            <li><strong>studia magisterskie z pedagogiki</strong> z indywidualnym programem kształcenia w zakresie psychologii i psychoterapii<span>Uniwersytet Mikołaja Kopernika</span></li>
            <li><strong>dwuletnie szkolenie warsztatowo-superwizyjne</strong> z zakresu terapeutycznej pracy z rodziną z uwzględnieniem podstaw systemowej terapii rodzin<span>Ośrodek Szkoleniowo-Terapeutyczny przy Towarzystwie „Powrót z U” w Warszawie</span></li>
            <li><strong>dwuletnie Podyplomowe Studium Socjoterapii</strong><span>Uniwersytet Warszawski</span></li>
            <li><strong>dwuletnia Szkoła Trenerów</strong><span>SIEĆ-Warszawa</span></li>
            <li><strong>czteroletnie podyplomowe studia w zakresie psychoterapii</strong><span>Profesjonalna Szkoła Psychoterapii w ramach współpracy Szkoły Wyższej Psychologii Społecznej i Instytutu Psychologii Zdrowia</span></li>
            <li><strong>roczna Szkoła Psychoterapii Par</strong><span>Laboratorium Psychoedukacji</span></li>
          </ul>

          <h2>Doświadczenie</h2>
          {ul(['ponad 20 lat pracy jako terapeuta i pedagog w różnych placówkach oświatowych i służby zdrowia;', 'od 2006 r. współpraca z Instytutem Psychologii Zdrowia Polskiego Towarzystwa Psychologicznego w zakresie szkolenia profesjonalistów w Studium Pomocy Psychologicznej', 'praca z grupami: treningi interpersonalne, psychoterapia grupowa, warsztaty pracy terapeutycznej, warsztaty pracy wychowawczej dla nauczycieli i rodziców, warsztaty kontaktu z pacjentem dla lekarzy;', 'szkolenia dla lekarzy, nauczycieli, pracowników socjalnych i osób duchownych dotyczące psychologicznych aspektów pomagania;', 'od 2006 roku prowadzenie zajęć dydaktycznych w Wyższej Szkole Bankowej w Toruniu z zakresu zagadnień psychospołecznych'])}

          <h2>Moi nauczyciele i zawodowe autorytety</h2>
          <ul class="tags">
            <li>Jerzy Mellibruda</li>
            <li>Wanda Sztander</li>
            <li>Zofia Sobolewska-Mellibruda</li>
            <li>Carl Rogers</li>
            <li>Irvin Yalom</li>
          </ul>

          <div class="private">
            <p>Prywatnie jestem mężatką i matką trójki dorosłych dzieci. W wolnych chwilach podróżuję, wędruję, zwiedzam okolice bliższe i dalsze. Lubię jazz, rekreacyjnie biegam.</p>
          </div>
        </div>
      </div>
    </section>
"""

# --------------------------------------------------------------------------
# Współpracuję
# --------------------------------------------------------------------------
WSPOL = """
    <section class="section section-tight">
      <div class="container">
        <div class="partners">
          <a class="partner" href="http://www.nawzgorzu.info/" target="_blank" rel="noopener">
            <span class="partner-logo"><img src="assets/img/logo-na-wzgorzu.jpg" alt="Na wzgórzu" loading="lazy"></span>
            <span class="partner-name">Na wzgórzu</span>
          </a>
          <a class="partner" href="https://www.facebook.com/Instytut-Psychologii-Zdrowia-PTP-154599717922904/" target="_blank" rel="noopener">
            <span class="partner-logo"><img src="assets/img/logo-instytut-psychologii-zdrowia.png" alt="Instytut Psychologii Zdrowia PTP" loading="lazy"></span>
            <span class="partner-name">Instytut Psychologii Zdrowia PTP</span>
          </a>
          <a class="partner" href="http://www.psychoterapiaintegracyjna.pl" target="_blank" rel="noopener">
            <span class="partner-logo"><img src="assets/img/logo-pspi.png" alt="Polskie Stowarzyszenie Psychoterapii Integracyjnej" loading="lazy"></span>
            <span class="partner-name">Polskie Stowarzyszenie Psychoterapii Integracyjnej</span>
          </a>
        </div>

        <div class="banner-box">
          <h2>Mój banner</h2>
          <a href="assets/img/banner-alter-ego.png" target="_blank"><img src="assets/img/banner-alter-ego.png" alt="ALTER EGO – banner" width="400" height="92" loading="lazy"></a>
        </div>
      </div>
    </section>
"""

# --------------------------------------------------------------------------
# Orientacja teoretyczna
# --------------------------------------------------------------------------
ORIENT = f"""
    <section class="section section-tight">
      <div class="container article">
        <div class="article-body">
          <p class="lead-text">Pracuję w podejściu integracyjnym, co oznacza, że korzystam z dorobku różnych szkół psychoterapii. Sposób pracy dostosowuję do problemów klienta i jego indywidualności.</p>
          <p>Najwięcej czerpię z nurtów psychoterapii:</p>
          <ul class="tags">
            <li>psychodynamicznej</li>
            <li>egzystencjalnej</li>
            <li>humanistycznej</li>
            <li>Gestalt</li>
            <li>poznawczo-behawioralnej</li>
          </ul>
          <h2>Podstawowe założenia</h2>
          <ol class="principles">
            <li>Doświadczenia z dzieciństwa znacząco wpływają na dorosłe życie człowieka. Ich ślady mogą być źródłem cierpienia utrudniającego bieżące funkcjonowanie i rozwój.</li>
            <li>Niezależnie od przeszłości człowiek może mieć większy wpływ na swoje życie w pożądanym przez siebie kierunku.</li>
            <li>Możliwe jest zmniejszenie wpływu trudnych, urazowych doświadczeń z przeszłości na bieżące życie. Człowiek jest zdolny pokonywać ograniczenia, zmieniać destrukcyjne schematy na takie, które zwiększają jego szanse na realizację ważnych dla niego celów i wartości.</li>
            <li>Poszerzanie świadomości siebie we wszystkich sferach: ciała, myśli, spostrzeżeń i emocji pomaga lepiej radzić sobie z aktualnymi wyzwaniami.</li>
            <li>Jednym ze źródeł trudności życiowych są destrukcyjne przekonania, które mają wpływ na emocje i zachowanie. Można nauczyć się rozpoznawania, eliminowania lub korygowania dysfunkcyjnego myślenia.</li>
            <li>Istotnym czynnikiem leczącym jest relacja terapeutyczna. Rolą terapeuty jest towarzyszenie klientowi, pomaganie mu w przyjmowaniu odpowiedzialności za podejmowane decyzje i ich konsekwencje, stwarzanie mu warunków do samorozwoju.</li>
          </ol>
        </div>
        <aside class="article-aside">
          {figure('orientacja-teoretyczna.jpg', 'Czarna kula – orientacja teoretyczna')}
        </aside>
      </div>
    </section>
"""

# --------------------------------------------------------------------------
# Cennik
# --------------------------------------------------------------------------
CENNIK = f"""
    <section class="section section-tight">
      <div class="container narrow">
        <dl class="prices">
          <div class="price-row">
            <dt>konsultacja, porada<span>do 50 min.</span></dt>
            <dd>200 zł<small>w soboty – 300 zł</small></dd>
          </div>
          <div class="price-row">
            <dt>psychoterapia indywidualna<span>sesja 50 min.</span></dt>
            <dd>200 zł<small>w soboty – 300 zł</small></dd>
          </div>
          <div class="price-row">
            <dt>terapia par<span>sesja</span></dt>
            <dd>280 zł<small>w soboty – 400 zł</small></dd>
          </div>
          <div class="price-row">
            <dt>psychoterapia grupowa<span>cały program to 200 godzin w ciągu 8 miesięcy</span></dt>
            <dd>800 zł<small>miesięcznie (40 zł za godzinę)</small></dd>
          </div>
          <div class="price-row">
            <dt>warsztaty, treningi</dt>
            <dd class="dd-text">cena ustalana indywidualnie</dd>
          </div>
        </dl>
        <p class="note">W uzasadnionych przypadkach można liczyć na zniżkę lub raty.</p>
        <p class="muted">Zasady odwoływania i przekładania spotkań: <a href="pierwsza-wizyta.html#odwolywanie">pierwsza wizyta i zasady współpracy</a>.</p>
        <div class="account">
          <span class="eyebrow">Numer konta</span>
          <div class="account-row">
            <span class="account-no">85 1140 2004 0000 3902 5369 6072</span>
            <button type="button" class="btn btn-ghost btn-sm" data-copy="85114020040000390253696072">{ICON['copy']} <span>Kopiuj</span></button>
          </div>
        </div>
      </div>
    </section>
"""

# --------------------------------------------------------------------------
# Kontakt
# --------------------------------------------------------------------------
KONTAKT = f"""
    <section class="section section-tight">
      <div class="container contact-grid">
        <div class="contact-card">
          <p class="contact-org"><strong>ALTER EGO</strong><br>Gabinet Psychoterapii i Rozwoju Osobistego<br>Bożena Słomińska</p>
          <ul class="contact-list">
            <li>{ICON['pin']}<span>Szosa Chełmińska 154E/2<br>87-100 Toruń</span></li>
            <li>{ICON['phone']}<span><a href="{PHONE_HREF}">tel. 609 881 788</a><br><small class="muted">Gdy nie mogę odebrać, oddzwaniam.</small></span></li>
            <li>{ICON['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>{ICON['fb']}<a href="{FACEBOOK}" target="_blank" rel="noopener">facebook.com/alterego.torun</a></li>
          </ul>
          <div class="actions">
            <a class="btn btn-primary" href="{MAP_ROUTE}" target="_blank" rel="noopener">{ICON['route']} Wyznacz trasę</a>
            <a class="btn btn-ghost" href="{MAP_OPEN}" target="_blank" rel="noopener">{ICON['pin']} Zobacz większą mapę</a>
            <a class="btn btn-ghost" href="{VCARD}" download>{ICON['card']} Zapisz kontakt w telefonie</a>
          </div>
        </div>
        {map_frame()}
      </div>
    </section>
"""

PIERWSZA = f"""
    <section class="section section-tight">
      <div class="container article">
        <div class="article-body">
          <h2>Jak umówić wizytę</h2>
          <p>Na spotkanie można umówić się telefonicznie – <a href="{PHONE_HREF}">{PHONE}</a> – lub mailowo – <a href="mailto:{EMAIL}">{EMAIL}</a>. Gdy nie mogę odebrać, oddzwaniam. Skierowanie nie jest potrzebne.</p>

          <h2>Pierwsze spotkanie</h2>
          <p>Pierwsze spotkanie ma charakter konsultacji i trwa do 50 minut. Rozmawiamy o tym, co skłoniło Cię do szukania pomocy, jakie masz oczekiwania i czego potrzebujesz. Nie trzeba się do niego specjalnie przygotowywać – wystarczy przyjść i opowiedzieć o sobie tyle, ile chcesz.</p>
          <p>Zwykle potrzeba od jednego do kilku spotkań konsultacyjnych. Na ich podstawie wspólnie decydujemy, czy i w jakiej formie podjąć dalszą pracę – psychoterapii indywidualnej, terapii par, psychoterapii grupowej, poradnictwa czy interwencji kryzysowej.</p>

          <h2>Kontrakt terapeutyczny</h2>
          <p>Przed rozpoczęciem psychoterapii ustalamy wspólnie zasady współpracy (kontrakt):</p>
          {ul(['cel terapii – to, nad czym chcemy pracować,', 'częstotliwość spotkań – zwykle raz w tygodniu, w stałym dniu i o stałej godzinie,', 'czas trwania sesji – 50 minut,', 'wysokość i sposób opłaty,', 'zasady odwoływania spotkań i przerw urlopowych.'])}

          <h2>Poufność</h2>
          <p>Wszystko, co zostanie powiedziane podczas spotkań, objęte jest tajemnicą zawodową. Nie przekazuję nikomu informacji o tym, że ktoś korzysta z pomocy w gabinecie, ani o treści rozmów.</p>
          <p>Wyjątki od tej zasady przewidują przepisy prawa – przede wszystkim sytuacje bezpośredniego zagrożenia życia lub zdrowia klienta albo innych osób.</p>
          <p>W trosce o jakość pracy korzystam z superwizji i zawodowych konsultacji – omawiane sytuacje są przedstawiane w sposób, który nie pozwala rozpoznać klienta.</p>

          <h2 id="odwolywanie">Odwoływanie i przekładanie spotkań</h2>
          {ul(['Jeśli nie możesz przyjść, odwołaj lub przełóż spotkanie najpóźniej 24 godziny wcześniej – telefonicznie, SMS-em lub mailowo.', 'Spotkanie odwołane później lub nieodwołane jest płatne jak sesja.', 'Spóźnienie nie wydłuża sesji – kończy się ona o ustalonej godzinie.', 'O planowanych przerwach (np. urlopowych) informujemy się nawzajem z wyprzedzeniem.'])}

          <h2>Opłaty</h2>
          <p>Opłata za spotkanie jest zgodna z <a href="cennik.html">cennikiem</a>. W uzasadnionych przypadkach można liczyć na zniżkę lub raty.</p>

          <h2>Pozostałe zasady</h2>
          {ul(['Między sesjami kontaktujemy się w sprawach organizacyjnych; ważne tematy omawiamy podczas spotkań.', 'Na sesję przychodzimy trzeźwi – spotkanie nie odbywa się pod wpływem alkoholu ani innych substancji psychoaktywnych.', 'Decyzję o zakończeniu terapii warto omówić na sesji – dobrym zwyczajem jest spotkanie podsumowujące.'])}
        </div>
        <aside class="article-aside">
          {figure('gabinet.jpg', 'Gabinet ALTER EGO w Toruniu')}
        </aside>
      </div>
    </section>

    <section class="section section-tight section-alt" id="pomoc-w-kryzysie">
      <div class="container narrow">
        <h2>Pomoc w kryzysie</h2>
        <p>Gabinet nie jest miejscem pomocy doraźnej. Jeśli Twoje życie lub zdrowie albo życie innej osoby jest zagrożone, nie czekaj na wizytę – skorzystaj z pomocy od razu:</p>
        <dl class="hotlines">
          <div><dt><a href="tel:112">112</a></dt><dd>numer alarmowy – w sytuacji bezpośredniego zagrożenia życia</dd></div>
          <div><dt><a href="tel:800702222">800 70 2222</a></dt><dd>Centrum Wsparcia dla Osób Dorosłych w Kryzysie Psychicznym – bezpłatnie, całodobowo</dd></div>
          <div><dt><a href="tel:116123">116 123</a></dt><dd>Kryzysowy Telefon Zaufania dla osób dorosłych – bezpłatnie</dd></div>
          <div><dt><a href="tel:116111">116 111</a></dt><dd>Telefon Zaufania dla Dzieci i Młodzieży – bezpłatnie, całodobowo</dd></div>
        </dl>
        <p class="muted">Można też zgłosić się bezpośrednio na izbę przyjęć najbliższego szpitala psychiatrycznego lub do szpitalnego oddziału ratunkowego.</p>
      </div>
    </section>
"""

PRYWATNOSC = f"""
    <section class="section section-tight">
      <div class="container narrow legal">
        <h2>1. Administrator danych</h2>
        <p>Administratorem danych osobowych jest Bożena Słomińska, prowadząca ALTER EGO Gabinet Psychoterapii i Rozwoju Osobistego, Szosa Chełmińska 154E/2, 87-100 Toruń. Kontakt: <a href="mailto:{EMAIL}">{EMAIL}</a>, tel. {PHONE}.</p>

        <h2>2. Jakie dane przetwarzam i w jakim celu</h2>
        {ul(['<strong>Kontakt telefoniczny i mailowy</strong> – imię, nazwisko, numer telefonu, adres e-mail i treść wiadomości, w celu odpowiedzi i umówienia spotkania (art. 6 ust. 1 lit. b i f RODO).', '<strong>Psychoterapia i konsultacje</strong> – informacje przekazane podczas spotkań, w tym dotyczące zdrowia, w zakresie niezbędnym do udzielania pomocy psychologicznej; są one objęte tajemnicą zawodową (art. 9 ust. 2 lit. h RODO).', '<strong>Rozliczenia</strong> – dane niezbędne do wystawienia dokumentów księgowych (art. 6 ust. 1 lit. c RODO).'])}

        <h2>3. Jak długo przechowuję dane</h2>
        <p>Dane przechowuję przez czas potrzebny do realizacji celu, w którym zostały zebrane, a po jego zakończeniu – przez okres wymagany przepisami prawa (np. podatkowymi) lub do czasu przedawnienia ewentualnych roszczeń.</p>

        <h2>4. Komu przekazuję dane</h2>
        <p>Nie sprzedaję ani nie udostępniam danych innym podmiotom. Dostęp do nich mogą mieć wyłącznie dostawcy usług, z których korzystam (np. poczty elektronicznej, hostingu strony, biura rachunkowego) – w zakresie niezbędnym do świadczenia tych usług – oraz organy uprawnione na podstawie przepisów prawa.</p>

        <h2>5. Twoje prawa</h2>
        <p>Masz prawo dostępu do swoich danych, ich sprostowania, usunięcia, ograniczenia przetwarzania, przeniesienia oraz wniesienia sprzeciwu. Przysługuje Ci także prawo wniesienia skargi do Prezesa Urzędu Ochrony Danych Osobowych (ul. Stawki 2, 00-193 Warszawa).</p>

        <h2>6. Strona internetowa i pliki cookies</h2>
        <p>Strona nie korzysta z plików cookies ani z narzędzi analitycznych i nie zbiera danych przez formularze. Czcionki są wczytywane z tego samego serwera co strona. Serwer, na którym działa strona, może – jak każdy serwer – zapisywać techniczne logi (np. adres IP, datę wizyty), wykorzystywane wyłącznie do zapewnienia jego działania i bezpieczeństwa.</p>

        <h3 id="mapa">Mapa Google</h3>
        <p>Mapa z lokalizacją gabinetu jest wczytywana dopiero po kliknięciu przycisku „Pokaż mapę Google”. Wówczas przeglądarka łączy się z serwerami Google Ireland Ltd., które mogą przetwarzać Twój adres IP i zapisywać pliki cookies zgodnie z <a href="https://policies.google.com/privacy?hl=pl" target="_blank" rel="noopener">polityką prywatności Google</a>. Twój wybór jest zapamiętywany wyłącznie w Twojej przeglądarce; możesz go w każdej chwili wycofać:</p>
        <p><button type="button" class="btn btn-ghost btn-sm" data-map-revoke>Nie wyświetlaj mapy automatycznie</button></p>

        <h3>Linki zewnętrzne</h3>
        <p>Strona zawiera odnośniki do innych serwisów (np. Facebook, Mapy Google, strony organizacji, z którymi współpracuję). Po przejściu do nich obowiązują zasady prywatności tych serwisów.</p>

        <p class="muted">Ostatnia aktualizacja: wrzesień 2026.</p>
      </div>
    </section>
"""

NOT_FOUND = """
    <section class="section section-tight">
      <div class="container narrow">
        <p>Strona, której szukasz, nie istnieje lub zmieniła adres.</p>
        <div class="actions">
          <a class="btn btn-primary" href="index.html">Strona główna</a>
          <a class="btn btn-ghost" href="kontakt.html">Kontakt</a>
        </div>
      </div>
    </section>
"""


PAGES = [
    ("index.html", None,
     "Gabinet Psychoterapii i Rozwoju Osobistego ALTER EGO w Toruniu. Bożena Słomińska – psychoterapia indywidualna, grupowa, terapia par, poradnictwo, interwencja kryzysowa, treningi.",
     HOME, None, None, None),
    ("komu-pomagam.html", "komu pomagam",
     "Komu pomagam – osoby dorosłe w trudnościach osobistych, osoby zainteresowane rozwojem, profesjonaliści pomagający innym.",
     KOMU, "alter ego", "Komu pomagam", None),
    ("formy-pomocy.html", "formy pomocy",
     "Formy pomocy: psychoterapia indywidualna, psychoterapia grupowa, terapia par, terapia DDA i DDD, poradnictwo rodzinne, interwencja kryzysowa.",
     FORMY, "alter ego", "Formy pomocy", None),
    ("oferta-szkoleniowa.html", "oferta szkoleniowa",
     "Oferta szkoleniowa: trening interpersonalny, treningi komunikacji, asertywności, warsztaty wychowawcze, programy rozwoju osobistego.",
     OFERTA, "alter ego", "Oferta szkoleniowa", None),
    ("o-mnie.html", "o mnie",
     "Bożena Słomińska – psychoterapeuta z certyfikatem PSPI, trener rozwoju osobistego z rekomendacjami PTP. Wykształcenie i doświadczenie.",
     OMNIE, "o mnie", "Bożena Słomińska", None),
    ("wspolpracuje.html", "współpracuję",
     "Współpracuję: Na wzgórzu, Instytut Psychologii Zdrowia PTP, Polskie Stowarzyszenie Psychoterapii Integracyjnej.",
     WSPOL, "alter ego", "Współpracuję", None),
    ("orientacja-teoretyczna.html", "orientacja teoretyczna",
     "Orientacja teoretyczna – podejście integracyjne: psychodynamiczne, egzystencjalne, humanistyczne, Gestalt, poznawczo-behawioralne.",
     ORIENT, "alter ego", "Orientacja teoretyczna", None),
    ("cennik.html", "cennik",
     "Cennik: konsultacja, psychoterapia indywidualna, terapia par, psychoterapia grupowa, warsztaty i treningi.",
     CENNIK, "alter ego", "Cennik", None),
    ("pierwsza-wizyta.html", "pierwsza wizyta",
     "Pierwsza wizyta w gabinecie ALTER EGO: jak się umówić, jak wygląda konsultacja, kontrakt terapeutyczny, poufność, zasady odwoływania spotkań, pomoc w kryzysie.",
     PIERWSZA, "alter ego", "Pierwsza wizyta i zasady współpracy", None),
    ("polityka-prywatnosci.html", "polityka prywatności",
     "Polityka prywatności gabinetu ALTER EGO – administrator danych, cele przetwarzania, prawa osób, pliki cookies i mapa Google.",
     PRYWATNOSC, "alter ego", "Polityka prywatności", None),
    ("kontakt.html", "kontakt",
     "Kontakt: ALTER EGO, Bożena Słomińska, Szosa Chełmińska 154E/2, 87-100 Toruń, tel. 609 881 788, kontakt@alterego-torun.pl.",
     KONTAKT, "alter ego", "Kontakt", None),
]


def main():
    for filename, title, desc, body, eyebrow, heading, lead in PAGES:
        (ROOT / filename).write_text(
            layout(filename, title, desc, body, eyebrow, heading, lead), encoding="utf-8")
        print("wrote", filename)

    (ROOT / "404.html").write_text(
        layout("404.html", "nie znaleziono strony", "Nie znaleziono strony.", NOT_FOUND,
               "błąd 404", "Nie znaleziono strony"), encoding="utf-8")

    urls = "\n".join(
        f"  <url><loc>{SITE_URL}{'' if f == 'index.html' else f}</loc></url>" for f, *_ in PAGES)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    print("wrote 404.html, sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
