import smtplib
from email.mime.text import MIMEText

msg = MIMEText("So many people buy masks!!!")

"""
https://myaccount.google.com/u/1/lesssecureapps?pageId=none
"""
msg['Subject'] = "We don't like virus!"
msg['From'] = "King of Mask"
msg['To'] = "xxxxx@xxxxx.com"

"""
host setting
"""
host = "smtp.gmail.com"
nego_combo = ("starttls", 587)

if nego_combo[0] == "no-encrypt":
    smtpclient = smtplib.SMTP(host, nego_combo[1], timeout=10)
elif nego_combo[0] == "starttls":
    smtpclient = smtplib.SMTP(host, nego_combo[1], timeout=10)
    smtpclient.ehlo()
    smtpclient.starttls()
    smtpclient.ehlo()
elif nego_combo[0] == "ssl":
    context = ssl.create_default_context()
    smtpclient = smtplib.SMTP_SSL(host, nego_combo[1], timeout=10, context=context)
smtpclient.set_debuglevel(2)


"""
Log in to server
"""
username = "xxxxx@gmail.com"
password = "xxxxx"
smtpclient.login(username, password)

"""
Send email
"""
smtpclient.send_message(msg)
smtpclient.quit()
