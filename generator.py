import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

data = pd.read_csv('demo.csv')
data.drop_duplicates(subset=['Emails'], keep='last', inplace=True)
names = data['Names'].to_list()
emails = data['Emails'].to_list()
if os.path.exists('certificates'):
    pass
else:
    os.mkdir('certificates')
with open("logs.txt", 'a') as f:
    for (name, email) in zip(names, emails):
        try:
            file_path = 'base_file.png'
            image = Image.open(file_path)
            draw = ImageDraw.Draw(image)

            (x, y) = (950, 1120)
            color = 'rgb(45, 52, 54)'
            name = name
            font = ImageFont.truetype('arial.ttf', size=160)
            draw.text((x, y), name, fill=color, font=font)

            (x, y) = (850, 1820)
            color = 'rgb(45, 52, 54)'
            name = "Saad Aslam"
            font = ImageFont.truetype('SouthamDemo.otf', size=180)
            draw.text((x, y), name, fill=color, font=font)

            (x, y) = (1950, 1820)
            color = 'rgb(45, 52, 54)'
            name = "Fahad Ashiq"
            font = ImageFont.truetype('SouthamDemo.otf', size=180)
            draw.text((x, y), name, fill=color, font=font)

            cert_dir = 'certificates/'
            cert_path = cert_dir+email+'.pdf'
            image.save(cert_path)
            print(str(email) + " Success")
            f.write(str(email) + " Success")
            f.write("\n")
        except:
            f.write("\n")
            print(str(email) + " Failed")
            f.write(str(email)+" Failed")
    f.close()
