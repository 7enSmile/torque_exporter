import subprocess
import json


class TorqueManager:

    @staticmethod
    def _count_of_tasks(number):
        result = subprocess.run(['qstat', '-B'], capture_output=True)
        result_list = list(filter(lambda x: x != "", result.stdout.decode().split('\n')[2].split(" ")))
        return int(result_list[number])

    @staticmethod
    def get_count_of_all_tasks():
        return TorqueManager._count_of_tasks(2)

    @staticmethod
    def get_count_of_que_tasks():
        return TorqueManager._count_of_tasks(3)

    @staticmethod
    def get_count_of_run_tasks():
        return TorqueManager._count_of_tasks(4)

    @staticmethod
    def get_count_of_hld_tasks():
        return TorqueManager._count_of_tasks(5)

    @staticmethod
    def get_count_of_wat_tasks():
        return TorqueManager._count_of_tasks(6)

    @staticmethod
    def get_count_of_trn_tasks():
        return TorqueManager._count_of_tasks(7)

    @staticmethod
    def get_count_of_ext_tasks():
        return TorqueManager._count_of_tasks(8)

    @staticmethod
    def get_count_of_com_tasks():
        return TorqueManager._count_of_tasks(9)

    @staticmethod
    def get_list_of_queue():
        result = subprocess.run(['qstat', '-Q'], capture_output=True)
        result_list = result.stdout.decode().split('\n')
        queue_list_json = []
        for i in range(2, len(result_list) - 1):
            queue_list = list(filter(lambda x: x != "", result_list[i].split(' ')))
            queue_json = {"name": queue_list[0], "tasks": queue_list[2]}
            queue_list_json.append(queue_json)
        return queue_list_json

    @staticmethod
    def get_list_of_user():
        list_name_user_json = []
        list_name_user = []
        result = subprocess.run(['qstat', '-a'], capture_output=True)
        result_list = result.stdout.decode().split('\n')
        if len(result_list) < 6:
            return list_name_user_json
        for i in range(5, len(result_list) - 1):
            list_name_user.append(list(filter(lambda x: x != "", result_list[i].split(" ")))[1])
        list_name_user = list(set(list_name_user))
        for user in list_name_user:
            param = '-u ' + user
            result = subprocess.run(['qstat', '-u {}'.format(user)], capture_output=True)
            result_list = result.stdout.decode().split('\n')
            user_json = {"name": user, "tasks": len(result_list) - 6}
            list_name_user_json.append(user_json)
        return list_name_user_json




