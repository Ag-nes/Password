from unittest.main import main
from credentials import Credentials
from user import User

def create_user(first_name, last_name, user_name, password):
    user =  User(first_name, last_name, user_name, password)
    return user

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def find_accounts(user_name):
    return User.find_by_user_name(user_name)


def exist_user(user_name):
    return User.user_exists(user_name)

def display_accounts():
    return User.display_users()

def create_page(page, password):
    credentials = Credentials(page, password)
    return credentials

def save_page(credentials):
    credentials.save_page()

def find_page(pager):
    return Credentials.find_by_page(pager)


def isexist_page(pager):
    return Credentials.page_exists(pager)

def delete_page(credentials):
    credentials.delete_page()

def display_pages():
    return Credentials.display_page()

def head():
    print('WELCOME TO PASSWORD-LOCKER')
    print('Select what best suits your needs')
    while True:

        print(" 1) LOGIN \n 2) REGISTER \n 3) USER-PASSWORDS\n 4) USERS \n 5) SIGN OUT")

        choice = int(input())
        if choice == 1:
            print('Enter username')
            username = input()
            print('Your password?')
            credentials = input()
            user = find_accounts(username)
            if User.user_name == username and user.credentials == credentials:

                print('logged in ')
                while True:

                    print(
                        f'Welcome {username}, follow the prompts')

                    print(
                        ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                    log_choice = int(input())
                    if log_choice == 1:
                        print('New page')
                        print('*'*100)

                        print('Page name')
                        page = input()

                        print('credential')
                        credentials = input()

                    # created and saved page
                        save_page(create_page(page, password))

                    elif log_choice == 2:
                        print("Enter the name of the page you want to delete")

                        page = input()
                        if isexist_page(page):
                            remove_page = (page)
                            delete_page(remove_page)

                        else:
                            print(f'Theres no {page}')

                    elif log_choice == 3:
                        if display_pages():
                            for pag in display_pages():
                                print(
                                    f'{pag.page}:{pag.password}'
                                )
                        else:
                            print('NO PASSWORD SAVED YET')
                            print('\n')

                    elif log_choice == 4:
                        print('')
                        break
            else:
                print('wrong credentials')

        if choice == 2:
            print('NEW ACCOUNT')
            print('*'*100)

            print('FIRSTNAME')
            first_name = input()

            print('LASTNAME')
            last_name = input()

            print('USERNAME')
            user_name = input()

            print('PASSWORD')
            password = input()

            save_user(create_user(
                first_name, last_name, user_name, password))
            
            print('ACCOUNT CREATED')
            while True:

                print(
                    f'Welcome {user_name}, Follow the prompts')
                print(
                    ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                log_choice = int(input())
                if log_choice == 1:
                    print('New page')
                    print('*'*100)

                    print('Page name')
                    page = input()

                    print('password')
                    password = input()

                    save_page(create_page(page, password))

                elif log_choice == 2:
                    print("Enter the name of the page you want to delete")

                    page = input()
                    if isexist_page(page):
                        remove_page = (page)
                        delete_page(remove_page)

                    else:
                        print(f'I cant find {page}')

                elif log_choice == 3:
                    if display_pages():
                        for pag in display_pages():
                            print(
                                f'{pag.page}:{pag.password}'
                            )
                    else:
                        print('PLEASE SAVE YOUR PASSWORD')

                elif log_choice == 4:
                    break

        elif choice == 3:
            print('ABOUT PASSWORD-LOCKER')
            print(
                '''
            Password-locker is an application that allows users to store password of multi-accounts.Store your passwords with this application cause its the best.
                                    ''')

        elif choice == 4:
            if display_accounts():
                for user in display_accounts():
                    print(
                        f'{user.user_name}'
                    )
            else:
                print('NO USER')

        elif choice == 5:
            print('pawa')
            break


if __name__ == '__main__':
    head()




