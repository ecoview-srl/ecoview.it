# ecoview.it

Sito di Ecoview srl – ambiente, pianificazione, foreste, GIS e formazione.

**Stato:** bozza su `ecoview-srl.github.io/ecoview.it`, non indicizzata dai motori di ricerca (`robots.txt` e meta `noindex`).

## Struttura
- `index.html` – pagine e dati del sito (attività, lavori, pubblicazioni, persone)
- `img/` – foto, loghi, copertine, ritratti, immagini del portfolio WebGIS
- `404.html` – porta i vecchi indirizzi del sito WordPress (es. `/chi-siamo/`, `/progetti-consulenza-ambientale/gis/`) alla sezione corrispondente del nuovo sito
- `tools/golive.py` – prepara il sito per la pubblicazione su ecoview.it

## Passaggio su ecoview.it

### Prima
1. Inserire la sede legale nella pagina Privacy (oggi «[da indicare]») e rileggere il testo.
2. Fare un backup completo del sito WordPress su Aruba (file e database).

### Il giorno del passaggio
1. Nella cartella del repository: `python3 tools/golive.py` (toglie `noindex` e le note di bozza, crea `CNAME`, `robots.txt`, `sitemap.xml`), poi commit e push.
2. GitHub → repository → Settings → Pages → Custom domain: `ecoview.it`.
3. Pannello DNS di Aruba, dominio `ecoview.it`:
   - record **A** per `ecoview.it` (@): `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (al posto di quelli che puntano all'hosting WordPress);
   - record **CNAME** per `www`: `ecoview-srl.github.io`;
   - **non toccare** i record **MX** (posta) né quelli di `gis.ecoview.it` e degli altri sottodomini.
4. Dopo la propagazione (da qualche ora a un giorno): GitHub → Settings → Pages → spuntare **Enforce HTTPS**.

### Dopo
- Verificare il sito su ecoview.it e www.ecoview.it e qualche vecchio indirizzo (es. `ecoview.it/chi-siamo/`).
- Google Search Console: aggiungere il dominio e inviare `sitemap.xml`.
- Redirect da NaturaGIS e migrazione dei WebGIS ospitati.
- Disattivare l'hosting WordPress su Aruba (tenendo il dominio e la posta).
