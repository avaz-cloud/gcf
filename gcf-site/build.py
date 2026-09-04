#!/usr/bin/env python3
"""Static-site generator for the Guernsey Chess Federation redesign.
Assembles shared header/nav/footer + per-page content into plain HTML files.
No runtime templating on the client — output is fully static HTML.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("club.html", "The Club"),
    ("juniors.html", "Juniors"),
    ("events.html", "Events"),
    ("news.html", "News"),
    ("results.html", "Results"),
    ("contact.html", "Contact"),
]

SPRITE = """
<svg aria-hidden="true" focusable="false" style="position:absolute;width:0;height:0;overflow:hidden">
  <symbol id="icon-pawn" viewBox="0 0 100 140">
    <circle cx="50" cy="32" r="17"/>
    <rect x="44" y="48" width="12" height="9"/>
    <polygon points="35,57 65,57 60,68 40,68"/>
    <polygon points="40,68 60,68 67,97 33,97"/>
    <rect x="29" y="97" width="42" height="9"/>
    <polygon points="22,106 78,106 83,121 17,121"/>
  </symbol>
  <symbol id="icon-menu" viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="1.7" fill="none" stroke-linecap="round"/></symbol>
  <symbol id="icon-close" viewBox="0 0 24 24"><path d="M5 5l14 14M19 5L5 19" stroke="currentColor" stroke-width="1.7" fill="none" stroke-linecap="round"/></symbol>
  <symbol id="icon-arrow" viewBox="0 0 24 24"><path d="M4 12h16M14 6l6 6-6 6" stroke="currentColor" stroke-width="1.7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></symbol>
  <symbol id="icon-facebook" viewBox="0 0 24 24"><path d="M15 8.5h2V5.4c-.35-.05-1.54-.15-2.94-.15-2.9 0-4.9 1.77-4.9 5.02v2.63H6.5v3.5h2.66V22h3.6v-5.6h2.55l.4-3.5h-2.95v-2.28c0-1.01.28-1.7 1.74-1.7z" fill="currentColor"/></symbol>
  <symbol id="icon-x" viewBox="0 0 24 24"><path d="M4.5 4.5l15 15M19.5 4.5l-15 15" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></symbol>
  <symbol id="icon-instagram" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="4.2" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="12" cy="12" r="3.6" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="16.7" cy="7.3" r="1" fill="currentColor"/></symbol>
  <symbol id="icon-mail" viewBox="0 0 24 24"><rect x="3.5" y="5.5" width="17" height="13" rx="1.5" stroke="currentColor" stroke-width="1.4" fill="none"/><path d="M4.5 6.5l7.5 6 7.5-6" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></symbol>
  <symbol id="icon-pin" viewBox="0 0 24 24"><path d="M12 21s7-6.1 7-11.3A7 7 0 0 0 5 9.7C5 14.9 12 21 12 21z" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linejoin="round"/><circle cx="12" cy="9.6" r="2.3" stroke="currentColor" stroke-width="1.4" fill="none"/></symbol>
</svg>
"""


def header(active):
    desktop_items = []
    mobile_items = []
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ""
        desktop_items.append('<a href="{}"{}>{}</a>'.format(href, cur, label))
        mobile_items.append(
            '<li><a href="{}"{}>{}<svg width="18" height="18" aria-hidden="true"><use href="#icon-arrow"/></svg></a></li>'.format(
                href, cur, label
            )
        )
    desktop = "\n            ".join(desktop_items)
    mobile = "\n            ".join(mobile_items)
    return f"""
  <a class="skip-link" href="#main">Skip to main content</a>
  <header class="site-header">
    <div class="header-bar">
      <a class="brand" href="index.html">
        <svg class="brand-mark" viewBox="0 0 100 140" aria-hidden="true"><use href="#icon-pawn"/></svg>
        <span class="brand-text">
          <span class="full">Guernsey Chess Federation</span>
          <span class="sub">Since 1931</span>
        </span>
      </a>
      <nav class="primary-nav" aria-label="Primary">
        {desktop}
      </nav>
      <div class="header-cta">
        <a class="btn" href="club.html">Visit the Club</a>
        <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav">
          <svg class="icon-open" width="20" height="20" aria-hidden="true"><use href="#icon-menu"/></svg>
          <svg class="icon-close" width="20" height="20" aria-hidden="true"><use href="#icon-close"/></svg>
        </button>
      </div>
    </div>
  </header>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">
    <ul>
      {mobile}
    </ul>
    <div class="mobile-cta wrap" style="padding-left:0">
      <a class="btn" style="width:100%;justify-content:center" href="club.html">Visit the Club</a>
    </div>
  </nav>
"""


FOOTER = """
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="footer-brand">
            <svg viewBox="0 0 100 140" aria-hidden="true"><use href="#icon-pawn" fill="#e9dfc9"/></svg>
            <span>Guernsey Chess Federation</span>
          </div>
          <p class="footer-note">The governing body for chess in Guernsey, and home of the Guernsey Chess Club. Meeting every Tuesday evening at Les Cotils &mdash; all standards welcome.</p>
          <div class="social-row">
            <a href="https://www.facebook.com/GuernseyChess/" aria-label="Guernsey Chess on Facebook"><svg width="15" height="15" aria-hidden="true"><use href="#icon-facebook"/></svg></a>
            <a href="https://twitter.com/GuernseyChess" aria-label="Guernsey Chess on X (Twitter)"><svg width="15" height="15" aria-hidden="true"><use href="#icon-x"/></svg></a>
            <a href="https://www.instagram.com/guernseychess/" aria-label="Guernsey Chess on Instagram"><svg width="15" height="15" aria-hidden="true"><use href="#icon-instagram"/></svg></a>
          </div>
        </div>
        <div class="footer-col">
          <h3>Federation</h3>
          <ul>
            <li><a href="about.html">About the Federation</a></li>
            <li><a href="club.html">The Club</a></li>
            <li><a href="results.html">Results &amp; Gradings</a></li>
            <li><a href="contact.html">Officers &amp; Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h3>Play</h3>
          <ul>
            <li><a href="events.html">Guernsey International Chess Festival</a></li>
            <li><a href="juniors.html">Junior Chess Club</a></li>
            <li><a href="events.html#inter-insular">Inter-Insular v Jersey</a></li>
            <li><a href="news.html">News</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h3>Get in touch</h3>
          <ul>
            <li><a href="mailto:chess@gcf.org.gg">chess@gcf.org.gg</a></li>
            <li>Les Cotils, St Peter Port</li>
            <li>Tuesdays from 7:30pm</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; Guernsey Chess Federation. Club records and results are maintained by the Federation&rsquo;s officers.</span>
        <span>Affiliated to FIDE, the International Chess Federation</span>
      </div>
    </div>
  </footer>
"""

REVEAL_OVERLAY = """
  <div class="reveal-overlay" role="presentation" aria-hidden="true">
    <div class="reveal-piece">
      <svg viewBox="0 0 100 140" aria-hidden="true"><use href="#icon-pawn"/></svg>
    </div>
    <div class="reveal-wordmark">Guernsey Chess Federation</div>
  </div>
