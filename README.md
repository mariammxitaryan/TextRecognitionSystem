# OCR CLI Utility

A **simple**, **lightweight**, command-line OCR (Optical Character Recognition) tool that converts image files into text. Ideal for batch processing and easy to integrate into any workflow—no GUI required!

---

## 🎯 Features

- 🔍 **Multi-file & directory support**: Process individual images or entire folders of PNG, JPG, TIFF, BMP.
- 🌐 **Language selection**: Choose your Tesseract `-l` language code (e.g., `eng`, `spa`, `fra`).
- ⚙️ **Tesseract config options**: Control `--psm` (Page Segmentation Mode) and `--oem` (OCR Engine Mode).
- 📂 **Custom output directory**: Store all `.txt` results in a dedicated folder.
- 🛠️ **Robust error handling**: Skips invalid paths, logs failures, continues processing.
- 📄 **Logging**: Informative `[INFO]` and `[ERROR]` messages in your terminal.

---

## 📦 Installation

### 1. Clone this repository

### 2. Set up a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
# .\venv\Scripts\activate  # Windows PowerShell
```

### 3. Install dependencies
```bash
pip install Pillow pytesseract
```

### 4. Install Tesseract OCR Engine
- **macOS** (Homebrew): `brew install tesseract`
- **Ubuntu/Debian**: `sudo apt-get install tesseract-ocr`
- **Windows**: Download from [Tesseract Releases](https://github.com/tesseract-ocr/tesseract/releases) and add to `PATH`.

---

## 🚀 Usage

```bash
python ocr_utils.py [paths...] [options]
```

### Basic examples

- **Single image**
  ```bash
  python ocr_utils.py image.png
  ```

- **Multiple images**
  ```bash
  python ocr_utils.py img1.jpg img2.png
  ```

- **Entire directory**
  ```bash
  python ocr_utils.py folder_of_images/
  ```

### Options

| Flag                | Description                                      | Default    |
| ------------------- | ------------------------------------------------ | ---------- |
| `-l`, `--lang`      | Tesseract language code                          | `eng`      |
| `-o`, `--outdir`    | Output directory for `.txt` files                | `ocr_output` |
| `--psm <0-13>`      | Page Segmentation Mode                           | `6`        |
| `--oem <0-3>`       | OCR Engine Mode                                  | `3`        |

**Example:**
```bash
python ocr_utils.py scans/ -l spa -o texts --psm 3 --oem 1
```

---

## 📂 Project Structure

```text
ocr-cli-utility/
├── ocr_utils.py       # Main OCR script with CLI interface
├── venv/              # (Optional) Python virtual environment
└── README.md          # Project documentation (this file)
```

---

## 🤝 Contributing

1. Fork this repo
2. Create a branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add awesome feature"`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---
