from app.services.auth.jwt import jwt_core

def authenticate(web_request_function):
    def wrapper():
        if not is_authenticated():
            get_jwt_token()
        web_request_function()
        # remember that you can do something here algo, such as create an expiration boolean on JWT core
        # and do this validation after the web_request_function be called.
        # adding more validation to your app.
        # is_expired(jwt_core['JWT Token Is Expired'])

    return wrapper


def is_authenticated():
    """
    verifies if there is an authentication on the memory, and if it is valid
    e.g JWT token on some variable and it is not expired
    """

    if not jwt_core['JWT Token']:
        print('There is no JWT Token...')
        return False
    
    else:
        expiration = jwt_core['JWT Token Expiration']


        # the expiration validation is not going to be done in that way, you should implement your way.
        # this is just the logic example.
        if expiration == True:
            print('The JWT token is expired... You need another one.')
            return False
        else:
            return True


def get_jwt_token():
    """
    a function that gets a jwt token, you may have any kind of authentication mode
    on this example we are considering JWT
    """
    jwt_core['JWT Token Expiration'] = '1000'
    jwt_core['JWT Token'] = 'ey19203iorfkdpsgai-0q349tiksdpgksdokfge=242t-igksdpfokhbfsdohjpdtg0h8inspeh'
