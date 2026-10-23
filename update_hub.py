"""
update_hub.py - Automatischer Artikel- & Wissens-Updater für den Personal Intel Hub.
Erlaubt das programmatische Anhängen neuer Dossiers, Videos und Zusammenfassungen an articles.js.
"""

import json
import re
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ARTICLES_JS = BASE_DIR / "articles.js"


def load_hub_data():
    """Liest die window.INTEL_HUB_DATA Struktur aus articles.js."""
    if not ARTICLES_JS.exists():
        raise FileNotFoundError(f"{ARTICLES_JS} existiert nicht.")

    content = ARTICLES_JS.read_text(encoding="utf-8")
    match = re.search(r"window\.INTEL_HUB_DATA\s*=\s*(\{.*?\});\s*$", content, re.DOTALL)
    if not match:
        raise ValueError("Konnte window.INTEL_HUB_DATA in articles.js nicht parsen.")

    json_str = match.group(1)
    # Behebt gängige JS-Literale falls nötig, oder verwendet Standard-JSON
    return json.loads(json_str)


def save_hub_data(data):
    """Speichert die Struktur formatiert zurück in articles.js und pusht zu GitHub."""
    import subprocess
    data["lastUpdated"] = datetime.now().isoformat()
    js_content = (
        "// Automatisch gepflegte Wissens- und Artikeldatenbank für den Personal Intel Hub\n"
        "// Diese Datei wird bei jeder Aktualisierung automatisch um neue Funde, Zusammenfassungen und Videos erweitert.\n\n"
        f"window.INTEL_HUB_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    )
    ARTICLES_JS.write_text(js_content, encoding="utf-8")
    print(f"Erfolgreich aktualisiert: {len(data.get('articles', []))} Artikel in articles.js gespeichert.")

    # Automatischer Git-Push zu GitHub Pages
    try:
        subprocess.run(["git", "add", "articles.js"], cwd=BASE_DIR, check=True)
        res = subprocess.run(["git", "commit", "-m", f"Auto-Update: Hub Stand {datetime.now().strftime('%d.%m.%Y %H:%M')}"], cwd=BASE_DIR, capture_output=True, text=True)
        if "nothing to commit" not in res.stdout:
            subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR, check=True)
            print("Erfolgreich zu GitHub Pages gepusht!")
    except Exception as e:
        print(f"Git Sync Info: {e}")


def add_article(article_dict):
    """Fügt einen neuen Artikel hinzu, sofern die ID nicht bereits existiert."""
    data = load_hub_data()
    existing_ids = {a.get("id") for a in data.get("articles", [])}

    if article_dict.get("id") in existing_ids:
        print(f"Artikel mit ID '{article_dict.get('id')}' existiert bereits. Übersprungen.")
        return False

    # Vorne anfügen (neueste zuerst)
    data.setdefault("articles", []).insert(0, article_dict)
    save_hub_data(data)
    return True


if __name__ == "__main__":
    print("Personal Intel Hub Updater ist bereit.")
    try:
        current_data = load_hub_data()
        print(f"Aktueller Bestand: {len(current_data.get('articles', []))} Artikel.")
        print(f"Zuletzt aktualisiert: {current_data.get('lastUpdated')}")
    except Exception as e:
        print(f"Hinweis: {e}")
