#!/usr/bin/env python3
"""
Replace the testimonials section in index.html with a real horizontal slider
containing all testimonials extracted from the old site.
"""

import re

# All real testimonials from the old site
testimonials = [
    {
        "name": "Inbal Peri Rahamim",
        "text": "מסכימה עם כל מילה שלך. את הסדנא הראשונה עשיתי פרונטלי עם סיון לפני 6.5 שנים. מאז עשיתי באון ליין, אך לאחרונה הרגשתי שצריכה לדייק יותר ולחזור הביתה. סיון המלאכית בדמות אדם, נותנת מעצמה 200% באהבה ואכפתיות ונתינה אין סופית מהלב. הסדנא של סיון זו מתנה שלא מפסיקה לתת."
    },
    {
        "name": "",
        "text": "הי גם אני הייתי בגבול הסוכרת — עכשיו מאוזן לחלוטין, הרבה יותר ערנית ואנרגתית"
    },
    {
        "name": "",
        "text": "הסוכר ירד. נפיחות בבטן ירדה. גזים ירדו וכאבי בטן נעלמו. תודה לך"
    },
    {
        "name": "",
        "text": "אין יותר מיגרנות, אין יותר צרבות. בדיקות הדם שלי מעולם לא היו כך טובות — תמיד היו לי חוסרים בברזל וב-B12. הפלא ופלא — אין בעיות ספיגה ועכשיו הרמות של הויטמינים תקינות לחלוטין ללא שום תוספי תזונה. הכולסטרול התאזן. איזה כיף!!!"
    },
    {
        "name": "",
        "text": "הרופאה התקשרה — הטריגליצרידים נמוכים (56), אבל הגלוקוז בדם היה 101 — אזהרה לטרום סוכרת. עכשיו 86. הHba1c היה בגבול הנורמלי העליון 5.8 — הכל חזר לנורמה 🙏🙏"
    },
    {
        "name": "",
        "text": "סבלתי מכבד שומני מעל עשור — עכשיו סופית לאחר אולטראסאונד הכבד השומני לא קיים יותר! הסוכרת התאזנה וירדתי במינוני האינסולין משמעותית. אני מלאת אנרגיה וחיוניות ומרגישה ממש טוב"
    },
    {
        "name": "",
        "text": "אני התחלתי את הסדנא עם גלוקוז 104 וכולסטרול 258. כעבור חודש וחצי עשיתי בדיקות... גלוקוז 89 וכולסטרול 147. ונכון להיום פחות 13 ק\"ג."
    },
    {
        "name": "",
        "text": "שחלות פוליציסטיות וקושי להיכנס להריון בעקבות כך... מדהים שלאחר חודשים בתהליך רופא הפוריות שלי אמר שאין לי יותר שחלות פוליציסטיות וכבר בטיפול הראשון נקלטתי ועכשיו יש לי בובה מדהימה!!! ❤️"
    },
    {
        "name": "",
        "text": "אתמול קיבלתי תוצאות של בדיקות דם. לפני כשנה וחצי היה לי כולסטרול גבוה עד כדי שהרופאה שקלה כדורים להורדה, סוכר גבוה וחוסר ב-B12. הכל ירד והתאזן. לא זוכרת מתי הפעם האחרונה היו לי כאלו תוצאות."
    },
    {
        "name": "",
        "text": "בלי כדורים! אחרי 3 חודשים בלבד בשיטה! המוגלובין מסוכרר ירד מ-6.3 ל-5.7. בתוך הנורמה!!! תודה ענקית למלכות סיון! לא להתייאש — התוצאות מגיעות הרבה יותר מהר ממה שנראה לכן כרגע! 😊"
    },
    {
        "name": "",
        "text": "עם סכרת נעורים, הורדתי חצי מכמות אינסולין שאני מזריקה. מדד ה-A1C ירד ל-6.5 שזה מדהים. יש אנרגיה ואני לא עייפה 😊"
    },
    {
        "name": "",
        "text": "המוגלובין מסוכרר ירד מ-5.6 ל-5.4. טריגליצרידים ירדו מ-314 ל-136. חודשים בשיטה."
    },
    {
        "name": "",
        "text": "רמות הסוכר שלי ירדו ב-70%! מ-66 יחידות אינסולין לפני הסדנא — כיום 20 יחידות. ומקווה שהפריון בדרך 😊"
    },
    {
        "name": "",
        "text": "חולת סכרת כבר 6 שנים. אחרי ניתוח בריאטרי הסוכר נעלם ואז חזר עם העלייה במשקל. לפני הסדנא סוכר 121 — היום סוכר 80. אין כדורים, אין מעקב, לפי הרופא 'נירפאתי'"
    },
    {
        "name": "",
        "text": "לפני שנה לא יכולתי כמעט ללכת. כאבי ברכיים עד דמעות, בדיקות דם על סף סוכרת, בלוטת התריס 1400 מג לשבוע. ועכשיו ירידה של 47 ק\"ג, צעירה ב-20 שנה, בלוטת תריס ירידה ל-900 מג, קלילה ומקפצת במדרגות. סיון את מצילת חיים."
    },
    {
        "name": "",
        "text": "סבלתי מלחץ דם גבוה, סוכרת על הגבול ומבלוטת התריס. היום 11 חודשים מתחילת הסדנא — לא לוקחת כדורים ללחץ דם. הסוכר מעולה ובלוטת התריס מאוזנת. המשקל ירד כ-30 קילו ומאושרת על הדרך שעשיתי. תודה סיון"
    },
    {
        "name": "",
        "text": "באתי עם סיפור של סוכר גבוה בצום. החלטתי לתת צ'אנס אחרון לפני תחילת טיפול תרופתי. הסוכר ירד בצום מ-140 ל-80!! ירדתי גם במשקל. אבל יותר חשוב שאני בריאה"
    },
    {
        "name": "",
        "text": "יותר מ-6 שנים בתכנית... עשיתי אולטרסאונד — הכל תקין. והכבד לא שומני. ואין לי אסתמה יותר, ורופאי מחק לי את התרופות מהתיק הרפואי.."
    },
    {
        "name": "",
        "text": "ירד לי הסוכר. מגרנות נעלמו. מחזור שבוע מלא במקום חמישה ימים. כל הבדיקות תקינות. הבולמוסים נעלמו ובעיקר שקט בראש ושחרור נפשי מהדיאטות הנוראיות. תודה לאל שהנחה אותי לסיון בזמן 💗"
    },
    {
        "name": "",
        "text": "הסוכר שהיה לי גבולי ירד נהדר. הפסקתי כדורים ללחץ דם. והעיקר — שחרור רגשי והאוכל כבר לא מנהל אותי. 20 ק\"ג פחות כבר שנה וחצי וקל, הכי קל. אין מלחמה על שמירת המשקל, יש רק שמחה וקלילות גופנית תענוג 🤗🤗"
    },
]

