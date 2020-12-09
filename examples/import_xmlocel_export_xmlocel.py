import ocel


def execute_script():
    print("validated input", ocel.validate("../logs/minimal.xmlocel", "../schemas/schema.xml"))
    log = ocel.import_log("../logs/minimal.xmlocel")
    ocel.export_log(log, "log1.xmlocel")
    print("validated output", ocel.validate("log1.xmlocel", "../schemas/schema.xml"))


if __name__ == "__main__":
    execute_script()
