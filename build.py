import json, base64

with open('img_data.json') as f:
    imgs = json.load(f)

html = f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>פשוט בריא | סיון אופירי</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

  :root {{
    --cream:   #F7F5F0;
    --white:   #FFFFFF;
    --sage-bg: #EAF0E8;
    --sage-mid:#F2EFE9;
    --olive:   #2C3D2D;
    --olive2:  #3D5A3E;
    --sage-txt:#6B8C6E;
    --sage-num:#9BB89E;
    --gold:    #D4B96A;
    --text-dark:#2C3D2D;
    --text-mid: #4A4A4A;
    --text-light:#6B6B6B;
    --radius-sm:14px;
    --radius-md:20px;
    --radius-lg:24px;
    --radius-pill:50px;
  }}

  html {{ scroll-behavior: smooth; }}

  body {{
    font-family: 'Heebo', sans-serif;
    background: var(--cream);
    color: var(--text-dark);
    direction: rtl;
    -webkit-font-smoothing: antialiased;
  }}

  /* ─── STICKY NAV ─── */
  .nav {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(247,245,240,0.92);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(44,61,45,0.08);
    padding: 14px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .nav-logo {{
    font-size: 20px;
    font-weight: 700;
    color: var(--olive);
    letter-spacing: -0.5px;
  }}
  .nav-logo span {{ color: var(--sage-txt); }}
  .nav-links {{
    display: flex;
    gap: 28px;
    list-style: none;
  }}
  .nav-links a {{
    font-size: 14px;
    font-weight: 500;
    color: var(--text-mid);
    text-decoration: none;
    transition: color .2s;
  }}
  .nav-links a:hover {{ color: var(--olive); }}
  .nav-cta {{
    background: var(--olive);
    color: #fff !important;
    padding: 9px 22px;
    border-radius: var(--radius-pill);
    font-size: 13px !important;
    font-weight: 700 !important;
    transition: background .2s !important;
  }}
  .nav-cta:hover {{ background: var(--olive2) !important; }}
  @media(max-width:768px){{
    .nav-links {{ display: none; }}
    .nav {{ padding: 12px 20px; }}
  }}

  /* ─── SHARED ─── */
  .section {{ padding: 80px 40px; }}
  .section-inner {{ max-width: 860px; margin: 0 auto; }}
  .section-inner-sm {{ max-width: 680px; margin: 0 auto; }}
  .tag {{
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--sage-txt);
    background: var(--sage-bg);
    padding: 5px 18px;
    border-radius: var(--radius-pill);
    margin-bottom: 18px;
  }}
  .tag-dark {{
    color: var(--sage-num);
    background: rgba(255,255,255,0.1);
  }}
  .section-title {{
    font-size: clamp(28px, 4vw, 38px);
    font-weight: 900;
    color: var(--text-dark);
    line-height: 1.25;
    margin-bottom: 16px;
  }}
  .section-sub {{
    font-size: 16px;
    font-weight: 300;
    color: var(--text-mid);
    line-height: 1.85;
    max-width: 600px;
  }}
  .btn {{
    display: inline-block;
    background: var(--olive);
    color: #fff;
    font-family: 'Heebo', sans-serif;
    font-size: 16px;
    font-weight: 700;
    padding: 16px 44px;
    border-radius: var(--radius-pill);
    border: none;
    cursor: pointer;
    text-decoration: none;
    transition: background .2s, transform .15s;
    line-height: 1;
  }}
  .btn:hover {{ background: var(--olive2); transform: translateY(-2px); }}
  .btn-lg {{
    font-size: 17px;
    padding: 18px 52px;
  }}
  .btn-green {{
    background: var(--olive2);
  }}
  .text-center {{ text-align: center; }}

  /* ─── SECTION 1: HERO ─── */
  #hero {{
    background: var(--cream);
    padding: 0;
    overflow: hidden;
  }}
  .hero-inner {{
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 88vh;
    align-items: center;
  }}
  .hero-text {{
    padding: 80px 60px 80px 40px;
  }}
  .hero-badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--sage-bg);
    color: var(--olive2);
    font-size: 12px;
    font-weight: 700;
    padding: 7px 18px;
    border-radius: var(--radius-pill);
    margin-bottom: 28px;
    letter-spacing: 0.05em;
  }}
  .hero-badge-dot {{
    width: 6px; height: 6px;
    background: var(--sage-txt);
    border-radius: 50%;
  }}
  .hero-h1 {{
    font-size: clamp(64px, 8vw, 96px);
    font-weight: 900;
    color: var(--olive);
    line-height: 1;
    letter-spacing: -2px;
    margin-bottom: 12px;
  }}
  .hero-h2 {{
    font-size: clamp(18px, 2.5vw, 24px);
    font-weight: 300;
    color: var(--text-mid);
    line-height: 1.5;
    margin-bottom: 20px;
    max-width: 480px;
  }}
  .hero-p {{
    font-size: 15px;
    font-weight: 300;
    color: var(--text-light);
    line-height: 1.85;
    max-width: 460px;
    margin-bottom: 36px;
  }}
  .hero-trust {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin-top: 20px;
    font-size: 13px;
    color: var(--text-light);
  }}
  .hero-trust-item {{
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .hero-trust-dot {{
    width: 5px; height: 5px;
    background: var(--sage-txt);
    border-radius: 50%;
  }}
  .hero-img-wrap {{
    position: relative;
    height: 100%;
    min-height: 88vh;
    overflow: hidden;
  }}
  .hero-img-wrap img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center top;
  }}
  .hero-img-overlay {{
    position: absolute;
    inset: 0;
    background: linear-gradient(to right, var(--cream) 0%, transparent 30%);
  }}
  @media(max-width:900px){{
    .hero-inner {{ grid-template-columns: 1fr; min-height: auto; }}
    .hero-img-wrap {{ min-height: 55vw; order: -1; }}
    .hero-img-overlay {{ background: linear-gradient(to bottom, transparent 60%, var(--cream) 100%); }}
    .hero-text {{ padding: 40px 24px 60px; }}
    .hero-h1 {{ font-size: clamp(56px, 14vw, 80px); }}
  }}

  /* ─── SECTION 2: PAIN ─── */
  #pain {{
    background: var(--white);
  }}
  .pain-icon-row {{
    display: flex;
    gap: 40px;
    margin-top: 48px;
    flex-wrap: wrap;
  }}
  .pain-icon-item {{
    display: flex;
    align-items: flex-start;
    gap: 16px;
    flex: 1;
    min-width: 200px;
  }}
  .pain-icon-box {{
    width: 44px;
    height: 44px;
    min-width: 44px;
    background: var(--sage-bg);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .pain-icon-box svg {{ width: 22px; height: 22px; }}
  .pain-icon-label {{
    font-size: 14px;
    font-weight: 500;
    color: var(--text-dark);
    line-height: 1.5;
  }}
  .pain-icon-sub {{
    font-size: 13px;
    font-weight: 300;
    color: var(--text-light);
    margin-top: 3px;
    line-height: 1.6;
  }}
  .pain-quote {{
    margin-top: 48px;
    border-right: 3px solid var(--sage-txt);
    padding-right: 20px;
    font-size: 17px;
    font-weight: 500;
    color: var(--text-dark);
    line-height: 1.7;
  }}

  /* ─── SECTION 3: SYLLABUS ─── */
  #syllabus {{
    background: var(--sage-bg);
  }}
  .syllabus-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-top: 40px;
  }}
  .syllabus-card {{
    background: var(--white);
    border-radius: var(--radius-sm);
    padding: 24px;
    border: 1px solid rgba(107,140,110,0.15);
    transition: transform .2s, box-shadow .2s;
  }}
  .syllabus-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(44,61,45,0.08);
  }}
  .syllabus-num {{
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--sage-num);
    margin-bottom: 10px;
  }}
  .syllabus-card-title {{
    font-size: 15px;
    font-weight: 700;
    color: var(--text-dark);
    margin-bottom: 8px;
    line-height: 1.4;
  }}
  .syllabus-card-text {{
    font-size: 13.5px;
    font-weight: 300;
    color: var(--text-light);
    line-height: 1.7;
  }}
  @media(max-width:768px){{
    .syllabus-grid {{ grid-template-columns: 1fr; }}
  }}

  /* ─── SECTION 4: BONUSES ─── */
  #bonuses {{
    background: var(--cream);
    padding: 80px 40px;
  }}
  .bonuses-outer {{
    max-width: 860px;
    margin: 0 auto;
  }}
  .bonuses-box {{
    background: var(--olive);
    border-radius: var(--radius-lg);
    padding: 52px 40px 40px;
    margin-top: 32px;
  }}
  .bonuses-box-tag {{
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--gold);
    border: 1px solid var(--gold);
    padding: 5px 16px;
    border-radius: var(--radius-pill);
    margin-bottom: 16px;
    opacity: 0.9;
  }}
  .bonuses-box-title {{
    font-size: 26px;
    font-weight: 900;
    color: #fff;
    margin-bottom: 32px;
    line-height: 1.3;
  }}
  .bonuses-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }}
  .bonus-card {{
    background: var(--white);
    border-radius: 16px;
    padding: 26px 20px;
    display: flex;
    gap: 16px;
    align-items: flex-start;
  }}
  .bonus-icon {{
    width: 50px;
    height: 50px;
    min-width: 50px;
    background: var(--sage-bg);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .bonus-icon svg {{ width: 24px; height: 24px; }}
  .bonus-card-title {{
    font-size: 14px;
    font-weight: 700;
    color: var(--text-dark);
    margin-bottom: 6px;
    line-height: 1.4;
  }}
  .bonus-card-text {{
    font-size: 13px;
    font-weight: 300;
    color: var(--text-light);
    line-height: 1.6;
  }}
  .bonus-tag {{
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    color: var(--gold);
    border: 1px solid rgba(212,185,106,0.4);
    padding: 2px 10px;
    border-radius: 40px;
    margin-top: 8px;
  }}
  .bonuses-footer {{
    border-top: 1px solid rgba(255,255,255,0.1);
    margin-top: 32px;
    padding-top: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }}
  .bonuses-footer-text {{
    font-size: 13px;
    color: rgba(255,255,255,0.55);
  }}
  .bonuses-footer-value {{
    font-size: 13px;
    color: var(--gold);
    font-weight: 500;
  }}
  @media(max-width:640px){{
    .bonuses-grid {{ grid-template-columns: 1fr; }}
    .bonuses-box {{ padding: 36px 24px 28px; }}
  }}

  /* ─── SECTION 5: PRICING ─── */
  #pricing {{
    background: var(--cream);
    padding: 0 40px 80px;
  }}
  .pricing-box {{
    max-width: 560px;
    margin: 0 auto;
    background: var(--olive);
    border-radius: var(--radius-md);
    padding: 52px 40px;
    text-align: center;
  }}
  .pricing-tag {{
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--sage-num);
    margin-bottom: 16px;
  }}
  .pricing-title {{
    font-size: 26px;
    font-weight: 900;
    color: #fff;
    line-height: 1.3;
    margin-bottom: 10px;
  }}
  .pricing-sub {{
    font-size: 15px;
    font-weight: 300;
    color: rgba(255,255,255,0.65);
    margin-bottom: 32px;
    line-height: 1.6;
  }}
  .pricing-old {{
    font-size: 16px;
    color: rgba(255,255,255,0.4);
    text-decoration: line-through;
    margin-bottom: 4px;
  }}
  .pricing-price {{
    font-size: 72px;
    font-weight: 900;
    color: #fff;
    line-height: 1;
    letter-spacing: -2px;
  }}
  .pricing-currency {{
    font-size: 32px;
    vertical-align: super;
    font-weight: 700;
  }}
  .pricing-installments {{
    font-size: 14px;
    color: rgba(255,255,255,0.6);
    margin-top: 8px;
    margin-bottom: 32px;
  }}
  .pricing-note {{
    margin-top: 20px;
    font-size: 12px;
    color: rgba(255,255,255,0.4);
    line-height: 1.8;
  }}
  .pricing-features {{
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    margin-bottom: 28px;
  }}
  .pricing-feat {{
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 13px;
    color: rgba(255,255,255,0.7);
  }}
  .pricing-feat svg {{ width: 16px; height: 16px; color: var(--sage-num); }}

  /* ─── SECTION 6: ABOUT ─── */
  #about {{
    background: var(--white);
  }}
  .about-inner {{
    max-width: 1000px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1.3fr;
    gap: 60px;
    align-items: center;
  }}
  .about-img-wrap {{
    border-radius: var(--radius-lg);
    overflow: hidden;
    aspect-ratio: 3/4;
    box-shadow: 0 20px 60px rgba(44,61,45,0.12);
  }}
  .about-img-wrap img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
  }}
  .about-tag {{ margin-bottom: 16px; }}
  .about-name {{
    font-size: 36px;
    font-weight: 900;
    color: var(--text-dark);
    margin-bottom: 8px;
    line-height: 1.1;
  }}
  .about-role {{
    font-size: 15px;
    font-weight: 400;
    color: var(--sage-txt);
    margin-bottom: 24px;
  }}
  .about-p {{
    font-size: 15px;
    font-weight: 300;
    color: var(--text-mid);
    line-height: 1.9;
    margin-bottom: 16px;
  }}
  .about-stats {{
    display: flex;
    gap: 32px;
    margin-top: 32px;
    flex-wrap: wrap;
  }}
  .about-stat-num {{
    font-size: 36px;
    font-weight: 900;
    color: var(--olive);
    line-height: 1;
  }}
  .about-stat-label {{
    font-size: 13px;
    font-weight: 300;
    color: var(--text-light);
    margin-top: 4px;
  }}
  @media(max-width:768px){{
    .about-inner {{ grid-template-columns: 1fr; gap: 32px; }}
    .about-img-wrap {{ aspect-ratio: 4/3; }}
  }}

  /* ─── SECTION 7: TESTIMONIALS ─── */
  #testimonials {{
    background: var(--sage-mid);
  }}
  .testimonials-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-top: 40px;
  }}
  .testimonial-card {{
    background: var(--white);
    border-radius: var(--radius-sm);
    padding: 22px 18px;
    border: 1px solid rgba(107,140,110,0.15);
  }}
  .testimonial-placeholder {{
    width: 100%;
    aspect-ratio: 4/3;
    background: var(--sage-bg);
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
    color: var(--sage-txt);
    font-size: 12px;
    font-weight: 500;
  }}
  .testimonial-placeholder svg {{ width: 32px; height: 32px; opacity: 0.5; }}
  .testimonial-name {{
    font-size: 13px;
    font-weight: 700;
    color: var(--text-dark);
    margin-top: 14px;
  }}
  .testimonial-text {{
    font-size: 13px;
    font-weight: 300;
    color: var(--text-light);
    line-height: 1.7;
    margin-top: 6px;
  }}
  .testimonials-note {{
    text-align: center;
    margin-top: 24px;
    font-size: 13px;
    color: var(--text-light);
    font-style: italic;
  }}
  @media(max-width:768px){{
    .testimonials-grid {{ grid-template-columns: 1fr; }}
  }}

  /* ─── SECTION 8: FINAL CTA ─── */
  #final-cta {{
    background: var(--cream);
    text-align: center;
  }}
  .final-cta-inner {{
    max-width: 640px;
    margin: 0 auto;
  }}
  .final-cta-img {{
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover;
    object-position: top center;
    margin: 0 auto 32px;
    display: block;
    box-shadow: 0 12px 40px rgba(44,61,45,0.15);
    border: 4px solid var(--sage-bg);
  }}
  .final-cta-title {{
    font-size: clamp(26px, 4vw, 36px);
    font-weight: 900;
    color: var(--text-dark);
    line-height: 1.3;
    margin-bottom: 16px;
  }}
  .final-cta-p {{
    font-size: 16px;
    font-weight: 300;
    color: var(--text-light);
    line-height: 1.8;
    margin-bottom: 36px;
  }}
  .final-cta-sig {{
    margin-top: 28px;
    font-size: 15px;
    color: var(--sage-txt);
    font-weight: 400;
  }}

  /* ─── FOOTER ─── */
  footer {{
    background: var(--olive);
    color: rgba(255,255,255,0.6);
    text-align: center;
    padding: 32px 24px;
    font-size: 13px;
    line-height: 1.8;
  }}
  footer a {{
    color: rgba(255,255,255,0.5);
    text-decoration: none;
  }}
  footer a:hover {{ color: #fff; }}
  .footer-links {{
    display: flex;
    justify-content: center;
    gap: 24px;
    margin-bottom: 12px;
    flex-wrap: wrap;
  }}

  /* ─── SCROLL ANIMATIONS ─── */
  .fade-up {{
    opacity: 0;
    transform: translateY(28px);
    transition: opacity .6s ease, transform .6s ease;
  }}
  .fade-up.visible {{
    opacity: 1;
    transform: translateY(0);
  }}
</style>
</head>
<body>

<!-- ═══════════════════════════════════════════
     NAV
═══════════════════════════════════════════ -->
<nav class="nav">
  <div class="nav-logo">פשוט <span>בריא</span></div>
  <ul class="nav-links">
    <li><a href="#pain">למה זה חשוב</a></li>
    <li><a href="#syllabus">הסילבוס</a></li>
    <li><a href="#bonuses">בונוסים</a></li>
    <li><a href="#about">על סיון</a></li>
    <li><a href="#pricing" class="nav-cta">להצטרפות</a></li>
  </ul>
</nav>

<!-- ═══════════════════════════════════════════
     SECTION 1 — HERO
═══════════════════════════════════════════ -->
<section id="hero">
  <div class="hero-inner">
    <div class="hero-text fade-up">
      <div class="hero-badge">
        <span class="hero-badge-dot"></span>
        קורס דיגיטלי
        <span class="hero-badge-dot"></span>
        20 שיעורים
        <span class="hero-badge-dot"></span>
        בקצב שלכם
      </div>
      <h1 class="hero-h1">פשוט<br>בריא</h1>
      <h2 class="hero-h2">הידע שיחזיר לכם את השליטה על הגוף והבריאות</h2>
      <p class="hero-p">אחרי יותר מעשרים שנים של למידה וליווי של עשרות אלפי נשים ומשפחותיהן — זיקקתי את כל הידע על תזונה ובריאות לקורס דיגיטלי אחד: בהיר, נגיש וסופר-פרקטי. אכילה מכל אבות המזון, קרוב לטבע, ובסנכרון מלא עם הגוף.</p>
      <a href="#pricing" class="btn btn-lg">כן, אני רוצה להצטרף לקורס במחיר ההשקה</a>
      <div class="hero-trust">
        <div class="hero-trust-item">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="#6B8C6E" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          גישה מיידית
        </div>
        <div class="hero-trust-dot"></div>
        <div class="hero-trust-item">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="#6B8C6E" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          מכל מכשיר
        </div>
        <div class="hero-trust-dot"></div>
        <div class="hero-trust-item">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="#6B8C6E" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          לכל החיים
        </div>
      </div>
    </div>
    <div class="hero-img-wrap">
      <img src="{imgs['hero']}" alt="סיון אופירי בשוק הפירות" loading="eager">
      <div class="hero-img-overlay"></div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════
     SECTION 2 — PAIN POINTS
═══════════════════════════════════════════ -->
<section id="pain" class="section">
  <div class="section-inner-sm fade-up">
    <span class="tag">למה זה חשוב</span>
    <h2 class="section-title">המזון הונדס.<br>הגוף שלנו משלם את המחיר — כל יום.</h2>
    <p class="section-sub">תעשיית המזון מבצעת הנדסה גנטית באוכל והנדסת תודעה אצל הצרכנים. המדפים בסופר עמוסים בסוכר מוסתר, חומרים משמרים וחומרים שלא ראויים למאכל אדם. לאורך שנים איבדנו את מנגנון הרעב והשובע הטבעי — ואף אחד לא סיפר לנו.</p>

    <div class="pain-icon-row">
      <div class="pain-icon-item">
        <div class="pain-icon-box">
          <svg fill="none" viewBox="0 0 24 24" stroke="#3D5A3E" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        </div>
        <div>
          <div class="pain-icon-label">מנגנון הרעב והשובע מבולבל</div>
          <div class="pain-icon-sub">השתוקקות לאכילת יתר שנוצרת מחומרים ממכרים</div>
        </div>
      </div>
      <div class="pain-icon-item">
        <div class="pain-icon-box">
          <svg fill="none" viewBox="0 0 24 24" stroke="#3D5A3E" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126z"/></svg>
        </div>
        <div>
          <div class="pain-icon-label">אנרגיה לא יציבה לאורך היום</div>
          <div class="pain-icon-sub">נפילות אנרגיה, עייפות, קושי להתרכז</div>
        </div>
      </div>
      <div class="pain-icon-item">
        <div class="pain-icon-box">
          <svg fill="none" viewBox="0 0 24 24" stroke="#3D5A3E" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9 5.25h.008v.008H12v-.008z"/></svg>
        </div>
        <div>
          <div class="pain-icon-label">בלבול מידע ומיתוסים</div>
          <div class="pain-icon-sub">כל יום המלצה חדשה, כל שנה "דיאטה" חדשה</div>
        </div>
      </div>
      <div class="pain-icon-item">
        <div class="pain-icon-box">
          <svg fill="none" viewBox="0 0 24 24" stroke="#3D5A3E" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"/></svg>
        </div>
        <div>
          <div class="pain-icon-label">הסביבה הביתית לא תומכת</div>
          <div class="pain-icon-sub">מטבח, קניות, הרגלים — הכל צריך שדרוג</div>
        </div>
      </div>
    </div>

    <div class="pain-quote">
      ידע הוא כוח. וברגע שמסירים את המעובד מהגוף — הוא פשוט מפסיק לבקש אותו.
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════
     SECTION 3 — SYLLABUS
═══════════════════════════════════════════ -->
<section id="syllabus" class="section">
  <div class="section-inner fade-up">
    <div class="text-center">
      <span class="tag">הסילבוס</span>
      <h2 class="section-title">20 שיעורים קצרים. בקצב שלכם.<br>מהנייד, מהמחשב, או באוזניות בדרך לעבודה.</h2>
    </div>
    <div class="syllabus-grid">
      <div class="syllabus-card">
        <div class="syllabus-num">01</div>
        <div class="syllabus-card-title">האמת על האוכל שלנו</div>
        <div class="syllabus-card-text">מסקירה על תעשיית המזון והנדסה גנטית — ועד ניפוץ המיתוסים השולטים בעולם המודרני.</div>
      </div>
      <div class="syllabus-card">
        <div class="syllabus-num">02</div>
        <div class="syllabus-card-title">להבין את המנגנון מבפנים</div>
        <div class="syllabus-card-text">רעב, שובע, תנגודת אינסולין, מניעת סוכרת, אנרגיה יציבה ושינה טובה יותר.</div>
      </div>
      <div class="syllabus-card">
        <div class="syllabus-num">03</div>
        <div class="syllabus-card-title">שינוי הבית והמטבח</div>
        <div class="syllabus-card-text">נשנה את הסביבה, את סדר היום ונלמד לבחור נכון בכל מצב — בלי קיצוניות.</div>
      </div>
      <div class="syllabus-card">
        <div class="syllabus-num">04</div>
        <div class="syllabus-card-title">חוקי הסופרמרקט</div>
        <div class="syllabus-card-text">מדריך 10 השניות: לקרוא רכיבים, לזהות סוכר מוסתר ולנצח את הטריקים של התעשייה.</div>
      </div>
      <div class="syllabus-card">
        <div class="syllabus-num">05</div>
        <div class="syllabus-card-title">שדרוג המטבח הביתי</div>
        <div class="syllabus-card-text">מוצרים מומלצים, תחליפים ראויים, איך לבשל ולאפות נכון — ובלי להשתעבד למטבח.</div>
      </div>
      <div class="syllabus-card">
        <div class="syllabus-num">06</div>
        <div class="syllabus-card-title">חיים מחוץ לבית</div>
        <div class="syllabus-card-text">מסעדות, חופשות, טיסות — מדריך הישרדות לחיים אמיתיים, בלי לאבד את הדרך.</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════
     SECTION 4 — BONUSES
═══════════════════════════════════════════ -->
<section id="bonuses">
  <div class="bonuses-outer fade-up" style="padding: 80px 0;">
    <div class="text-center">
      <span class="tag">בונוסים בלעדיים</span>
      <h2 class="section-title">נרשמים היום ומקבלים 4 מתנות לכל המשפחה — בלי עלות נוספת</h2>
      <p class="section-sub" style="margin: 0 auto;">שווי הבונוסים לבד עולה על מחיר הקורס</p>
    </div>
    <div class="bonuses-box">
      <div class="bonuses-box-tag">מתנה לנרשמים — במחיר ההשקה בלבד</div>
      <div class="bonuses-box-title">4 בונוסים דיגיטליים מיידיים</div>
      <div class="bonuses-grid">
        <div class="bonus-card">
          <div class="bonus-icon">
            <svg fill="none" viewBox="0 0 24 24" stroke="#3D5A3E" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25"/></svg>
          </div>
          <div>
            <div class="bonus-card-title">ספר מתכונים דיגיטלי "פשוט בריא"</div>
            <div class="bonus-card-text">מתכונים פשוטים, מהירים וקלים להכנה שכל המשפחה (והילדים) יאהבו.</div>
            <span class="bonus-tag">מתנה</span>
          </div>
        </div>
        <div class="bonus-card">
          <div class="bonus-icon">
            <svg fill="none" viewBox="0 0 24 24" stroke="#3D5A3E" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 002.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 00-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75 2.25 2.25 0 00-.1-.664m-5.8 0A2.251 2.251 0 0113.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25z"/></svg>
          </div>
          <div>
            <div class="bonus-card-title">המדריך המלא לרכיבים מוסתרים</div>
            <div class="bonus-card-text">איך לזהות ולנצח צבעי מאכל, חומרים משמרים וסוכר בהסוואה.</div>
            <span class="bonus-tag">מתנה</span>
          </div>
        </div>
        <div class="bonus-card">
          <div class="bonus-icon">
            <svg fill="none" viewBox="0 0 24 24" stroke="#3D5A3E" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"/></svg>
          </div>
          <div>
            <div class="bonus-card-title">חוברת מתכונים לילדים</div>
            <div class="bonus-card-text">מתכונים מיוחדים שנוצרו בשביל הילדים שלכם — בריא, טעים ומהנה.</div>
            <span class="bonus-tag">מתנה</span>
          </div>
        </div>
        <div class="bonus-card">
          <div class="bonus-icon">
            <svg fill="none" viewBox="0 0 24 24" stroke="#3D5A3E" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 12h16.5m-16.5 3.75h16.5M3.75 19.5h16.5M5.625 4.5h12.75a1.875 1.875 0 010 3.75H5.625a1.875 1.875 0 010-3.75z"/></svg>
          </div>
          <div>
            <div class="bonus-card-title">מילון הסוכר</div>
            <div class="bonus-card-text">מדריך המילים הנרדפות לסוכר — כי לסוכר יש יותר מ-60 שמות שונים.</div>
            <span class="bonus-tag">מתנה</span>
          </div>
        </div>
      </div>
      <div class="bonuses-footer">
        <span class="bonuses-footer-text">גישה מיידית לכל הבונוסים עם ההרשמה</span>
        <span class="bonuses-footer-value">ערך מוסף: ללא עלות נוספת ✦</span>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════
     SECTION 5 — PRICING
═══════════════════════════════════════════ -->
<section id="pricing" class="section" style="padding-top: 0;">
  <div class="fade-up">
    <div class="pricing-box">
      <div class="pricing-tag">המחיר שלנו</div>
      <div class="pricing-title">השקיעו בבריאות שלכם —<br>עכשיו במחיר השקה</div>
      <div class="pricing-sub">הידע שישמש אתכם לכל החיים, נגיש תמיד, בכל זמן ומכל מכשיר.</div>
      <div class="pricing-features">
        <div class="pricing-feat">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          20 שיעורים
        </div>
        <div class="pricing-feat">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          4 בונוסים
        </div>
        <div class="pricing-feat">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          גישה לכל החיים
        </div>
        <div class="pricing-feat">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          מכל מכשיר
        </div>
      </div>
      <div class="pricing-old">במקום ₪1,299</div>
      <div class="pricing-price"><span class="pricing-currency">₪</span>490</div>
      <div class="pricing-installments">או 3 תשלומים נוחים של ₪163 בלבד</div>
      <a href="#PAYMENT_LINK" class="btn btn-lg btn-green">כן, אני רוצה גישה מיידית לקורס ולבונוסים</a>
      <div class="pricing-note">גישה לכל החיים · מתאים לנשים וגברים · מכל מכשיר ובכל זמן</div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════
     SECTION 6 — ABOUT
═══════════════════════════════════════════ -->
<section id="about" class="section">
  <div class="about-inner fade-up">
    <div class="about-img-wrap">
      <img src="{imgs['about']}" alt="סיון אופירי">
    </div>
    <div class="about-content">
      <span class="tag about-tag">אם טרם הכרנו</span>
      <div class="about-name">סיון אופירי</div>
      <div class="about-role">מאמנת תזונה | מייסדת שיטת "פשוט לרדת במשקל"</div>
      <p class="about-p">הגעתי לעולם הבריאות והוולנס אחרי 25 שנים של הפרעות אכילה קשות שנבעו מחוסר ידע. משנת 2003 אני מלווה נשים ובני משפחותיהן בתהליכי חיים.</p>
      <p class="about-p">בשנת 2009 פיתחתי את השיטה "פשוט לרדת במשקל" ומאז אני מלווה נשים ומשפחות בשינוי בתחום המשקל, הפרעות אכילה, אכילה רגשית, התמכרות לאכילה ושינוי תפיסות עולם — באמצעות 5 אספקטים: פיזיולוגיה, תזונה, קוגניציה, רגש ותודעה.</p>
      <p class="about-p">המחקר והניסיון שלי לימדו אותי ש"ראשית רפואה היא תזונה". ראיתי מה קורה כשאנשים מתחילים להבין את הגוף שלהם — ובריאות נכנסת לחייהם בקלות.</p>
      <div class="about-stats">
        <div>
          <div class="about-stat-num">20+</div>
          <div class="about-stat-label">שנות ניסיון</div>
        </div>
        <div>
          <div class="about-stat-num">עשרות<br>אלפים</div>
          <div class="about-stat-label">נשים ומשפחות</div>
        </div>
        <div>
          <div class="about-stat-num">2003</div>
          <div class="about-stat-label">שנת התחלה</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════
     SECTION 7 — TESTIMONIALS
═══════════════════════════════════════════ -->
<section id="testimonials" class="section">
  <div class="section-inner fade-up">
    <div class="text-center">
      <span class="tag">עדויות</span>
      <h2 class="section-title">ניתן לעדויות לדבר בעד עצמן</h2>
    </div>
    <div class="testimonials-grid">
      <!-- 6 placeholders — יוחלפו בצילומי מסך אמיתיים -->
      {"".join([f'''
      <div class="testimonial-card">
        <div class="testimonial-placeholder">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z"/></svg>
          <span>צילום מסך המלצה {i+1}</span>
        </div>
      </div>''' for i in range(6)])}
    </div>
    <p class="testimonials-note">* צילומי מסך אמיתיים מלקוחות יוחלפו בקרוב</p>
  </div>
</section>

<!-- ═══════════════════════════════════════════
     SECTION 8 — FINAL CTA
═══════════════════════════════════════════ -->
<section id="final-cta" class="section">
  <div class="final-cta-inner fade-up">
    <img src="{imgs['cta_end']}" alt="סיון אופירי" class="final-cta-img">
    <h2 class="final-cta-title">לא בשביל המשקל —<br>בשביל הנשמה והגוף.</h2>
    <p class="final-cta-p">תנו לעצמכם את ההזדמנות לעלות על המסלול להטיב עם הגוף והנפש. הידע שתרכשו כאן ילווה אתכם לכל החיים.</p>
    <a href="#PAYMENT_LINK" class="btn btn-lg">אני רוצה גישה מיידית לקורס פשוט בריא</a>
    <div class="final-cta-sig">מחכה לכם בקורס, סיון ♡</div>
  </div>
</section>

<!-- ═══════════════════════════════════════════
     FOOTER
═══════════════════════════════════════════ -->
<footer>
  <div class="footer-links">
    <a href="#hero">ראשי</a>
    <a href="#syllabus">הסילבוס</a>
    <a href="#about">על סיון</a>
    <a href="#pricing">הצטרפות</a>
    <a href="https://www.sivanofiri.com">האתר הראשי</a>
  </div>
  <div>© 2025 סיון אופירי | כל הזכויות שמורות</div>
  <div style="margin-top:6px; font-size:11px; opacity:.5;">sivanofiri.com</div>
</footer>

<script>
// Intersection Observer for fade-up animations
const observer = new IntersectionObserver((entries) => {{
  entries.forEach(entry => {{
    if (entry.isIntersecting) {{
      entry.target.classList.add('visible');
    }}
  }});
}}, {{ threshold: 0.12 }});

document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));
</script>

</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Done! File size: {len(html):,} chars")
