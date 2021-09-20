# importing libraries
import os
import re
import time
import smtplib
import imghdr
from email.message import EmailMessage
from email.utils import formataddr

EMAIL_ADDRESS = 'Your_email'
EMAIL_PASSWORD = 'Your_password'

i = 1
with open("emaillogs.txt", 'a') as f:
    for filename in os.listdir('certificates'):
        try:
            with open(os.path.join('certificates', filename), 'rb') as fp:
                file_data = fp.read()
                msg = EmailMessage()
                msg['Subject'] = 'Securing your digital frontiers certificate'
                msg['From'] = formataddr(
                    ('Saad Hassan', 'saad.haxxan786@gmail.com'))
                mail_to = filename.rsplit(".", 1)[0]
                msg['To'] = mail_to
                msg.set_content('''Hi,\nThank you for attending the training session Securing your Digital Frontier: A Challenge to Cyber Security. Kindly find the attached certificate. Make sure to post your feedback about the session with the certificate on your session.\nSpeaker Profile:  https://www.linkedin.com/in/saad-aslam-dev/''')
                msg.add_attachment(file_data, maintype='application',
                                   subtype='pdf', filename='securing your digital frontiers.pdf')
                print('read file '+str(i)+" "+str(filename))
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)
                print(str(mail_to) + " Sending Success")
                f.write(str(mail_to) + " Sending Success")
                f.write("\n")
                i += 1
        except:
            print(str(mail_to) + " Sending Failed")
            f.write("\n")
            f.write(str(mail_to)+" Sending Failed")
    f.close()
