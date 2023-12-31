import yagmail
import time
from datetime import datetime as dt
import pandas as pd

sender = 'vinayreddykappeta@gmail.com'
#receiver = 'kappetavinayreddy@gmail.com'

subject = "This is the new subject"

contents = """
Here is the contents of email
"""
df = pd.read_csv('/config/workspace/mail_automation/contact.csv')
print(df)


now = dt.now()
yag = yagmail.SMTP(user = sender,password = 'zlolqddvsysarxrk' )

def generate_file(file_name,content):
    with open(file_name,'w') as file:
        file.write(str(content))

for index,row in df.iterrows():
    generate_file(f'{row["name"]}.txt',row['amount'])

    contents = [f""" 
    Here is the contents of email, Hii {row['name']}
    """,f"{row['name']}.txt"]
    print(contents)
    yag.send(to = row['email'],subject=subject,contents = contents)
    print("Email sent!")


