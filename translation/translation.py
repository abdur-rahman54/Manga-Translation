
from flask import Flask, request, render_template
from google.cloud import vision
from google.cloud import translate_v2 as translate

# Configure Google Cloud APIs
vision_client = vision.ImageAnnotatorClient()
translate_client = translate.Client()


# Get manga image URL from form
manga_url = input("Write the manga link: ")
manga_url = request.form['manga_url']
    
# Detect language of manga image
response = vision_client.annotate_image({
    'image': {'source': {'image_uri': manga_url}},
    'features': [{'type': vision.enums.Feature.Type.LANGUAGE_DETECTION}]
    })
detected_language = response.languages[0].language_code
    
# Translate manga content to English
translation = translate_client.translate(
    request.form['manga_text'],
    source_language=detected_language,
    target_language='en')
    
translated_text = translation['translatedText']
   
print(translated_text)
#return render_template('translated.html', translated_text=translated_text)
