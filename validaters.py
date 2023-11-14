import datetime


def validate_phone(phone: str) -> True | False:
    '''Проверка соответствия номера формату +7 xxx xxx xx xx'''
    return phone.startswith('+7') and len(phone) == 12 and phone[1:].isdigit()


def validate_date(date: str) -> True | False:
    '''Проверка даты соответствию формату DD.MM.YYYY или YYYY-MM-DD.'''
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False


def validate_email(email: str) -> True | False:
    '''Проверка email на корректность'''
    return '@' in email and '.' in email


def validate_field(field_name: str, field_type: str, value) -> True | False:
    '''Валидация поля'''
    if field_type == 'phone':
        return validate_phone(value)
    elif field_type == 'date':
        return validate_date(value)
    elif field_type == 'email':
        return validate_email(value)
    return True  # Всегда считаем текстовые поля валидными


def determine_field_type(field_name: str, value: str) -> str:
    '''Определяет тип поля на основе его значения'''
    if validate_date(value):
        return 'date'
    elif validate_phone(value):
        return 'phone'
    elif validate_email(value):
        return 'email'
    return 'text'
