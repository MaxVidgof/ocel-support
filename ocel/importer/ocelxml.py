from dateutil import parser as date_parser
from lxml import etree, objectify


def parse_xml(value, tag_str_lower):
    if "float" in tag_str_lower:
        return float(value)
    elif "date" in tag_str_lower:
        return date_parser.parse(value)
    return str(value)


def apply(input_path, parameters=None):
    if parameters is None:
        parameters = {}

    parser = etree.XMLParser(remove_comments=True)
    tree = objectify.parse(input_path, parser=parser)
    root = tree.getroot()

    obj = {}
    obj["ocel:events"] = {}
    obj["ocel:objects"] = {}

    for child in root:
        if child.tag.lower().endswith("events"):
            for event in child:
                eve = {}
                for child2 in event:
                    if child2.get("key") == "id":
                        eve["ocel:id"] = child2.get("value")
                    elif child2.get("key") == "timestamp":
                        eve["ocel:timestamp"] = date_parser.parse(child2.get("value"))
                    elif child2.get("key") == "activity":
                        eve["ocel:activity"] = child2.get("value")
                    elif child2.get("key") == "omap":
                        omap = []
                        for child3 in child2:
                            omap.append(child3.get("value"))
                        eve["ocel:omap"] = omap
                    elif child2.get("key") == "vmap":
                        eve["ocel:vmap"] = {}
                        for child3 in child2:
                            eve["ocel:vmap"][child3.get("key")] = parse_xml(child3.get("value"), child3.tag.lower())
                obj["ocel:events"][eve["ocel:id"]] = eve
                del eve["ocel:id"]
        elif child.tag.lower().endswith("objects"):
            for object in child:
                obj = {}
                for child2 in object:
                    if child2.get("key") == "id":
                        obj["ocel:id"] = child2.get("value")
                    elif child2.get("key") == "type":
                        obj["ocel:type"] = child2.get("value")
                    elif child2.get("key") == "ovmap":
                        obj["ocel:ovmap"] = {}
                        for child3 in child2:
                            obj["ocel:ovmap"][child3.get("key")] = parse_xml(child3.get("value"), child3.tag.lower())
                obj["ocel:objects"][obj["ocel:id"]] = obj
                del obj["ocel:id"]

    print(obj)

    return obj
