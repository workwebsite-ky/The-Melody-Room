# The Melody Room — Website

A five-page, production-ready static site. No build step, no dependencies, no
server required. Upload the folder to any host and it works.

---

## READ THIS FIRST — what needs your input

I built this without the logo or photos (the file upload came through empty, and
Facebook/Instagram block automated downloading). Five things need a decision
before you publish:

| # | Item | Where | Why |
|---|------|-------|-----|
| 1 | **Brand colours** | `css/style.css` line ~18 | I chose a palette. Swap it for the real logo colours — instructions below. |
| 2 | **The logo** | `assets/images/logo-mark.svg` | I designed a placeholder mark. Replace with the real logo. |
| 3 | **Sam's photo** | `assets/images/founder-placeholder.svg` | Currently an illustrated placeholder on the About page. |
| 4 | **Prices** | `tickets.html` | The ticket and sponsorship figures are invented placeholders. **Do not publish without checking these.** |
| 5 | **Phone number** | see below | Two different numbers are in circulation. |

**On the phone number:** you gave me `+1 870-882-6696` and that is what the site
uses. The Melody Room Facebook page currently lists `(417) 766-8251`. Confirm
which one should be public and update it if needed (search the files for
`8708826696`).

**On "nonprofit":** you asked me to describe the business as *Music • Arts •
Community • Opportunity* rather than a nonprofit music program, so that is the
language used throughout. Note that recent local reporting says the organisation
was granted nonprofit status and has a board — I used the board names on the
About page. If any of that is out of date, edit `about.html`.

---

## Pages

| File | Purpose |
|------|---------|
| `index.html` | Home — hero, programs, why us, press story, FAQ |
| `programs.html` | The six program formats in detail |
| `tickets.html` | Ticket tiers, sponsorship tiers, private hire |
| `about.html` | Sam's story, timeline, mission, board, press |
| `contact.html` | Contact form, details, Google Map |

---

## Changing the colours (2 minutes)

Every colour on the site comes from six variables at the top of `css/style.css`:

```css
:root {
  --ink:    #120B18;   /* darkest background       */
  --velvet: #241432;   /* secondary dark           */
  --brass:  #E9A93F;   /* PRIMARY accent           */
  --gel:    #FF3D68;   /* SECONDARY accent         */
  --cool:   #4CC9E0;   /* tertiary, used sparingly */
  --ivory:  #F7F2E8;   /* light sections           */
}
```

Change `--brass` and `--gel` to the logo's two main colours and the whole site
re-themes — buttons, gradients, borders, icons, hover states, everything.

The artwork carries the same colours. After changing the palette, edit the
matching values at the top of `_source/build_assets.py` and run
`python3 _source/build_assets.py` to regenerate every image in the new colours.

**Contrast check:** if you pick a light primary colour, check the text on the
gradient buttons is still readable — button text is dark on purpose.

---

## Replacing the images

All artwork lives in `assets/images/`. Keep the **same filename** and the site
picks it up with no code changes.

| File | Replace with | Size |
|------|--------------|------|
| `logo-mark.svg` | The real logo (SVG best, PNG fine) | square |
| `founder-placeholder.svg` | Photo of Sam | ~800×1000, portrait |
| `hero-stage.svg` | A wide crowd/stage photo | ~1600×800 |
| `prog-*.svg` (6 files) | Real photos of each program | ~800×600 |
| `og-image.jpg` | Social share image | exactly 1200×630 |

If you swap an SVG for a `.jpg` or `.png`, update the filename in the `src="..."`
of the relevant page too.

**On using photos from Facebook and Instagram:** several of the best shots of
your events are credited to Guerrilla Creative Photography and to Brandon Alms
(the Biz 417 portrait). Get written permission before putting those on the site —
photographers retain copyright even for photos of your own events.

Compress photos before uploading (squoosh.app or tinypng.com). Aim under 300 KB
each; the site is fast right now and large images are the usual thing that ruins
that.

---

## The contact form

The form validates in the browser, then opens the visitor's own email app with
the message pre-filled and addressed to `themelodyroom417@yahoo.com`. That means
it works the moment you upload it, with nothing to configure.

The trade-off: it relies on the visitor having an email app set up. To collect
submissions properly instead, sign up for [Formspree](https://formspree.io) or
use Netlify Forms, then in `contact.html` change:

```html
<form id="contact-form" data-to="themelodyroom417@yahoo.com" novalidate>
```

to:

```html
<form id="contact-form" action="https://formspree.io/f/YOUR_ID" method="POST">
```

and delete the `contactForm()` line inside `init()` at the bottom of
`js/script.js`.

To change the destination address, edit `data-to` on that form tag.

---

## Publishing

**Easiest (free):** go to [app.netlify.com/drop](https://app.netlify.com/drop)
and drag this whole folder onto the page. It is live in about 30 seconds. Then
connect `themelodyroom417.com` in Netlify's domain settings.

**Traditional hosting:** upload everything to `public_html` via FTP. Keep the
folder structure exactly as-is — `index.html` must sit at the top level, with
`css/`, `js/` and `assets/` beside it.

After going live:
1. Update `SITE` in `_source/_partials.py` if the domain differs, and rebuild.
2. Submit the site to [Google Search Console](https://search.google.com/search-console).
3. Add the website link to the Facebook and Instagram bios.

---

## What is built in

- Responsive from 320px up; tested at 390px, 768px and 1440px
- Sticky nav that compacts on scroll, full-screen mobile menu
- Loading animation, scroll reveals, animated counters, parallax, hover states
- A spotlight in the hero that follows the cursor (drifts on its own on phones)
- FAQ accordion, back-to-top, floating WhatsApp button
- SEO: unique titles and meta descriptions per page, Open Graph and Twitter
  cards, canonical URLs, `PerformingGroup` and `FAQPage` structured data,
  alt text on every image, one `<h1>` per page
- Accessibility: skip link, keyboard focus outlines, ARIA on the menu, accordion
  and form, `prefers-reduced-motion` respected throughout
- Performance: no frameworks, no jQuery, SVG artwork (a few KB each), lazy
  loading below the fold

---

## Regenerating things

The `_source/` folder holds the scripts that produced this site. You never need
them to edit the site by hand — HTML, CSS and JS are all plain and commented.

```bash
cd _source
python3 build_assets.py   # regenerate artwork (needs: pip install pillow)
python3 build_site.py     # regenerate the five HTML pages
```

`build_site.py` builds all pages from shared header/footer templates in
`_partials.py`, so changing the nav or footer once updates all five pages. If
you edit the HTML by hand instead, do not re-run it — it will overwrite your
changes.

---

## Content sources

The copy is based on published reporting rather than invented:

- Biz 417, *How Sam Timmerman Creates Space for Creatives at the Melody Room*, Sept 2025
- Springfield Daily Citizen, coverage of The Melody Room and its nonprofit status
- The Melody Room's own Facebook and Instagram profiles and event listings

Both quotes on the site are real, short and credited to their publication. The
Emili German story is reported by Biz 417.

**There are no invented customer testimonials on this site** — I left them out
rather than fake them. To add some, copy genuine reviews from your Facebook page
(you have 50) into the `.quote-card` blocks in `index.html`. There is a comment
in the file marking the spot.
