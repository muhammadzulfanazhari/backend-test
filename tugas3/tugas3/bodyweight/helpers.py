import json

from jsonschema import validate
from django.http import HttpResponse

def format_response(message, status_code=200, values=[]):
    response = HttpResponse(
        json.dumps({
            'success': (str(status_code)[0] == "2"),  # when code is 2XX
            'message': message,
            'data': values,
        }),
        content_type='application/json',
        status=status_code
    )
    return response


def format_response_list_data(result):
    message = "List data"
    values = [
        {
            "tanggal": i.tanggal.strftime('%Y-%m-%d'),
            "min": i.bb_min,
            "max": i.bb_max,
            "perbedaan": i.bb_max - i.bb_min,
        } for i in result
    ]
    return format_response(message=message, values=values)


def validate_post(request):
    schema = {
        "type": "object",
        "properties": {
            "tanggal": {"type": "string"},
            "min": {"type": "number"},
            "max": {"type": "number"}
        },
        "required": ["tanggal", "min", "max"],
        "additionalProperties": False
    }
    validate(instance=request, schema=schema)


def validate_put(request):
    schema = {
        "type": "object",
        "properties": {
            "tanggal_lama": {"type": "string"},
            "tanggal_baru": {"type": "string"},
            "min_baru": {"type": "number"},
            "max_baru": {"type": "number"}
        },
        "required": ["tanggal_lama", "tanggal_baru"],
        "additionalProperties": False
    }
    validate(instance=request, schema=schema)


def validate_delete(request):
    schema = {
        "type": "object",
        "properties": {
            "tanggal": {"type": "string"}
        },
        "required": ["tanggal"],
        "additionalProperties": False
    }
    validate(instance=request, schema=schema)