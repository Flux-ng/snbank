import json
print('-----Welcome UCB Platform-----')
def staff_login():
    try:
        choice = input('Action: enter Login to sign in, close to Close App ').lower()
        while choice == 'login':
            print('provide your login details here to sign in')
            input(str('Enter Username: '))
            input(str('Enter password: '))
            with open('staff.txt') as file:
                staff_info = json.load(file)
            if choice == 'close':
                print('App closed. Thank')
    except ValueError:
        print('Wrong password or Username, try again')
        return




staff_login()