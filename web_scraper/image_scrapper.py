import requests
from PIL import Image
from io import BytesIO

"""

def download_image(url):
    # Send a request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the image using Pillow
        img = Image.open(BytesIO(response.content))

        # Save the image to a file
        img.save('scraped_image.jpg')

        # Print a success message
        print('Image downloaded successfully.')

    # If the request was not successful, print an error message
    else:
        print(f'Error {response.status_code}: Could not download image.')


"""
def download_image(url):
    # Send a request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Decode the image data
        img_data = response.content.decode()

        # Open the image using Pillow
        img = Image.open(BytesIO(img_data))

        # Save the image to a file
        img.save('scraped_image.jpg')

        # Print a success message
        print('Image downloaded successfully.')

    # If the request was not successful, print an error message
    else:
        print(f'Error {response.status_code}: Could not download image.')



# Example usage:
url = input("Write or paste your link: ")
download_image(url)







