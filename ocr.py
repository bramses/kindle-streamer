from PIL import Image

import pytesseract

def ocr_image(image_path: str) -> str:
    return pytesseract.image_to_string(Image.open(image_path))
