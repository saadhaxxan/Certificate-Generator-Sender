# importing libraries
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
# reading csv
data = pd.read_csv('senders.csv', sep=',', names=['Names', 'Emails'])
# remove null values
data.dropna(inplace=True, axis=1)
# dropping dupicate rows
data.drop_duplicates(subset=['Emails'], keep='last', inplace=True)
# convert to list
names = data['Names'].to_list()
emails = data['Emails'].to_list()
# checking if the directory exists
if os.path.exists('certificates'):
    print("Folder already exists")
else:
    os.mkdir('certificates')
# opening log file and writing ceritifcates
with open("logs.txt", 'a') as f:
    for (name, email) in zip(names, emails):
        try:
            file_path = 'base_file.png'
            image = Image.open(file_path)
            rgb = Image.new('RGB', image.size, (255, 255, 255))  # white background
            rgb.paste(image, mask=image.split()[3])
            draw = ImageDraw.Draw(rgb)
            (x, y) = (170, 820)
            color = 'rgb(0, 151, 230)'
            name = name
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
            cert_dir = 'certificates/'
            cert_path = cert_dir+email+'.pdf'
            rgb.save(cert_path)
            print(str(email) + " Success")
            f.write(str(email) + " Success")
            f.write("\n")
        except:
            print(str(email) + " Failed")
            f.write("\n")
            f.write(str(email)+" Failed")
    f.close()
