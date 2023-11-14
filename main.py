from flask import Flask, jsonify, request

from database import get_form_list
from validaters import determine_field_type, validate_field

app = Flask(__name__)


def matching_form(form_data: dict):
    forms = get_form_list()
    for form in forms:
        form_fields = set(form.keys()) - {'form_name'}
        data_fields = set(form_data.keys())
        if form_fields.issubset(data_fields):
            matching_fields = all(
                validate_field(field_name=field, field_type=form[field],
                               value=form_data[field]) for field in form_fields)
            if matching_fields:
                return form['form_name']
    return None


@app.route('/get_form', methods=['POST'])
def get_form():
    form_name = matching_form(request.form)
    if form_name:
        return jsonify({'form_name': form_name})
    else:
        fields_type = {field: determine_field_type(field_name=field,
                                                   value=request.form[field]) for field in request.form}
        return jsonify(fields_type)


if __name__ == '__main__':
    app.run()
