#!/usr/bin/env python3
"""Builds the five site pages."""
from _partials import *   # noqa

# ==========================================================================
# 1. HOME
# ==========================================================================
PROGRAMS = [
    ("open-mic", "prog-open-mic.svg", "Free entry", "card-tag--free", "Open Mic Nights",
     "The night this whole thing was built for. Sign up, take the stage, play to a room "
     "that actually listens. Music, comedy and spoken word all share the same mic, and "
     "the cover is free every time."),
    ("spotlight", "prog-poetry.svg", "Monthly", "card-tag--gel", "Featured Artist Spotlight",
     "One artist per night gets more than three songs. A full set, a proper introduction "
     "and a live band behind them &mdash; the platform most emerging performers in "
     "Springfield are never handed."),
    ("concerts", "prog-concerts.svg", "Ticketed", "", "Intimate Live Concerts",
     "Curated, close-up shows where the back row is still close enough to see a musician's "
     "hands. Soul, jazz, gospel, country, hip-hop and everything between, programmed as a "
     "single evening rather than a lineup."),
    ("safe-haven", "prog-safe-haven.svg", "Community", "card-tag--free", "Safe Haven Concerts",
     "A quarterly concert series built with Community Partners of the Ozarks as part of "
     "their gun safety and violence reduction work &mdash; using a stage, rather than a "
     "podium, to talk about keeping the city safe."),
    ("workshops", "prog-workshops.svg", "Growing", "", "Artist Development Workshops",
     "Practical sessions on the parts of a music career nobody teaches: stage presence, "
     "booking yourself, pricing your work and building an audience that shows up more "
     "than once."),
    ("private", "prog-private.svg", "By request", "card-tag--gel", "Private &amp; Corporate Events",
     "Bring the room to your event. We curate the lineup, provide the band and run the "
     "night end to end for fundraisers, launches, weddings and company celebrations "
     "across southwest Missouri."),
]

cards = ""
for pid, img, tag, tagmod, title, desc in PROGRAMS:
    cards += f'''
      <article class="card" data-reveal>
        <div class="card-media">
          <img src="assets/images/{img}" alt="{title} at {NAME} in {CITY}, Missouri"
               width="800" height="600" loading="lazy" decoding="async">
          <span class="card-tag {tagmod}">{tag}</span>
        </div>
        <div class="card-body">
          <h3>{title}</h3>
          <p>{desc}</p>
          <a class="link-arrow" href="programs.html#{pid}">Details <span>&rarr;</span></a>
        </div>
      </article>'''

WHY = [
    ("No gatekeeping", "You do not need a following, a manager or a release to get a slot. "
     "The founder was turned away from Springfield venues for being unknown, so being "
     "unknown is not a disqualifier here."),
    ("A room that listens", "Phones down, chairs facing the stage, sound that is actually "
     "mixed. Performers consistently tell us it is the first time an audience gave them "
     "real attention."),
    ("Every genre, one stage", "Gospel follows hip-hop follows bluegrass. The mix is "
     "deliberate &mdash; it is how audiences discover something they would never have "
     "bought a ticket for."),
    ("Run like a business", "Bookings confirmed in writing, set times published, sound "
     "check on schedule. A grassroots mission does not have to mean a chaotic night."),
]
why = ""
for i, (t, d) in enumerate(WHY, 1):
    why += f'''
      <article class="feature" data-reveal>
        <span class="feature-num">{i:02d}</span>
        <h3>{t}</h3>
        <p>{d}</p>
      </article>'''

FAQS = [
    ("How do I get a slot at an open mic?",
     "Send us a message through the contact page or reach out on Facebook or Instagram "
     "with your name, what you perform and roughly how long you need. Sign-ups also open "
     "at the door before each show, though slots fill quickly &mdash; messaging ahead is "
     "the safer route."),
    ("Do I have to pay to perform or to watch?",
     "Open mic nights are free to attend and free to perform. Ticketed shows are our "
     "curated concerts and special events, and those prices are listed on the tickets page."),
    ("What kind of acts do you book?",
     "Musicians, singers, bands, rappers, poets, spoken word artists and comedians. "
     "R&amp;B, soul, neo soul, gospel, funk, country, rock, jazz, hip-hop, bluegrass and "
     "Christian contemporary have all shared this stage."),
    ("Do you have your own venue?",
     "We host at partner venues around Springfield while we work toward a permanent home. "
     "Every event listing names the venue and address, so always check the current listing "
     "on Facebook before you travel."),
    ("Can I book The Melody Room for a private event?",
     "Yes. We curate lineups and run full evenings for fundraisers, corporate events, "
     "weddings and community programming. Email us with your date, venue and audience size "
     "and we will send a proposal."),
    ("How can a business support what you do?",
     "Through show sponsorship, season partnership or in-kind support such as venue space "
     "and equipment. Partnership tiers are on the tickets page, and we are happy to build "
     "something that fits your goals."),
]
faq = ""
for i, (q, a) in enumerate(FAQS):
    faq += f'''
      <div class="faq-item" data-reveal>
        <button class="faq-q" type="button" aria-expanded="false" aria-controls="faq-{i}">
          {q}<span class="faq-icon" aria-hidden="true"></span>
        </button>
        <div class="faq-a" id="faq-{i}"><div><p>{a}</p></div></div>
      </div>'''

