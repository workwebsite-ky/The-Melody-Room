#!/usr/bin/env python3
"""
Builds the five HTML pages from shared partials so the nav, footer and SEO
markup can never drift apart. Re-run after editing any template below.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE   = "https://themelodyroom417.com"
NAME   = "The Melody Room"
EMAIL  = "themelodyroom417@yahoo.com"
PHONE  = "+1 870-882-6696"
TEL    = "+18708826696"
WA     = "18708826696"
CITY   = "Springfield"
REGION = "MO"
ZIP    = "65803"
FB     = "https://www.facebook.com/TheMelodyRoom417"
IG     = "https://www.instagram.com/themelodyroom417/"

# ---------------------------------------------------------------- icon set
LOGO = '''<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false">
      <defs><linearGradient id="bg-%s" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
        <stop offset="0" stop-color="#E9A93F"/><stop offset="1" stop-color="#FF3D68"/></linearGradient></defs>
      <rect x="2" y="2" width="60" height="60" rx="17" fill="none" stroke="url(#bg-%s)" stroke-width="3.2"/>
      <path d="M17 50V28a15 15 0 0 1 30 0v22" fill="none" stroke="url(#bg-%s)" stroke-width="3.2" stroke-linecap="round"/>
      <g fill="url(#bg-%s)"><rect x="23.4" y="40" width="3.6" height="7" rx="1.8"/>
      <rect x="30.2" y="34" width="3.6" height="13" rx="1.8"/>
      <rect x="37" y="37.5" width="3.6" height="9.5" rx="1.8"/></g></svg>'''

TICK = ('<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10.5l4 4 8-9"/></svg>')

IC_MAIL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
           '<rect x="2.5" y="4.5" width="19" height="15" rx="2.5"/><path d="M3 7l9 6 9-6"/></svg>')
IC_PHONE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
            '<path d="M6 3h3l2 5-2.5 1.5a12 12 0 006 6L16 13l5 2v3a2 2 0 01-2.2 2A17 17 0 014 5.2 2 2 0 016 3z"/></svg>')
IC_PIN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
          '<path d="M12 21s7-5.6 7-11a7 7 0 10-14 0c0 5.4 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>')
IC_CLOCK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
            '<circle cx="12" cy="12" r="9"/><path d="M12 7v5.5l3.5 2"/></svg>')

IC_FB = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-8h2.7l.4-3.1h-3.1V7.9c0-.9.25-1.5 1.55-1.5H16.7V3.6A21 21 0 0014.3 3.5c-2.4 0-4 1.46-4 4.14V9.9H7.6V13h2.7v8z"/></svg>')
IC_IG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
         '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.1" fill="currentColor" stroke="none"/></svg>')
IC_WA = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 00-8.6 15L2 22l5.2-1.4A10 10 0 1012 2zm0 2a8 8 0 016.8 12.2l-.3.5.8 2.8-2.9-.8-.5.3A8 8 0 1112 4zm-3.4 4c-.2 0-.5.1-.7.4-.3.3-.9.9-.9 2.1s.9 2.4 1 2.6c.1.2 1.7 2.8 4.3 3.8 2.1.8 2.6.7 3 .6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.6-.3-1.6-.8c-.2-.1-.4-.1-.6.1l-.8 1c-.2.2-.3.2-.5.1a6.6 6.6 0 01-3.3-2.9c-.1-.2 0-.4.1-.5l.5-.6.2-.4v-.4l-.7-1.7c-.2-.5-.4-.4-.6-.4z"/></svg>')

IC_ARROW_UP = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
               'stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5"/><path d="M5.5 11.5L12 5l6.5 6.5"/></svg>')

NAV_ITEMS = [
    ("index.html", "Home"),
    ("programs.html", "Programs"),
    ("tickets.html", "Tickets &amp; Partners"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]


# ------------------------------------------------------------------- HEAD
def head(title, desc, page, extra_schema=""):
    links = "\n        ".join(
        f'<a href="{h}">{t}</a>' for h, t in NAV_ITEMS
    )
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- ============================== SEO ============================== -->
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{page}">
<meta name="theme-color" content="#120B18">
<meta name="author" content="{NAME}">
<meta name="robots" content="index, follow">

<!-- Open Graph / social sharing -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{page}">
<meta property="og:image" content="{SITE}/assets/images/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/images/og-image.jpg">

<!-- Local SEO -->
<meta name="geo.region" content="US-MO">
<meta name="geo.placename" content="{CITY}, {REGION}">

<link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
<link rel="apple-touch-icon" href="assets/images/logo-mark.svg">

<!-- Fonts: Anton (poster display) / Inter Tight (body) / Space Mono (run-sheet labels) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter+Tight:wght@400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">

<link rel="stylesheet" href="css/style.css">

<!-- Structured data: helps Google show the venue in local results -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "PerformingGroup",
  "name": "{NAME}",
  "url": "{SITE}",
  "logo": "{SITE}/assets/images/logo-mark.svg",
  "image": "{SITE}/assets/images/og-image.jpg",
  "description": "A live event platform in {CITY}, Missouri offering stage time for music, spoken word and performance art.",
  "foundingDate": "2022",
  "founder": {{ "@type": "Person", "name": "Sam Timmerman" }},
  "email": "{EMAIL}",
  "telephone": "{PHONE}",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "{CITY}",
    "addressRegion": "{REGION}",
    "postalCode": "{ZIP}",
    "addressCountry": "US"
  }},
  "sameAs": ["{FB}", "{IG}"]
}}
</script>
{extra_schema}
</head>
<body>

<a class="skip" href="#main">Skip to content</a>

<!-- ========================= LOADING ANIMATION ========================= -->
<div id="preloader">
  <div class="preloader-inner">
    <div class="preloader-mark">{LOGO % ('pre', 'pre', 'pre', 'pre')}</div>
    <p class="preloader-label">House lights down</p>
    <div class="preloader-bar"><i></i></div>
  </div>
</div>

<!-- ============================== NAV ============================== -->
<header class="nav">
  <div class="nav-inner">
    <a class="brand" href="index.html" aria-label="{NAME} — home">
      {LOGO % ('nav', 'nav', 'nav', 'nav')}
      <span class="brand-text">
        <span class="brand-name">{NAME}</span>
        <span class="brand-sub">Springfield, Missouri</span>
      </span>
    </a>

    <nav class="nav-links" id="nav-links" aria-label="Main">
      {links}
      <a class="btn btn--primary" href="contact.html#lineup">Get on the lineup</a>
    </nav>

    <div class="nav-cta">
      <a class="btn btn--primary" href="contact.html#lineup">Get on the lineup</a>
    </div>

    <button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav-links">
      <i></i><i></i><i></i>
    </button>
  </div>
</header>

<main id="main">
'''


# ----------------------------------------------------------------- FOOTER
def footer():
    prog = "\n        ".join(
        f'<a href="programs.html#{s}">{n}</a>' for s, n in [
            ("open-mic", "Open Mic Nights"), ("spotlight", "Featured Artist Spotlight"),
            ("concerts", "Intimate Concerts"), ("safe-haven", "Safe Haven Concerts"),
            ("workshops", "Artist Workshops"), ("private", "Private &amp; Corporate Events")])
    return f'''</main>

<!-- ============================== FOOTER ============================== -->
<footer class="footer">
  <div class="shell">
    <div class="footer-grid">

      <div class="footer-brand">
        <a class="brand" href="index.html" aria-label="{NAME} — home">
          {LOGO % ('ft', 'ft', 'ft', 'ft')}
          <span class="brand-text">
            <span class="brand-name">{NAME}</span>
            <span class="brand-sub">Springfield, Missouri</span>
          </span>
        </a>
        <p class="muted">Music. Arts. Community. Opportunity. A stage in {CITY} for the
        artists nobody has heard yet &mdash; and the audiences who find them first.</p>
        <div class="socials">
          <a href="{FB}" target="_blank" rel="noopener" aria-label="{NAME} on Facebook">{IC_FB}</a>
          <a href="{IG}" target="_blank" rel="noopener" aria-label="{NAME} on Instagram">{IC_IG}</a>
          <a href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="Message us on WhatsApp">{IC_WA}</a>
        </div>
      </div>

      <div>
        <h4>Explore</h4>
        <nav class="footer-links" aria-label="Footer">
          <a href="index.html">Home</a>
          <a href="programs.html">Programs</a>
          <a href="tickets.html">Tickets &amp; Partners</a>
          <a href="about.html">About</a>
          <a href="contact.html">Contact</a>
        </nav>
      </div>

      <div>
        <h4>Programs</h4>
        <nav class="footer-links" aria-label="Programs">
        {prog}
        </nav>
      </div>

      <div>
        <h4>Reach us</h4>
        <nav class="footer-links">
          <a href="mailto:{EMAIL}">{EMAIL}</a>
          <a href="tel:{TEL}">{PHONE}</a>
          <a href="contact.html">{CITY}, {REGION} {ZIP}</a>
          <a href="contact.html#lineup">Perform with us</a>
        </nav>
      </div>

    </div>

    <div class="footer-base">
      <span>&copy; <span data-year>2026</span> {NAME}. All rights reserved.</span>
      <span>Music &bull; Arts &bull; Community &bull; Opportunity</span>
    </div>
  </div>
</footer>

<!-- ========================= FLOATING ACTIONS ========================= -->
<a class="quick-chat" href="https://wa.me/{WA}" target="_blank" rel="noopener"
   aria-label="Message {NAME} on WhatsApp">{IC_WA}</a>
<button class="to-top" type="button" aria-label="Back to top">{IC_ARROW_UP}</button>

<script src="js/script.js"></script>
</body>
</html>
'''


# -------------------------------------------------------- shared fragments
def cta_band(title, text, primary=("contact.html#lineup", "Get on the lineup"),
             ghost=("tickets.html", "See tickets &amp; passes")):
    return f'''
<section class="section cta-band">
  <div class="shell shell--narrow">
    <p class="eyebrow eyebrow--center" data-reveal>Next step</p>
    <h2 data-reveal>{title}</h2>
    <p class="lead" data-reveal style="margin-bottom:2.2rem">{text}</p>
    <div class="btn-row" data-reveal>
      <a class="btn btn--primary" href="{primary[0]}">{primary[1]}</a>
      <a class="btn btn--ghost" href="{ghost[0]}">{ghost[1]}</a>
    </div>
  </div>
</section>
'''


def marquee():
    genres = ["R&amp;B", "Soul", "Neo Soul", "Gospel", "Funk", "Country", "Rock", "Jazz",
              "Hip-Hop", "Bluegrass", "Spoken Word", "Comedy", "Christian Contemporary"]
    lis = "".join(f"<li>{g}</li>" for g in genres)
    return f'<div class="marquee" aria-hidden="true"><ul>{lis}</ul></div>\n'


def page_head(crumb, title, lead):
    return f'''
<section class="page-head">
  <div class="shell">
    <p class="crumbs" data-reveal><a href="index.html">Home</a> &nbsp;/&nbsp; {crumb}</p>
    <h1 data-reveal>{title}</h1>
    <p class="lead" data-reveal>{lead}</p>
  </div>
</section>
'''


def write(name, body):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(body)
    print("  ", name)
