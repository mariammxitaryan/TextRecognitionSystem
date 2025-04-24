import os
import sys
import argparse
import glob
import logging
from PIL import Image, UnidentifiedImageError
import pytesseract

# ===============================================
#    Simple CLI OCR Utility - ocr_utils.py
#    This script converts images to text files
# ===============================================

# -----------------------------------------------
# setup_logger()
#   Configure the logging format and level
#   - INFO and above will be shown
#   - Format: [LEVEL] message
# -----------------------------------------------
def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(message)s'
    )

# -----------------------------------------------
# parse_args()
#   Parse command-line arguments:
#   - paths: image files or directories
#   - lang: OCR language code (default: eng)
#   - outdir: output directory for .txt files
#   - psm: Tesseract page segmentation mode
#   - oem: Tesseract OCR engine mode
# -----------------------------------------------
def parse_args():
    parser = argparse.ArgumentParser(
        description="Simple CLI OCR: convert images to text files."
    )
    parser.add_argument(
        'paths', nargs='+',
        help="Image file(s) or directories to process."
    )
    parser.add_argument(
        '-l', '--lang', default='eng',
        help="Tesseract language code (default: eng)."
    )
    parser.add_argument(
        '-o', '--outdir', default='ocr_output',
        help="Directory to save .txt outputs (default: ./ocr_output)."
    )
    parser.add_argument(
        '--psm', type=int, choices=range(0,14), default=6,
        help="Tesseract page segmentation mode (0–13, default: 6)."
    )
    parser.add_argument(
        '--oem', type=int, choices=range(0,4), default=3,
        help="Tesseract OCR engine mode (0–3, default: 3)."
    )
    return parser.parse_args()

# -----------------------------------------------
# collect_images(paths)
#   Given a list of file or directory paths,
#   gather all supported image files:
#   - Searches directories for *.png, *.jpg, etc.
#   - Warns if a path is invalid
#   - Returns a sorted, unique list of files
# -----------------------------------------------
def collect_images(paths):
    exts = ('*.png','*.jpg','*.jpeg','*.tiff','*.bmp')
    files = []
    for p in paths:
        if os.path.isdir(p):
            for ext in exts:
                files.extend(glob.glob(os.path.join(p, ext)))
        elif os.path.isfile(p):
            files.append(p)
        else:
            logging.warning(f"Path not found, skipping: {p}")
    return sorted(set(files))

# -----------------------------------------------
# ocr_image(img_path, lang, oem, psm)
#   Perform OCR on a single image:
#   - Attempts to open the image
#   - Configures Tesseract OEM & PSM modes
#   - Returns extracted text, or None on failure
# -----------------------------------------------
def ocr_image(img_path, lang, oem, psm):
    try:
        img = Image.open(img_path)
    except (FileNotFoundError, UnidentifiedImageError) as e:
        logging.error(f"Cannot open image {img_path}: {e}")
        return None

    config = f"--oem {oem} --psm {psm}"
    try:
        text = pytesseract.image_to_string(img, lang=lang, config=config)
        return text
    except pytesseract.TesseractError as e:
        logging.error(f"OCR failed for {img_path}: {e}")
        return None

# -----------------------------------------------
# main()
#   Entry point of the script:
#   - Sets up logging
#   - Parses arguments
#   - Creates output directory
#   - Collects images
#   - Processes each image and writes out text files
# -----------------------------------------------
def main():
    setup_logger()
    args = parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    images = collect_images(args.paths)

    if not images:
        logging.error("No images found to process.")
        sys.exit(1)

    logging.info(f"Found {len(images)} image(s). Starting OCR...")

    for img_path in images:
        logging.info(f"Processing: {img_path}")
        text = ocr_image(img_path, args.lang, args.oem, args.psm)
        if text is None:
            continue

        base = os.path.splitext(os.path.basename(img_path))[0]
        out_path = os.path.join(args.outdir, f"{base}.txt")
        try:
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(text)
            logging.info(f"Saved: {out_path}")
        except IOError as e:
            logging.error(f"Failed to write {out_path}: {e}")

    logging.info("OCR batch complete.")

# -----------------------------------------------
# If run directly, invoke main()
# -----------------------------------------------
if __name__ == '__main__':
    main()