FAQ_SCHEMA = '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + \
    ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (q.replace('"', "'"), a.replace("&mdash;", "-").replace("&amp;", "and").replace('"', "'"))
        for q, a in FAQS) + "]}\n</script>"

home = head(
    f"{NAME} | Live Music, Open Mic &amp; Spoken Word in {CITY}, MO",
    f"{NAME} is a live event platform in {CITY}, Missouri giving stage time to musicians, "
    f"poets and comedians. Free open mic nights, intimate concerts and artist spotlights. "
    f"Founded by Sam Timmerman.",
    "index.html", FAQ_SCHEMA)

home += f'''
<!-- ============================== HERO ============================== -->
<section class="hero">
  <img class="hero-bg" src="assets/images/hero-stage.svg"
       alt="Stage lighting washing over the audience at a {NAME} show" width="1600" height="800">
  <div class="spotlight" aria-hidden="true"></div>

  <div class="shell">
    <div class="hero-content">
      <p class="eyebrow">{CITY}, Missouri &nbsp;&bull;&nbsp; Est. 2022</p>
      <h1>
        <span class="reveal-word"><span style="animation-delay:.05s">A stage for</span></span><br>
        <span class="reveal-word"><span style="animation-delay:.15s">the artists</span></span><br>
        <span class="reveal-word"><span class="spill" style="animation-delay:.25s">nobody has</span></span><br>
        <span class="reveal-word"><span class="spill" style="animation-delay:.35s">heard yet.</span></span>
      </h1>
      <p class="lead">Our founder was turned away by local venues for being a &ldquo;no name.&rdquo;
      So he built the room he could not get into &mdash; and filled it. Music, spoken word and
      performance art in {CITY}, every genre welcome, no following required.</p>

      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html#lineup">Get on the lineup</a>
        <a class="btn btn--ghost" href="programs.html">See what&rsquo;s on</a>
      </div>

      <dl class="hero-meta">
        <div><dt>Open mic cover</dt><dd>Always free</dd></div>
        <div><dt>Genres booked</dt><dd>All of them</dd></div>
        <div><dt>Founded by</dt><dd>Sam Timmerman</dd></div>
      </dl>
    </div>
  </div>

  <div class="scroll-hint" aria-hidden="true"><span>Scroll</span><i></i></div>
</section>

{marquee()}

<!-- ============================== INTRO + STATS ============================== -->
<section class="section">
  <div class="shell">
    <div class="split">
      <div>
        <p class="eyebrow" data-reveal>The room</p>
        <h2 data-reveal>Springfield&rsquo;s stage for<br>the ones you have not<br>heard of yet</h2>
        <p class="lead" data-reveal>{NAME} started in 2022 as a live event platform for music,
        spoken word and performance art. It has grown into a hub for underrepresented voices
        and a genuine part of Springfield&rsquo;s creative economy &mdash; open mic nights,
        poetry events and curated shows that regularly play to a full room.</p>
        <p data-reveal>We are not a bar with a stage in the corner. Every night is programmed,
        every performer is introduced, and the audience comes to listen. That is the whole
        difference, and it is why artists keep coming back.</p>
        <div class="btn-row" data-reveal style="margin-top:1.8rem">
          <a class="btn btn--ghost" href="about.html">Read our story</a>
        </div>
      </div>

      <div data-reveal>
        <div class="stats">
          <div class="stat">
            <div class="stat-num"><span data-count="2022">0</span></div>
            <p class="stat-label">Founded in Springfield</p>
          </div>
          <div class="stat">
            <div class="stat-num"><span data-count="4">0</span></div>
            <p class="stat-label">Venues outgrown so far</p>
          </div>
          <div class="stat">
            <div class="stat-num"><span data-count="100">0</span>%</div>
            <p class="stat-label">Recommended across 50 Facebook reviews</p>
          </div>
          <div class="stat">
            <div class="stat-num">$<span data-count="0">0</span></div>
            <p class="stat-label">Cover charge on open mic nights</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================== PROGRAMS ============================== -->
<section class="section section--velvet" id="programs">
  <div class="shell">
    <div class="section-head">
      <p class="eyebrow" data-reveal>What we run</p>
      <h2 data-reveal>Six ways onto the stage</h2>
      <p class="lead" data-reveal>From a free Tuesday open mic to a fully produced concert,
      every format exists to put a working artist in front of a real audience.</p>
    </div>
    <div class="grid grid--3">{cards}
    </div>
  </div>
</section>

<!-- ============================== WHY US ============================== -->
<section class="section section--paper">
  <div class="shell">
    <div class="section-head">
      <p class="eyebrow" data-reveal>Why artists come back</p>
      <h2 data-reveal>What makes this room different</h2>
    </div>
    <div class="grid grid--4">{why}
    </div>
  </div>
</section>

<!-- ============================== STORY / PRESS ============================== -->
<!-- NOTE FOR THE CLIENT: the two quotes below are real, published and credited.
     To add audience testimonials, paste genuine reviews from your Facebook page
     into extra .quote-card blocks rather than inventing them. -->
<section class="section">
  <div class="shell">
    <div class="split split--flip">
      <div data-reveal>
        <div class="frame frame--wide" data-parallax="0.06">
          <img src="assets/images/prog-poetry.svg"
               alt="Spotlight on a spoken word performance at {NAME}"
               width="800" height="600" loading="lazy" decoding="async">
          <p class="frame-caption">Featured artist spotlight &bull; spoken word</p>
        </div>
      </div>
      <div>
        <p class="eyebrow" data-reveal>What happens here</p>
        <h2 data-reveal>One night, one poem,<br>a sold-out book</h2>
        <p class="lead" data-reveal>Local poet Emili German performed a tribute piece at one of
        our open mic nights. The audience gave her a standing ovation &mdash; and she sold out
        her debut book that same night.</p>
        <p data-reveal>That is the return we are after. Not applause, but a career moving one
        real step forward, in a city that had not made space for it yet.</p>
        <p class="muted" data-reveal style="font-family:var(--mono);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase">
          As reported by Biz 417, September 2025</p>
      </div>
    </div>

    <div class="grid grid--2" style="margin-top:clamp(3rem,6vw,4.5rem)">
      <article class="quote-card" data-reveal>
        <span class="quote-mark" aria-hidden="true">&ldquo;</span>
        <p>On why the platform is run with structure and strategy, not as a side project:
        <span class="accent">&ldquo;It&rsquo;s not a hobby, it&rsquo;s a business.&rdquo;</span></p>
        <p class="quote-by">Sam Timmerman, founder &bull; via Biz 417</p>
      </article>
      <article class="quote-card" data-reveal>
        <span class="quote-mark" aria-hidden="true">&ldquo;</span>
        <p>On why he keeps booking unknown performers:
        <span class="accent">&ldquo;I just do it because I love to see people happy.&rdquo;</span></p>
        <p class="quote-by">Sam Timmerman, founder &bull; via Springfield Daily Citizen</p>
      </article>
    </div>
  </div>
</section>

<!-- ============================== FAQ ============================== -->
<section class="section section--paper">
  <div class="shell shell--narrow">
    <div class="section-head section-head--center">
      <p class="eyebrow eyebrow--center" data-reveal>Questions</p>
      <h2 data-reveal>Before you come down</h2>
    </div>
    <div class="faq">{faq}
    </div>
  </div>
</section>

{cta_band("Bring us what you have been working on",
          "Whether you have played a hundred shows or none, there is a slot with your name on "
          "it. Tell us what you do and we will find you a night.")}
'''
home += footer()
write("index.html", home)


