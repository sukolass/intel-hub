# Personal Intel & Apologetics Hub

Ein maßgeschneidertes persönliches Informations- und Recherche-Dashboard mit fundierten Dossiers, Zeitleisten zur Marktreife für Bürger, Video-Einbettungen und automatischer Aktualisierung.

## 🚀 Schnellstart

1. **Website öffnen:**
   * Öffne einfach die Datei `index.html` per Doppelklick in deinem Browser oder über den Link:
     `file:///C:/Users/boern/.gemini/antigravity/scratch/personal-intel-hub/index.html`

2. **Als aktiven Workspace festlegen:**
   * Es wird empfohlen, diesen Ordner (`C:\Users\boern\.gemini\antigravity\scratch\personal-intel-hub`) als aktiven Arbeitsbereich (Workspace) in Antigravity festzulegen, damit alle künftigen Recherchen und automatischen Updates direkt hier einfließen.

---

## 📂 Struktur des Projekts

* **`index.html`**: Das interaktive Dashboard mit Filterung, Echtzeit-Suche, Video-Embeds, Detailansichten und Formular für eigene Themenvorschläge.
* **`articles.js`**: Die entkoppelte Datenbank aller Artikel, Dossiers und Videos.
* **`update_hub.py`**: Python-Skript, das neue Artikel und Recherchen automatisiert an `articles.js` anhängt und Duplikate verhindert.

---

## 🔄 Wie automatische Updates funktionieren

1. **Hintergrund-Automation (Scheduled Automation):**
   * Ein geplanter Hintergrund-Agent (z. B. täglich oder wöchentlich) sucht nach den neuesten Videos und Forschungsberichten.
   * Gefundene Neuigkeiten werden strukturiert aufbereitet und automatisch an `articles.js` angehängt.
2. **Eigene Themen vorschlagen:**
   * Über den Button *„Neues Thema vorschlagen“* in der Seitenleiste kannst du jederzeit neue Kategorien oder Fragestellungen eingeben.
   * Diese werden sofort angezeigt und in die Suchliste künftiger Recherche-Läufe übernommen.
