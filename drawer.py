from PIL import Image, ImageDraw, ImageFont
import os
file_path = 'base_file.png'
image = Image.open(file_path)
rgb = Image.new('RGB', image.size, (255, 255, 255))  # white background
rgb.paste(image, mask=image.split()[3])
draw = ImageDraw.Draw(rgb)
(x, y) = (170, 820)
color = 'rgb(0, 151, 230)'
name = 'Muhammad Saad Hassan'
font = ImageFont.truetype('arial.ttf', size=140)
draw.text((x, y), name, fill=color, font=font)

(x, y) = (1000, 1280)
color = 'rgb(45, 52, 54)'
name = "Securing your Digital Frontier"
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), name, fill=color, font=font, stroke_width=1,
          stroke_fill="black")

(x, y) = (170, 1800)
color = 'rgb(45, 52, 54)'
name = "Saad Aslam"
font = ImageFont.truetype('arial.ttf', size=50)
draw.text((x, y), name, fill=color, font=font)

# cert_dir = 'certificates/'
# cert_path = cert_dir+'test'+'.pdf'
rgb.save('test.pdf', 'PDF', resolution=100.0)
