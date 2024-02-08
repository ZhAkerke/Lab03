#From the functions1
#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

#2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

#3
def solve(num_heads, num_legs):
    for num_chickens in range(num_heads + 1):
        num_rabbits = num_heads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == num_legs:
            return num_chickens, num_rabbits
    return "No solution found."

#4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

#5
from itertools import permutations

def string_permutations(string):
    perms = [''.join(p) for p in permutations(string)]
    return perms

#6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

#7
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

#8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 0

#9
def sphere_volume(radius):
    volume = (4/3) * 3.14159 * (radius**3)
    return volume

#10
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#11
def is_palindrome(word):
    return word == word[::-1]

#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

#13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    num_guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break

print(grams_to_ounces(100))
print(fahrenheit_to_celsius(32))
print(solve(35, 94))
print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(string_permutations('abc'))
print(reverse_words("We are ready"))
print(has_33([1, 3, 3]))
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(sphere_volume(5))
print(unique_elements([1, 2, 3, 3, 4, 4, 5]))
print(is_palindrome("madam"))
histogram([4, 9, 7])
guess_the_number()
