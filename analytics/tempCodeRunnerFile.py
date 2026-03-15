import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

import pytesseract
from PIL import Image

img = Image.open("static/images/bg2.png")

text = pytesseract.image_to_string(img)

print(text)
