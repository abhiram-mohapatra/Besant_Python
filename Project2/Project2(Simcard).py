import random
import requests
import smtplib
import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kanha@1234",
    database="simcard"
)

mycursor=mydb.cursor()

def main():
    print("Welcome to our site")
    print("You can avail you Airtel Sim easily from this site")
    choice = input("\nAre you a registered user?(yes/no): ").lower()
    if choice == 'yes':
        login()
    elif choice == 'no':
        register()
    else:
        print("\nInvalid choice!")
        main()

def register():
    print("*****SIGN UP*****")
    fullname=input("Enter your fullname: ")
    email=input("Enter your emailid: ")
    username=input("Enter your username: ")
    password=input("Enter your password: ")

    sql="insert into user_data(fullname,email,username,password) values (%s,%s,%s,%s)"
    val=(fullname,email,username,password)

    mycursor.execute(sql,val)
    mydb.commit() #to save the data into table
    print("\nRegistration successfully")
    login()


def login():
    print("\n*****SIGN IN*****")
    username=input("Enter your username: ")
    password=input("Enter your password: ")

    sql="select * from user_data where username=%s and password=%s"
    val=(username,password)

    mycursor.execute(sql,val)

    result=mycursor.fetchone()
    if result:
        sim_registration()
    else:
        print("Enter a valid username or password")
        login()

def sim_registration():
    print("Enter your following details to issue a simcard")
    fullname=input("Enter your Fullname: ")
    fathers_name=input("Enter your Father's Name: ")
    dob=input("Enter your Date of Birth: ")
    email=input("Enter your email: ")
    aadhar_number=int(input("Enter your Aadhar Number: "))
    alternate_number=int(input("Enter an Alternate Number: "))

    sql="insert into customer_details(fullname,fathers_name,dob,email,aadhar_number,alternate_number) values (%s,%s,%s,%s,%s,%s)"
    val=(fullname,fathers_name,dob,email,aadhar_number,alternate_number)

    mycursor.execute(sql,val)
    mydb.commit() #to save the data into table
    print("Registration for issue of new simcard is successfull")
    
    issue_number(fullname,email)

def issue_number(fullname,email):
    new_number=random.randint(8000000000,8999999999)
    print("\nCongratulations!!! Your airtel sim is issued and your new airtel number is: ",new_number)

    sql="update customer_details set assigned_number=%s where fullname=%s"
    val=(new_number,fullname)
    mycursor.execute(sql,val)
    mydb.commit()

    mail(fullname,email)

def mail(fullname,email):
    sender_email="sender mail"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, "password")
    message = f"Congratulation {fullname} your new airtel sim has been issued and you number has also been issued"

    try:
        s.sendmail(sender_email,email,message)
        print("A confirmation mail has been sent to your registered mail id")
        print("\nThank you for choosing Airtel, hope you like our service. \nPlease vist again.")
        s.quit()
    except:
        print("Sorry, we are unable to send a confirmation mail due to some technical issue")
main()
