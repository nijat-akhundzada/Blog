def create_user(users: dict) -> dict:
    ''' Create a user, then store the user and return users. '''

    # Getting all email in order to check uniqueness
    emails = users.keys()

    # Getting information of user from input and getting unique email
    while True:
        email = input('Email (*required): ')
        if email in emails:
            print('Email address should be unique, please change it')
        else:
            break

    username = input('Username (*required): ')
    password = input('Password (*required): ')
    user = {
        'username': username,
        'password': password,
        'is_logged_in':False,
    }

    # Store the new user in users
    users[email] = user

    return email


def get_user(email: str, users: dict) -> dict:
    return users.get(email)


def login_user(email: str, password: str, users: dict) -> bool:
    ''' Check this user exist. If it, return True, otherwise return False '''

    # Getting user via email
    user = get_user(email, users)

    if user['is_logged_in']:
        return True

    if user is None:
        print('User does not exist!')
        return False

    password_real = user['password']

    if password_real != password:
        print('Password is not correct!')
        return False

    return True


def change_password(email: str, old_password: str, new_password: str, users: dict) -> bool:
    ''' Change password if the previous one is match '''

    # Getting user via email
    user = get_user(email, users)

    if user is None:
        print('User does not exist!')
        return False

    # Updating password
    if old_password == user['password']:
        user['password'] = new_password
        return True

    return False

def change_username(email:str,new_username, users:dict) ->dict:
    ''' Change username of a user. '''

    user = users.get('email')
    user['username'] = new_username

    return user
