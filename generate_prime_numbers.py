import random
import fermat
import pickle

carmichael_numbers = []
numbers_to_pickle = []

with open('./data/carmichael16.txt') as carmichael:
    carmichael_numbers = carmichael.read().splitlines()

number_count = 100
multiple = 100
start_range = 2
end_range = 100
for package in range(1, 9):
    not_prime_count = 0
    print("Package: " + str(package))
    print("Range: " + str(start_range) + "-" + str(end_range))

    for number in range(number_count):
        while True:
            random_number = random.randint(start_range, end_range)
            if fermat.is_probable_prime(random_number) is True:
                if random_number not in carmichael_numbers:
                    numbers_to_pickle.append(random_number)
                    break

            elif not_prime_count < number_count:
                numbers_to_pickle.append(random_number)
                not_prime_count += 1

    start_range = end_range
    end_range *= multiple

pickle.dump(numbers_to_pickle, open("./data/data_set.p", "wb+"))


