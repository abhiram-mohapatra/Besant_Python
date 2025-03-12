import smtplib
import random
import string

def send_mail():
    try:
        f=open("D:\\BESANT_TECHNOLOGIES[PYTHON]\\ASSIGNMENT\employee_mails.txt","r")
        employee_mails=f.read()
        employee_mails=employee_mails.split(",")
        print(employee_mails)
    except:
        print("File not available")

    sender_email="kanhamohapatra12@gmail.com"
    
    for i in employee_mails:
        verification_code=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=5))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, "fakb yfvk dsec ozxv")
        message = f"A sign in attempt requires further verification. To complete the sign in, enter the verification code.\nYour verification code is {verification_code}.\n\nPlease note that the code is valid for only one session. If you try to refresh the page or leave the portal, you will be required to regenerate a new code.\n\nDo not share this code with anyone."

        try:
            s.sendmail(sender_email, i, message)
            print("Mail has been sent successfully")
            s.quit()
        except:
            print("Mail not sent")

send_mail()