"""


def page(
    filename,
    title,
    description,
    active,
    body,
    og_title=None,
    include_reveal=False,
    extra_head="",
):
    og_title = og_title or title
    reveal = REVEAL_OVERLAY if include_reveal else ""
    fade_class = " is-revealed" if not include_reveal else ""
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://www.gcf.org.gg/{filename}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Guernsey Chess Federation">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://www.gcf.org.gg/{filename}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#f6f1e6">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 140'%3E%3Cg fill='%237c2530'%3E%3Ccircle cx='50' cy='32' r='17'/%3E%3Crect x='44' y='48' width='12' height='9'/%3E%3Cpolygon points='35,57 65,57 60,68 40,68'/%3E%3Cpolygon points='40,68 60,68 67,97 33,97'/%3E%3Crect x='29' y='97' width='42' height='9'/%3E%3Cpolygon points='22,106 78,106 83,121 17,121'/%3E%3C/g%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,500;0,600;0,700;0,800;1,500&amp;family=Inter:wght@400;500;600;700&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
{extra_head}</head>
<body class="{'no-scroll' if include_reveal else fade_class.strip()}">
{reveal}{SPRITE}{header(active)}
<main id="main" class="js-content-fade{fade_class}">
{body}
</main>
{FOOTER}
<script src="assets/js/main.js"></script>
</body>
</html>
"""


OUT = {}

# ---------------------------------------------------------------- HOME
OUT["index.html"] = page(
    "index.html",
    "Guernsey Chess Federation & Club",
    "The governing body for chess in Guernsey. Home of the Guernsey Chess Club, meeting every Tuesday at Les Cotils, and organiser of the Guernsey International Chess Festival.",
    "index.html",
    include_reveal=True,
    body="""
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="eyebrow">Chess in Guernsey since 1931</p>
        <h1>Guernsey Chess Federation</h1>
        <p class="lede">The governing body for chess in Guernsey &mdash; and home of the Guernsey Chess Club, which meets every Tuesday evening at Les Cotils. Beginners, juniors, club players and titled visitors are all welcome at the board.</p>
        <div class="hero-actions">
          <a class="btn btn-oxblood" href="club.html">Visit the club on Tuesday</a>
          <a class="btn btn-ghost" href="events.html">The 2026 Festival</a>
        </div>
        <div class="hero-meta">
          <div><strong>Tuesdays, 7:30pm</strong>&nbsp;club night at Les Cotils</div>
          <div><strong>Ages 8&ndash;16</strong>&nbsp;junior club, term-time</div>
          <div><strong>1&ndash;7 Nov 2026</strong>&nbsp;50th International Festival</div>
        </div>
      </div>
      <div class="hero-board" aria-hidden="true">
        <svg viewBox="0 0 400 400">
          <defs>
            <pattern id="board" width="50" height="50" patternUnits="userSpaceOnUse">
              <rect width="50" height="50" fill="#efe7d4"/>
              <rect width="25" height="25" fill="#d9cca9"/>
              <rect x="25" y="25" width="25" height="25" fill="#d9cca9"/>
            </pattern>
          </defs>
          <rect x="1" y="1" width="398" height="398" fill="url(#board)" stroke="#b9a87c" stroke-width="2"/>
          <rect x="150" y="300" width="50" height="50" fill="#7c2530" opacity="0.55"/>
          <g transform="translate(160,308) scale(0.22)" fill="#201c17"><use href="#icon-pawn"/></g>
          <g transform="translate(60,208) scale(0.22)" fill="#201c17"><use href="#icon-pawn"/></g>
          <g transform="translate(260,58) scale(0.22)" fill="#fffdf8"><use href="#icon-pawn"/></g>
        </svg>
      </div>
    </div>
  </section>

  <div class="board-divider" aria-hidden="true"></div>

  <section class="tight">
    <div class="wrap">
      <div class="fact-strip reveal-on-scroll">
        <div><span class="n">1931</span><span class="l">First Guernsey Chess Championship</span></div>
        <div><span class="n">1975</span><span class="l">First International Chess Festival</span></div>
        <div><span class="n">50th</span><span class="l">Festival edition, November 2026</span></div>
        <div><span class="n">8&ndash;16</span><span class="l">Junior Chess Club age range</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="hero-grid" style="grid-template-columns: 1.3fr 0.9fr; align-items:start;">
        <div class="hairline-box reveal-on-scroll" style="padding:40px;">
          <p class="eyebrow">Featured &middot; 1&ndash;7 November 2026</p>
          <h2 style="font-size:1.9rem;">The 50th Guernsey International Chess Festival</h2>
          <p class="prose" style="color:var(--ink-soft)">Two FIDE-rated classical tournaments &mdash; Open and Challengers &mdash; plus a FIDE-rated Blitz event, held at the Peninsula Hotel. Prize funds of &pound;3,000 (Open) and &pound;900 (Challengers), with the prizegiving dinner included on 7 November. Registration is open now.</p>
          <a class="text-link" href="events.html">Read the full festival details <svg><use href="#icon-arrow"/></svg></a>
        </div>
        <div class="v-space">
          <div class="card reveal-on-scroll">
            <span class="card-meta">Every Tuesday</span>
            <h3>Club Night</h3>
            <p>Social and league chess from 7:30pm at Les Cotils. No need to book &mdash; just come along.</p>
            <a class="text-link" href="club.html">About the club <svg><use href="#icon-arrow"/></svg></a>
          </div>
          <div class="card reveal-on-scroll">
            <span class="card-meta">Term-time Tuesdays</span>
            <h3>Junior Chess</h3>
            <p>A club for young players aged 8&ndash;16, run alongside the main club at Les Cotils Coffee Shop.</p>
            <a class="text-link" href="juniors.html">Junior chess details <svg><use href="#icon-arrow"/></svg></a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="tight" style="background:var(--paper-alt); border-top:1px solid var(--rule); border-bottom:1px solid var(--rule);">
    <div class="wrap">
      <div class="section-head" style="display:flex; justify-content:space-between; align-items:flex-end; gap:20px; flex-wrap:wrap;">
        <div>
          <p class="eyebrow">From the Federation</p>
          <h2 style="margin-bottom:0;">Latest news</h2>
        </div>
        <a class="text-link" href="news.html">All news <svg><use href="#icon-arrow"/></svg></a>
      </div>
      <div class="reveal-on-scroll">
        <div class="feature-row">
          <div class="date">18 Mar 2025</div>
          <div>
            <h3>The 49th BWCI Guernsey International Chess Festival, 19&ndash;25 October 2025</h3>
            <p>Held at the St James Concert and Assembly Hall, with a Blitz tournament and simultaneous exhibition on the evening of 18 October, and the prizegiving dinner on 21 October.</p>
          </div>
        </div>
        <div class="feature-row">
          <div class="date">28 Feb 2025</div>
          <div>
            <h3>Guernsey at the FIDE World Senior Team Chess Championships, Prague</h3>
            <p>Peter Kirby, Peter Rowe, Toby Brookfield, Jamie Morgan and Russell Finch represented Guernsey in the 50+ category, for the second time as a national team.</p>
          </div>
        </div>
        <div class="feature-row" style="border-bottom:none;">
          <div class="date">13 Oct 2024</div>
          <div>
            <h3>WFM and WCM titles awarded to Arita Strade and Gerda Nevska</h3>
            <p>Both players earned FIDE titles for their performances at the 45th Chess Olympiad in Budapest, scoring 6.5/10 and 6/11 respectively.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap hero-grid" style="grid-template-columns: 0.9fr 1.1fr; align-items:center;">
      <div class="reveal-on-scroll">
        <p class="eyebrow">The Federation</p>
        <h2>Governing chess in Guernsey since 1931</h2>
        <p class="prose">The Guernsey Chess Federation organises the island&rsquo;s internal leagues and championship, runs the annual Inter-Insular match against Jersey for the Hollis Cup, selects players to represent Guernsey internationally, and co-organises the Guernsey International Chess Festival each year. In practice, its members play together through the Guernsey Chess Club.</p>
        <a class="text-link" href="about.html">More about the Federation <svg><use href="#icon-arrow"/></svg></a>
      </div>
      <div class="reveal-on-scroll">
        <div class="table-wrap">
          <table>
            <caption>On the board this year</caption>
            <tbody>
              <tr><th scope="row">Championship</th><td>Winter League, played over two cycles</td></tr>
              <tr><th scope="row">Division 2 &amp; 3</th><td>Graded internal leagues</td></tr>
              <tr><th scope="row">Summer League</th><td>Open to non-members, June&ndash;August</td></tr>
              <tr><th scope="row">Quickplay &amp; Blitz</th><td>Faster time-control club tournaments</td></tr>
              <tr><th scope="row">Inter-Insular</th><td>Guernsey v Jersey, for the Hollis Cup</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <section class="panel-oxblood">
    <div class="wrap" style="display:flex; justify-content:space-between; align-items:center; gap:24px; flex-wrap:wrap;">
      <div>
        <h2 style="margin-bottom:0.3em;">New to the club? Just come along.</h2>
        <p style="margin:0; max-width:56ch;">Visitors and new players are always welcome on a Tuesday evening. If you&rsquo;d like to know more first, one of the officers below will be glad to help.</p>
      </div>
      <a class="btn btn-ghost" href="contact.html">Get in touch</a>
    </div>
  </section>
""",
)

