import pickle
import sys
import random
import os


def generate_and_pickle_random_numbers(number_of_random_numbers, starting_num=0, ending_num=sys.maxsize-1):
    """

    Generates {number_of_random_numbers} numbers, in range ({starting_num}, {ending_num})
    Then it saves it in a pickle format.
    :param number_of_random_numbers: number of random numbers
    :param starting_num: all numbers will be bigger that this number
    :param ending_num: all numbers will be lower than this number
    :return:
    """
    try:

        numbers = random.sample(range(starting_num, ending_num), number_of_random_numbers)

    except ValueError:
        print("Sample size exceeded population size.")

    file_name = "./data/%s_random_numbers_from_%s_to_%s.p" % (number_of_random_numbers, starting_num, ending_num)

    pickle.dump(numbers, open(file_name, "wb+"))

    print("%s numbers saved to file %s" % (number_of_random_numbers, file_name))


def get_random_numbers(filename=None):
    """
    Loads random numbers from pickle file.
    If no file name is provided it chooses random file in data directory.
    :param filename:
    :return:
    """

    if filename is None:
        filename = "./data/" + random.choice(os.listdir("./data/"))

    print("Loading data from %s file" % filename)

    return pickle.load(open(filename, "rb"))
