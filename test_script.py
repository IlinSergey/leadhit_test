import requests


URL = 'http://127.0.0.1:5000/get_form'

test_data = [
    # is form
    {
        "user_name": "Alex",
        "user_email": "test@example.com",
        "password1": "Bijo9",
        "password2": "Bijo9",
    },
    {
        "title": "some title",
        "description": "some description",
        "created": "2022-05-01",
    },
    {
        "user_name": "Alex",
        "user_email": "test@example.com",
        "user_phone": "+79211234567",
        "created": "2022-11-14",
    },
    # not form
    {
        "user": "Alex",
        "email": "test@example.com",
        "phone": "+79211234567",
    },
]


if __name__ == '__main__':
    for data in test_data:
        response = requests.post(url=URL, data=data)
        print(f'status code: {response.status_code}')
        print(response.json())
