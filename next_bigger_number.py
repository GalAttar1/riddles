# next bigger number
# refers to maya's blog https://algoritmim.co.il/interview-practice/next-bigger-number/

def next_bigger_number(num):
    digits = count_digits(num)
    # stop condition
    if digits == 3 and int(num/10) % 10 == 0:  # the second digit is 0
        new_3num = (int(num / 100)) * 100 + (int(num % 10)) * 10
        return new_3num
    elif digits == 1:
        return -1
    elif digits == 2:
        new_number = int((num % 10) * 10 + int(num / 10))
        print("new_number=", new_number)
        if new_number - num > 0:
            return new_number
        else:
            return -1
    #
    temp = 10 ** (digits - 1)
    first_digit = int(num / temp)
    result = is_firstDigit_maxOmin(num, digits)
    num_without_first = num - (10 ** (digits - 1)) * first_digit
    if result == -1:
        print("is first Digit max o min: min")
        rec_next = next_bigger_number(num_without_first)
        if rec_next == -1:
            x = num % 10
            res = (x * (10 ** (digits - 1))) + int(num / 10)
        else:
            res = (first_digit * (10 ** (digits - 1)) + rec_next)
        return res
    elif result == 0:
        print("is first Digit max o min: middle")
    else:
        print("is first Digit max o min: max")
        rec_next = next_bigger_number(num_without_first)
        print
        if rec_next == -1:
            return -1
        else:
            res = (first_digit * (10 ** (digits - 1)) + rec_next)
            return res
    return -1

def count_digits(num):
    counter = 0
    while num != 0:
        counter = counter + 1
        num = int(num / 10)
    return counter


def is_firstDigit_maxOmin(num, num_of_digits):
    first_digit = int(num / (10 ** (num_of_digits - 1)))
    greater = smaller = True
    while num >= 10:
        x = num % 10
        num = int(num / 10)
        if smaller and first_digit >= x:
            smaller = False
        elif greater and first_digit <= x:
            greater = False
    if greater:
        return 1
    elif smaller:
        return -1
    return 0


# not helpful
def max_min_digits(num):
    maxi = mini = num % 10
    while num != 0:
        num = int(num / 10)
        x = num % 10
        if x > maxi:
            maxi = x
        elif x < mini:
            mini = x


# test, main
num = 80431
print(num, " -->", next_bigger_number(num))
