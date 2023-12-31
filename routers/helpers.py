from starlette.exceptions import HTTPException


def check_user_authentication(user):
    # print("Check user authentication being called ")
    role = user.get("user_role").lower()
    print(role)
    # developer, business_owner, admin
    if user is None or role not in ["user", "admin", "business_owner", "developer"]:
        print(f"The user {user} is not authorized to access this resource")
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
def check_user_authentication_admin(user):
    # print("Check user authentication being called ")
    role = user.get("user_role").lower()
    print(role)
    # developer, business_owner, admin
    if user != "admin":
        print(f"The user {user} must be an admin this resource")
        raise HTTPException(status_code=401, detail="Admin Authentication Failed")
    return "The user must be an admin this resource"
