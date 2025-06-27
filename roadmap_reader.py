from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"put tesseract path here"

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"Error reading image: {e}"
