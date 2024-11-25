import urllib.parse

def get_mongo_url():
    login = {
        "host": "cluster1.tgo3l.mongodb.net",
        "port": 27017,
        "username": "guest_account",
        "password": "e8RZETLbPWzhgvXH"
    }
    username = login['username']
    password = urllib.parse.quote(login['password'])
    host = login['host']
    return f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority"
