import requests
from bs4 import BeautifulSoup
from PIL import Image
import io
import pytesseract
from langdetect import detect
from google.cloud import translate_v2 as translate

# Set up Google Translate API client
#translate_client = translate.Client()


# Define function to extract text from webpage
def extract_text_from_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    return text

"""

# Define function to extract text from image
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


# Example usage
url = input("Write or paste your manga link: ")
text = extract_text_from_webpage(url)

# If the text contains images, extract text from the images
image_paths = find_image_paths_in_text(text)

for image_path in image_paths:
    image_text = extract_text_from_image(image_path)
    text += " " + image_text

"""

# Example usage

url = "https://www.manhuatai.com/"

text = extract_text_from_webpage(url)

# Detect language of text
language = detect(text)


print(language)