# ==========================================================================
# 2. PROGRAMS
# ==========================================================================
DETAIL = {
    "open-mic": ("Open Mic Nights", "Free entry", "prog-open-mic.svg", [
        "Sign-up opens at the door, and messaging ahead secures a slot",
        "Music, comedy and spoken word on the same bill",
        "House band available to back you if you need one",
        "No cover charge, ever",
    ], "Springfield open mic night for musicians, poets and comedians"),
    "spotlight": ("Featured Artist Spotlight", "Monthly", "prog-poetry.svg", [
        "A full set rather than a three-song slot",
        "Proper stage introduction and social promotion",
        "Live band accompaniment where it fits the material",
        "Photography and video you can keep and use",
    ], "Monthly featured artist showcase in Springfield, Missouri"),
    "concerts": ("Intimate Live Concerts", "Ticketed", "prog-concerts.svg", [
        "Curated lineups programmed as a single evening",
        "Close-up rooms where every seat is a good seat",
        "Professionally mixed sound and stage lighting",
        "Tickets released through our Facebook page and Eventbrite",
    ], "Intimate live music concerts in Springfield, MO"),
    "safe-haven": ("Safe Haven Concerts", "Community", "prog-safe-haven.svg", [
        "Run quarterly with Community Partners of the Ozarks",
        "Part of an ongoing gun safety and violence reduction initiative",
        "Free and open to the public",
        "Programming built with, not just for, the neighbourhoods involved",
    ], "Community concert series supporting gun safety in Springfield"),
    "workshops": ("Artist Development Workshops", "Growing", "prog-workshops.svg", [
        "Stage presence and performance craft",
        "Booking, pricing and negotiating your own shows",
        "Building an audience that returns",
        "Small groups, working musicians teaching",
    ], "Music and performance workshops for Springfield artists"),
    "private": ("Private &amp; Corporate Events", "By request", "prog-private.svg", [
        "Curated lineup matched to your audience",
        "Full production: band, sound, hosting and run of show",
        "Fundraisers, launches, weddings and company events",
        "Available across southwest Missouri",
    ], "Book live music and entertainment for private events in Springfield"),
}