# Build testimonial cards HTML
def build_card(t):
    name_html = f'<div class="tcard-name">{t["name"]}</div>' if t["name"] else ''
    return f'''      <div class="tcard">
        <div class="tcard-quote">&ldquo;</div>
        <p class="tcard-text">{t["text"]}</p>
        {name_html}
        <div class="tcard-checkmarks">✓✓</div>
      </div>'''

cards_html = "\n".join(build_card(t) for t in testimonials)

# New CSS for the slider
new_css = """  /* ─── SECTION 7: TESTIMONIALS SLIDER ─── */
  #testimonials {
    background: var(--sage-mid);
    overflow: hidden;
  }
  .tslider-wrapper {
    position: relative;
    margin-top: 40px;
  }
  .tslider-track {
    display: flex;
    gap: 20px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    padding: 8px 4px 20px;
    cursor: grab;
  }
  .tslider-track::-webkit-scrollbar { display: none; }
  .tslider-track.dragging { cursor: grabbing; user-select: none; }
  .tcard {
    flex: 0 0 calc(33.333% - 14px);
    min-width: 280px;
    background: var(--white);
    border-radius: var(--radius-sm);
    padding: 28px 24px 22px;
    border: 1px solid rgba(107,140,110,0.15);
    scroll-snap-align: start;
    display: flex;
    flex-direction: column;
    gap: 10px;
    box-shadow: 0 2px 12px rgba(44,61,45,0.06);
    transition: box-shadow 0.2s;
  }
  .tcard:hover { box-shadow: 0 6px 24px rgba(44,61,45,0.12); }
  .tcard-quote {
    font-size: 52px;
    line-height: 1;
    color: var(--sage-txt);
    opacity: 0.4;
    font-family: Georgia, serif;
    margin-bottom: -8px;
  }
  .tcard-text {
    font-size: 14px;
    font-weight: 400;
    color: var(--text-mid);
    line-height: 1.75;
    flex: 1;
  }
  .tcard-name {
    font-size: 13px;
    font-weight: 700;
    color: var(--olive);
    margin-top: 6px;
  }
  .tcard-checkmarks {
    font-size: 13px;
    color: var(--sage-txt);
    font-weight: 600;
    margin-top: 4px;
  }
  /* Navigation arrows */
  .tslider-nav {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 24px;
  }
  .tslider-btn {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    border: 2px solid var(--olive);
    background: transparent;
    color: var(--olive);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    transition: all 0.2s;
    line-height: 1;
  }
  .tslider-btn:hover {
    background: var(--olive);
    color: var(--white);
  }
  .tslider-btn:disabled {
    opacity: 0.3;
    cursor: default;
  }
  .tslider-count {
    font-size: 13px;
    color: var(--text-light);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .tslider-dots {
    display: flex;
    gap: 6px;
    align-items: center;
  }
  .tslider-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--sage-num);
    transition: all 0.2s;
    cursor: pointer;
  }
  .tslider-dot.active {
    background: var(--olive);
    width: 20px;
    border-radius: 4px;
  }
  @media(max-width:900px){
    .tcard { flex: 0 0 calc(50% - 10px); }
  }
  @media(max-width:600px){
    .tcard { flex: 0 0 88%; }
  }"""

