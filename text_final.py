from PIL import Image
import pytesseract

im = Image.open("Epo Automation Content.jpeg")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)