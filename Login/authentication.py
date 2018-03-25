def login(_id):
    members = ['mdoubleu', 'egoing', 'flamewndls']
    for member in members:
        if member == _id:
            return True
    return False

def password(pw):
    passwords = [1234, 5678, 0000]
    for password in passwords:
        if password == pw:
            return True
    return False
