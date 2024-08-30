from app.services.auth.jwt import jwt_core
from app.services.auth import authenticate


@authenticate
def decorated_web_function():

    header ={

        'Token': jwt_core['JWT Token'],
        'Accept-Content': 'application/json'
        
    }

    print(f"doing a request with the jwt token {header['Token']}")


def non_decorated_web_function():

    header ={

        'Token': jwt_core['JWT Token'],
        'Accept-Content': 'application/json'
        
    }

    print('doing a request without the jwt token because we did not use the decorator')