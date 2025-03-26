import requests
import smtplib
import pandas as pd
import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kanha@1234",
    database="shop"
)

mycursor=mydb.cursor()

def get_data():
    url = "http://demo3584836.mockable.io/Shopping_data"
    response=requests.get(url)

    if response.status_code==200:
        get_data=response.json()

        myval=pd.DataFrame(get_data)
        
        #store the data in csv file
        myval.to_csv("D:\\BESANT_TECHNOLOGIES[PYTHON]\\Project\shop_details.csv")
    else:
        print("API link is not activated")

def send_mail(final_amount,gst_amount,final_amount_including_gst,mail):
    sender_email="sender mail"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, "password")
    message = f"Your total bill before GST is {final_amount} \nGST = {gst_amount} \nYour total bill after 18% GST is: {final_amount_including_gst}"

    try:
        s.sendmail(sender_email,mail, message)
        print("Mail has been sent successfully")
        print("\nThanks for Shopping at our store. \nPlease vist again.")
        s.quit()
    except:
        print("Mail not sent")

def supermarket(fullname):
    print("\nHere is the list of items available")
    get_data()

    df=pd.read_csv("D:\\BESANT_TECHNOLOGIES[PYTHON]\\Project\shop_details.csv")
    print(df)

    row_count = df.shape[0]
    print("Select the quantity of each product you want ")
    i=0
    final_amount=0
    while i<row_count:
        s_data=df.iloc[i,1]

        quantity=int(input(f"Enter the quantity of {s_data} you want to buy: "))
        
        amount=int(df.iloc[i,2])
        total_amount=quantity*amount
        print(f"Total price of {s_data} that you want is {total_amount} ")
        final_amount=final_amount+total_amount
        i=i+1

    print("\nYour total bill before GST is: ",final_amount)
    
    #gst calculation
    gst_amount=final_amount*(18/100)
    print("\nGST = ",gst_amount)
    
    final_amount_including_gst=final_amount+gst_amount
    print("Your total bill after 18% GST is: ",final_amount_including_gst)
    
    sql="update user_data set total_bill=%s where fullname=%s"
    val=(final_amount_including_gst,fullname)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Final Bill upadated successfully in database")

    mail_choice = input("\nDo you want you total bill in mail?(yes/no): ").lower()
    if mail_choice == 'yes':
        mail=input("Enter your mail id: ")
        send_mail(final_amount,gst_amount,final_amount_including_gst,mail)
    elif mail_choice == 'no':
        print("\nThanks for Shopping at our store. \nPlease vist again.")

#Registration Block
def register():
    print("*****SIGN UP*****")
    fullname=input("Enter your fullname: ")
    mobile=int(input("Enter your mobile number: "))
    username=input("Enter your username: ")
    password=input("Enter your password: ")

    sql="insert into user_data(fullname,mobile,username,password) values (%s,%s,%s,%s)"
    val=(fullname,mobile,username,password)

    mycursor.execute(sql,val)
    mydb.commit() #to save the data into table
    print("Registration successfully")
    login()

#Login Block
def login():
    print("*****SIGN IN*****")
    username=input("Enter your username: ")
    password=input("Enter your password: ")

    sql="select * from user_data where username=%s and password=%s"
    val=(username,password)

    mycursor.execute(sql,val)

    result=mycursor.fetchone()
    if result:
        fullname=result[0]
        store(fullname)
    else:
        print("Enter a valid username or password")
        login()

   
def store(fullname):
    choice = input("\nDo you want to purchase anything?(yes/no): ").lower()
    if choice == 'yes':
        supermarket(fullname)
    elif choice == 'no':
        print("Thanks, Please visit again")
    else:
        print("\nInvalid choice!")
        store()

#Main Block
def main():
    print("\nWelcome to our Store! We sell both groceries and fruits")
    choice = input("\nDo you have an account?(yes/no): ").lower()
    if choice == 'yes':
        login()
    elif choice == 'no':
        register()
    else:
        print("\nInvalid choice!")
        main()

# Start the program
main()
