# De Haas Styling: website voor Bibi

Een statische one-pager (`index.html`) in de look en feel van Instagram **@dehaasstyling**: crème, taupe (#685B4D), espresso, warm hout, groen en serif-kapitalen ("DE HAAS | STYLING"). Glazen kaartjes zoals in haar posts.

**Bekijken:** dubbelklik `index.html`, of draai `python3 -m http.server 8765` in deze map en open http://127.0.0.1:8765.
**Online zetten:** de hele map uploaden. Er is geen build-stap nodig (bijvoorbeeld GitHub Pages, Netlify of TransIP-hosting op dehaasstyling.nl).

## Bron (gescraped op 17-11-2026, openbaar profiel, zonder inloggen)
- `bron/instagram/posts.json`: alle 12 zichtbare posts en reels met de volledige captions
- `bron/instagram/profiel.json`: bio, highlights en links
- `bron/mijnsalon-behandelingen.txt`: behandelingen uit https://dehaasstyling.mijnsalon.nl
- `bron/reels/`: de reels in 1080p (DASH, zonder audio-mux), `bron/instagram/`: foto's

`python3 prepare_assets.py` maakt `assets/` (webp/jpg en stille mp4-loops) opnieuw aan uit `bron/`.

## Wat er op de site staat (alles uit haar eigen posts en bio)
- Hero met een video van Bibi die een behandeling geeft, plus "−50% op je eerste behandeling" (uit haar post)
- Over Bibi: haar eigen introtekst (post van 17-08), afgesloten met "Stralende groet, Bibi"
- 6 behandelingen uit mijnsalon. **Alleen de prijs van Organic Treat (€69,00) is bekend**, uit een post. De rest verwijst naar de agenda.
- Extra's: deep tissue massage, multi-zuurpeeling (AHA/PHA), natural nail BIAB
- Het Organic Treat-ritueel: reiniging, peeling/masker, schoudermassage, lichttherapie, naverzorging
- Skincare: Maria Åkerberg en INIKA Organic, gratis huidadvies, SPF-tip
- De salon (video-rondleiding), Instagram-grid en contact (mail, bellen, WhatsApp, Instagram)
- SEO: meta-tags en schema.org BeautySalon. Het boeken loopt via mijnsalon.

## Nog navragen bij Bibi vóór livegang
1. **Prijzen** van Organic Treat VIP, Clear Skin Treat, Pedicure Basis, BIAB en deep tissue
2. **Adres.** Nu staat er alleen "Empel · Den Bosch" (locatietag en bio).
3. **KvK-nummer** en eventueel een privacyverklaring voor de footer
4. Of Superlash en Natural Tanning (Instagram-highlights) ook als behandeling op de site moeten. De highlights zijn zonder inloggen niet te lezen.
5. E-mail: de bio noemt info@dehaasstyling.nl en één oude post noemt Info.dehaasstyling@gmail.com. De site gebruikt het .nl-adres.
6. Domein dehaasstyling.nl bestaat al (DNS → 37.97.254.27), maar geeft nog geen https-site

## Wijzigingslog
- 17-11-2026: map nieuw aangemaakt door Claude. Er zijn geen bestaande bestanden gewijzigd. Getest in Chrome op desktop (1440 px) en mobiel (390 px): geen console-fouten en geen horizontale scroll.
- 17-11-2026: gepubliceerd in github.com/julian08100/dehaasstyling (GitHub Pages: https://julian08100.github.io/dehaasstyling/). De oude site van april 2026 is bewaard als tag `v1-april-2026` (herstel: `git checkout v1-april-2026 -- .`).
