import yagmail
import time
from datetime import datetime as dt

sender = 'vinayreddykappeta@gmail.com'
receiver = 'kappetavinayreddy@gmail.com'

subject = "This is the subject"

contents = """
Here is the contents of email
"""
while True:
    now = dt.now()
    if now.hour == 8 and now.minute == 38:
        yag = yagmail.SMTP(user = sender,password = 'zlolqddvsysarxrk' )

        yag.send(to = receiver,subject=subject,contents = contents)

        print("Email sent!")
        time.sleep(60)

