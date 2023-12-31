import smtplib

sender= ""
receiver = ""

message = "Helloooooooooooooooo"

server = smtplib.SMTP('smtp.office365.com',587)
server.startls()
server.login(sender,password)
server.sendmail(sender,receiver,message)
server.quit()