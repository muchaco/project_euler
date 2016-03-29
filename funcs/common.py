import math


def sum_of_multiples(list_of_bases, max_number):
    my_set = set()
    for j in list_of_bases:
        my_set = my_set.union(set([i for i in xrange(max_number) if i % j == 0]))
    return sum(my_set)


def ith_fibonacci(i):
    nums = [1, 1]
    while len(nums) < i:
        nums.append(nums[-1]+nums[-2])
    return nums[i-1]


is_palindrome = lambda word: str(word) == str(word)[::-1]


def start_from(a, b, matrix):
    def atlo1(a, b, matrix):
        try:
            return matrix[a][b] * matrix[a+1][b-1] * matrix[a+2][b-2] * matrix[a+3][b-3]
        except IndexError:
            return 0

    def atlo2(a, b, matrix):
        try:
            return matrix[a][b] * matrix[a+1][b+1] * matrix[a+2][b+2] * matrix[a+3][b+3]
        except IndexError:
            return 0

    def lefele(a, b, matrix):
        try:
            return matrix[a][b] * matrix[a+1][b] * matrix[a+2][b] * matrix[a+3][b]
        except IndexError:
            return 0

    def oldal(a, b, matrix):
        try:
            return matrix[a][b] * matrix[a][b+1] * matrix[a][b+2] * matrix[a][b+3]
        except IndexError:
            return 0
    return max([oldal(a, b, matrix), atlo1(a, b, matrix), atlo2(a, b, matrix), lefele(a, b, matrix)])


def greatest_product_in(number, length):
    i = 0
    prods = []
    while i + length <= len(number):
        akt_num = number[i:i + length]
        prod = 1
        for j in akt_num:
            prod *= int(j)
        prods.append(prod)
        i += 1
    return max(prods)

sum_of_digits = lambda n, j = lambda k: k: sum([j(int(i)) for i in str(n)])


