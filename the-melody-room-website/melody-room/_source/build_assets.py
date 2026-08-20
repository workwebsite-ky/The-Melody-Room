#!/usr/bin/env python3
"""
Generates all brand artwork for The Melody Room website.
Palette is defined once here so regenerating with the real logo colors is a one-line change.
"""
import os, math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "images")
os.makedirs(OUT, exist_ok=True)

INK    = "#120B18"   # house lights down
VELVET = "#241432"   # stage curtain
BRASS  = "#E9A93F"   # amber stage wash
GEL    = "#FF3D68"   # magenta lighting gel
COOL   = "#4CC9E0"   # cool gel
IVORY  = "#F7F2E8"   # flyer paper


def w(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body)
    print("  ", name)


# ---------------------------------------------------------------- logo mark
# A doorway with light spilling out of it = "the room". Equaliser bars form the
# threshold, so the mark reads as both an open door and a level meter.
MARK = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="The Melody Room">
  <defs>
    <linearGradient id="tmr-spill" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{BRASS}"/><stop offset="1" stop-color="{GEL}"/>
    </linearGradient>
  </defs>
  <rect x="2" y="2" width="60" height="60" rx="17" fill="none" stroke="url(#tmr-spill)" stroke-width="3.2"/>
  <path d="M17 50V28a15 15 0 0 1 30 0v22" fill="none" stroke="url(#tmr-spill)" stroke-width="3.2" stroke-linecap="round"/>
  <g fill="url(#tmr-spill)">
    <rect x="23.4" y="40" width="3.6" height="7"  rx="1.8"/>
    <rect x="30.2" y="34" width="3.6" height="13" rx="1.8"/>
    <rect x="37.0" y="37.5" width="3.6" height="9.5" rx="1.8"/>
  </g>
</svg>'''
w("logo-mark.svg", MARK)
w("favicon.svg", MARK)

# ------------------------------------------------------------- logo lockup
w("logo-lockup.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 72" role="img" aria-label="The Melody Room logo">
  <defs>
    <linearGradient id="lk" x1="36" y1="8" x2="36" y2="64" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{BRASS}"/><stop offset="1" stop-color="{GEL}"/>
    </linearGradient>
  </defs>
  <g transform="translate(8,4)">
    <rect x="2" y="2" width="60" height="60" rx="17" fill="none" stroke="url(#lk)" stroke-width="3.2"/>
    <path d="M17 50V28a15 15 0 0 1 30 0v22" fill="none" stroke="url(#lk)" stroke-width="3.2" stroke-linecap="round"/>
    <g fill="url(#lk)">
      <rect x="23.4" y="40" width="3.6" height="7" rx="1.8"/>
      <rect x="30.2" y="34" width="3.6" height="13" rx="1.8"/>
      <rect x="37.0" y="37.5" width="3.6" height="9.5" rx="1.8"/>
    </g>
  </g>
  <text x="88" y="36" font-family="Anton, Impact, sans-serif" font-size="27" fill="{IVORY}">THE MELODY ROOM</text>
  <text x="89" y="54" font-family="Space Mono, monospace" font-size="10.5" letter-spacing="4" fill="{BRASS}">SPRINGFIELD, MISSOURI</text>
</svg>''')

# ------------------------------------------------------------- hero artwork
def hero():
    beams = []
    # three overlapping light cones from the rig, in gel colours
    for x, col, op, spread in ((430, BRASS, .30, 190), (800, GEL, .22, 230), (1180, COOL, .16, 200)):
        beams.append(
            f'<path d="M{x} -40 L{x-spread} 760 L{x+spread} 760 Z" fill="url(#beam-{col[1:]})" opacity="{op}"/>')

    grads = "".join(
        f'''<linearGradient id="beam-{c[1:]}" x1="0" y1="0" x2="0" y2="760" gradientUnits="userSpaceOnUse">
             <stop offset="0" stop-color="{c}" stop-opacity=".95"/>
             <stop offset="1" stop-color="{c}" stop-opacity="0"/></linearGradient>''' for c in (BRASS, GEL, COOL))

    # audience silhouettes along the bottom
    random.seed(7)
    heads = []
    x = -20
    while x < 1640:
        r = random.uniform(20, 32)
        y = 760 - random.uniform(-6, 14)
        heads.append(f'<circle cx="{x:.0f}" cy="{y-r*1.5:.0f}" r="{r:.0f}"/>'
                     f'<rect x="{x-r*1.45:.0f}" y="{y-r*0.5:.0f}" width="{r*2.9:.0f}" height="{r*3:.0f}" rx="{r*0.9:.0f}"/>')
        x += random.uniform(52, 84)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 800" role="img"
     aria-label="Stage lighting washing over an audience at a Melody Room show">
  <defs>
    {grads}
    <radialGradient id="floor" cx="800" cy="700" r="620" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{BRASS}" stop-opacity=".38"/>
      <stop offset="1" stop-color="{BRASS}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="room" x1="0" y1="0" x2="0" y2="800" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{VELVET}"/><stop offset="1" stop-color="{INK}"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="800" fill="url(#room)"/>
  {''.join(beams)}
  <ellipse cx="800" cy="705" rx="600" ry="120" fill="url(#floor)"/>
  <!-- mic stand, centre stage -->
  <g stroke="{INK}" stroke-width="7" fill="{INK}" opacity=".92">
    <line x1="800" y1="470" x2="800" y2="700" stroke-linecap="round"/>
    <ellipse cx="800" cy="702" rx="52" ry="9" stroke="none"/>
    <rect x="786" y="424" width="28" height="58" rx="14" stroke="none"/>
  </g>
  <g fill="{INK}" opacity=".96">{''.join(heads)}</g>
