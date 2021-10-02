import smtplib

# class creation
class visitorForm:
    mycount = 0
    def __init__(self,myname,myphone,myemail,mypassword,sender_id):
        self.name = myname
        self.phone = myphone
        server = smtplib.SMTP("smtp.gmail.com" , 587)
        server.starttls()
        login_id = myemail
        login_password = mypassword
        server.login(login_id,login_password)
        message = "Welcome to Linux World"
        server.sendmail(login_id,sender_id,message)
        server.quit
        visitorForm.mycount += 1
    def getphone(self):
        print(self.phone)
   

# Object creation
spandan = visitorForm(myname = "Jack k" , myphone = 11111,myemail = "spandan.dutta_cs.ccv19@gla.ac.in",mypassword=9412454043,sender_id="navyaswarup2004@gmail.com")

# To count how many number of students have joined.
print("The number of students are: ",visitorForm.mycount)
