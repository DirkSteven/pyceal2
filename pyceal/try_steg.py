from PIL import Image, ImageDraw, ImageFont


def encode_image(image_path, message):
    image = Image.open(image_path)
    binary_message = ''.join([format(ord(i), "08b") for i in message])
    if len(binary_message) > image.width * image.height:
        raise ValueError("Message is too large to encode in image.")
    encoded_image = image.copy()
    binary_message = binary_message + "0" * (image.width * image.height - len(binary_message))
    index = 0
    for x in range(image.width):
        for y in range(image.height):
            pixel = list(image.getpixel((x, y)))
            for i in range(3):
                if index < len(binary_message):
                    pixel[i] = int(format(pixel[i], "08b")[:-1] + binary_message[index], 2)
                    index += 1
            encoded_image.putpixel((x, y), tuple(pixel))
    return encoded_image

def decode_image(image_path):
    image = Image.open(image_path)
    binary_message = ""
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            for i in range(3):
                binary_message += format(pixel[i], "08b")[-1]
    message = ""
    for i in range(0, len(binary_message), 8):
        message += chr(int(binary_message[i:i+8], 2))
        if message[-5:] == "#####":
            message = message[:-5]
            break
    return message

message = "This is a secret message."
image_path = "bsu.png"
encoded_image = encode_image(image_path, message)
encoded_image.save("encoded_image.png")
decoded_message = decode_image("encoded_image.png")
print(decoded_message)