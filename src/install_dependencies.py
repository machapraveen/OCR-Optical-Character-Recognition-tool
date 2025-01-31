import subprocess
import sys

# List of required packages
packages = ["pytesseract", "openpyxl", "pillow", "opencv-python", "pandas"]

# Install each package
for package in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("All dependencies installed successfully.")
