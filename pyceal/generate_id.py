from PIL import Image, ImageDraw, ImageFont, ImageOps
from rembg import remove
import numpy as np
import cv2
from pyceal.models import User
from flask_login import current_user
import base64
import io


class Generate_ID():
    KEY = "NEU-BSU"
    message = "**Leading Innovations, Transforming Lives**"
    validation_message = "**Leading Innovations, Transforming Lives**"
    error_message = "Access Denied Due to Invalid Key OR The Image Was Not Encoded Using Our System."

    def __init__(self, current_user):
        self.user = current_user

    data = {
        'full_name': 'fullname',
        'program': 'program',
        'sr_code': 'sr_code',
        'contact_person': 'parent',
        'contact_number': 'contacts',
        'address': 'address',
        'year_validity': 'year'
    }

    def prt_name(self):
        print(self.user.full_name)

    def set_user_data(self):
        self.data['full_name'] = self.user.full_name
        self.data['program'] = self.user.program
        self.data['sr_code'] = self.user.sr_code
        self.data['contact_person'] = self.user.contact_person
        self.data['contact_number'] = self.user.contact_number
        self.data['address'] = self.user.address
        self.data['year_validity'] = self.user.year_validity

    def create_id_pic(self):
        id_img = self.user.id_img_data
        id_pic = Image.open(io.BytesIO(id_img)).resize((398, 398))
        return id_pic

    def create_sign_pic(self, sign_img_data):
        sign_pic = Image.open(io.BytesIO(sign_img_data))

        sign_pic = sign_pic.resize((300, 250)).convert("RGBA")
        sign_pic = remove(sign_pic)
        sign_pic.convert('RGB')

        return sign_pic

    def encode_image(self, pil_img, message, key):
        image = pil_img

        if image.mode != 'RGB':
            image = image.convert('RGB')

        message += ' ' + key + ' '

        binary_message = ''.join(format(ord(char), '08b') for char in message)

        width, height = image.size

        print(width, height)

        if len(binary_message) > width * height:
            raise ValueError("Message too long to fit in image")

        pixels = image.load()
        index = 0

        for x in range(width):
            for y in range(height):
                binary_pixel = format(pixels[x, y][0], '08b')

                if index < len(binary_message):
                    new_binary_pixel = binary_pixel[:-1] + binary_message[index]

                    pixels[x, y] = (
                        int(new_binary_pixel, 2),
                        pixels[x, y][1],
                        pixels[x, y][2]
                    )

                    index += 1

        return image

    def decode_image(self, binary_data, key):
        image = Image.open(io.BytesIO(binary_data))

        width, height = image.size

        binary_message = ''
        pixels = image.load()

        for x in range(width):
            for y in range(height):
                binary_pixel = format(pixels[x, y][0], '08b')
                binary_message += binary_pixel[-1]

        message = ''

        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i+8]
            message += chr(int(byte, 2))

        message_words = message.split()

        if key in message_words:
            index = message_words.index(key)
            message = ' '.join(message_words[:index])
            return message

        return self.error_message

    def get_text_size(self, drawObj, text, font):
        bbox = drawObj.textbbox((0, 0), text, font=font)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        return (width, height)

    def make_id(self):
        id_template = Image.open(
            'pyceal/static/images/user_images/trial_temp.jpg'
        )

        id_pic = self.create_id_pic()

        sign_pic = Image.open(
            io.BytesIO(self.user.sign_img_data)
        ).convert("RGBA")

        drawObj = ImageDraw.Draw(id_template)

        # Paste ID picture
        id_pic_x = ((id_template.width // 2) - id_pic.width) // 2
        id_pic_y = 293

        id_template.paste(id_pic, (id_pic_x, id_pic_y))

        # Write SR Code
        text = self.data['sr_code']
        font_size = 35

        font = ImageFont.truetype("times.ttf", font_size)

        text_size = self.get_text_size(drawObj, text, font)

        text_x = ((id_template.width / 2) - text_size[0]) / 2
        text_y = ((id_template.height - text_size[1]) / 2) - 25

        drawObj.text(
            (text_x, text_y),
            text,
            font=font,
            fill=(0, 0, 0)
        )

        # Write Full Name
        font = ImageFont.truetype("arialbd.ttf", font_size)

        text = self.data['full_name'].upper()

        text_size = self.get_text_size(drawObj, text, font)

        text_x = ((id_template.width / 2) - text_size[0]) / 2
        text_y += 120

        drawObj.text(
            (text_x, text_y),
            text,
            font=font,
            fill=(255, 255, 255)
        )

        # Write Program
        font = ImageFont.truetype("arial.ttf", font_size)

        text = self.data['program']

        text_size = self.get_text_size(drawObj, text, font)

        text_x = ((id_template.width / 2) - text_size[0]) / 2
        text_y += 60

        drawObj.text(
            (text_x, text_y),
            text,
            font=font,
            fill=(255, 255, 255)
        )

        # Write Parent Name
        font = ImageFont.truetype("arialbd.ttf", font_size)

        text = self.data['contact_person'].upper()

        text_size = self.get_text_size(drawObj, text, font)

        text_x = (id_template.width / 2) + 50
        text_y -= 465

        drawObj.text(
            (text_x, text_y),
            text,
            font=font,
            fill=(0, 0, 0)
        )

        # Write Contact Number
        text = self.data['contact_number'].upper()

        text_size = self.get_text_size(drawObj, text, font)

        text_x = (id_template.width / 2) + 50
        text_y += 110

        drawObj.text(
            (text_x, text_y),
            text,
            font=font,
            fill=(0, 0, 0)
        )

        # Write Address
        text = self.data['address'].upper()

        text_size = self.get_text_size(drawObj, text, font)

        text_x = (id_template.width / 2) + 50
        text_y += 55

        drawObj.text(
            (text_x, text_y),
            text,
            font=font,
            fill=(0, 0, 0)
        )

        # Write Year Validity
        font = ImageFont.truetype("arial.ttf", size=28)

        text = self.data['year_validity'].upper()

        text_size = self.get_text_size(drawObj, text, font)

        text_x = (id_template.width / 2) + 55
        text_y += 185

        drawObj.text(
            (text_x, text_y),
            text,
            font=font,
            fill=(0, 0, 0)
        )

        # Paste Signature
        sign_pic_x = (id_template.width // 2) + sign_pic.width
        sign_pic_y = (id_template.height - sign_pic.height) - 350

        id_template.paste(
            sign_pic,
            (sign_pic_x, sign_pic_y),
            sign_pic
        )

        # Encode Image
        id_template = self.encode_image(
            id_template,
            self.message,
            self.KEY
        )

        # Save Output
        id_template.save(
            "pyceal/static/images/user_images/output_pic.png"
        )