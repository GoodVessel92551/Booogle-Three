from replit import db
print(db["beta"])
def beta(name):
    if name in db["beta"]:
        return True
    else:
        return False

def admin(name):
    if name == "GoodVessel92551":
        return True
    else:
        return False