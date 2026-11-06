from pathlib import Path
import webbrowser

page = Path(__file__).parent / "Shravani_Portfolio" / "index.html"
if not page.exists():
    raise FileNotFoundError("index.html not found inside Shravani_Portfolio folder.")
webbrowser.open(page.resolve().as_uri())
print("Portfolio opened in your browser.")
