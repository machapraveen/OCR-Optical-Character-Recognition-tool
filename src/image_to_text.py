import pytesseract
from PIL import Image
import cv2

# Set Tesseract OCR path (only for Windows users)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this if needed

# Load image
image_path = "image.png"  # Ensure the image is in the same directory
image = cv2.imread(image_path)

# Convert image to grayscale for better OCR
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Save processed image temporarily
processed_image_path = "processed.png"
cv2.imwrite(processed_image_path, gray)

# Extract text
extracted_text = pytesseract.image_to_string(Image.open(processed_image_path))

# Save extracted text to a file
with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(extracted_text)

print("Text extraction completed. Check extracted_text.txt")
