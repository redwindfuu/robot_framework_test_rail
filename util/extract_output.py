from util.xml_util import XmlUtil


def processing_output(path_to_output):
    """
    This function processes the output of the model and returns the result in a more readable format.
    :param output: output of the model
    :return: result in a more readable format
    """
    output_result = XmlUtil(path_to_output)

    # Get all test cases
    suites = output_result.get_elements_by_tag("suite/suite")
    result = []
    for suite in suites:
        test_cases = suite.findall(".//test")
        test_results = []
        for test_case in test_cases:
            test_obj = {"test_suite": suite.attrib["name"], "name": test_case.get("name"),
                        "status": test_case.find("status").get("status")}
            tags = test_case.findall("tag")
            for tag in tags:
                if tag.text.startswith("id="):
                    test_obj["test_case_id"] = tag.text.split("=")[1]
            test_results.append(test_obj)

        result.append({"testcases": test_results, "suite_name": suite.attrib["name"]})
    return result