</svg>'''
w("hero-stage.svg", hero())


# ------------------------------------------------- programme / service cards
def card(title, accent, motif):
    """Duotone abstract card. `motif` is extra SVG drawn in the light pool."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="800" y2="600" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{VELVET}"/><stop offset="1" stop-color="{INK}"/>
    </linearGradient>
    <linearGradient id="cone" x1="300" y1="0" x2="300" y2="600" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{accent}" stop-opacity=".85"/>
      <stop offset="1" stop-color="{accent}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="pool" cx="400" cy="470" r="300" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{accent}" stop-opacity=".45"/>
      <stop offset="1" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <path d="M400 -30 L150 620 L650 620 Z" fill="url(#cone)" opacity=".33"/>
  <ellipse cx="400" cy="470" rx="290" ry="90" fill="url(#pool)"/>
  <g stroke="{accent}" fill="none" stroke-width="6" stroke-linecap="round" opacity=".95">{motif}</g>
</svg>'''


def waveform(cx, cy, n=17, span=260, seed=3, amp=64):
    random.seed(seed)
    step = span / (n - 1)
    return "".join(
        f'<line x1="{cx-span/2+i*step:.0f}" y1="{cy-random.uniform(12,amp):.0f}" '
        f'x2="{cx-span/2+i*step:.0f}" y2="{cy+random.uniform(12,amp):.0f}"/>' for i in range(n))


CARDS = {
    # open mic — a microphone
    "prog-open-mic.svg": (BRASS, '<rect x="372" y="200" width="56" height="112" rx="28"/>'
                                 '<path d="M338 292a62 62 0 0 0 124 0"/><line x1="400" y1="354" x2="400" y2="410"/>'
                                 '<line x1="356" y1="412" x2="444" y2="412"/>' + waveform(400, 480, 13, 300, 5, 40)),
    # spoken word — an open book
    "prog-poetry.svg": (GEL, '<path d="M400 250v170"/><path d="M400 250c-40-34-96-40-146-30v170c50-10 106-4 146 30"/>'
                             '<path d="M400 250c40-34 96-40 146-30v170c-50-10-106-4-146 30"/>'
                             '<line x1="300" y1="300" x2="360" y2="306"/><line x1="440" y1="306" x2="500" y2="300"/>'
                             '<line x1="300" y1="340" x2="360" y2="346"/><line x1="440" y1="346" x2="500" y2="340"/>'),
    # concert — piano keys, Sam is a pianist
    "prog-concerts.svg": (COOL, ''.join(f'<rect x="{262+i*32}" y="238" width="30" height="168" rx="5"/>' for i in range(9))
                          + ''.join(f'<rect x="{281+i*32}" y="238" width="20" height="100" rx="4" fill="{INK}" stroke="{COOL}" stroke-width="4"/>'
                                    for i in (0, 1, 3, 4, 5, 7))),
    # workshops — a circle of seats
    "prog-workshops.svg": (BRASS, ''.join(
        f'<circle cx="{400+150*math.cos(a):.0f}" cy="{320+92*math.sin(a):.0f}" r="26"/>'
        for a in [i * math.pi / 4 for i in range(8)]) + '<circle cx="400" cy="320" r="14" stroke-width="4"/>'),
    # safe haven — a shield around a soundwave
    "prog-safe-haven.svg": (COOL, '<path d="M400 196l128 48v104c0 84-58 132-128 156-70-24-128-72-128-156V244z"/>'
                            + waveform(400, 350, 9, 150, 11, 42)),
    # private hire — string lights over tables
    "prog-private.svg": (GEL, '<path d="M180 214q220 96 440 0" stroke-width="4"/>'
                         + ''.join(f'<circle cx="{200+i*57}" cy="{250+34*math.sin(i*0.62)-14*i*0.1:.0f}" r="11"/>' for i in range(8))
                         + '<rect x="290" y="380" width="220" height="14" rx="7"/><line x1="330" y1="394" x2="330" y2="452"/>'
                           '<line x1="470" y1="394" x2="470" y2="452"/>'),
}
for fn, (acc, motif) in CARDS.items():
    w(fn, card(fn[5:-4].replace("-", " ").title(), acc, motif))


