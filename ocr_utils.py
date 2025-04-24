import os
import pytesseract
from PIL import Image

TESSERACT_CMD = os.getenv('TESSERACT_CMD', 'tesseract')
SUPPORTED_FORMATS = ['png', 'jpg', 'jpeg', 'tiff']

def perform_ocr(image_path: str, lang: std='eng', config: str='--oem 3 --psm 6') -> str:
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    ext = image_path.split('.')[-1].lower()
    from config import SUPPORTED_FORMATS
    if ext not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported format: {ext}")
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang=lang, config=config)

def ocr_to_json(image_path: str, lang = str='eng') -> dict:
    img = Image.open(image_path)
    data = pytesseract.image_to_data(img, lang=lang, output_type=pytesseract.Output.DICT)
    words =[]
    for i, text in enumerate(data['text']):
        if text.strip():
            words.append({
                'word': text,
                'left': data['left'][i],
                'top': data['top'][i],
                'width': data['width'][i],
                'height': data['height'][i]
            })
    return {'words': words}
    

