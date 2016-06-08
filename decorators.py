import time
from functools import wraps
import psutil
import os

def print_statistics(function):
    """
    Decorator.
    Saves function statistics to logs.
    Logged statistics:
    - execution time
    - cpu usage
    - memory usage

    :param function:
    :return:
    """
    @wraps(function)
    def function_statistic_logger(*args, **kwargs):
        module_name = function.__module__
        tested_number = args[0]
        this_process = psutil.Process()

        this_process.cpu_percent()
        t0 = time.clock()
        memory_before = this_process.memory_info()
        result = function(*args, **kwargs)
        t1 = time.clock()
        memory_after = this_process.memory_info()
        cpu_percent = this_process.cpu_percent()

        values = {
            'number': str(tested_number),
            'execution_time': str(t1-t0),
            'cpu_usage': str(cpu_percent),
            'memory_rss': str(memory_after.rss - memory_before.rss),
            'memory_vms': str(memory_after.vms - memory_before.vms)
        }

        log_entry = "%(number)s %(execution_time)s %(cpu_usage)s  %(memory_rss)s %(memory_vms)s\n" % values

        log_file = "./logs/%s.log" % module_name

        with open(log_file, 'ab') as log:
            log.write(str.encode(log_entry))

        return result
    return function_statistic_logger


