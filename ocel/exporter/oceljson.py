import json
import datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


def apply(log, output_path, parameters=None):
    if parameters is None:
        parameters = {}

    json.dump(log, open(output_path, "w"), indent=2, default=myconverter)
