from pytube import YouTube
import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *

# send an email
def send_email(subject, message, to_email):
    from_email = "prtm1367@gmail.com"
    password = "Turbodrive@100"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('##server ###', 123)    # need to add server
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# Function to handle video processing
def process_video(video_src):
    cascade_src = "gun.xml"
    cap = cv2.VideoCapture(video_src)
    car_cascade = cv2.CascadeClassifier(cascade_src)
    
    while True:
        ret, img = cap.read()
        if type(img) == type(None):
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        count = 0
        cars = car_cascade.detectMultiScale(gray, 1.1, 2)

        for (x, y, w, h) in cars:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            count += 1

        if cv2.waitKey(33) == 27:
            break
        if count > 2:
            subject = "High Threat Detected"
            message = "Video Has High Amount of threat detected"
            to_email = "pritam.udugade@gmail.com"
            send_email(subject, message, to_email)
            print("Mail is successfully sent")
            exit()

    cv2.destroyAllWindows()


# handle input anf
def printtext():
    global e
    string = e.get()
    a = str(string)
    yt = YouTube(a)
    videos = yt.streams.all()
    
    s = 1
    for v in videos:
        print(str(s) + ". " + str(v))
        s += 1
    
    n = int(input("Enter your choice to download: "))
    vid = videos[n - 1]
    destination = "C:\\Users\\aksha\\Downloads"
    vid.download(destination)
    
    print(f"Video '{yt.title}' has been successfully downloaded.")
    video_src = f"{destination}\\{yt.title}.mp4"
    process_video(video_src)


"""
root = Tk()
root.title("Force One")
root.geometry("200x200")

# Load the image
logo = PhotoImage()

# Create the Label widget and display the image
w1 = Label(root, image=logo)
w1.pack()

e = Entry(root)
e.place(relx=0.5, rely=0.5, anchor='n')
e.focus_set()

t = Label(root, text="Enter your link here", font=("Helvetica", 12), fg='#FF981D', bg='#8c0095')
t.place(relx=0.5, rely=0.4, anchor='n')

b = Button(root, text='proceed', command=printtext, fg='red')
b.pack(side='bottom')
b.place(relx=0.5, rely=0.6, anchor='n')

root.mainloop()

"""

          
from tkinter import *

def printtext():
    print(e.get())

root = Tk()
root.title("Gun detector")

# Change the window size
root.geometry("800x500")

# logo maker
logo = PhotoImage()

# Label widget 
w1 = Label(root, image=logo)
w1.pack()

e = Entry(root)
e.place(relx=0.5, rely=0.6, anchor='center')  

t = Label(root, text="Enter your link here", font=("Helvetica", 12), fg='#FF981D', bg='#8c0095')
t.place(relx=0.5, rely=0.5, anchor='center') 

b = Button(root, text='Proceed', command=printtext, fg='black')
b.pack(side='bottom')
b.place(relx=0.5, rely=0.7, anchor='center') 

root.mainloop()













          
          
