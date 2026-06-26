class UserServiceError(Exception):
    pass

def get_user_from_db(user_id):
    if not isinstance(user_id, int):
        raise ValueError("INVALID NUMBER")
    
    if user_id <= 0:
        raise ValueError("INVALID USER ID")
    
    return {"id": user_id}

def fetch_user(user_id):
    try:
        return get_user_from_db(user_id)

    except ValueError as e:
        raise UserServiceError(
            "USER_FETCH_FAILED"
        ) from e

print(fetch_user(-100))