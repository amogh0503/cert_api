from PIL import Image, ImageDraw, ImageFont
from datetime import date
import pandas as pd
import numpy as np
import yagmail
import os

#Function to verify if the certificate exists in the search_path
def find_files(filename, search_path):
    result = []

    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(filename)
    return result


#Function to attach the certificate file and send using 
#gmail account (hackersvilla.xyz@gmail.com) to all participants
def mail_send(recv_mail, filename,name):
    receiver = recv_mail
    body = "Hi "+name+"! Here's your Certificate of Participation for Hack-n-Slash Webinar by HackersVilla :)"
    location = "certs/"+filename.strip()
    
    yag = yagmail.SMTP("hackersvilla.xyz@gmail.com")
    yag.send(
        to=receiver,
        subject="Knock Knock! Its HackersVilla..",
        contents=body,
        attachments=location,
    )


#Fetch today's date for printing on certificate
today = date.today()
date = today.strftime("%B %d, %Y")

#Storing entire csv file into a dataframe
df = pd.read_csv('list.csv')

#Length of dataframe (for iterating in the loop)
entries = len(df)

#Storing the names and emails of participants as a numpy array
arr = np.array(df[['name','email','date']])
date = arr[0][2]

print("Found",entries,"participants")
print("Creating Certificates now.. Please Wait")


#Segment to create certificate
font1 = ImageFont.truetype('Herland.ttf',170)
font2 = ImageFont.truetype('Poppins-SemiBold.otf',34)
for index,j in df.iterrows():
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)

    W = 3650
    msg = '{}'.format(j['name'])
    w, h = draw.textsize(msg, font=font1)
    draw.text(((W-w)/2,900), msg, fill="white", font=font1)
    
    #draw.text(xy=(1700,900),text='{}'.format(j['name']),fill="white",font=font1)
    draw.text(xy=(2400,1385),text=date,fill="#00f0ff",font=font2)
    img.save('certs/{}.jpg'.format(j['name']))

print("Certificates have been created and are ready to mail")
print("Stariting now \n\n")


#Segment to iterate over every row in the array, verify the cert file and send on the corresponding email of participant
for x in range(entries):
    name = arr[x][0]
    img = ""
    img = img + name + ".jpg"
    print("Name of Participant:", name)
    print("Searching for cert", img)
    if find_files(img,"./certs"):
        print("Certificate Found for", name)
        email = arr[x][1]
        print("Sending email on",email)
        mail_send(email,img,name)
        print("Certificate Sent\n\n")
    else:
        print("Certificate file not found for",name)
        print("Continuing further..\n\n")

print("Huff! I am done boss")

