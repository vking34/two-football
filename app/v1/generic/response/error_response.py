SIGNUP_EXISTING_USER_ERROR = {
    'status': False,
    'message': 'Username/Phone number/Email is used already',
    'code': 101
}

FAIL_LOGIN = {
    'status': False,
    'message': 'Username/password is wrong',
    'code': 201
}

MISSING_AUTHORIZATION_FIELD = {
    'status': False,
    'message': 'Header is missing the authorization field',
    'code': 301
}

BAD_AUTHORIZATION = {
    'status': False,
    'message': 'Value of the authorization field is not in the correct form',
    'code': 302
}

FORBIDDEN_RESPONSE = {
    'status': False,
    'message': 'Request is forbidden',
    'code': 303
}

EXPIRED_TOKEN = {
    'status': False,
    'message': 'Expired access token',
    'code': 304
}

INVALID_TOKEN = {
    'status': False,
    'message': 'Invalid access token',
    'code': 305
}

USER_NOT_FOUND = {
    'status': False,
    'message': 'User not found',
    'code': 401
}

BAD_CARD_REQUEST = {
    'status': False,
    'message': 'Payload consists an invalid card code / password.',
    'code': 501
}