blocks = ""
for idx, (pid, img, tag, tagmod, title, desc) in enumerate(PROGRAMS):
    d_title, d_tag, d_img, bullets, seo = DETAIL[pid]
    flip = " split--flip" if idx % 2 else ""
    lis = "".join(f'<li>{TICK}<span>{b}</span></li>' for b in bullets)
    tone = "section--paper" if idx % 2 else ""
    blocks += f'''
<section class="section {tone}" id="{pid}">
  <div class="shell">
    <div class="split{flip}">
      <div>
        <p class="eyebrow" data-reveal>{d_tag}</p>
        <h2 data-reveal>{d_title}</h2>
        <p class="lead" data-reveal>{desc}</p>
        <ul class="price-list" data-reveal style="margin-top:1.6rem">{lis}</ul>
        <div class="btn-row" data-reveal>
          <a class="btn btn--primary" href="contact.html#lineup">Ask about {d_title.split(" ")[0].lower()}</a>
        </div>
      </div>
      <div data-reveal>
        <div class="frame frame--wide" data-parallax="0.05">
          <img src="assets/images/{d_img}" alt="{seo}" width="800" height="600"
               loading="lazy" decoding="async">
          <p class="frame-caption">{seo}</p>
        </div>
      </div>
    </div>
  </div>
</section>'''

progpage = head(
    f"Programs | Open Mic, Concerts &amp; Workshops | {NAME}",
    f"Explore every {NAME} program in {CITY}, MO: free open mic nights, featured artist "
    f"spotlights, intimate concerts, Safe Haven community shows, artist workshops and "
    f"private event booking.",
    "programs.html")
progpage += page_head(
    "Programs",
    "Every way onto our stage",
    f"Six formats, one purpose: putting {CITY} artists in front of an audience that came "
    f"to listen. Pick the one that fits where you are in your career.")
progpage += marquee() + blocks
progpage += cta_band(
    "Not sure which night is yours?",
    "Tell us what you perform and how long you have been at it. We will point you to the "
    "right room.",
    ghost=("about.html", "Meet the founder"))
progpage += footer()
write("programs.html", progpage)


