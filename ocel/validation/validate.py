from ocel.validation import oceljson, ocelxml


def apply(input_path, parameters=None):
    if ".json" in input_path:
        return oceljson.apply(input_path, parameters=parameters)
    else:
        return ocelxml.apply(input_path, parameters=parameters)
