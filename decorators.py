import time
from functools import wraps


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

        t0 = time.clock()

        result = function(*args, **kwargs)

        t1 = time.clock()
        values = {
            'number': str(tested_number),
            'execution_time': str(t1-t0),
            'result': result
        }

        log_entry = "%(number)s %(result)s %(execution_time)s\n" % values
        log_file = "./logs/%s.log" % module_name

        with open(log_file, 'ab') as log:
            log.write(str.encode(log_entry))

        return result
    return function_statistic_logger