# New HTML section
new_section_html = f"""<section id="testimonials" class="section">
  <div class="section-inner fade-up">
    <div class="text-center">
      <span class="tag">עדויות</span>
      <h2 class="section-title">מה אומרים עלינו</h2>
      <p class="section-sub">למעלה מ-20,000 בוגרים כבר שינו את חייהם עם פשוט בריא</p>
    </div>
    <div class="tslider-wrapper">
      <div class="tslider-track" id="tslider">
{cards_html}
      </div>
    </div>
    <div class="tslider-nav">
      <button class="tslider-btn" id="tPrev" onclick="tSlide(-1)" aria-label="הקודם">&#8592;</button>
      <div class="tslider-dots" id="tDots"></div>
      <button class="tslider-btn" id="tNext" onclick="tSlide(1)" aria-label="הבא">&#8594;</button>
    </div>
  </div>
</section>"""

# JavaScript for slider
slider_js = """
  // ─── TESTIMONIALS SLIDER ───
  (function() {
    const track = document.getElementById('tslider');
    const dotsContainer = document.getElementById('tDots');
    if (!track) return;

    // Drag to scroll
    let isDown = false, startX, scrollLeft;
    track.addEventListener('mousedown', e => {
      isDown = true;
      track.classList.add('dragging');
      startX = e.pageX - track.offsetLeft;
      scrollLeft = track.scrollLeft;
    });
    track.addEventListener('mouseleave', () => { isDown = false; track.classList.remove('dragging'); });
    track.addEventListener('mouseup', () => { isDown = false; track.classList.remove('dragging'); });
    track.addEventListener('mousemove', e => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - track.offsetLeft;
      const walk = (x - startX) * 1.5;
      track.scrollLeft = scrollLeft - walk;
    });

    // Dots
    const cards = track.querySelectorAll('.tcard');
    const visibleCount = () => {
      const w = track.offsetWidth;
      if (w < 600) return 1;
      if (w < 900) return 2;
      return 3;
    };
    const totalGroups = () => Math.ceil(cards.length / visibleCount());

    function buildDots() {
      dotsContainer.innerHTML = '';
      const n = totalGroups();
      for (let i = 0; i < n; i++) {
        const d = document.createElement('span');
        d.className = 'tslider-dot' + (i === 0 ? ' active' : '');
        d.addEventListener('click', () => goToGroup(i));
        dotsContainer.appendChild(d);
      }
    }

    function currentGroup() {
      const cardW = cards[0] ? cards[0].offsetWidth + 20 : 300;
      const vc = visibleCount();
      return Math.round(track.scrollLeft / (cardW * vc));
    }

    function goToGroup(g) {
      const cardW = cards[0] ? cards[0].offsetWidth + 20 : 300;
      const vc = visibleCount();
      track.scrollTo({ left: g * cardW * vc, behavior: 'smooth' });
    }

    function updateDots() {
      const g = currentGroup();
      dotsContainer.querySelectorAll('.tslider-dot').forEach((d, i) => {
        d.classList.toggle('active', i === g);
      });
    }

    track.addEventListener('scroll', updateDots);
    window.addEventListener('resize', buildDots);
    buildDots();

    window.tSlide = function(dir) {
      const g = currentGroup();
      const next = Math.max(0, Math.min(totalGroups() - 1, g + dir));
      goToGroup(next);
    };
  })();
"""

# Read the current HTML
with open('/home/ubuntu/sivan-landing/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the old testimonials CSS block
old_css_pattern = r'/\* ─── SECTION 7: TESTIMONIALS ─── \*/.*?(?=/\* ─── SECTION 8:)'
html = re.sub(old_css_pattern, new_css + '\n\n  ', html, flags=re.DOTALL)

# 2. Replace the old testimonials section HTML
old_section_pattern = r'<!-- ═+\s*SECTION 7 — TESTIMONIALS\s*═+ -->\s*<section id="testimonials".*?</section>'
html = re.sub(old_section_pattern, new_section_html, html, flags=re.DOTALL)

# 3. Insert the slider JS before the closing </script> tag (find the last one before </body>)
# Find the closing </script> before </body>
close_script = html.rfind('</script>')
if close_script != -1:
    html = html[:close_script] + slider_js + '\n' + html[close_script:]

# Write back
with open('/home/ubuntu/sivan-landing/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done! Testimonials slider updated successfully.")
