import pytest
import os
from collections import defaultdict

from requests.exceptions import ConnectTimeout
from testrail_api import TestRailAPI


class Testrail:
    client = None
    path_log = os.path.abspath(os.path.dirname(__file__)) + '/logs/'

    @classmethod
    def logging_start(cls):
        self = cls()
        self.connect_testrail()
        project_id = self.get_project_id()
        pytest.run_id = self.get_run_id(project_id)

    def connect_testrail(self):
        try:
            self.client = TestRailAPI('http://testrail.rambler-co.ru/', 'n.permyakov', os.environ['IOS_HOST_PASSWORD'])
        except ConnectTimeout as error:
            print('[ERROR] Connection timeout', error)
        return None

    def get_project_id(self):
        try:
            projects = self.client.projects.get_projects()
            for p in projects:
                if p['name'] == 'Касса (Mobile)':
                    return p['id']
        except ConnectTimeout as error:
            print('[ERROR] Connection timeout', error)
        return None

    def get_run_id(self, project_id):
        try:
            runs = self.client.runs.get_runs(project_id)
            for r in runs:
                if r['name'] == 'Касса X iOs (regress)':
                    return r['id']
        except ConnectTimeout as error:
            print('[ERROR] Connection timeout', error)
        return None

    @classmethod
    def logging_case(cls, case_id):
        self = cls()
        self._clear_result_step()
        pytest.case_id = case_id[1:] if case_id.startswith('C') else case_id

    def _clear_result_step(self):
        with open(self.path_log + 'testrail.log', 'r+') as file:
            file.truncate(0)

    @classmethod
    def logging_step(cls, outcome, nodeid, duration):
        self = cls()
        self.connect_testrail()
        duration = str(round(duration, 2))
        self._write_result_step(outcome=outcome, comment=nodeid, duration=duration)

    def _write_result_step(self, outcome: str, comment: str, duration: str):
        with open(self.path_log + 'testrail.log', 'a', encoding='utf-8') as file:
            file.write(outcome + ',' + comment + ',' + duration + '\n')

    @classmethod
    def logging_result(cls):
        self = cls()
        self.connect_testrail()
        statuses_step = defaultdict(int)
        comment = 'status    | time    | action\n'
        sum_duration = 0
        for outcome, nodeid, duration in self._read_result_step():
            if outcome != 'passed':
                statuses_step[outcome] += 1
            comment += outcome + '   ' + duration + '  ' + nodeid + '\n'
            sum_duration += float(duration)
        actual_status_id = '1'
        if bool(statuses_step):
            actual_outcome = max(statuses_step, key=statuses_step.get)
            if actual_outcome == 'failed':
                actual_status_id = '5'
        elapsed = self._convert_duration_elapsed(sum_duration)
        self.client.results.add_result_for_case(run_id=pytest.run_id, case_id=pytest.case_id, status_id=actual_status_id, comment=comment, elapsed=elapsed, assignedto_id=187)
        self._clear_result_step()

    def _read_result_step(self):
        with open(self.path_log + 'testrail.log', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                yield line.split(',')

    @staticmethod
    def _convert_duration_elapsed(timeout):
        div_timeout = timeout // 60
        mod_timeout = int(timeout) % 60
        if div_timeout:
            return str(div_timeout) + 'm ' + str(mod_timeout) + 's'
        else:
            return str(int(mod_timeout) + 1) + 's'




