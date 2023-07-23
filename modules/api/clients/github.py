import requests


class GitHub:

    def get_user_defunct(self):
        r = requests.get('https://api.github.com/users/defunkt')
        body = r.json()

        return body
    
    def get_not_exist_user(self):
        r = requests.get('https://api.github.com/users/butenkosergii')
        body = r.json()

        return body
    