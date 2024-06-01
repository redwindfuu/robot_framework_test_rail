from util.extract_output import *
from integrate_to_testrails import *

# Run main func
if __name__ == "__main__":
    '''
        Hàm processing_output(path_to_output) 
        sẽ lấy ra các phần tử test case từ file output.xml
        sau đó trả về một list các test case với các thông tin như sau:
        [
            {
                "testcases": [
                    {
                        "test_suite": "suite_name",
                        "name": "test_case_name",
                        "status": "status",
                        "test_case_id": "test_case_id"
                    },
                    ...
                ],
                "suite_name": "suite_name"
            },
            ...
        ]
    '''
    result = processing_output("output.xml")
    print(result)
    push_results_to_testrail(result)
    print(result)



