import pytesseract
from PIL import Image
import os

# Optional for macOS - helps Python find the Tesseract tool
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

# Folder containing your images
image_folder = "images"

# List all image files (jpg, jpeg, png)
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Loop through each image and extract text
image = Image.open("images/test.jpg")
text = pytesseract.image_to_string(image)

print("Extracted Text:\n")
print(text)