print("index.html built")

# ---------------------------------------------------------------- ABOUT
OUT["about.html"] = page(
    "about.html",
    "About the Federation | Guernsey Chess Federation",
    "How the Guernsey Chess Federation is organised, its history since 1931, and its role running the island's leagues, the Inter-Insular match and international representation.",
    "about.html",
    body="""
  <header class="page-header">
    <div class="wrap">
      <a class="breadcrumb" href="index.html">&larr; Home</a>
      <p class="eyebrow">About</p>
      <h1>The Federation</h1>
      <p class="lede">Guernsey Chess Federation is the governing body for chess on the island. In practice, its members meet and play together through the Guernsey Chess Club &mdash; the two names describe the same organisation, worn for different purposes.</p>
    </div>
  </header>

  <section>
    <div class="wrap hero-grid" style="grid-template-columns: 1fr 1fr; align-items:start;">
      <div class="prose reveal-on-scroll">
        <h2>What the Federation does</h2>
        <p>The Federation organises the island&rsquo;s internal leagues and the Guernsey Chess Championship, runs the annual Inter-Insular match against Jersey, selects and supports players representing Guernsey at international level, and co-organises the Guernsey International Chess Festival each autumn.</p>
        <p>Day to day, this work is carried out by a small committee of volunteer officers &mdash; a President, Treasurer, Secretary, Tournament Secretary and Media Officer &mdash; supported by an Auditor and a Chess in Schools coordinator. Their contact details are on the <a href="contact.html">Contact page</a>.</p>
      </div>
      <div class="prose reveal-on-scroll">
        <h2>Affiliation</h2>
        <p>Guernsey is a member federation of FIDE, the International Chess Federation, and fields players and teams in FIDE-rated international events, including the Chess Olympiad, the FIDE World Senior Team Chess Championship, and the European Small Nations Association (ESNA) championships alongside Andorra, Cyprus, the Faroe Islands, Jersey, Liechtenstein, Luxembourg, Malta, Monaco and San Marino.</p>
        <p>Locally, Guernsey&rsquo;s closest rivalry is with Jersey, contested annually in the Inter-Insular match for the Hollis Cup &mdash; a fixture dating back to 1931.</p>
      </div>
    </div>
  </section>

  <div class="board-divider" aria-hidden="true"></div>

  <section>
    <div class="wrap">
      <p class="eyebrow">History</p>
      <h2>Nearly a century at the board</h2>
      <div class="reveal-on-scroll">
        <div class="feature-row">
          <div class="date">1930&ndash;31</div>
          <div>
            <h3>The Championship and the Hollis Cup</h3>
            <p>The Guernsey Chess Championship trophy was presented by C.F. Peek Esq in 1930, and the Club has organised the Championship every year since 1931. That same year, the first Inter-Insular match against Jersey was played at the Richmond Hotel, for the Hollis Cup presented by Mrs B. Hollis. The winner of the top board is recognised as Channel Island Champion and receives the Garde Trophy; since 1996, the winner of the highest non-top board receives the David Browning Trophy.</p>
          </div>
        </div>
        <div class="feature-row">
          <div class="date">1975</div>
          <div>
            <h3>The first International Chess Festival</h3>
            <p>The Guernsey International Chess Festival began in October 1975 at the Old Government House Hotel. It moved to St Martin&rsquo;s Hotel in 1979, to the Peninsula Hotel from 1994 to 2019, and to the St James Concert and Assembly Hall from 2022 to 2025. The Festival returns to the Peninsula Hotel for its 50th edition in November 2026. A Holiday Tournament has run alongside the main Open event since 1983.</p>
          </div>
        </div>
        <div class="feature-row">
          <div class="date">1977 &amp; 1991</div>
          <div>
            <h3>Junior chess and the Reserves match</h3>
            <p>The Federation began organising the Guernsey Junior Chess Championships in 1977, across four age categories. A Reserves match, for the Withers Shield, was added to the Inter-Insular fixture in 1991.</p>
          </div>
        </div>
        <div class="feature-row" style="border-bottom:none;">
          <div class="date">Today</div>
          <div>
            <h3>A small, welcoming federation</h3>
            <p>The Federation remains volunteer-run, with the Club meeting weekly at Les Cotils. Members regularly represent Guernsey at Olympiad, Senior Team and Small Nations level, and the island continues to host one of the longest-running international chess festivals in the Channel Islands.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="panel-oxblood">
    <div class="wrap" style="display:flex; justify-content:space-between; align-items:center; gap:24px; flex-wrap:wrap;">
      <div>
        <h2 style="margin-bottom:0.3em;">Want to know how the Federation is run?</h2>
        <p style="margin:0; max-width:56ch;">Every officer&rsquo;s role and contact details are listed on the Contact page.</p>
      </div>
      <a class="btn btn-ghost" href="contact.html">Officers &amp; contact</a>
    </div>
  </section>
""",
)
print("about.html built")

