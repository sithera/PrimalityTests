import os
import time
from functools import wraps
import psutil


def print_statistics(function):
    """
    Checks how long does it take to execute function.
    :param function:
    :return:
    """
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.clock()

        result = function(*args, **kwargs)
        t1 = time.clock()

        tested_number = args[0]
        cpu_usage = str(psutil.Process(os.getpid()).cpu_percent())
        memory_usage = str(psutil.Process(os.getpid()).memory_info())
        module_name = function.__module__
        execution_time = str(t1-t0)

        log_row = "%s %s %s %s %s\n" % (str(tested_number), str(result),
                                      execution_time, cpu_usage, memory_usage)

        log_file_name = "./saved_logs/%s.log" % module_name

        with open(log_file_name, 'ab') as log:
            log.write(str.encode(log_row))

        return result
    return function_timer


