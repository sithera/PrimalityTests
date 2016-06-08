import data_provider
import fermat
import os
import improved_miller_rabin
import frobenius
import solovay_strassen

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
    for number in numbers:
        fermat.is_probable_prime(number)


def run_miller_rabin(numbers):
    for number in numbers:
        improved_miller_rabin.is_prime(number)


def run_frobenius(numbers):
    for number in numbers:
        frobenius.is_probable_prime(number)


def run_solovay_strassen(numbers):
    for number in numbers:
        solovay_strassen.is_probable_prime(number)


def run_all_tests(numbers):
    run_fermat(numbers)
    run_miller_rabin(numbers)
    run_solovay_strassen(numbers)
    # run_frobenius(numbers)

if __name__ == "__main__":
    global numbers
    file_name = "./data/data_set.p"
    numbers = data_provider.get_random_numbers(file_name)
    command = "run_testing_function(%s)"

    # clean_logs("./logs")

    # for func_name in ["miller_rabin.is_probable_prime", "improved_miller_rabin.is_prime",
    #                   "fermat.is_probable_prime", "solovay_strassen.is_probable_prime",
    #                   "aks.is_prime"]:
    #
    #     cProfile.run(command % func_name)

    run_all_tests(numbers)
    print("Finished!")

