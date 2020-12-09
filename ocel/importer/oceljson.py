import json


def apply(input_path, parameters=None):
    if parameters is None:
        parameters = {}
    log_obj = json.load(open(input_path, "rb"))
    return log_obj
