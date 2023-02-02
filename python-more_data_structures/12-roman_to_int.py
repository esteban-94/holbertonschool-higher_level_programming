#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_number = 0
    int_num_list = []
    for rom_num in roman_string:
        int_num_list.append(rom_dict.get(rom_num))
    int_num_list.append(0)
    for i in range(len(int_num_list) - 1):
        if int_num_list[i] >= int_num_list[i + 1]:
            int_number += int_num_list[i]
        else:
            int_number -= int_num_list[i]
    return int_number
