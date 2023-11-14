from typing import List

from tinydb import TinyDB
from tinydb.table import Document

db = TinyDB('db.json')


def get_form_list() -> List[Document]:
    return db.all()
