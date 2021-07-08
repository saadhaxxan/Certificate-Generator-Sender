import pandas as pd
from PIL import Image, ImageDraw, ImageFont

data = pd.read_csv('techtehvaarorg.csv')
names = data['Name'].to_list()
emails = data['Email'].to_list()
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

            #
            # image.show()

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


# import pandas as pd

# def generate_certificate(names, event_name, status, date, ambassador):
#     path = str(BASE_DIR) + '/media/certificates'
#     shutil.rmtree(path)
#     os.mkdir(path)
#     for name in names:
#         cert_id = generate_certificate_id()
#         query_obj = Certificate(event_name=event_name,
#                                 attendee_name=name, certificate_id=cert_id)
#         query_obj.save()
#         module_dir = os.path.dirname(__file__)  # get current directory
#         file_path = os.path.join(module_dir, 'base_file.jpg')
#         image = Image.open(file_path)
#         draw = ImageDraw.Draw(image)
#         font = ImageFont.truetype('arial.ttf', size=45)
#         (x, y) = (75, 400)
#         color = 'rgb(41, 128, 185)'
#         font = ImageFont.truetype('arial.ttf', size=80)
#         draw.text((x, y), name, fill=color, font=font)

#         (x, y) = (75, 600)
#         text = 'In recognition of your attendance and completion of the \nMicrosoft Student Ambassadors ' + event_name
#         color = 'rgb(0, 0, 0)'
#         font = ImageFont.truetype('arial.ttf', size=40)
#         draw.text((x, y), text, fill=color, font=font)

#         (x, y) = (75, 800)
#         text = 'Event Hosted By\n'+ambassador+'\n' + \
#             status+' Microsoft Learn Student Ambassador'
#         color = 'rgb(0, 0, 0)'
#         font = ImageFont.truetype('arial.ttf', size=30)
#         draw.text((x, y), text, fill=color, font=font)
#         # name = name.replace(" ","_")

#         # cert_id
#         cert_dir = os.path.join(BASE_DIR, 'media/certificates/')
#         cert_path = cert_dir + name + '_certificate'+'.pdf'
#         image.save(cert_path)
#     cert_dir = os.path.join(BASE_DIR, 'media/certificates')
#     filePaths = retrieve_file_paths(cert_dir)
#     zip_file = zipfile.ZipFile('certificates.zip', 'w')
#     with zip_file:
#         for file in filePaths:
#             zip_file.write(file)
#     shutil.rmtree(path)
#     return True
