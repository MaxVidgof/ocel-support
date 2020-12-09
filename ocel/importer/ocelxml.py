from lxml import etree, objectify


def apply(input_path, parameters=None):
    if parameters is None:
        parameters = {}

    parser = etree.XMLParser(remove_comments=True)
    tree = objectify.parse(input_path, parser=parser)
    root = tree.getroot()
