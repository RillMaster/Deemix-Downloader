# 🎵 Deemix Downloader

A simple Python script to download music from Deezer via [deemix](https://deemix.app/) — tracks, albums, artists and playlists in seconds.

---

## ✅ Requirements

- Python 3.8+
- [deemix](https://deemix.app/) installed
- A Deezer account (free or Premium)
- Your Deezer **ARL token** (see below)

---

## 🔑 Getting your Deezer ARL

The ARL is a token that authenticates you with Deezer. It is required for deemix to work.

**On Chrome / Firefox / Edge:**

1. Go to [https://www.deezer.com](https://www.deezer.com) and log in
2. Open DevTools → `F12`
3. Go to the **Application** tab (Chrome) or **Storage** tab (Firefox)
4. Click **Cookies** → `https://www.deezer.com`
5. Find the cookie named **`arl`** and copy its value

Then paste it into deemix when prompted on first launch:

```bash
deemix --arl YOUR_ARL_TOKEN -b mp3_320 -p ./music "https://www.deezer.com/album/302127"
```

> 💡 The ARL is saved automatically after the first use. You won't need to enter it again.  
> ⚠️ Your ARL expires periodically. If downloads stop working, grab a fresh one.

---

## 💻 Installation

### 🐧 Linux

```bash
# Install Python if needed
sudo apt install python3 python3-pip   # Debian / Ubuntu
sudo pacman -S python python-pip       # Arch

# Install deemix
pip install deemix
```

### 🪟 Windows

1. Download and install [Python](https://www.python.org/downloads/) — check **"Add Python to PATH"** during install
2. Open **Command Prompt** or **PowerShell**:

```powershell
pip install deemix
```

3. Find the deemix path:

```powershell
where deemix
# Example: C:\Users\youruser\AppData\Local\Programs\Python\Python311\Scripts\deemix.exe
```

### 🍎 macOS

```bash
# Install Homebrew if needed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python

# Install deemix
pip3 install deemix
```

---

## ⚙️ Configuration

Open `download_music.py` and edit the two variables at the top:

```python
OUTPUT_DIR = "/home/youruser/music"              # Folder where files will be saved
DEEMIX     = "/home/youruser/.local/bin/deemix"  # Path to the deemix executable
```

| OS | Default deemix path |
|----|---------------------|
| 🐧 Linux | `/home/youruser/.local/bin/deemix` |
| 🪟 Windows | `C:\Users\youruser\AppData\Local\Programs\Python\Python311\Scripts\deemix.exe` |
| 🍎 macOS | `/usr/local/bin/deemix` |

To find it automatically:

```bash
# Linux / macOS
which deemix

# Windows (PowerShell)
where deemix
```

---

## 🚀 Usage

```bash
# Linux / macOS
python3 download_music.py

# Windows
python download_music.py
```

Then paste a Deezer link and press Enter:

```
🔗 Deezer link: https://www.deezer.com/album/302127
```

### Available commands

| Key | Action |
|-----|--------|
| `h` | Show help |
| `c` | Change audio quality |
| `q` | Quit |

---

## 🔗 Supported link types

| Type | Example |
|------|---------|
| 🎵 Track | `https://www.deezer.com/track/3135556` |
| 💿 Album | `https://www.deezer.com/album/302127` |
| 🎤 Artist | `https://www.deezer.com/artist/92` |
| 📋 Playlist | `https://www.deezer.com/playlist/1963962142` |

---

## 🎚️ Available qualities

| Quality | Requirement |
|---------|-------------|
| MP3 128 kbps | Free account |
| MP3 320 kbps | Premium required |
| FLAC lossless | Premium required |

---

## 📁 Downloaded files structure

```
music/
└── Linkin Park/
    └── Meteora/
        ├── 01 - Foreword.mp3
        ├── 02 - Don't Stay.mp3
        └── ...
```

---

## ⚠️ Disclaimer

This project is for **personal use only**.  
Please respect Deezer's terms of service and the copyright laws of your country.

---

## 📄 License

MIT — free to use and modify.
