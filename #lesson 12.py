#lesson 12

#1

import threading
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def check_prime_in_range(start, end, result_list):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    result_list.extend(primes)

def threaded_prime_checker(start_range, end_range, num_threads):
    thread_list = []
    results = []
    result_lock = threading.Lock()
    result_per_thread = [[] for _ in range(num_threads)]

    range_size = (end_range - start_range) // num_threads

    for i in range(num_threads):
        thread_start = start_range + i * range_size
        thread_end = start_range + (i + 1) * range_size if i != num_threads - 1 else end_range
        thread = threading.Thread(target = check_prime_in_range, args=(thread_start, thread_end, result_per_thread[i]))
        thread.start()                    
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()

    for sublist in result_per_thread:
        results.extend(sublist)

    results.sort()
    print("prime numbers found: ")
    print(results)

if __name__ == "__main__":
    start = 1
    end = 100
    num_threads = 4
    threaded_prime_checker(start, end, num_threads)


#2

import threading
from collections import Counter
import os

def count_words(lines, result_list, index):
    word_count = Counter()
    for line in lines:
        words = line.strip().lower().split()
        word_count.update(words)
    result_list[index] = word_count

def threaded_word_count(filename, num_threads):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads =  []
    results = [None] * num_threads

    for i in range (num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else total_lines
        thread = threading.Thread(target= count_words, args = (lines[start, end], results, i ))
    for thread in threads:
        thread.join()

    final_result = Counter()
    for partial_result in results:
        final_result.update(partial_result)

    print("word counts: ")
    for word, count in final_result.most_common():
        print(f"{word}: {count}")

if __name__ == "__main__":
    filename = "lesson12.txt"
    num_threads = 4
    if os.path.exists(filename):
        threaded_word_count(filename, num_threads)
    else:
        print(f"file {filename} not found")