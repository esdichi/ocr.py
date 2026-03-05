import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

archivo = "imagen.jpg" 

imagen = Image.open(archivo)
texto = pytesseract.image_to_string(imagen, lang="eng")

print("--- Texto Extraído ---")
print(texto)