# -------------------------------------------------------- founder portrait
w("founder-placeholder.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 1000" role="img"
     aria-label="Placeholder portrait of founder Sam Timmerman at the keyboard">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1000" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{VELVET}"/><stop offset="1" stop-color="{INK}"/>
    </linearGradient>
    <linearGradient id="cone" x1="0" y1="0" x2="0" y2="1000" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{BRASS}" stop-opacity=".8"/>
      <stop offset="1" stop-color="{BRASS}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="pool" cx="400" cy="800" r="330" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{BRASS}" stop-opacity=".4"/><stop offset="1" stop-color="{BRASS}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="1000" fill="url(#bg)"/>
  <path d="M400 -40 L120 1000 L680 1000 Z" fill="url(#cone)" opacity=".3"/>
  <ellipse cx="400" cy="800" rx="320" ry="110" fill="url(#pool)"/>
  <g fill="{INK}" opacity=".95">
    <circle cx="400" cy="430" r="86"/>
    <path d="M400 530c-108 0-174 62-188 164h376c-14-102-80-164-188-164z"/>
    <rect x="176" y="742" width="448" height="36" rx="10"/>
    <rect x="222" y="778" width="356" height="110" rx="8"/>
  </g>
  <g stroke="{BRASS}" stroke-width="4" opacity=".75">
    {''.join(f'<line x1="{232+i*32}" y1="742" x2="{232+i*32}" y2="778"/>' for i in range(13))}
  </g>
</svg>''')


# ---------------------------------------------------------- pattern + grain
w("stage-pattern.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <rect width="120" height="120" fill="none"/>
  <g stroke="{BRASS}" stroke-width="1" opacity=".16">
    <line x1="0" y1="0" x2="120" y2="120"/><line x1="-60" y1="60" x2="60" y2="180"/>
    <line x1="60" y1="-60" x2="180" y2="60"/>
  </g>
</svg>''')

grain = Image.new("L", (160, 160))
random.seed(11)
grain.putdata([random.randint(0, 255) for _ in range(160 * 160)])
grain.convert("RGBA").putalpha(26)
g = Image.new("RGBA", (160, 160))
px = grain.load()
g.putdata([(255, 255, 255, int(px[i % 160, i // 160] * 0.10)) for i in range(160 * 160)])
g.save(os.path.join(OUT, "grain.png"))
print("   grain.png")


# ------------------------------------------------------- social share image
def font(size, bold=True):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
              else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


og = Image.new("RGB", (1200, 630), INK)
d = ImageDraw.Draw(og)
for y in range(630):  # vertical curtain gradient
    t = y / 630
    d.line([(0, y), (1200, y)], fill=(int(0x24 + (0x12 - 0x24) * t),
                                      int(0x14 + (0x0B - 0x14) * t),
                                      int(0x32 + (0x18 - 0x32) * t)))
glow = Image.new("RGB", (1200, 630), INK)
gd = ImageDraw.Draw(glow)
gd.polygon([(600, -60), (250, 700), (950, 700)], fill=BRASS)
gd.ellipse([260, 430, 940, 700], fill=GEL)
og = Image.blend(og, glow.filter(ImageFilter.GaussianBlur(90)), 0.42)
d = ImageDraw.Draw(og)
d.text((80, 232), "THE MELODY ROOM", font=font(78), fill=IVORY)
d.text((84, 336), "LIVE MUSIC  ·  SPOKEN WORD  ·  SPRINGFIELD, MO", font=font(27), fill=BRASS)
d.text((84, 392), "A stage for the artists nobody has heard yet.", font=font(31, False), fill="#CFC2D8")
og.save(os.path.join(OUT, "og-image.jpg"), quality=88, optimize=True)
print("   og-image.jpg")

print("\nAssets written to", OUT)
