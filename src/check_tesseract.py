import pytesseract

# Set the correct path manually
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

try:
    print("Tesseract version:", pytesseract.get_tesseract_version())
    print("Tesseract is installed and configured correctly.")
except Exception as e:
    print("Tesseract is not installed or not configured properly:", e)
