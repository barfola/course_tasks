# region task 1

def get_binary_representation_of_number(decimal_number, memory_size_in_bits):
    return bin(decimal_number)[2::].zfill(memory_size_in_bits)


def get_binary_number_after_not_operator(decimal_number, memory_size_in_bits):
    biggest_number_for_bits_amount = pow(2, memory_size_in_bits) - 1
    return get_binary_representation_of_number(biggest_number_for_bits_amount ^ decimal_number, memory_size_in_bits)


def twos_complement_method(decimal_number, memory_size_in_bits):
    binary_number_after_not_operator = get_binary_number_after_not_operator(decimal_number, memory_size_in_bits)

    convert_to_integer = int(binary_number_after_not_operator, 2)
    twos_complement = convert_to_integer + 1

    negative_representation_of_binary_number = get_binary_representation_of_number(twos_complement, memory_size_in_bits)
    print(negative_representation_of_binary_number)


# endregion task 1


