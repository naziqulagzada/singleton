def require_login(func):
    def wrapper(user):
        if not user.get("is_authenticated"):
            return "Please login"
        return func(user)
    return wrapper

def require_role(role):
    def decorator(func):
        def wrapper(user):
            if user.get("role") != role:
                return f" Only for role {role}"
            return func(user)
        return wrapper
    return decorator

def home(user):
    return " Public page"

@require_login
def profile(user):
    return f" Profile of {user['name']}"

@require_login
@require_role("admin")
def dashboard(user):
    return f" Admin dashboard for {user['name']}"

guest  = {"name": "Guest", "is_authenticated": False, "role": "guest"}
user   = {"name": "Ali", "is_authenticated": True, "role": "user"}
admin  = {"name": "Sara", "is_authenticated": True, "role": "admin"}

print(home(guest))
print(profile(guest))
print(profile(user))
print(dashboard(user))
print(dashboard(admin))
