import json
import os
import random

header= '-----Welcome to SNBANK Platform-----'
print(header.upper())

def login_algorithm():
    signed_in = False
    while True:
        try:
            login_action = input(str('Enter "login" to sign in/"close" to close the APP ')).lower()
        except ValueError:
            print('Invalid input')
            continue
        if login_action == 'close':
            print('App closed! Thank you.')
            quit()
        elif login_action == 'login':
            while not signed_in:
                username = str(input('Enter your registered username: '))
                password = str(input('Enter your registered password: '))
                with open('staff.txt') as file:
                    user_details = json.load(file)
                    for user in user_details:
                        if user["Username"] == username and user["Password"] == password:
                            signed_in = True
                            print('Welcome! You are now signed in')
                            break
                    else:
                        print('Wrong username and/password, Please try again')

# Successfull sign in and read to carryout some banking operation
        if signed_in:
            is_done = False
            while not is_done:
                operation_choice = input('Press N to create a new bank A/C, C to check A/C details, L to logout ').upper()
                if operation_choice == 'N':
                    print('Your are in New Acc creation environment')
                    print('Personal Account Opening Form ')
                    acc_name = str(input('Enter Acc name: ')).upper()
                    opening_bal = str(input('Enter initial deposit amount: '))
                    acc_type = str(input('Enter Acc type '))
                    acc_email = str(input('Enter a valid email address '))
                    acc_number = "".join(str(random.randint(0, 9)) for i in range(10))

                    #Writting Custmers' details to the customer.txt file
                    with open('customer.txt', 'w') as file:
                        try:
                            customer_data = json.load(file)
                        except:
                            customer_data = []

                            customer_data.append({
                            'acc_number': acc_number,
                            'acc_name': acc_name,
                            'acc_type': acc_type,
                            'opening_bal': opening_bal,
                            'acc_email': acc_email,
                        })
                        with open('customer.txt', 'w') as file:
                            json.dump(customer_data, file)
                            print(acc_number)
                elif operation_choice == 'C':

                    #checking customers' account details
                    customer_ban = str(input("Enter customers' acc number "))
                    with open('customer.txt', 'r') as file:
                        customer_data = json.load(file)
                        fetch = False
                        for customer_data in customer_data:
                            if customer_ban  ==  customer_data['acc_number']:
                                print('Account holder name: ', customer_data['acc_name'])
                                print('Account Number: ', customer_data['acc_number'])
                                print('Account type: ', customer_data['acc_type'])
                                print('Account balance: ', customer_data['opening_bal'])
                                print('Email address: ', customer_data['acc_email'])
                                fetch = True
                        if not fetch:
                            print('Sorry no record found for this number. Try again')

                            #Program terminated
                elif operation_choice == 'L':
                    is_done = True
                    print('You are now signed out. Thank you!')
login_algorithm()



      





















