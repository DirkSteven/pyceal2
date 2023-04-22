from PIL import Image, ImageDraw, ImageFont
from pyceal.models import User
from flask_login import current_user
import base64
import io


class Generate_ID():
   
    def __init__(self, current_user):
        self.user = current_user
        self.prt_current_user()

    data = {
        'full_name': 'fullname',
        'program': 'program',
        'sr_code': 'sr_code',
        'contact_person':'parent',
        'contact_number':'contacts',
        'address':'address',
        'year_validity':'year'
    }

    def prt_name(self):
        print(self.user.full_name)

    def prt_current_user(self):
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
    
    def create_sign_pic(self):
        sign_img = self.user.sign_img_data
        sign_pic = Image.open(io.BytesIO(sign_img)).resize((398, 350))
        return sign_pic
    
    def make_id(self):
        id_template = Image.open('trial_temp.jpg')
        id_pic = self.create_id_pic()
        sign_pic = self.create_sign_pic()
        drawObj = ImageDraw.Draw(id_template)

        id_pic_x = ((id_template.width//2) - id_pic.width)// 2
        id_pic_y = 293
        id_template.paste(id_pic, ((id_pic_x), (id_pic_y)))

        #write the sr-code
        text = self.data['sr_code']
        font_size = 35
        font = ImageFont.truetype("times.ttf", font_size)
        text_size = drawObj.textsize(text, font=font)
        text_x = ((id_template.width/2) - text_size[0]) / 2 
        text_y = ((id_template.height - text_size[1]) / 2 ) - 25
        drawObj.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

        #write the name
        font = ImageFont.truetype("arialbd.ttf", font_size)
        text = self.data['full_name'].upper()
        text_size = drawObj.textsize(text, font=font)
        text_x = ((id_template.width/2) - text_size[0]) / 2 
        text_y += 120
        drawObj.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

        #write the program
        font = ImageFont.truetype("arial.ttf", font_size)
        text = self.data['program']
        text_size = drawObj.textsize(text, font=font)
        text_x = ((id_template.width/2) - text_size[0]) / 2 
        text_y += 60
        drawObj.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

        #Write the parents's name
        font = ImageFont.truetype("arialbd.ttf", font_size)
        text = self.data['contact_person'].upper()
        text_size = drawObj.textsize(text, font=font)
        text_x = ((id_template.width/2)) + 50
        text_y -= 465
        drawObj.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

        #Write contact details
        font = ImageFont.truetype("arialbd.ttf", font_size)
        text = self.data['contact_number'].upper()
        text_size = drawObj.textsize(text, font=font)
        text_x = ((id_template.width/2)) + 50
        text_y += 110
        drawObj.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

        #Write addrress details
        font = ImageFont.truetype("arialbd.ttf", font_size)
        text = self.data['address'].upper()
        text_size = drawObj.textsize(text, font=font)
        text_x = ((id_template.width/2)) + 50
        text_y += 55
        drawObj.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

        #Write year
        font = ImageFont.truetype("arial.ttf", size=28)
        text = self.data['year_validity'].upper()
        text_size = drawObj.textsize(text, font=font)
        text_x = ((id_template.width/2)) + 55

        text_y += 185
        drawObj.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

        #paste sign image
        sign_pic_x = (id_template.width//2) + sign_pic.width//2
        sign_pic_y = (id_template.height-sign_pic.height) - 300

        id_template.paste(sign_pic, (sign_pic_x, sign_pic_y), sign_pic)

        id_template.save("pyceal/static/images/user_images/output_pic.png")



    
# from PIL import Image, ImageDraw, ImageFont

# #Set image to appropriate sizes for ID



# #Set font
# font_style = "TNR.ttf"
# font_bold = "TNR_BOLD.ttf"
# font_size = 35
# font = ImageFont.truetype(font_style, font_size)

# #Set image to appropriate sizes for Sign.
# sign_pic = (Image.open("sign_test.png").resize((398, 398))).convert("RGBA")

# # Split the image into its individual color channels
# r, g, b, a = sign_pic.split()

# # Create a new image by merging the non-white channels
# new_image = Image.merge("RGB", (r, g, b))

# # Create a mask by setting the alpha channel of the new image to a threshold value
# mask = new_image.convert("L").point(lambda x: 0 if x == 255 else 255, mode='1')

# # Set the alpha channel of the new image to the mask
# sign_pic.putalpha(mask)

# print(id_template.width/2)
# name = input ("Enter your Name:")
# sr_code = input ("Enter your SR-Code:")
# program = input ("Enter your Course Program:")
# parent = input ("Enter your Parent/Guardian's Name:")
# contacts = input ("Enter your Parent/Guardian's Contact Information:")
# addrres = input ("Enter your Addrress:")
# year = input ("Enter the year of validity:")
# data = {
#     'name': name,
#     'sr_code': sr_code,
#     'program': program,
#     'parent':parent,
#     'contacts':contacts,
#     'addrres':addrres,
#     'year':year
# ,
# }



# #write the sr-code
# text = data['sr_code']
# text_size = drawObj.textsize(text, font=font)
# text_x = ((id_template.width/2) - text_size[0]) / 2 
# text_y = ((id_template.height - text_size[1]) / 2 ) - 25
# drawObj.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

# #write the name
# font = ImageFont.truetype("arialbd.ttf", font_size)
# text = data['name'].upper()
# text_size = drawObj.textsize(text, font=font)
# text_x = ((id_template.width/2) - text_size[0]) / 2 
# text_y += 120
# drawObj.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

# #write the program
# font = ImageFont.truetype("arial.ttf", font_size)
# text = data['program']
# text_size = drawObj.textsize(text, font=font)
# text_x = ((id_template.width/2) - text_size[0]) / 2 
# text_y += 60
# drawObj.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

# #Write the parents's name
# font = ImageFont.truetype("arialbd.ttf", font_size)
# text = data['parent'].upper()
# text_size = drawObj.textsize(text, font=font)
# text_x = ((id_template.width/2)) + 50
# text_y -= 465
# drawObj.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

# #Write contact details

# font = ImageFont.truetype("arialbd.ttf", font_size)
# text = data['contacts'].upper()
# text_size = drawObj.textsize(text, font=font)
# text_x = ((id_template.width/2)) + 50
# text_y += 110
# drawObj.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

# #Write addrress details

# font = ImageFont.truetype("arialbd.ttf", font_size)
# text = data['addrres'].upper()
# text_size = drawObj.textsize(text, font=font)
# text_x = ((id_template.width/2)) + 50
# text_y += 55
# drawObj.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

# #Write year

# font = ImageFont.truetype("arial.ttf", size=22)
# text = data['year'].upper()
# text_size = drawObj.textsize(text, font=font)
# text_x = ((id_template.width/2)) + 55

# text_y += 185
# drawObj.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

# #paste sign image
# sign_pic_x = (id_template.width//2) + sign_pic.width//2
# sign_pic_y = (id_template.height-sign_pic.height) - 300

# id_template.paste(sign_pic, (sign_pic_x, sign_pic_y), sign_pic)



# id_template.save('output.png')


