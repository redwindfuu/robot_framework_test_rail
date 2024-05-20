from testrail_api import TestRailAPI
import util.config as config


def push_results_to_testrail(result):
    api = TestRailAPI(config.host, config.user, config.api_key)
    run_id = config.run_id

    for item in result:
        suite = item['testcases']
        for case in suite:
            case_id = case['test_case_id']
            status = case['status']
            if case_id is not None:
                if status == 'PASS':
                    api.results.add_result_for_case(
                        run_id=int(run_id),
                        case_id=int(case_id),
                        status_id=1,
                    )
                elif status == 'FAIL':
                    api.results.add_result_for_case(
                        run_id=int(run_id),
                        case_id=int(case_id),
                        status_id=5,
                    )
        print("Pushed results to TestRail >>" + item['suite_name'])
