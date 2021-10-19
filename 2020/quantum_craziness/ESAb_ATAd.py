
testing = False


def test_print(string):
    """ prints a string to a separate output file """
    OUTPUT_FILENAME = 'output.txt'
    if testing:
        with open(OUTPUT_FILENAME, 'a') as output_file:
            print(string, file=output_file)


def complement(bit_list):
    """ returns the complement of an array """
    return [(1 - i) if isinstance(i, int) else '_' for i in bit_list]


def reverse(bit_list):
    """ reverses a list """
    return bit_list[::-1]


def get(pos):
    """ gets one bit from the database """

    global tries

    print(pos+1, flush=True)
    result = int(input())

    tries += 1

    return result


def get_two(i1, i2):
    """ gets two bits from the database """
    if tries > 0 and tries % 10 == 9:
        get(0)    # burn one so that the next two aren't interrupted by quantum fluctuation
    return get(i1), get(i2)


def what_happened(bits, match_index, unmatch_index):
    """ ascertains which of the four possibilities took place, then returns the updated bit array """

    # weird array, no matched bits (a kind of anti-palindrome)
    if match_index == -1:

        old_unmatch_bit = bits[unmatch_index]
        new_unmatch_bit = get(unmatch_index)

        if new_unmatch_bit == old_unmatch_bit:
            return bits                   # nada or both
        else:
            return complement(bits)       # complement or reverse

        # 0111..0001  OG
        # 1000..1110  comp
        # 1000..1110  rev
        # 0111..0001  both

    # palindrome array
    elif unmatch_index == -1:

        old_match_bit = bits[match_index]
        new_match_bit = get(match_index)

        if new_match_bit == old_match_bit:
            return bits                    # nada or reverse
        else:
            return complement(bits)        # complement or both

    # normal array
    else:

        old_match_bit = bits[match_index]
        old_unmatch_bit = bits[unmatch_index]
        new_match_bit, new_unmatch_bit = get_two(match_index, unmatch_index)

        if new_match_bit == old_match_bit:
            if new_unmatch_bit == old_unmatch_bit:
                return bits
            else:
                return reverse(bits)
        else:
            if new_unmatch_bit == old_unmatch_bit:
                return reverse(complement(bits))
            else:
                return complement(bits)


def get_arr(bit_count):
    """ returns a string representation of the mysterious array """

    bits = ['_' for _ in range(bit_count)]   # creates an empty array of bits
    match_index, unmatch_index = -1, -1

    while '_' in bits:

        test_print("".join([str(i) for i in bits]))

        if tries % 10 == 9:   # since we get two at a time, we have to burn one here
            get(0)
        if tries > 0 and tries % 10 == 0:   # possible quantum error - go see what happened
            bits = what_happened(bits, match_index, unmatch_index)
            test_print("".join([str(i) for i in bits]))

        # get two new bits
        i = bits.index('_')
        bits[i], bits[bit_count - (i + 1)] = get_two(i, bit_count - (i + 1))

        # hunting for special bits..
        if match_index == -1 and bits[i] == bits[bit_count - (i + 1)]:
            match_index = i
        if unmatch_index == -1 and bits[i] != bits[bit_count - (i + 1)]:
            unmatch_index = i

    return "".join([str(i) for i in bits])


t, b = [int(_) for _ in input().split()]

for _ in range(t):
    tries = 0
    arr = get_arr(b)
    print(arr, flush=True)

    correct = input()
