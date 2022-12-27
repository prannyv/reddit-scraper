import praw
import smtplib
from email.mime.text import MIMEText

reddit = praw.Reddit(
    client_id="7xzZmO91rjmHMfjGRurQ-A",
    client_secret="pjEg0G1bOJioUSXH7V0hkFSi0P5rnw",
    password="2025awesomE",
    user_agent="HeadphoneManReddit0.1",
    username="pangwan123",
)

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



