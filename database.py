from typing import List

from tinydb import TinyDB
from tinydb.table import Document


db = TinyDB('db.json')


forms_list = [
    {
        'form_name': 'Register user form',
        'user_name': 'text',
        'user_email': 'email',
        'password1': 'text',
        'password2': 'text',
    },
    {
        'form_name': 'Add product form',
        'title': 'text',
        'description': 'text',
        'created': 'date',
    },
    {
        'form_name': 'Create order form',
        'user_name': 'text',
        'user_email': 'email',
        'user_phone': 'phone',
        'created': 'date',
    },
]


def get_form_list() -> List[Document]:
    return db.all()


if __name__ == '__main__':
    for form in forms_list:
        db.insert(form)