# ==========================================================================
# 3. TICKETS & PARTNERS
# ==========================================================================
# NOTE: prices are placeholders — see README before publishing.
TIERS = [
    ("Open mic", "Free", "every event", False,
     "The front door of everything we do. Come to watch or come to play &mdash; both cost nothing.",
     ["Free entry, no ticket needed", "Free performance slot", "House band backing available",
      "Music, comedy and spoken word welcome"], ("contact.html#lineup", "Reserve a slot")),
    ("Showcase ticket", "$15", "per person", True,
     "Entry to a curated concert night: a programmed lineup, full production and a room built "
     "for listening.",
     ["Reserved entry to one showcase", "Programmed lineup with full sound and lighting",
      "Early access to the next release", "Supports free open mic programming"],
     ("contact.html", "Get tickets")),
    ("Season pass", "$60", "six shows", False,
     "For the regulars. Six curated shows across the season at a lower rate per night, with "
     "first refusal on seats.",
     ["Entry to six curated showcases", "Priority seating before general release",
      "Invitations to closed rehearsals and previews", "Transferable if you cannot make a night"],
     ("contact.html", "Buy a season pass")),
]
PARTNERS = [
    ("Friend of the Room", "$250", "per year", False,
     "For individuals and small businesses who want the free nights to stay free.",
     ["Name credited on our website and socials", "Two tickets to a curated showcase",
      "Season programming sent to you first"], ("contact.html", "Become a friend")),
    ("Stage Sponsor", "$1,000", "per show", True,
     "Put your name on a single night, from the stage announcement to the printed bill.",
     ["Named sponsor of one full event", "Logo on all event artwork and promotion",
      "Verbal credit from the stage", "Six tickets and reserved seating",
      "Photography from the night for your own channels"], ("contact.html", "Sponsor a show")),
    ("Season Partner", "$2,500", "per season", False,
     "A season-long partnership for organisations investing in Springfield's creative economy.",
     ["Named partner across the full season", "Logo placement at every event",
      "Co-branded community programming", "Twelve tickets across the season",
      "Quarterly impact summary you can report on"], ("contact.html", "Start a conversation")),
]


def price_cards(tiers):
    out = ""
    for name, fig, per, featured, desc, feats, (href, label) in tiers:
        lis = "".join(f'<li>{TICK}<span>{f}</span></li>' for f in feats)
        flag = '<span class="price-flag">Most popular</span>' if featured else ""
        cls = "price-card price-card--featured" if featured else "price-card"
        btn = "btn btn--primary" if featured else "btn btn--ghost"
        out += f'''
      <article class="{cls}" data-reveal>
        {flag}
        <p class="price-name">{name}</p>
        <div class="price-fig">{fig}</div>
        <p class="price-per">{per}</p>
        <p class="price-desc">{desc}</p>
        <ul class="price-list">{lis}</ul>
        <a class="{btn}" href="{href}">{label}</a>
      </article>'''
    return out


tickets = head(
    f"Tickets, Passes &amp; Sponsorship | {NAME}",
    f"Open mic nights are always free. Showcase tickets, season passes and business "
    f"sponsorship tiers supporting live music and spoken word in {CITY}, Missouri.",
    "tickets.html")
tickets += page_head(
    "Tickets &amp; Partners",
    "Tickets, passes and partnership",
    "Open mic nights are free and always will be. Curated shows are ticketed, and business "
    "partnerships are what keep the free nights free.")
