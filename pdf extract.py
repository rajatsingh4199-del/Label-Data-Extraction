from PIL import Image
import pytesseract

# Open the image using Pillow (PIL)
image = Image.open('your_image.png')

# Perform OCR on the image
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print(extracted_text)
