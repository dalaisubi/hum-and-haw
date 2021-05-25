import requests, json

BASE_URL = "https://api.github.com/"

def get_repos(username):
    try:
        r = username and requests.get(f'{BASE_URL}users/{username}/repos').json() or None

        if r:
            resp = { "status": True, "data": r}
        else:
            resp = {"status": False, "message": "username required"}
    except Exception as e:
        resp = {"status": False, "message": str(e)}
    return resp

def get_followers(username):
    try:
        r = username and requests.get(f'{BASE_URL}users/{username}/followers').json() or None

        if resp:
            resp = { "status": True, "data": r}
        else:
            resp = {"status": False, "message": "username required"}
    except Exception as e:
        resp = {"status": False, "message": str(e)}
    return resp