# ---------------------------------------------------------------- CLUB
OUT["club.html"] = page(
    "club.html",
    "The Club | Guernsey Chess Federation",
    "The Guernsey Chess Club meets every Tuesday at 7:30pm at Les Cotils. Details of club nights, internal leagues, gradings and how to get involved.",
    "club.html",
    body="""
  <header class="page-header">
    <div class="wrap">
      <a class="breadcrumb" href="index.html">&larr; Home</a>
      <p class="eyebrow">The Club</p>
      <h1>Club nights &amp; competitions</h1>
      <p class="lede">The Guernsey Chess Club meets every Tuesday evening at Les Cotils. Visitors are always welcome &mdash; whether you want to play in a rated tournament or simply enjoy a social game.</p>
    </div>
  </header>

  <section>
    <div class="wrap hero-grid" style="grid-template-columns: 0.9fr 1.1fr; align-items:start;">
      <div class="hairline-box reveal-on-scroll" style="padding:36px;" id="visit">
        <p class="eyebrow">Where &amp; when</p>
        <h2 style="font-size:1.5rem;">Tuesdays, 7:30pm</h2>
        <p style="color:var(--ink-soft)">Les Cotils, St Peter Port. Come along on the night, or contact one of the officers first if you&rsquo;d like to know more &mdash; see the <a class="text-link" style="display:inline-flex" href="contact.html">Contact page</a>.</p>
        <hr class="rule" style="margin:20px 0;">
        <p style="color:var(--ink-soft); margin-bottom:0;">Membership rates are set by the committee. Contact the Treasurer at <a href="mailto:treasurer@gcf.org.gg">treasurer@gcf.org.gg</a> for current details.</p>
      </div>
      <div class="prose reveal-on-scroll">
        <h2>New to chess, or new to the club?</h2>
        <p>The Club has previously run a free eight-week Adult Beginners Chess Course, covering the basic rules, good move selection, simple checkmates and basic tactics such as forks, pins and skewers. Courses like this are arranged from time to time &mdash; email <a href="mailto:chess@gcf.org.gg">chess@gcf.org.gg</a> to ask about the next one, or just come along on a Tuesday and one of the club&rsquo;s stronger players will happily give you a game.</p>
        <p>Younger players aged 8&ndash;16 are catered for separately by the <a href="juniors.html">Junior Chess Club</a>, which runs alongside the main club during school term.</p>
      </div>
    </div>
  </section>

  <div class="board-divider" aria-hidden="true"></div>

  <section>
    <div class="wrap">
      <p class="eyebrow">Internal competitions</p>
      <h2>The club season</h2>
      <p class="prose" style="margin-bottom:2em;">Club chess runs across two seasons: a Winter Season of leagues and knockout-style tournaments from September to May, and a Summer League from June to August that is open to non-members as well as members.</p>
      <div class="reveal-on-scroll">
        <div class="table-wrap">
          <table>
            <caption>Club competitions</caption>
            <thead>
              <tr><th scope="col">Competition</th><th scope="col">Format</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Championship</strong></td><td>The Club&rsquo;s top graded league, run since 1931 over two cycles (before and after Christmas). The winner is declared Guernsey Chess Champion and traditionally plays board 1 in the Inter-Insular match.</td></tr>
              <tr><td><strong>Division 2</strong></td><td>Graded league below the Championship.</td></tr>
              <tr><td><strong>Division 3</strong></td><td>Graded league for newer and developing players.</td></tr>
              <tr><td><strong>Summer League</strong></td><td>Runs June&ndash;August and is open to non-members &mdash; contact the Tournament Secretary to register.</td></tr>
              <tr><td><strong>Quickplay Open</strong></td><td>Faster time-control tournament held during the season.</td></tr>
              <tr><td><strong>Blitz Tournament</strong></td><td>Typically 5 minutes plus a small increment per move, open to members and non-members.</td></tr>
              <tr><td><strong>Quickplay Buzzer</strong></td><td>A ten-second-per-move buzzer format, played in a friendly spirit &mdash; a good introduction to faster chess.</td></tr>
              <tr><td><strong>Most Improved Player</strong></td><td>A season award recognising the player who has progressed furthest.</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <section class="tight" style="background:var(--paper-alt); border-top:1px solid var(--rule); border-bottom:1px solid var(--rule);">
    <div class="wrap hero-grid" style="grid-template-columns: 1fr 1fr; align-items:center;">
      <div class="reveal-on-scroll">
        <p class="eyebrow">Gradings</p>
        <h2>Club ELO gradings</h2>
        <p class="prose">The Club maintains its own ELO-style grading list, calculated annually from games played in the preceding twelve months, alongside FIDE ratings for members who hold them.</p>
        <a class="text-link" href="results.html#gradings">View the gradings list <svg><use href="#icon-arrow"/></svg></a>
      </div>
      <div class="reveal-on-scroll">
        <div class="callout">&ldquo;Visitors are always welcome. Please feel free to contact one of the officers if you wish to find out more.&rdquo;</div>
      </div>
    </div>
  </section>
""",
)
print("club.html built")

# ---------------------------------------------------------------- JUNIORS
JUNIOR_CHAMPIONS = [
    ("2000", "A Harbour", "T Moore", "B James", "S Hamperl"),
    ("1999", "B McManus", "S Orchard", "R Russell", "D Davison"),
    ("1998", "O Rowe", "A Harbour / S Orchard", "R Russell", "D Davison"),
    ("1997", "O Rowe", "B McManus", "R Russell", "B Wadley"),
    ("1996", "P Zadori", "J Burgess / O Rowe", "B McManus", "R Russell"),
    ("1995", "L Le Page", "T Woodington / J Burgess", "A Harbour", "K Abbotts"),
    ("1994", "P Hunt", "J Burgess", "M Fallaize", "J Draper"),
    ("1993", "P English", "T Woodington", "C Parrott", "S Mortimer"),
    ("1992", "J Briggs", "J Arnold", "J Carey", "S Geall"),
    ("1991", "C Mahy", "J Briggs", "M Godfrey", "J Geall"),
    ("1990", "C Mahy", "S Cummins", "M Godfrey", "J Carey"),
    ("1989", "N Lloyd", "J Briggs / C Mahy", "J Crabb", "C Parrott"),
    ("1988", "T Lomax", "M Ozanne", "J Arnold", "M Godfrey"),
    ("1987", "S Smith", "M Daley / M Ozanne", "D Legg", "J Arnold"),
    ("1986", "E Carey", "C Ledgard / M Daley / N Blackburn", "M Ozanne", "J Arnold"),
    ("1985", "J Moser", "C Ledgard", "N Lloyd", "J Barclay"),
    ("1984", "F Hamperl", "J Moser", "M Daley / N Blackburn / N Lloyd / W Walden / M Ozanne / D Strappini", "S Cummins / J Barclay"),
    ("1983", "J Bridel", "J Moser", "C Ledgard", "M Ozanne / N Amy"),
    ("1982", "K Martel", "F Hamperl / M Le Cras", "T Lomax", "M Ozanne / B Norman"),
    ("1981", "K Martel", "F Hamperl / C Osborne", "J Moser", "D Lemee / N Lloyd"),
    ("1980", "M Le Tissier", "K Martel / R Webber", "P Eker", "N Le Page / N Lloyd"),
    ("1979", "A La Chapelle", "K Martel / F Hamperl / A Howe / P Saunders / C Osborne", "&mdash;", "N Lloyd"),
    ("1978", "A Whittaker / A La Chapelle", "K Martel", "S Eker", "J Moser"),
    ("1977", "P Cutter / A Whittaker", "D English", "K Martel", "C Wall"),
]
junior_rows = "\n".join(
    "<tr><td class=\"num\">{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(*row)
    for row in JUNIOR_CHAMPIONS
)

