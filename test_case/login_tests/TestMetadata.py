from robot.libraries.BuiltIn import BuiltIn


def get_test_metadata(name):
    tags = BuiltIn().get_variable_value('${TEST TAGS}')
    prefix = name.lower() + '='
    for tag in tags:
        if tag.lower().startswith(prefix):
            return tag[len(prefix):]
    raise ValueError("Metadata '%s' not found!" % name)
