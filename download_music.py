import subprocess
import re

OUTPUT_DIR = "/home/rillmaster/music"
DEEMIX     = "/home/rillmaster/.local/bin/deemix"

# ── Supported link types ──────────────────────────────────────────────────────
URL_TYPES = {
    "track":    ("🎵", "Track"),
    "album":    ("💿", "Album"),
    "artist":   ("🎤", "Artist"),
    "playlist": ("📋", "Playlist"),
}

def detect_type(url: str) -> tuple[str, str]:
    """Returns (emoji, label) based on the Deezer URL type."""
    for key, (emoji, label) in URL_TYPES.items():
        if f"/{key}/" in url or f"/{key}?" in url:
            return emoji, label
    return "🔗", "Content"

def is_valid_deezer_url(url: str) -> bool:
    return bool(re.search(r"(deezer\.com|link\.deezer\.com)", url))

def download(url: str, quality: str = "mp3_320"):
    emoji, label = detect_type(url)
    print(f"\n{emoji}  {label} detected")
    print(f"⬇️  Downloading : {url}")
    print(f"🎚️  Quality : {quality}\n")

    result = subprocess.run(
        [DEEMIX, "-b", quality, "-p", OUTPUT_DIR, url],
        capture_output=False,
    )

    if result.returncode == 0:
        print(f"\n✅ {label} downloaded successfully!")
    else:
        print(f"\n❌ Error while downloading {label.lower()}.")

def choose_quality() -> str:
    qualities = {
        "1": ("mp3_128", "MP3  128 kbps"),
        "2": ("mp3_320", "MP3  320 kbps  [default]"),
        "3": ("flac",    "FLAC (lossless)"),
    }
    print("\n🎚️  Choose quality:")
    for k, (_, label) in qualities.items():
        print(f"   {k}. {label}")
    choice = input("   Choice [2]: ").strip() or "2"
    codec, _ = qualities.get(choice, qualities["2"])
    return codec

def print_help():
    print("""
╔══════════════════════════════════════════════╗
║           Available commands                 ║
╠══════════════════════════════════════════════╣
║  h  →  Show this help                        ║
║  c  →  Change audio quality                  ║
║  q  →  Quit the program                      ║
╠══════════════════════════════════════════════╣
║           Supported Deezer links             ║
╠══════════════════════════════════════════════╣
║  🎵 Track    → deezer.com/track/XXXXXXX      ║
║  💿 Album    → deezer.com/album/XXXXXXX      ║
║  🎤 Artist   → deezer.com/artist/XXXXXXX     ║
║  📋 Playlist → deezer.com/playlist/XXXXXXX   ║
╚══════════════════════════════════════════════╝
""")

def main():
    print("=" * 48)
    print("      Deemix Downloader  by RillMaster")
    print("=" * 48)
    print(f"📁 Output folder: {OUTPUT_DIR}")
    print("   (type 'h' for help, 'q' to quit)\n")

    quality = "mp3_320"  # default quality

    while True:
        url = input("🔗 Deezer link: ").strip()

        if url.lower() == "q":
            print("\nGoodbye! 👋")
            break

        if url.lower() == "h":
            print_help()
            continue

        if url.lower() == "c":
            quality = choose_quality()
            print(f"✅ Quality set to: {quality}\n")
            continue

        if not url:
            continue

        if not is_valid_deezer_url(url):
            print("❌ Invalid link — please use a deezer.com link")
            print("   (type 'h' to see accepted formats)\n")
            continue

        download(url, quality)

if __name__ == "__main__":
    main()
