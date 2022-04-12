import urllib.request
import json
import time
import smtplib
import webbrowser
import datetime
x=input("Enter pincode :- ")
y=input("Enter date (Enter date in dd-mm-yyyy format ):-")
z=input("Enter minimum age:-")

sixdays=[]
day_delta = datetime.timedelta(days=1)
date_dt3 = datetime.datetime.strptime(y, '%d-%m-%Y')
end_date = date_dt3 + 6*day_delta

for i in range((end_date - date_dt3).days):
    end_date1=date_dt3 + i*day_delta
    date_dt4 = end_date1.strftime("%d-%m-%Y")
    sixdays.append(date_dt4)
print(sixdays)
def sendEmail(mail):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akankita44@gmail.com', 'anirudh4444@kumar')
    server.sendmail('akankita44@gmail.com', 'anirudh.c.kumar@accenture.com', mail)
    server.close()
def play():
    webbrowser.open("https://www.youtube.com/watch?v=CCJctjIO5kU")
mm=0
while(True):
    finaldate=sixdays[mm]
    print(finaldate)
    mm=mm+1
    req = urllib.request.Request('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}'.format(x,finaldate),headers={'User-Agent': 'Anirudh'})
    html= urllib.request.urlopen(req).read()
    a = json.loads(html)
    if (len(a['centers'])>0):
        for p in a['centers']:
            for s in p['sessions']:
                if s['min_age_limit'] == int(z) and s['available_capacity'] > 0:
                    mail="Name of the center:-{} |||| Address of center:-{} |||| Total available capacity:-{}".format(p['name'],p['address'],s['available_capacity'])
                    sendEmail(mail)
                    play()
                    print("Name of the center :-")
                    print(p['name'])
                    print("Address of center :-")
                    print(p['address'])
                    print("Total available capacity:-")
                    print(s['available_capacity'])
                    print("Slots avvailable")
                    time.sleep(10)
                    #os.listdir('C:\\Users\\akank\\OneDrive\\Desktop\\OnboardManagement\\Onboarding\\src\\config\\audio')
                    #playsound.playsound('C:\\Users\\akank\\OneDrive\\Desktop\\OnboardManagement\\Onboarding\\src\\config\\audio.mp3',True)
                else:
                    print("All booked for "+p['name'])
                    time.sleep(20)
                    break
                if(mm==6):
                    mm=0
                    break
    else:
        print("No slots available")
        time.sleep(20)
        if(mm==6):
            mm=0
        print("Sending request again")