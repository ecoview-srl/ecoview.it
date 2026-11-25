"""Da lanciare il giorno del passaggio su ecoview.it, dalla cartella del repository:
    python3 tools/golive.py
Toglie i blocchi per i motori di ricerca e le note "Indirizzo mantenuto", scrive CNAME,
robots.txt e sitemap.xml. Poi: commit, push, e cambio dei record DNS su Aruba (vedi README)."""
import re, datetime
s = open('index.html', encoding='utf-8').read()
s = re.sub(r'\s*<meta name="robots"[^>]*>', '', s)
s = s.replace('const url=p=>`<div class="url">Indirizzo mantenuto: <code>ecoview.it/${p}</code></div>`;', 'const url=p=>``;')
s = s.replace('<p class="note" style="margin:14px 0 22px">Bozza da verificare prima della pubblicazione (sede legale e testo finale).</p>', '')
open('index.html', 'w', encoding='utf-8').write(s)
open('CNAME', 'w').write('ecoview.it\n')
open('robots.txt', 'w').write('User-agent: *\nAllow: /\n\nSitemap: https://ecoview.it/sitemap.xml\n')
d = datetime.date.today().isoformat()
open('sitemap.xml', 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://ecoview.it/</loc><lastmod>{d}</lastmod></url>\n</urlset>\n')
left = [x for x in ('noindex', 'Indirizzo mantenuto', '[da indicare]') if x in s]
print('Fatto.' if not left else f'Attenzione, nel sito resta ancora: {left}')