OUT["juniors.html"] = page(
    "juniors.html",
    "Junior Chess | Guernsey Chess Federation",
    "Junior Chess Club for ages 8-16, every Tuesday during term time at Les Cotils. History of the Guernsey Junior Chess Championships since 1977.",
    "juniors.html",
    body=f"""
  <header class="page-header">
    <div class="wrap">
      <a class="breadcrumb" href="index.html">&larr; Home</a>
      <p class="eyebrow">Juniors</p>
      <h1>Junior Chess</h1>
      <p class="lede">A weekly club for young players, and a tradition of junior competition on the island going back to 1977.</p>
    </div>
  </header>

  <section>
    <div class="wrap hero-grid" style="grid-template-columns: 0.9fr 1.1fr; align-items:start;">
      <div class="hairline-box reveal-on-scroll" style="padding:36px;">
        <p class="eyebrow">Every term-time Tuesday</p>
        <h2 style="font-size:1.5rem;">6:00&ndash;7:15pm</h2>
        <p style="color:var(--ink-soft)">Junior Chess Club is for young people aged 8 to 16, held at the Les Cotils Coffee Shop, running alongside the main club.</p>
        <a class="btn" style="margin-top:8px;" href="mailto:juniors@gcf.org.gg">Email juniors@gcf.org.gg</a>
      </div>
      <div class="prose reveal-on-scroll">
        <h2>Chess in schools</h2>
        <p>Alongside the weekly junior club, the Federation has a Chess in Schools coordinator working with island schools. Local schools have also run their own open junior tournament since 2000; as a result, the Federation&rsquo;s own Junior Chess Championships have not been held separately since that year.</p>
        <p>For school-related enquiries, contact the Federation&rsquo;s Chess in Schools officer &mdash; details on the <a href="contact.html">Contact page</a>.</p>
      </div>
    </div>
  </section>

  <div class="board-divider" aria-hidden="true"></div>

  <section>
    <div class="wrap">
      <p class="eyebrow">Roll of honour</p>
      <h2>Guernsey Junior Chess Championships, 1977&ndash;2000</h2>
      <p class="prose" style="margin-bottom:1.6em;">The Federation organised the Junior Championships across four age categories each year from 1977. Since 1992, the Under-18 winner has received the Chris Mahy Cup; since 1995, the Under-16 winner has received the Dot Ogier Shield.</p>
      <div class="reveal-on-scroll">
        <div class="table-wrap">
          <table>
            <caption>Junior champions by age category</caption>
            <thead>
              <tr><th scope="col">Year</th><th scope="col">Under 18</th><th scope="col">Under 16</th><th scope="col">Under 13</th><th scope="col">Under 10</th></tr>
            </thead>
            <tbody>
{junior_rows}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <section class="panel-oxblood">
    <div class="wrap" style="display:flex; justify-content:space-between; align-items:center; gap:24px; flex-wrap:wrap;">
      <div>
        <h2 style="margin-bottom:0.3em;">Bring your child along on a Tuesday</h2>
        <p style="margin:0; max-width:56ch;">No experience necessary &mdash; junior sessions are relaxed and suitable for complete beginners as well as improving players.</p>
      </div>
      <a class="btn btn-ghost" href="mailto:juniors@gcf.org.gg">Email the junior club</a>
    </div>
  </section>
""",
)
print("juniors.html built")

# ---------------------------------------------------------------- EVENTS
OUT["events.html"] = page(
    "events.html",
    "Events & Tournaments | Guernsey Chess Federation",
    "The Guernsey International Chess Festival, the Inter-Insular match against Jersey, and Guernsey's international representation at Olympiad, Senior Team and Small Nations level.",
    "events.html",
    body="""
  <header class="page-header">
    <div class="wrap">
      <a class="breadcrumb" href="index.html">&larr; Home</a>
      <p class="eyebrow">Events</p>
      <h1>Events &amp; tournaments</h1>
      <p class="lede">From the club&rsquo;s weekly leagues to Guernsey&rsquo;s long-running international festival and its rivalry with Jersey, here is the island&rsquo;s chess calendar.</p>
    </div>
  </header>

  <section id="festival">
    <div class="wrap">
      <div class="hairline-box reveal-on-scroll" style="padding:44px;">
        <p class="eyebrow">1&ndash;7 November 2026 &middot; Peninsula Hotel, St Peter Port</p>
        <h2 style="font-size:2rem;">The 50th Guernsey International Chess Festival</h2>
        <p class="prose" style="color:var(--ink-soft); font-size:1.05rem;">Two FIDE-rated classical tournaments &mdash; Open and Challengers &mdash; run over one round per day, with a classical time control of 40 moves in 100 minutes followed by all remaining moves in a further 40 minutes, plus a 30-second increment from move one. A FIDE-rated Blitz tournament is also planned, with its date to be announced.</p>
        <div class="table-wrap" style="margin:1.6em 0;">
          <table>
            <caption>Prize funds</caption>
            <tbody>
              <tr><th scope="row">Open Tournament</th><td>&pound;3,000</td></tr>
              <tr><th scope="row">Challenger Tournament</th><td>&pound;900</td></tr>
              <tr><th scope="row">Blitz Tournament</th><td>&pound;175 minimum</td></tr>
            </tbody>
          </table>
        </div>
        <p class="prose" style="color:var(--ink-soft)">Figures are minimum cash prize funds, excluding additional Chessable prizes, and may increase with entries. The prizegiving dinner on 7 November is included. The Festival is financially supported by the FIDE Open Aid Project.</p>
        <div class="hero-actions" style="margin-top:1.2em;">
          <a class="btn btn-oxblood" href="https://guernseychessfestival.org.gg/">Festival site &amp; registration</a>
          <a class="btn btn-ghost" href="https://chess-results.com/">Chess-Results.com</a>
        </div>
      </div>
    </div>
  </section>

  <section class="tight">
    <div class="wrap">
      <p class="eyebrow">History</p>
      <h2>Half a century of the Festival</h2>
      <p class="prose">The first Guernsey International Chess Festival was held in October 1975 at the Old Government House Hotel. It moved to the Ronnie Ronalde St Martin&rsquo;s Hotel in 1979, to the Peninsula Hotel from 1994 until 2019, and to the St James Concert and Assembly Hall from 2022 to 2025. The Festival returns to the Peninsula Hotel for its 50th edition. A Holiday Tournament has run alongside the main Open event every year since 1983, and by 1989 the two tournaments together drew 226 players.</p>
    </div>
  </section>

  <div class="board-divider" aria-hidden="true"></div>

  <section id="inter-insular">
    <div class="wrap hero-grid" style="grid-template-columns: 1fr 1fr; align-items:start;">
      <div class="prose reveal-on-scroll">
        <p class="eyebrow">The island rivalry</p>
        <h2>Inter-Insular: Guernsey v Jersey</h2>
        <p>Guernsey and Jersey have met annually (bar wartime years) since 1931, playing for the Hollis Cup. The two teams meet over 16 boards, alternating host islands each year. The winner on top board becomes Channel Island Champion and takes the Garde Trophy; since 1996, the winner of the highest board that isn&rsquo;t board one receives the David Browning Trophy. A reserves match, for the Withers Shield, has run alongside the main fixture since 1991.</p>
        <p>The 85th match was played on Saturday 27 April 2024 at the Ambassadeur Hotel, Jersey. As recorded in the Federation&rsquo;s published match archive, the fixture&rsquo;s all-time record stands at Jersey 47 wins, Guernsey 30 wins and 7 draws &mdash; a record that continues to be updated each year.</p>
      </div>
      <div class="reveal-on-scroll">
        <div class="callout">&ldquo;No clocks, adjournments or adjudication in those days&rdquo; &mdash; on the first Inter-Insular match, played over 16 boards at the Richmond Hotel in 1931, which ended 8&ndash;8 and finished at 11.30pm.</div>
      </div>
    </div>
  </section>

  <section class="tight" style="background:var(--paper-alt); border-top:1px solid var(--rule); border-bottom:1px solid var(--rule);">
    <div class="wrap">
      <p class="eyebrow">Representing Guernsey</p>
      <h2>International chess</h2>
      <div class="grid-3">
        <div class="card reveal-on-scroll">
          <span class="card-meta">FIDE Chess Olympiad</span>
          <h3>Olympiad</h3>
          <p>Guernsey has fielded teams at the biennial FIDE Chess Olympiad, most recently the 45th Olympiad in Budapest, where several players earned FIDE titles.</p>
        </div>
        <div class="card reveal-on-scroll">
          <span class="card-meta">50+ category, since 2024</span>
          <h3>World Senior Team Championship</h3>
          <p>Guernsey has fielded a team at the FIDE World Senior Team Chess Championship since 2024, competing in Krakow, Poland and Prague, Czech Republic.</p>
        </div>
        <div class="card reveal-on-scroll">
          <span class="card-meta">ESNA</span>
          <h3>European Small Nations</h3>
          <p>Guernsey competes in ESNA individual and team championships alongside Andorra, Cyprus, the Faroe Islands, Jersey, Liechtenstein, Luxembourg, Malta, Monaco and San Marino.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap hero-grid" style="grid-template-columns: 1fr 1fr; align-items:start;">
      <div class="reveal-on-scroll">
        <p class="eyebrow">The club season</p>
        <h2>How the year is structured</h2>
        <div class="table-wrap">
          <table>
            <tbody>
              <tr><th scope="row">Winter Season</th><td>September&ndash;May: Championship, Division 2 &amp; 3, Blitz and Quickplay tournaments, and social chess</td></tr>
              <tr><th scope="row">Summer League</th><td>June&ndash;August, open to non-members</td></tr>
              <tr><th scope="row">Annual General Meeting</th><td>Held each spring at Les Cotils &mdash; recent AGMs have taken place in May</td></tr>
              <tr><th scope="row">Inter-Insular v Jersey</th><td>Typically played in spring, alternating host islands</td></tr>
              <tr><th scope="row">International Chess Festival</th><td>Held in autumn each year</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="reveal-on-scroll">
        <p class="eyebrow">Keep up to date</p>
        <h2>Current fixtures &amp; results</h2>
        <p class="prose">Live results for FIDE-rated events, including the Festival, are published on Chess-Results.com as they happen. For the latest club announcements, see our <a href="news.html">News page</a> or follow the Federation on social media.</p>
        <a class="text-link" href="news.html">Read the news archive <svg><use href="#icon-arrow"/></svg></a>
      </div>
    </div>
  </section>
""",
)
print("events.html built")