tickets += f'''
<section class="section">
  <div class="shell">
    <div class="section-head">
      <p class="eyebrow" data-reveal>For audiences and artists</p>
      <h2 data-reveal>Ways in</h2>
      <p class="lead" data-reveal>No membership, no minimum spend. Turn up to an open mic for
      free, or buy into the curated season if you want the fully produced nights.</p>
    </div>
    <div class="grid grid--3">{price_cards(TIERS)}
    </div>
    <p class="muted" data-reveal style="margin-top:2rem;font-size:.88rem">
      Ticket prices vary by event and venue. Every show is listed on our
      <a class="accent" href="{FB}" target="_blank" rel="noopener">Facebook page</a>
      with its final price, address and start time.</p>
  </div>
</section>

<section class="section section--paper">
  <div class="shell">
    <div class="section-head">
      <p class="eyebrow" data-reveal>For businesses</p>
      <h2 data-reveal>Sponsor a stage</h2>
      <p class="lead" data-reveal>Sponsorship pays for sound, lighting, venue hire and the
      artists themselves &mdash; which is what allows open mic nights to stay free to enter
      and free to perform. Your name sits on programming the city actually turns up to.</p>
    </div>
    <div class="grid grid--3">{price_cards(PARTNERS)}
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="split">
      <div>
        <p class="eyebrow" data-reveal>Private hire</p>
        <h2 data-reveal>Book the room<br>for your event</h2>
        <p class="lead" data-reveal>We curate the lineup, bring the band, run sound and host
        the evening &mdash; for fundraisers, product launches, weddings and company
        celebrations across southwest Missouri.</p>
        <p data-reveal>Pricing depends on the length of the night, the size of the lineup and
        whether you need production. Send us your date and we will come back with a written
        proposal, not a ballpark.</p>
        <div class="btn-row" data-reveal>
          <a class="btn btn--primary" href="contact.html">Request a quote</a>
          <a class="btn btn--ghost" href="tel:{TEL}">Call {PHONE}</a>
        </div>
      </div>
      <div data-reveal>
        <div class="frame frame--wide" data-parallax="0.05">
          <img src="assets/images/prog-private.svg"
               alt="Private event with live music curated by {NAME}"
               width="800" height="600" loading="lazy" decoding="async">
          <p class="frame-caption">Private &amp; corporate events</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''
tickets += cta_band(
    "Every ticket keeps a mic open",
    "Curated shows and sponsorships fund the free nights. Buying in is the most direct way to "
    "put an unknown artist on a stage.",
    primary=("contact.html", "Talk to us"), ghost=("programs.html", "See the programs"))
tickets += footer()
write("tickets.html", tickets)


# ==========================================================================
# 4. ABOUT
# ==========================================================================
TIMELINE = [
    ("2019", "A move, and a lot of closed doors",
     "Sam Timmerman left Arkansas for Missouri looking for a change of scenery. He knocked on "
     "the doors of Springfield venues and bars to introduce himself as a musician with his own "
     "band, and was repeatedly turned away for being an unknown name."),
    ("2022", "The Melody Room opens",
     "Rather than keep asking for a slot, he built the platform himself &mdash; a live event "
     "series for music, spoken word and performance art, deliberately booking the performers "
     "other venues would not."),
    ("2022&ndash;23", "Outgrowing the first rooms",
     "Shows sold out month after month. The Melody Room moved to Q Enoteca, then to the Blue "
     "Room Comedy Club downtown, and outgrew both of them."),
    ("2023&ndash;24", "The Riff, and a wider bill",
     "The series found a larger home at The Riff in the Classic&rsquo;s Complex, with lineups "
     "spanning jazz, bluegrass, country, rock, hip-hop and poetry &mdash; and kept selling out."),
    ("Now", "Structure, partners and a permanent home",
     "Free open mics continue at the Sunshine Event Center alongside quarterly Safe Haven "
     "concerts with Community Partners of the Ozarks. The next phase is a permanent venue, "
     "expanded programming and paid workshops."),
]
tl = "".join(f'''
      <article class="tl-item" data-reveal>
        <p class="tl-year">{y}</p>
        <div><h3>{t}</h3><p>{d}</p></div>
      </article>''' for y, t, d in TIMELINE)

VALUES = [
    ("Mission", "To give artists, musicians, bands and poets a stage and an audience "
     "regardless of whether anyone knows their name yet &mdash; and to make that stage a safe, "
     "inclusive space for people of every background."),
    ("Vision", "A permanent Springfield venue with year-round programming and paid artist "
     "development, operating as a self-sustaining part of the city&rsquo;s creative economy "
     "rather than a passion project."),
    ("How we measure it", "Not by ticket count alone. By whether a performer leaves with more "
     "than they came with: a recording, a booking, a following, a first sale."),
]
vals = "".join(f'''
      <article class="feature" data-reveal>
        <h3>{t}</h3><p>{d}</p>
      </article>''' for t, d in VALUES)

BOARD = [
    ("Sam Timmerman", "Founder &amp; Executive Director"),
    ("Francine Pratt", "Board Chair"),
    ("Cora Scott", "Board Member"),
    ("Gabie Edmunds", "Board Member"),
    ("Jessie Cowen", "Board Member"),
    ("Brecka Henderson", "Board Member"),
    ("Daniel Ogunyemi", "Board Member"),
]
board = "".join(f'''
      <article class="feature" data-reveal>
        <h3 style="font-size:1.02rem">{n}</h3>
        <p class="muted" style="font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;text-transform:uppercase">{r}</p>
      </article>''' for n, r in BOARD)

about = head(
    f"About {NAME} | Founded by Sam Timmerman in {CITY}, MO",
    f"The story behind {NAME}: how a musician turned away by {CITY} venues built a platform "
    f"for underrepresented voices, and where it is heading next.",
    "about.html")
about += page_head(
    "About",
    "Built by someone who was turned away",
    "The Melody Room exists because its founder could not get a slot. Rather than keep asking, "
    "he built the room &mdash; and then filled it.")
about += f'''
<section class="section">
  <div class="shell">
    <div class="split">
      <div>
        <p class="eyebrow" data-reveal>The founder</p>
        <h2 data-reveal>Sam Timmerman</h2>
        <p class="lead" data-reveal>By day, Sam is a behavior technician supervisor at The Arc
        of the Ozarks, managing care plans and leading a team supporting people with
        intellectual disabilities. After hours, he runs The Melody Room &mdash; handling
        bookings, artist outreach and logistics himself.</p>
        <p data-reveal>He arrived in Springfield from Arkansas in 2019 as a pianist with his own
        band, and spent months being told no. When he started programming his own nights and
        booking the performers other venues ignored, those nights began selling out &mdash;
        month after month, for a year straight, until he had to find a bigger room.</p>
        <p data-reveal>That experience is still the whole operating principle. Being unknown is
        not a reason to be turned away. It is the reason to be booked.</p>
        <div class="btn-row" data-reveal>
          <a class="btn btn--primary" href="contact.html#lineup">Get on the lineup</a>
        </div>
      </div>
      <div data-reveal>
        <!-- REPLACE: swap this placeholder for Sam's real photograph.
             Keep it roughly 4:5 portrait, around 800x1000px. -->
        <div class="frame frame--portrait" data-parallax="0.05">
          <img src="assets/images/founder-placeholder.svg"
               alt="Sam Timmerman, founder of {NAME} in {CITY}, Missouri"
               width="800" height="1000" loading="lazy" decoding="async">
          <p class="frame-caption">Sam Timmerman &bull; Founder &amp; Executive Director</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="shell">
    <div class="section-head">
      <p class="eyebrow" data-reveal>How we got here</p>
      <h2 data-reveal>Four rooms, and counting</h2>
      <p class="lead" data-reveal>Every move on this list happened for the same reason: the
      last room stopped being big enough.</p>
    </div>
    <div class="timeline">{tl}
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      <p class="eyebrow" data-reveal>What we are for</p>
      <h2 data-reveal>Mission &amp; vision</h2>
    </div>
    <div class="grid grid--3">{vals}
    </div>
  </div>
