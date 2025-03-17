#Supermarket using api(using mockable.io) including exception handling function based mail sending and using pandas(fullname email items groceries price using some logic)

import requests
import smtplib
import pandas as pd

def get_data():
    url = "http://demo3584836.mockable.io/Shopping_data"
    response=requests.get(url)

    if response.status_code==200:
        get_data=response.json()

        myval=pd.DataFrame(get_data)
        
        #store the data in csv file
        myval.to_csv("D:\\BESANT_TECHNOLOGIES[PYTHON]\\ASSIGNMENT\shop_details.csv")
    else:
        print("API link is not activated")

def send_mail(final_amount,gst_amount,final_amount_including_gst,mail):
    sender_email="kanhamohapatra12@gmail.com"
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

def supermarket():
    print("\nHere is the list of items available")
    get_data()

    df=pd.read_csv("D:\\BESANT_TECHNOLOGIES[PYTHON]\\ASSIGNMENT\shop_details.csv")
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
    
    gst_amount=final_amount*(18/100)
    print("\nGST = ",gst_amount)
    
    final_amount_including_gst=final_amount+gst_amount
    print("Your total bill after 18% GST is: ",final_amount_including_gst)

    mail_choice = input("\nDo you want you total bill in mail?(yes/no): ").lower()
    if mail_choice == 'yes':
        mail=input("Enter your mail id: ")
        send_mail(final_amount,gst_amount,final_amount_including_gst,mail)
    elif mail_choice == 'no':
        print("\nThanks for Shopping at our store. \nPlease vist again.")
        

def store():
    print("\nWelcome to our Store! We sell both groceries and fruits")

    choice = input("\nDo you want to purchase anything?(yes/no): ").lower()
    if choice == 'yes':
        supermarket()
    elif choice == 'no':
        print("Thanks, Please visit again")
    else:
        print("\nInvalid choice!")
        store()

# Start the program
store()