# ---------------------------------------------------------------- NEWS
NEWS_ITEMS = [
    ("18 Mar 2025", "The 49th BWCI Guernsey International Chess Festival, 19&ndash;25 October 2025",
     "Held at the St James Concert and Assembly Hall, with a Blitz tournament and simultaneous exhibition planned for the evening of 18 October, and the prizegiving dinner on 21 October."),
    ("28 Feb 2025", "Guernsey at the FIDE World Senior Team Chess Championships, Prague",
     "Peter Kirby, Peter Rowe, Toby Brookfield, Jamie Morgan and Russell Finch represented Guernsey in the 50+ category, for the second time as a national team, in a nine-round event with 54 teams."),
    ("13 Oct 2024", "WFM title awarded to Arita Strade",
     "Arita earned the Woman FIDE Master title for her performance at the 45th FIDE Chess Olympiad in Budapest, scoring 6.5 out of 10."),
    ("13 Oct 2024", "WCM title awarded to Gerda Nevska",
     "Gerda earned the Woman FIDE Candidate Master title for her performance at the 45th FIDE Chess Olympiad in Budapest, scoring 6 out of 11."),
    ("12 Oct 2024", "CM title awarded to Garth Owen",
     "Garth earned the FIDE Candidate Master title for his performance at the 45th FIDE Chess Olympiad in Budapest, scoring 4.5 out of 8."),
    ("6 Oct 2024", "CM title awarded to Jamie Morgan",
     "Jamie earned the FIDE Candidate Master title for his performance at the 44th FIDE Chess Olympiad in Chennai in 2022, scoring 4 out of 9."),
    ("17 Jun 2024", "Summer League 2024",
     "The Guernsey Chess Club 2024 Summer League started on Tuesday 25 June, open to non-members. Games began at 19:15."),
    ("13 Apr 2024", "AGM &mdash; Tuesday 14 May 2024",
     "Members were invited to the AGM at Les Cotils Coffee Shop. Anyone interested in standing for election to a club officer role was invited to get in touch."),
    ("8 Mar 2024", "European Small Nations Individual selection",
     "Arita Strade and Gerda Nevska were selected to represent Guernsey at the 5th European Small Nations Individual Open and 2nd Women&rsquo;s Championships in Andorra, against players from Andorra, Cyprus, the Faroe Islands, Jersey, Liechtenstein, Malta, Monaco and San Marino."),
    ("5 Feb 2024", "85th Inter-Insular match between Guernsey and Jersey",
     "The 85th Inter-Insular match for the Hollis Trophy was played on Saturday 27 April 2024 at the Ambassadeur Hotel, Jersey."),
    ("9 Jan 2024", "Free Adult Beginners Chess Course",
     "An eight-week course starting Thursday 25 January 2024 covered the basic rules of chess, good move selection, simple checkmates and basic tactics, held at Les Cotils."),
    ("21 Nov 2023", "8th European Small Nations Team Championship",
     "Andorra won the event, which concluded in Jersey. Peter Kirby, Fred Hamperl, Arita Strade, Gerda Nevska and Jamie Morgan represented Guernsey over nine rounds."),
    ("22 Nov 2022", "Guernsey retains the Hollis Trophy",
     "The 83rd Inter-Insular match, played at Jersey&rsquo;s Pomme D&rsquo;Or Hotel, went to the wire: Jersey led 7&ndash;6 until Arita Strade and Colin Goman won on time to secure the match for Guernsey. Arita Strade also won the David Browning Trophy for her win on board 3."),
    ("11 Jun 2022", "Championship results 2021/22",
     "Fred Hamperl became Guernsey Chess Champion for the 10th time as over-the-board chess returned to the Club at Les Cotils after two years of pandemic disruption, winning all seven games of his second cycle for a total of 11 points."),
]
news_rows = "\n".join(
    """<div class="list-row reveal-on-scroll">
          <div class="date">{}</div>
          <div class="body"><h4>{}</h4><p>{}</p></div>
        </div>""".format(*item)
    for item in NEWS_ITEMS
)

