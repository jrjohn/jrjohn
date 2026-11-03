#!/usr/bin/env python3
"""Generate one SVG per architecture card so the profile README can link each card to its repo.

GitHub strips links inside SVG images and does not support <map>, so a single diagram
can never be clickable. Each card is its own <img> wrapped in <a> instead.

Usage: python3 scripts/gen-cards.py   (writes assets/cards/*.svg)
"""
from pathlib import Path

FONT = "'Inter','Segoe UI',system-ui,-apple-system,sans-serif"
MONO = "'SF Mono','JetBrains Mono','Fira Code',Menlo,Consolas,monospace"

CLIENT, EMBEDDED, CLOUD, CORE = "#0891b2", "#d97706", "#7c3aed", "#059669"
TINT = {CLIENT: "#ecfeff", EMBEDDED: "#fffbeb", CLOUD: "#f5f3ff", CORE: "#ecfdf5"}

# key, label, score, accent
CARDS = [
    ("windows", "🪟 Windows", "9.0", CLIENT),
    ("macos", "🍎 macOS", "9.4", CLIENT),
    ("desktop-rust", "🦀 Rust", "8.7", CLIENT),
    ("angular", "🅰️ Angular", "9.4", CLIENT),
    ("react", "⚛️ React", "9.2", CLIENT),
    ("vue", "💚 Vue", "10.0", CLIENT),
    ("ios", "🍎 iOS", "9.5", CLIENT),
    ("android", "🤖 Android", "9.2", CLIENT),
    ("harmonyos", "🔷 HarmonyOS", "9.2", CLIENT),
    ("stm32", "🛠️ STM32", "7.5", EMBEDDED),
    ("esp32", "📡 ESP32", "8.3", EMBEDDED),
    ("springboot", "☕ Spring Boot", "9.3", CLOUD),
    ("python", "🐍 Python", "9.2", CLOUD),
    ("go", "🐹 Go", "8.6", CLOUD),
    ("cloud-rust", "🦀 Rust", "9.0", CLOUD),
    ("nodejs", "💚 Node.js", "9.5", CLOUD),
]
PRINCIPLES = [
    ("clean-architecture", "Clean Architecture"),
    ("offline-first", "Offline-First"),
    ("mvvm", "MVVM I/O/E Pattern"),
]

W, H, PAD = 148, 58, 6  # card size as in architecture.svg; PAD leaves room for the shadow

HEAD = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{{w}}" height="{H + 2 * PAD}" viewBox="0 0 {{w}} {H + 2 * PAD}">
<defs><filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#334155" flood-opacity="0.16"/></filter></defs>
'''


def star(cx, cy, r=3.6):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return " ".join(pts)


def card(label, score, accent):
    x, y = PAD, PAD
    w = W + 2 * PAD
    return HEAD.format(w=w) + (
        f'<g filter="url(#soft)"><rect x="{x}" y="{y}" width="{W}" height="{H}" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/></g>'
        f'<rect x="{x}" y="{y}" width="4" height="{H}" rx="2" fill="{accent}"/>'
        f'<text x="{x + 16}" y="{y + 24}" font-family="{FONT}" font-size="15" font-weight="600" fill="#1e293b">{label}</text>'
        f'<rect x="{x + 16}" y="{y + 34}" width="{44 + 7 * len(score)}" height="17" rx="8.5" fill="{TINT[accent]}" stroke="{accent}" stroke-width="0.8" stroke-opacity="0.5"/>'
        f'<polygon points="{star(x + 29, y + 42.5)}" fill="{accent}"/>'
        f'<text x="{x + 38}" y="{y + 46.5}" font-family="{MONO}" font-size="11.5" font-weight="700" fill="{accent}">{score}</text>'
        "\n</svg>\n"
    )


def principle(label):
    pw = 214
    x, y = PAD, PAD
    return HEAD.format(w=pw + 2 * PAD) + (
        f'<g filter="url(#soft)"><rect x="{x}" y="{y}" width="{pw}" height="{H}" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/></g>'
        f'<rect x="{x}" y="{y}" width="4" height="{H}" rx="2" fill="{CORE}"/>'
        f'<text x="{x + pw / 2}" y="{y + 34}" text-anchor="middle" font-family="{FONT}" font-size="14.5" font-weight="600" fill="#1e293b">{label}</text>'
        "\n</svg>\n"
    )


def main():
    out = Path(__file__).resolve().parent.parent / "assets" / "cards"
    out.mkdir(parents=True, exist_ok=True)
    for key, label, score, accent in CARDS:
        (out / f"{key}.svg").write_text(card(label, score, accent), encoding="utf-8")
    for key, label in PRINCIPLES:
        (out / f"{key}.svg").write_text(principle(label), encoding="utf-8")
    print(f"wrote {len(CARDS) + len(PRINCIPLES)} cards to {out}")


if __name__ == "__main__":
    main()
