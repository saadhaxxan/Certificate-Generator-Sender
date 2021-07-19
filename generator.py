# importing libraries
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
# reading csv
data = pd.read_csv('demo.csv')
# remove null values
data.dropna(inplace=True,axis=1)
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
            print(str(email) + " Failed")
            f.write("\n")
            f.write(str(email)+" Failed")
    f.close()