OUT["news.html"] = page(
    "news.html",
    "News | Guernsey Chess Federation",
    "Announcements, results and reports from the Guernsey Chess Federation and Club, including festival news, Inter-Insular results and international representation.",
    "news.html",
    body=f"""
  <header class="page-header">
    <div class="wrap">
      <a class="breadcrumb" href="index.html">&larr; Home</a>
      <p class="eyebrow">News</p>
      <h1>News &amp; announcements</h1>
      <p class="lede">A record of recent announcements from the Federation and Club. For day-to-day updates between posts, follow us on Facebook, X or Instagram.</p>
    </div>
  </header>

  <section>
    <div class="wrap" style="max-width:820px;">
      {news_rows}
      <p style="margin-top:2.5em; color:var(--ink-faint); font-size:0.92rem;">Looking for something older? The Federation keeps a fuller press and reports archive &mdash; contact <a class="text-link" style="display:inline-flex" href="mailto:media.officer@gcf.org.gg">the Media Officer</a> for past reports, including write-ups from the Small Nations and Senior Team championships.</p>
    </div>
  </section>

  <section class="panel-oxblood">
    <div class="wrap" style="display:flex; justify-content:space-between; align-items:center; gap:24px; flex-wrap:wrap;">
      <div>
        <h2 style="margin-bottom:0.3em;">Follow along between updates</h2>
        <p style="margin:0; max-width:56ch;">Social media carries the most current news &mdash; match nights, results and festival updates as they happen.</p>
      </div>
      <div class="social-row" style="margin-top:0;">
        <a href="https://www.facebook.com/GuernseyChess/" aria-label="Guernsey Chess on Facebook" style="border-color:rgba(255,255,255,0.5)"><svg width="15" height="15" aria-hidden="true"><use href="#icon-facebook"/></svg></a>
        <a href="https://twitter.com/GuernseyChess" aria-label="Guernsey Chess on X (Twitter)" style="border-color:rgba(255,255,255,0.5)"><svg width="15" height="15" aria-hidden="true"><use href="#icon-x"/></svg></a>
        <a href="https://www.instagram.com/guernseychess/" aria-label="Guernsey Chess on Instagram" style="border-color:rgba(255,255,255,0.5)"><svg width="15" height="15" aria-hidden="true"><use href="#icon-instagram"/></svg></a>
      </div>
    </div>
  </section>
""",
)
print("news.html built")

# ---------------------------------------------------------------- RESULTS
CHAMPIONS = [
    ("2022/23", "Fred Hamperl", ""), ("2021/22", "Fred Hamperl", ""), ("2020/21", "Fred Hamperl", ""),
    ("2019/20", "Chris Holland", "No CI competition"), ("2018/19", "Chris Holland", "="),
    ("2017/18", "Chris Holland", "="), ("2016/17", "Chris Holland", "="), ("2015/16", "Fred Hamperl", "="),
    ("2014/15", "Fred Hamperl", "*"), ("2013/14", "Fred Hamperl", "*"), ("2012/13", "Fred Hamperl", "="),
    ("2011/12", "Fred Hamperl", "*"), ("2010/11", "Fred Hamperl", "="), ("2009/10", "Fred Hamperl", "*"),
    ("2008/09", "Peter Rowe", ""), ("2007/08", "Peter Rowe", "="),
    ("2006/07", "Fred Hamperl &amp; Peter Rowe", "* (FH won CI)"), ("2005/06", "Peter Rowe", ""),
    ("2004/05", "Peter Rowe", ""), ("2003/04", "Fred Hamperl &amp; Peter Rowe", "="),
    ("2002/03", "Peter Rowe", "="), ("2001/02", "Tim Knight", "="),
]
champ_rows = "\n".join(
    '<tr><td class="num">{}</td><td>{}</td><td>{}</td></tr>'.format(y, w, ci) for y, w, ci in CHAMPIONS
)

GRADINGS = [
    ("1", "F Hamperl", "2006", "1983"), ("2", "P Kirby", "1990", "2000"), ("3", "P Rowe", "1924", "1938"),
    ("4", "G Nevska", "1842", "1840"), ("5", "T Brookfield", "1840", "1815"), ("6", "A Hale", "1819", "1881"),
    ("7", "M Kirk", "1759", "1738"), ("8", "P Cutter", "1697", "2073"), ("9", "J Cummins", "1604", "1729"),
    ("10", "B Nalichowski", "1590", "&mdash;"), ("11", "K Bateman", "1559", "1706"),
    ("12", "O Rowe", "1555", "1515"), ("13", "S Naftel", "1547", "&mdash;"), ("14", "T Harnden", "1497", "1488"),
    ("15", "D De L&rsquo;Isle", "1462", "&mdash;"), ("16", "C Goman", "1440", "1619"), ("17", "J Hill", "1301", "&mdash;"),
]
grading_rows = "\n".join(
    '<tr><td class="num">{}</td><td>{}</td><td class="num">{}</td><td class="num">{}</td></tr>'.format(*row)
    for row in GRADINGS
)

SUMMER_WINNERS = [
    ("2023", "Matt Kirk"), ("2022", "Fred Hamperl"), ("2021", "Fred Hamperl"), ("2020", "No competition"),
    ("2019", "Fred Hamperl &amp; Peter Rowe"), ("2018", "Chris Holland"), ("2017", "Chris Holland"),
    ("2016", "Chris Holland"), ("2015", "Toby Brookfield"), ("2014", "Fred Hamperl"),
]
summer_rows = "\n".join(
    '<tr><td class="num">{}</td><td>{}</td></tr>'.format(y, w) for y, w in SUMMER_WINNERS
)

OUT["results.html"] = page(
    "results.html",
    "Results & Gradings | Guernsey Chess Federation",
    "Guernsey Chess Champions roll of honour, club ELO gradings, Summer League winners and the Inter-Insular match record against Jersey.",
    "results.html",
    body=f"""
  <header class="page-header">
    <div class="wrap">
      <a class="breadcrumb" href="index.html">&larr; Home</a>
      <p class="eyebrow">Results</p>
      <h1>Results &amp; gradings</h1>
      <p class="lede">A record of the Club&rsquo;s major honours. For live results from FIDE-rated events, including the International Festival, see Chess-Results.com.</p>
    </div>
  </header>

  <section>
    <div class="wrap hero-grid" style="grid-template-columns:1fr 1fr; align-items:start;">
      <div class="reveal-on-scroll">
        <p class="eyebrow">Since 1931</p>
        <h2>Guernsey Chess Champions</h2>
        <p class="prose">The Championship winner is declared Guernsey Chess Champion for the year. A &lsquo;*&rsquo; denotes the winner was also Channel Island Champion that year; &lsquo;=&rsquo; denotes joint Channel Island Champion.</p>
        <div class="table-wrap">
          <table>
            <caption>Recent champions (fuller records to 1931 held by the Federation)</caption>
            <thead><tr><th scope="col">Season</th><th scope="col">Champion</th><th scope="col">CI title</th></tr></thead>
            <tbody>
{champ_rows}
            </tbody>
          </table>
        </div>
      </div>
      <div class="reveal-on-scroll">
        <p class="eyebrow">Summer League</p>
        <h2>Recent winners</h2>
        <p class="prose">The Summer League trophy was made and presented by Ian Rawlins-Duquemin.</p>
        <div class="table-wrap">
          <table>
            <thead><tr><th scope="col">Year</th><th scope="col">Winner</th></tr></thead>
            <tbody>
{summer_rows}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <div class="board-divider" aria-hidden="true"></div>

  <section id="gradings">
    <div class="wrap">
      <p class="eyebrow">Gradings</p>
      <h2>Club ELO gradings &mdash; 1 May 2022</h2>
      <p class="prose" style="margin-bottom:1.6em;">This is the most recent full club grading list captured from the Federation&rsquo;s records. Gradings are recalculated each year from games played between 1 May and the following 30 April. Current figures are held by the Ratings Officer &mdash; contact <a href="mailto:treasurer@gcf.org.gg">treasurer@gcf.org.gg</a> for up-to-date gradings.</p>
      <div class="reveal-on-scroll">
        <div class="table-wrap">
          <table>
            <caption>Club &amp; FIDE Elo, 1 May 2022</caption>
            <thead><tr><th scope="col">#</th><th scope="col">Player</th><th scope="col">Club Elo</th><th scope="col">FIDE Elo</th></tr></thead>
            <tbody>
{grading_rows}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <section class="tight" style="background:var(--paper-alt); border-top:1px solid var(--rule); border-bottom:1px solid var(--rule);">
    <div class="wrap hero-grid" style="grid-template-columns:1fr 1fr; align-items:center;">
      <div class="reveal-on-scroll">
        <p class="eyebrow">Inter-Insular record</p>
        <h2>Guernsey v Jersey, since 1931</h2>
        <p class="prose">As recorded in the Federation&rsquo;s published match archive, the all-time Inter-Insular record stands at Jersey 47 wins, Guernsey 30 wins and 7 draws. The 85th match was played on 27 April 2024 at the Ambassadeur Hotel, Jersey.</p>
        <a class="text-link" href="events.html#inter-insular">More on the Inter-Insular match <svg><use href="#icon-arrow"/></svg></a>
      </div>
      <div class="reveal-on-scroll">
        <div class="fact-strip" style="grid-template-columns:1fr 1fr 1fr;">
          <div><span class="n">47</span><span class="l">Jersey wins</span></div>
          <div><span class="n">30</span><span class="l">Guernsey wins</span></div>
          <div><span class="n">7</span><span class="l">Draws</span></div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap center">
      <p class="eyebrow">Current standings</p>
      <h2>Following a tournament live?</h2>
      <p class="prose" style="margin:0 auto 1.4em;">Round-by-round pairings and results for FIDE-rated events, including the Guernsey International Chess Festival, are published on Chess-Results.com as each round finishes.</p>
      <a class="btn btn-oxblood" href="https://chess-results.com/">Visit Chess-Results.com</a>
    </div>
  </section>
""",
)
print("results.html built")

