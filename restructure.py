with open('/home/ubuntu/sivan-landing/index.html', 'r') as f:
    html = f.read()

# The old block to replace (sections 4 + 5 together)
start_marker = '<!-- ═══════════════════════════════════════════\n     SECTION 4 — BONUSES'
end_marker = '<!-- ═══════════════════════════════════════════\n     SECTION 6 — ABOUT'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

# Extract the inner bonuses box HTML (cards only)
bonuses_box_start = html.find('<div class="bonuses-box">', start_idx)
bonuses_box_end = html.find('</div>\n  </div>\n</section>', bonuses_box_start) + len('</div>')
bonuses_box_html = html[bonuses_box_start:bonuses_box_end]

# Extract the pricing box HTML
pricing_box_start = html.find('<div class="pricing-box">', bonuses_box_end)
pricing_box_end = html.find('</div>\n  </div>\n</section>', pricing_box_start) + len('</div>')
pricing_box_html = html[pricing_box_start:pricing_box_end]

# Update bonuses box title to include gift icon
bonuses_box_html = bonuses_box_html.replace(
    '<div class="bonuses-box-title">4 בונוסים דיגיטליים מיידיים</div>',
    '<div class="bonuses-box-title"><span class="bonuses-box-title-icon">🎁</span> 4 בונוסים דיגיטליים מיידיים</div>'
)

# Build the new combined section
new_section = '''<!-- ═══════════════════════════════════════════
     SECTION 4+5 — BONUSES + PRICING SIDE BY SIDE
═══════════════════════════════════════════ -->
<section id="bonuses">
  <div class="bonuses-outer fade-up" style="padding: 80px 0;">
    <div class="text-center">
      <span class="tag">בונוסים בלעדיים</span>
      <h2 class="section-title">נרשמים היום ומקבלים 4 מתנות לכל המשפחה — בלי עלות נוספת</h2>
      <p class="section-sub" style="margin: 0 auto;">שווי הבונוסים לבד עולה על מחיר הקורס</p>
    </div>
    <div class="bonuses-pricing-row">
      <!-- RIGHT: Bonuses box (olive dark) -->
      ''' + bonuses_box_html + '''
      <!-- LEFT: Pricing box (light green) -->
      ''' + pricing_box_html + '''
    </div>
  </div>
</section>

'''

# Replace the old sections 4+5 with the new combined section
old_block = html[start_idx:end_idx]
html = html.replace(old_block, new_section)

with open('/home/ubuntu/sivan-landing/index.html', 'w') as f:
    f.write(html)

print("Done! Sections 4+5 restructured into side-by-side layout.")
