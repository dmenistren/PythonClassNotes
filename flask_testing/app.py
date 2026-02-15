import requests


URL = "http://localhost:5000"


def signup(data):
    api_req = requests.post(f"{URL}/signup", json=data)
    return api_req.json()


def login(data):
    api_req = requests.post(f"{URL}/login", json=data)
    return api_req.json()


if __name__ == "__main__":
    # data = {
    #     "username": "test_user",
    #     "email": "test@example.com",
    #     # "password": "test_password"
    # }
    # response = signup(data)
    # print(response)

    login_data = {
        "username": "test_user",
        "password": "test_password"
    }

    response = login(login_data)
    print(response)
