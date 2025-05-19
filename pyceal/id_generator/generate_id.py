from PIL import Image
from pyceal.models import User
from flask_login import current_user
import base64

def current_user():
    print(current_user)
# Assume that `data` is a dictionary containing the image data
# in base64 format, with a key `id_img` representing the image data.

# Decode the base64-encoded image data
# image_data = base64.b64decode()

# Create a PIL Image object from the image data
# image = Image.open(io.BytesIO(image_data))

# Manipulate the image as needed
# image = image.rotate(90)

# Save the manipulated image to a file
# image.save('output.jpg')