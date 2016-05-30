import data_provider
import miller_rabin
import improved_miller_rabin
import fermat
import aks
import solovay_strassen
import cProfile
import os

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
        # fermat.is_probable_prime(number)
        # aks.is_prime(number)
        solovay_strassen.is_probable_prime(number)

if __name__ == "__main__":
    # data_provider.generate_and_pickle_random_numbers(40000)

    global numbers
    file_name = "./data/400_random_numbers_from_0_to_9223372036854775806.p"
    numbers = data_provider.get_random_numbers(file_name)
    command = "run_testing_function(%s)"

    # clean_logs("./logs")

    # for func_name in ["miller_rabin.is_probable_prime", "improved_miller_rabin.is_prime",
    #                   "fermat.is_probable_prime", "solovay_strassen.is_probable_prime",
    #                   "aks.is_prime"]:
    #
    #     cProfile.run(command % func_name)

    test_by_number(numbers)
    print("Finished!")

