#Q1
def computePower(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

x = 2
y = 3
print(computePower(x, y))


#Q2
def temperatureRange(readings):
    return (min(readings), max(readings))

readings = [15, 14, 17, 20, 23, 28, 20]
print(temperatureRange(readings))


#Q3
def isWeekend(day):
    return day in [6, 7]

day = 6
print(isWeekend(day))


#Q4
def fuel_efficiency(distance, fuel):
    return round(distance / fuel, 2)

distance = 70
fuel = 21.5
print(fuel_efficiency(distance, fuel))


#Q5
def decodeNumbers(n):
    last_digit = n % 10
    remaining = n // 10
    num_digits = 1
    temp = remaining
    
    while temp > 0:
        temp //= 10
        num_digits *= 10
    
    return last_digit * num_digits + remaining

n = 12345
print(decodeNumbers(n))


#Q6.1
def find_min_with_for_loop(nums):
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val

def find_max_with_for_loops(nums):
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))
print(find_max_with_for_loops(nums))


#6.2
def find_min_with_while_loop(nums):
    min_val = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < min_val:
            min_val = nums[i]
        i += 1
    return min_val

def find_max_with_while_loops(nums):
    max_val = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > max_val:
            max_val = nums[i]
        i += 1
    return max_val

print(find_min_with_while_loop(nums))
print(find_max_with_while_loops(nums))


#Q7
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha(): 
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return (vowel_count, consonant_count)

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))


#Q8
def digital_root(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10 
    return digit_sum

num = 2468
print(digital_root(num))