# ---------------------------------------------------------------- CONTACT
OFFICERS = [
    ("Jon Hill", "President", "", "president@gcf.org.gg"),
    ("Peter Rowe", "Treasurer &amp; Ratings Officer", "+44 1481 238717", "treasurer@gcf.org.gg"),
    ("Peter Rowe", "Secretary", "", "secretary@gcf.org.gg"),
    ("Nick Royle", "Tournament Secretary", "", "tournament.secretary@gcf.org.gg"),
    ("Marie de Carteret", "Media Officer", "", "media.officer@gcf.org.gg"),
]
NON_COMMITTEE = [
    ("Terry Harnden", "Auditor", "+44 1481 249408", "terry.harnden@gov.gg"),
    ("Chris Holland", "Chess in Schools", "+44 1481 242139", "chrisholland@cwgsy.net"),
]


def officer_card(name, role, phone, email):
    phone_html = f'<div>{phone}</div>' if phone else ""
    return f"""<div class="officer-card reveal-on-scroll">
          <div><div class="name">{name}</div><div class="role">{role}</div></div>
          <div class="contact">{phone_html}<div><a href="mailto:{email}">{email}</a></div></div>
        </div>"""


officer_rows = "\n        ".join(officer_card(*o) for o in OFFICERS)
non_committee_rows = "\n        ".join(officer_card(*o) for o in NON_COMMITTEE)

OUT["contact.html"] = page(
    "contact.html",
    "Contact | Guernsey Chess Federation",
    "Contact the Guernsey Chess Federation's officers, find out where and when the club meets, and follow the Federation on social media.",
    "contact.html",
    body=f"""
  <header class="page-header">
    <div class="wrap">
      <a class="breadcrumb" href="index.html">&larr; Home</a>
      <p class="eyebrow">Contact</p>
      <h1>Officers &amp; contact</h1>
      <p class="lede">The Federation is run by a small committee of volunteers. Get in touch with the relevant officer below, or simply come along on a Tuesday.</p>
    </div>
  </header>

  <section>
    <div class="wrap hero-grid" style="grid-template-columns:1.1fr 0.9fr; align-items:start;">
      <div>
        <p class="eyebrow">Committee</p>
        {officer_rows}
        <p class="eyebrow" style="margin-top:2.2em;">Non-committee</p>
        {non_committee_rows}
      </div>
      <div class="v-space">
        <div class="hairline-box reveal-on-scroll" style="padding:32px;">
          <p class="eyebrow">Where we meet</p>
          <div style="display:flex; gap:12px; align-items:flex-start; margin-bottom:1em;">
            <svg width="20" height="20" style="flex-shrink:0; margin-top:2px; color:var(--oxblood)" aria-hidden="true"><use href="#icon-pin"/></svg>
            <div><strong>Les Cotils</strong><br>St Peter Port, Guernsey</div>
          </div>
          <div style="display:flex; gap:12px; align-items:flex-start;">
            <svg width="20" height="20" style="flex-shrink:0; margin-top:2px; color:var(--oxblood)" aria-hidden="true"><use href="#icon-mail"/></svg>
            <div><strong>Tuesdays, 7:30pm</strong><br>Main club night, visitors welcome<br><br><strong>Tuesdays, 6:00&ndash;7:15pm</strong><br>Junior club, term-time only, at Les Cotils Coffee Shop</div>
          </div>
        </div>
        <div class="hairline-box reveal-on-scroll" style="padding:32px;">
          <p class="eyebrow">General enquiries</p>
          <ul style="list-style:none; padding:0; margin:0; font-size:0.95rem;" class="v-space">
            <li><strong>Club &amp; general:</strong> <a class="text-link" style="display:inline-flex" href="mailto:chess@gcf.org.gg">chess@gcf.org.gg</a></li>
            <li><strong>Federation / AGM:</strong> <a class="text-link" style="display:inline-flex" href="mailto:gcf@gcf.org.gg">gcf@gcf.org.gg</a></li>
            <li><strong>Festival:</strong> <a class="text-link" style="display:inline-flex" href="mailto:festival@gcf.org.gg">festival@gcf.org.gg</a></li>
            <li><strong>Junior chess:</strong> <a class="text-link" style="display:inline-flex" href="mailto:juniors@gcf.org.gg">juniors@gcf.org.gg</a></li>
          </ul>
        </div>
        <div class="hairline-box reveal-on-scroll" style="padding:32px;">
          <p class="eyebrow">Follow us</p>
          <div class="social-row" style="margin-top:0;">
            <a href="https://www.facebook.com/GuernseyChess/" aria-label="Guernsey Chess on Facebook" style="border-color:var(--rule-strong); color:var(--ink)"><svg width="15" height="15" aria-hidden="true"><use href="#icon-facebook"/></svg></a>
            <a href="https://twitter.com/GuernseyChess" aria-label="Guernsey Chess on X (Twitter)" style="border-color:var(--rule-strong); color:var(--ink)"><svg width="15" height="15" aria-hidden="true"><use href="#icon-x"/></svg></a>
            <a href="https://www.instagram.com/guernseychess/" aria-label="Guernsey Chess on Instagram" style="border-color:var(--rule-strong); color:var(--ink)"><svg width="15" height="15" aria-hidden="true"><use href="#icon-instagram"/></svg></a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="tight" style="border-top:1px solid var(--rule);">
    <div class="wrap center">
      <p class="prose" style="margin:0 auto; color:var(--ink-faint); font-size:0.9rem;">Guernsey is a member federation of FIDE, the International Chess Federation.</p>
    </div>
  </section>
""",
)
print("contact.html built")

BUILD_DIR = ROOT
for fname, html in OUT.items():
    with open(os.path.join(BUILD_DIR, fname), "w", encoding="utf-8") as f:
        f.write(html)
print("Wrote", len(OUT), "file(s)")
