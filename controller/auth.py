from controller.firebaseOperations import auth
# TODO: implement a login system that check if the user is logged in or not
def checkLogin(token):
    try:
        auth.get_account_info(token)
        return True
    except:
        return False

def login_email(res):
    if 'email' not in res or 'password' not in res:
        return None

    email = res['email']
    password = res['password']
    try:
        data = auth.sign_in_with_email_and_password(email, password)
        return {
            'success': True,
            'token': data['idToken']
        }
    except:
        return {
            'success': False
        }