def write_down_number(number):
    numbers = ["null", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers_teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen"]
    numbers_10 = ["null", "teen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
                  "hundred"]
    str_num = str(number)
    if len(str_num) < 2:
        return numbers[number]
    if len(str_num) < 3:
        if str_num[0] == "1":
            if number < 19:
                return numbers_teen[number-10]
            return numbers[number-10] + numbers_10[int(str_num[0])]
        if str_num[1] == "0":
            return numbers_10[int(str_num[0])]
        return numbers_10[int(str_num[0])] + numbers[int(str_num[1])]
    if len(str_num) < 4:
        if int(str_num[1:]) == 0:
            return numbers[int(str_num[0])] + "hundred"
        return numbers[int(str_num[0])] + "hundredand" + write_down_number(int(str(number)[1:]))
    return "onethousand"


def ncr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def is_num_sum_of_two_in_list(n, lst, distinct_values=True):
    lst.sort()
    length = len(lst)
    if length < 2:
        return False
    i = 0
    j = length-1
    while j != i:
        actual_sum = lst[i] + lst[j]
        if actual_sum == n:
            return True
        elif actual_sum > n:
            j -= 1
        else:
            i += 1
    if not distinct_values:
        actual_sum = lst[i] + lst[j]
        if actual_sum == n:
            return True
    return False


def max_path_sum_in_triangle(file_name):
    with open(file_name) as f:
        adj = f.read().splitlines()
        adj = [[int(j) for j in i.split(" ")] + [0] for i in adj]
    # parse_triangle(input, adj)
    for i in xrange(1, len(adj)):
        for j in xrange(i+1):
            adj[i][j] += max(adj[i-1][j], adj[i-1][j-1])
    return max(adj[len(adj)-1])


def max_path_sum_in_matrix(file_name):
    with open(file_name) as f:
        adj = f.read().splitlines()
        adj = [[int(j) for j in i.split(",")] for i in adj]
        print(adj)
    # parse_matrix(input, adj)
    for i in xrange(1, len(adj)):
        for j in xrange(i+1):
            adj[i][j] += max(adj[i-1][j], adj[i-1][j-1])
    return max(adj[len(adj)-1])


factorial = lambda n: n * factorial(n-1) if n > 1 else n


def index_of(a, x):
    try:
        return a.index(x)
    except ValueError:
        return 0


def length_of_recurring_cycle(i):
    remainders = list([0])
    rem = 1
    while not index_of(remainders, rem):
        remainders.append(rem)
        rem = rem*10 % i
        if rem == 0:
            return 0
    return len(remainders)-index_of(remainders, rem)


def is_pandigital(a, b, include_null = False):
    _str = str(a)
    reference = default_pandigital(b, include_null)
    if len(_str) != len(reference):
        return False
    if set(_str) & set(reference) != set(reference):
        return False
    return True


def default_pandigital(n, include_null = False):
    if include_null:
        string = "0"
    else:
        string = ""
    for i in xrange(1, n+1):
        string += str(i)
    return string

strstr = lambda haystack, needle: False if haystack.upper().find(needle.upper()) < 0 else True


def permutations(head, tail=''):
    lst = []
    len_head = len(head)
    if len_head == 0:
        lst.append(tail)
    else:
        for i in xrange(len_head):
            lst += permutations(head[0:i] + head[i+1:], tail+head[i])
    return lst

#permutations = lambda x: [x[i]+j for i in xrange(len(x)) for j in permutations(x[:i]+x[i+1:])] if len(x) > 1 else x


def p43_permutations(head, tail=''):
    """
    problem 43 specific optimalization
    """
    lst = []
    _len = len(head)
    if _len == 0:
        lst.append(tail)
    if _len == 4:
        if int(head[1:4]) % 2 != 0:
            return lst
    elif _len == 5:
        if int(head[2:5]) % 3 != 0:
            return lst
    elif _len == 6:
        if int(head[3:6]) % 5 != 0:
            return lst
    elif _len == 7:
        if int(head[4:7]) % 7 != 0:
            return lst
    elif _len == 8:
        if int(head[5:8]) % 7 != 0:
            return lst
    elif _len == 9:
        if int(head[6:9]) % 11 != 0:
            return lst
    elif _len == 10:
        if int(head[7:10]) % 13 != 0:
            return lst
    elif _len == 11:
        if int(head[8:11]) % 17 != 0:
            return lst
    else:
        for i in range(len(head)):
            print("valami")
            lst += p43_permutations(head[0:i] + head[i+1:], tail+head[i])
    return lst


def circ_number(num):
    circulars = set()
    str_num = str(num)
    circulars.add(num)
    for i in xrange(len(str_num)):
        str_num = str_num[1:] + str_num[0]
        circulars.add(int(str_num))
    return circulars


def make_truncatable_list(num):
    tr_list = set([])
    str_num = str(num)
    for i in xrange(len(str_num)):
        tr_list.add(int(str_num[i:]))
        tr_list.add(int(str_num[:i+1]))
    return list(tr_list)


def num_x_tupli(number, tupli):
    product = ""
    for i in tupli:
        product += str(number * i)
    return int(product)

num_len = lambda n: int(math.log10(n))+1 if n != 0 else 1


def prod(lst):
    ret_val = 1
    for i in lst:
        ret_val *= i
    return ret_val


def word_value(word):
    alphabet = ["0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                "t", "u", "v", "w", "x", "y", "z"]
    return sum([alphabet.index(i.lower()) for i in word])


nth_triangle_num = lambda x: 0.5*x*(x-1)


def is_triangle_word(word):
    num = word_value(word)
    n = 1
    last_triangle_number = 0
    while last_triangle_number < num:
        last_triangle_number = int(nth_triangle_num(n))
        n += 1
    return last_triangle_number == num


# TODO: create module tests
def power_mod(a, b, modulus):
    pow_remainders = [a]
    bin_b = bin(b)[2:]
    len_b = len(bin_b)
    for i in xrange(1, len_b):
        pow_remainders.append((pow_remainders[i-1] ** 2) % modulus)
    prod = 1
    for i in xrange(len_b):
        if bin_b[i] == '1':
            prod *= (pow_remainders[len_b-i-1]) % modulus
    return prod % modulus


# TODO: create module tests
def varieties(a, b):
    for i in str(b):
        if i not in str(a):
            return False
    for i in str(a):
        if i not in str(b):
            return False
    return True


def is_geometric_seq(lst):
    _len = len(lst)
    if _len > 2:
        q = lst[1]/float(lst[0])
        for i in xrange(2, _len):
            if lst[i]/float(lst[i-1]) != q:
                return False
        return True
    else:
        return True

is_integer = lambda x: int(x) == x


if __name__ == "__main__":
    pass
