# A login authenticator

def login_required(func):
    def wrapper(*args, **kwargs):
        user = args[0]
        if user.get("name") == "Yogesh" and user.get("is_logged_in") == True:
            return func(*args, **kwargs)
        else:
            print("Access Denied")
    return wrapper

@login_required
def view_profile(user):
    print("Welcome", user["name"])
user = {
    "name": "Yogesh",
    "is_logged_in": False
}
view_profile(user)