</section>

<section class="section section--velvet">
  <div class="shell">
    <div class="section-head">
      <p class="eyebrow" data-reveal>Leadership</p>
      <h2 data-reveal>Who runs the room</h2>
      <p class="lead" data-reveal>The Melody Room is led by its founder and guided by a board
      drawn from across Springfield&rsquo;s community and business networks.</p>
    </div>
    <div class="grid grid--4">{board}
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="shell">
    <div class="section-head">
      <p class="eyebrow" data-reveal>Recognition</p>
      <h2 data-reveal>Covered by the local press</h2>
    </div>
    <div class="grid grid--2">
      <article class="quote-card" data-reveal style="background:rgba(18,11,24,.03);border-color:var(--line-dark)">
        <span class="quote-mark" aria-hidden="true">&ldquo;</span>
        <p style="color:var(--ink)">Profiled as an entrepreneur building a grassroots venture
        that is making waves in Springfield&rsquo;s creative economy.</p>
        <p class="quote-by">Biz 417 &bull; September 2025</p>
      </article>
      <article class="quote-card" data-reveal style="background:rgba(18,11,24,.03);border-color:var(--line-dark)">
        <span class="quote-mark" aria-hidden="true">&ldquo;</span>
        <p style="color:var(--ink)">Described as creating a safe space for intimate live music
        and for performers without a name yet.</p>
        <p class="quote-by">Springfield Daily Citizen</p>
      </article>
    </div>
  </div>
