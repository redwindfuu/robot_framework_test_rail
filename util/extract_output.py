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
            docs = test_case.findall("doc")
            list_testrail_id = []

            for doc in docs:
                list_testrail_id += get_testrail_id_from_docstring(doc.text)
            test_obj["test_case_ids"] = list_testrail_id
            test_results.append(test_obj)

        result.append({"testcases": test_results, "suite_name": suite.attrib["name"]})
    return result

def get_testrail_id_from_docstring(docstring):
    input_str = '''
            A DAG is a directed acyclic graph. It is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies. A DAG is defined in a Python script, which represents the DAGs structure (tasks and their dependencies) as code. The script is parsed by Airflow to generate the DAG object. The DAG object is then used by Airflow to schedule and execute the tasks.
            test case T1223 T2345 T3456
        '''
    process_str = docstring.split('\n')
    for i, line in enumerate(process_str):
        if line.strip().startswith('test cases'):
            return line.strip().split(' ')[2:]