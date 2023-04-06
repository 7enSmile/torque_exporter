from prometheus_client import start_http_server, Gauge

import torquepy
import json
import time
count_of_queue = Gauge('torque_count_of_queue', 'Description of gauge', ['name'])
count_of_task = Gauge('torque_count_of_tasks', 'Description of gauge', ['type'])
count_of_all_task = Gauge('torque_count_of_tasks_all', 'Description of gauge')
if __name__ == '__main__':
    start_http_server(8000)
    while True:
        count_of_all_task.set(torquepy.TorqueManager.get_count_of_all_tasks())
        count_of_task.labels("queued").set(torquepy.TorqueManager.get_count_of_que_tasks())
        count_of_task.labels("hold").set(torquepy.TorqueManager.get_count_of_hld_tasks())
        count_of_task.labels("run").set(torquepy.TorqueManager.get_count_of_run_tasks())
        count_of_task.labels("waiting").set(torquepy.TorqueManager.get_count_of_wat_tasks())
        count_of_task.labels("transiting").set(torquepy.TorqueManager.get_count_of_trn_tasks())
        count_of_task.labels("exit").set(torquepy.TorqueManager.get_count_of_ext_tasks())
        count_of_task.labels("complete").set(torquepy.TorqueManager.get_count_of_com_tasks())
        list_of_queue = torquepy.TorqueManager.get_list_of_queue()
        for queue in list_of_queue:
            count_of_queue.labels(queue["name"]).set(queue["tasks"])
        time.sleep(1)
