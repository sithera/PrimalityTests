import data_provider
import fermat
import os
import improved_miller_rabin
import frobenius
import solovay_strassen
from cpu_and_mem import CPUandMEM_Print

numbers = []
accuracy = 10000

def clean_logs(directory_path):
    for file_name in os.listdir(directory_path):
        os.remove(directory_path + os.sep + file_name)


def run_testing_function(function):
    for number in numbers:
        function(number)


def test_by_number(numbers):
    for number in numbers:
        # miller_rabin.is_probable_prime(number)
        # improved_miller_rabin.is_prime(number)
        fermat.is_probable_prime(number)
        # aks.is_prime(number)
        # solovay_strassen.is_probable_prime(number)


def run_fermat(numbers):
    print("Starting fermat")
    for number in numbers:
        fermat.is_probable_prime(number)


def run_miller_rabin(numbers):
    print("Starting miller rabin")
    for number in numbers:
        improved_miller_rabin.is_prime(number)


def run_frobenius(numbers):
    print("Starting frobenius")
    for number in numbers:
        frobenius.is_probable_prime(number)


def run_solovay_strassen(numbers):
    print("Starting solovay strassen")
    for number in numbers:
        solovay_strassen.is_probable_prime(number)


def run_all_tests(numbers):

    cpu_and_mem_getter = CPUandMEM_Print(os.getpid(), "logs/cpu_mem_fermat.log")
    cpu_and_mem_getter.start()
    run_fermat(numbers)
    cpu_and_mem_getter.stop()

    cpu_and_mem_getter = CPUandMEM_Print(os.getpid(), "logs/cpu_mem_miller_rabin.log")
    cpu_and_mem_getter.start()
    run_miller_rabin(numbers)
    cpu_and_mem_getter.stop()

    cpu_and_mem_getter = CPUandMEM_Print(os.getpid(), "logs/cpu_mem_solovay_strassen.log")
    cpu_and_mem_getter.start()
    run_solovay_strassen(numbers)
    cpu_and_mem_getter.stop()


if __name__ == "__main__":
    global numbers
    file_name = "./data/data_set.p"
    numbers = data_provider.get_random_numbers(file_name)
    run_all_tests(numbers)

    print("Finished!")

