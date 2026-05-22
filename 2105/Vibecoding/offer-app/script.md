# LinkedIn Posts Scraper

Browser-Console-Script zum Exportieren aller Posts eines LinkedIn-Profils als CSV.

## Anleitung

1. Öffne `linkedin.com/in/nick-saraev/recent-activity/all/`
2. Drücke `F12` → Tab **Console**
3. Kopiere das Script komplett und füge es ein
4. Drücke `Enter`
5. Das Script scrollt automatisch durch alle Posts (~2 Min) und lädt dann eine `.csv`-Datei herunter

Die CSV öffnest du in Excel mit: **Daten → Aus Text/CSV importieren** (damit Umlaute korrekt sind).

> **Hinweis:** LinkedIn kann den Scraping-Vorgang erkennen und den Account temporär einschränken. Verwende dies nur für eigene oder erlaubte Profile.

---

## Script

```javascript
// LinkedIn Posts Scraper v2 - In Browser Console ausführen
// Seite: linkedin.com/in/[username]/recent-activity/all/

(async function scrapeLinkedInPosts() {
  const posts = [];
  let lastHeight = 0;
  let noChangeCount = 0;

  const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));

  function extractPosts() {
    // Breiter Selektor: alle Container mit data-urn die "activity" enthalten
    const containers = document.querySelectorAll('[data-urn*="activity:"]');

    containers.forEach(el => {
      const urn = el.getAttribute('data-urn') || '';
      const postId = urn.match(/activity:(\d+)/)?.[1] || '';
      const url = postId
        ? `https://www.linkedin.com/feed/update/urn:li:activity:${postId}/`
        : '';

      // Text: alle span-Elemente mit dir="ltr" (LinkedIn-Standard für Post-Text)
      const textSpans = el.querySelectorAll('span[dir="ltr"]');
      let text = '';
      textSpans.forEach(span => {
        const t = span.innerText.trim();
        if (t.length > text.length) text = t; // längsten Text nehmen
      });

      // Datum: aria-hidden spans in der Actor-Zeile
      const allSpans = el.querySelectorAll('span[aria-hidden="true"]');
      let date = '';
      allSpans.forEach(s => {
        const t = s.innerText.trim();
        if (/^\d+[smhdw]$|^\d+ (minute|hour|day|week|month)/.test(t) || /\d+[dwmy]/.test(t)) {
          date = t;
        }
      });

      // Likes: Zahl vor "reactions" oder in reaction-count
      const likeEl = el.querySelector(
        '[aria-label*="reaction"], .social-details-social-counts__reactions-count, ' +
        'button[aria-label*="like"] span, span.social-details-social-counts__reactions-count'
      );
      let likes = likeEl ? likeEl.innerText.replace(/\D/g, '') : '';
      if (!likes) {
        // Fallback: suche nach einer Zahl neben einem Emoji-Icon
        const countEls = el.querySelectorAll('.social-details-social-counts__count-value, li.social-details-social-counts__count-value');
        if (countEls.length > 0) likes = countEls[0].innerText.trim();
      }

      // Kommentare
      const commentEls = el.querySelectorAll('button[aria-label*="comment"], li');
      let comments = '';
      commentEls.forEach(b => {
        const label = b.getAttribute('aria-label') || b.innerText || '';
        const match = label.match(/(\d+)\s*(comment|Kommentar)/i);
        if (match) comments = match[1];
      });

      if (text && !posts.find(p => p.url === url && url !== '')) {
        posts.push({ date, text, likes: likes || '0', comments: comments || '0', url });
      }
    });

    console.log(`📄 Posts gefunden: ${posts.length}`);
  }

  console.log("🔄 Starte Scraping...");

  for (let i = 0; i < 80; i++) {
    extractPosts();
    window.scrollTo(0, document.body.scrollHeight);
    await wait(2500);

    const newHeight = document.body.scrollHeight;
    if (newHeight === lastHeight) {
      noChangeCount++;
      if (noChangeCount >= 4) {
        console.log("✅ Ende erreicht.");
        break;
      }
    } else {
      noChangeCount = 0;
    }
    lastHeight = newHeight;
  }

  extractPosts();
  console.log(`✅ Fertig. ${posts.length} Posts exportiert.`);

  // CSV Export
  const esc = (s) => `"${String(s ?? '').replace(/"/g, '""').replace(/\n/g, ' ')}"`;
  const header = ['Datum', 'Text', 'Likes', 'Kommentare', 'URL'];
  const rows = posts.map(p => [esc(p.date), esc(p.text), esc(p.likes), esc(p.comments), esc(p.url)].join(','));
  const csv = '﻿' + [header.join(','), ...rows].join('\n');

  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'linkedin_posts.csv';
  a.click();
  console.log("💾 CSV wird heruntergeladen!");
})();
```

## Gespeicherte Felder

| Spalte | Beschreibung |
|--------|-------------|
| Datum | Zeitangabe des Posts (z.B. "2d", "1w") |
| Text | Vollständiger Post-Text |
| Likes | Anzahl Reactions/Likes |
| Kommentare | Anzahl Kommentare |
| URL | Direktlink zum Post |
