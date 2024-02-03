from itertools import permutations
import random

def gram_to_ounches(grams):
    return 28.3495231 * grams

def far_to_cel(farenheit):
    return (farenheit - 32) * 5 / 9

def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) / 2
    x = numheads - y
    return (int(x), int(y))

def filter_prime(a):
    return [num for num in a if sum([1 for i in range(1, num + 1) if num % i == 0]) == 2]

def prmts(s):
    return [''.join(p) for p in permutations(s)]

def reverse(s):
    sentence = list(map(str, s.split()))
    sentence.reverse()
    return sentence

def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] == 3:
            return True
    return False

def spy_game(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            if nums[i:] == [0] * (len(nums) - i):
                return False
            if 7 not in nums[i+1:]:
                return False
            break
    return True


def sphere_volume(radius):
    return 4/3 * 3.14 * radius**3 

def unique(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b

def is_palindrome(s):
    s1 = s[::-1]
    return (s == s1)

def histogram(a):
    for x in a: print('*' * x)

def game():
    num = random.randint(1, 20)
    name = input("Hello! What is you name?")
    count = 0
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    while True:
        input_guess = int(input("Take a guess. "))
        print()
        count += 1
        if input_guess < num: print("Your guess is too low.")
        if input_guess > num: print("Your guess is too high.")
        if input_guess == num:
            print(f'Good job, {name}! You guessed my number in {count} guesses!')
            break
