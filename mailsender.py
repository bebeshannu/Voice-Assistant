import speech_recognition as sr
import smtplib as smtp
import pyttsx3 as pytts



recognizer=sr.Recognizer()
speaker=pytts.init()
speaker.setProperty("rate",150)
def sendemail():
        with sr.Microphone() as source:
                speaker.say("Enter the reciever mail address")
                speaker.runAndWait()
                reciever=input("Enter the reciever mail address:")
                speaker.say("Tell me the body of mail to be sent")
                speaker.runAndWait()
                recognizer.adjust_for_ambient_noise(source,duration=1)
                recad=recognizer.listen(source)

       
                try:
       
                       text=recognizer.recognize_google(recad,language="en-US")
                       print("Your message:{}".format(text))
                except Exception as ex:
                       print(ex)
                message=text
                sender=smtp.SMTP('smtp.gmail.com',587)
                sender.ehlo()
                sender.starttls()
                mailaddress='saraswathiacharya315@gmail.com'
                password='qqjlrplstccryatq'
                Subject="This is a automated mail"
                sender.login(mailaddress,password)
                msg="Subject:{0}\n\n{1}".format(Subject,text)
                sender.sendmail(mailaddress,reciever,msg)
                print("Email has been sent")               