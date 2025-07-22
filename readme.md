
# 🖼️ PixMorph: Image to JPG Converter

PixMorph is a lightweight, user-friendly desktop application that allows you to **convert any image file into JPG format** using a simple GUI with drag-and-drop support. Built with Python, Tkinter, and the `wand` library, it supports multiple formats including HEIC, PNG, BMP, TIFF, and more.

---

## ✨ Features

- 🎨 Supports multiple image formats: `.heic`, `.png`, `.bmp`, `.tiff`, `.gif`, `.webp`, `.jpeg`, etc.
- 🖱️ Drag-and-drop or select files manually
- 📂 Convert multiple images at once
- 📊 Real-time progress bar
- 🗃️ Choose custom output folder
- 💻 Cross-platform (tested on macOS; can be adapted to Windows/Linux)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pixmorph-image-converter.git
cd pixmorph-image-converter
```

### 2. Set Up a Python Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

> **Note:** You must have [ImageMagick](https://imagemagick.org/script/download.php) installed and accessible in your system path.

On macOS (via Homebrew):

```bash
brew install imagemagick
```

If already installed but issues persist:

```bash
brew reinstall imagemagick
```

### 3. Run the App

```bash
python gui/main_gui.py
```

---

## 📦 Directory Structure

```
pixmorph-image-converter/
├── gui/
│   └── main_gui.py        # Main GUI application
├── converter/
│   ├── core.py            # Core conversion logic
│   └── utils.py           # Format checking utilities
├── assets/
│   └── logo.png           # App logo
├── requirements.txt       # Python dependencies
└── README.md
```

---

## 🛠 Dependencies

- `tkinter`
- `tkinterdnd2`
- `wand` (ImageMagick bindings)
- `Pillow`

Install via:

```bash
pip install -r requirements.txt
```

---

## 📷 Screenshot

![PixMorph GUI](assets/screenshot.png)

---

## 📃 License

MIT License © 2025 [Your Name]

---

## 🙌 Contributions

Pull requests, suggestions, and bug reports are welcome!
