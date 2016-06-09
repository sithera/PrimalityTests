import threading
import psutil


class CPUandMEM_Print(threading.Thread):

    def __init__(self, pid, log_file):
        threading.Thread.__init__(self)
        self.pid = pid
        self.log_file = log_file
        self.keep_running = True
        self.mem_readings = []
        self.cpu_readings = []

    def get_cpumem(self, pid):
        """
        Gets process memory and cpu usage values.
        :param pid:
        :return:
        """
        process = psutil.Process(pid)
        cpu_percent = psutil.cpu_percent()
        mem_percent = process.memory_percent()
        return (cpu_percent, mem_percent)

    def run(self):
        while self.keep_running:
            cpu_and_mem = self.get_cpumem(self.pid)
            self.mem_readings.append(cpu_and_mem[0])
            self.cpu_readings.append(cpu_and_mem[1])

            with open(self.log_file, 'ab') as log:
                log_entry = "%.2f\t%.2f\n" % (cpu_and_mem)
                log.write(str.encode(log_entry))

    def stop(self):
        self.keep_running = False
        mean_cpu = sum(self.cpu_readings) / float(len(self.cpu_readings))
        mean_mem = sum(self.mem_readings) / float(len(self.mem_readings))
        with open(self.log_file, 'ab') as log:
            log_entry = "%.2f\t%.2f\n" % (mean_cpu, mean_mem)
            # log.write(str.encode(log_entry))