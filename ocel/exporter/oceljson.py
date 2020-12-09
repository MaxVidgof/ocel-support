import json


def apply(log, output_path, parameters=None):
    if parameters is None:
        parameters = {}

    json.dump(log, open(output_path, "w"), indent=2)
