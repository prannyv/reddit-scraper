import praw
import smtplib
from email.mime.text import MIMEText


infoFile = open("hiddenInfo.txt", "r")


reddit = praw.Reddit(
    client_id=infoFile.readline().strip(),
    client_secret=infoFile.readline().strip(),
    password=infoFile.readline().strip(),
    user_agent=infoFile.readline().strip(),
    username=infoFile.readline().strip()
)
infoFile.close()




LOOKFORS = ("airpods pro", "airpod pros", "xm4","xm5", "3060","3070", "3080")

def addPostToList(submission):
    #submission is a submission Object
    file = open("headphoneInput", "a")
    file.write(submission.id+"\n")
    file.close()

def doesSubmissionContain(submission):
    #submission is a submission Object
    title = submission.title.lower()
    title = title[title.find("[", title.find("]")+1):]#cuts whats before [h]
    title = title[:title.find("]", title.find("]")+1)]#cuts it past [w]
    title = title[3:len(title)-2]
    # print(title)

    for word in LOOKFORS:
        if title.find(word) != -1:
            addPostToList(submission)
            msg = MIMEText(title)
            msg['Subject'] = word

            print("id:",submission.id,"\n","item:",title)





for submission in reddit.subreddit("HardwareSwap").new(limit=50):
    doesSubmissionContain(submission)