</section>
'''
about += cta_band(
    "The next room is the one we own",
    "A permanent venue, year-round programming and paid workshops. If you want to be part of "
    "building it, we would like to hear from you.",
    primary=("contact.html", "Get in touch"), ghost=("tickets.html", "See partnership tiers"))
about += footer()
write("about.html", about)


# ==========================================================================
# 5. CONTACT
# ==========================================================================
contact = head(
    f"Contact {NAME} | Book a Slot in {CITY}, MO",
    f"Get on the lineup, buy tickets or discuss sponsorship. Email {EMAIL} or call {PHONE}. "
    f"{NAME} is based in {CITY}, Missouri {ZIP}.",
    "contact.html")
contact += page_head(
    "Contact",
    "Tell us what you do",
    "Performer, audience member, venue or sponsor &mdash; this is the fastest way to reach us. "
    "We reply to everything within two business days.")
contact += f'''
<section class="section" id="lineup">
  <div class="shell">
    <div class="contact-grid">

      <!-- ---------------------------- FORM ---------------------------- -->
      <div>
        <p class="eyebrow" data-reveal>Send a message</p>
        <h2 data-reveal>Get on the lineup</h2>
        <p class="lead" data-reveal style="margin-bottom:2rem">If you are asking about a slot,
        tell us what you perform and roughly how long your set runs. That is usually all we
        need to place you.</p>

        <form id="contact-form" data-to="{EMAIL}" novalidate data-reveal>
          <div class="field">
            <label for="name">Your name</label>
            <input type="text" id="name" name="name" placeholder="Who are we talking to?"
                   autocomplete="name" required>
            <span class="field-error">Tell us who you are.</span>
          </div>

          <div class="field">
            <label for="email">Email address</label>
            <input type="email" id="email" name="email" placeholder="you@example.com"
                   autocomplete="email" required>
            <span class="field-error">Check the email address &mdash; we reply to this one.</span>
          </div>

          <div class="field">
            <label for="topic">What is this about?</label>
            <select id="topic" name="topic">
              <option>Performing at an open mic</option>
              <option>Featured artist spotlight</option>
              <option>Tickets and season passes</option>
              <option>Private or corporate booking</option>
              <option>Sponsorship or partnership</option>
              <option>Something else</option>
            </select>
          </div>

          <div class="field">
            <label for="message">Your message</label>
            <textarea id="message" name="message" required
              placeholder="What do you perform, and how long have you been doing it?"></textarea>
            <span class="field-error">Add a little more detail so we can help.</span>
          </div>

          <button class="btn btn--primary" type="submit">Send message</button>

          <p class="form-note">This form opens your own email app with the message ready to
          send, so nothing is stored on this website. Prefer to write directly? Email
          <a class="accent" href="mailto:{EMAIL}">{EMAIL}</a>.</p>

          <div class="form-status" id="form-status" role="status" aria-live="polite"></div>
        </form>
      </div>

      <!-- --------------------------- DETAILS --------------------------- -->
      <aside>
        <p class="eyebrow" data-reveal>Direct lines</p>
        <h2 data-reveal>Reach us</h2>

        <dl data-reveal style="margin:1.5rem 0 2rem">
          <div class="contact-line">
            <span class="contact-ico">{IC_MAIL}</span>
            <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
          </div>
          <div class="contact-line">
            <span class="contact-ico">{IC_PHONE}</span>
            <div><dt>Phone &amp; WhatsApp</dt><dd><a href="tel:{TEL}">{PHONE}</a></dd></div>
          </div>
          <div class="contact-line">
            <span class="contact-ico">{IC_PIN}</span>
            <div><dt>Based in</dt><dd>{CITY}, {REGION} {ZIP}<br>
              <span class="muted" style="font-size:.88rem">Venues vary by event &mdash; check the
              current listing before you travel.</span></dd></div>
          </div>
          <div class="contact-line">
            <span class="contact-ico">{IC_CLOCK}</span>
            <div><dt>Response time</dt><dd>Within two business days</dd></div>
          </div>
        </dl>

        <div class="socials" data-reveal style="margin-bottom:2rem">
          <a href="{FB}" target="_blank" rel="noopener" aria-label="{NAME} on Facebook">{IC_FB}</a>
          <a href="{IG}" target="_blank" rel="noopener" aria-label="{NAME} on Instagram">{IC_IG}</a>
          <a href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{IC_WA}</a>
        </div>

        <!-- Google Maps embed — no API key required -->
        <div class="map-frame" data-reveal>
          <iframe
            title="Map of {CITY}, Missouri"
            src="https://www.google.com/maps?q={CITY}%2C%20{REGION}%20{ZIP}&output=embed"
            loading="lazy" referrerpolicy="no-referrer-when-downgrade"
            allowfullscreen></iframe>
        </div>
      </aside>

    </div>
  </div>
</section>

<section class="section section--paper section--tight">
  <div class="shell">
    <div class="grid grid--3">
      <article class="feature" data-reveal>
        <h3>Performers</h3>
        <p>Name, what you perform, set length. Slots at open mic nights are free and fill
        quickly, so earlier is better.</p>
      </article>
      <article class="feature" data-reveal>
        <h3>Venues &amp; partners</h3>
        <p>If you run a space in Springfield and want to host a night, tell us your capacity
        and available dates.</p>
      </article>
      <article class="feature" data-reveal>
        <h3>Press</h3>
        <p>Photography, interviews and background on the organisation are available on
        request &mdash; email is the fastest route.</p>
      </article>
    </div>
  </div>
</section>
'''
contact += footer()
write("contact.html", contact)

print("\nDone.")
