from testrail_api import TestRailAPI
import util.config as config


def push_results_to_testrail(result):
    api = TestRailAPI(config.host, config.user, config.api_key)
    run_id = config.run_id

    for item in result:
        suite = item['testcases']
        for case in suite:
            status = case['status']
            for test_id in case['test_case_ids']:
                if test_id is not None:
                    id_number = test_id.split('T')[1]
                    if status == 'PASS':
                        api.results.add_result(
                            test_id=int(id_number),
                            status_id=1,
                        )
                    elif status == 'FAIL':
                        api.results.add_result(
                            test_id=int(id_number),
                            status_id=5,
                        )
        print("Pushed results to TestRail >>" + item['suite_name'])

