#
#
# Euler Problem 284
#
#



"""
A fun program to convert a number from any one base (from base 2 - binary
up to base 16 - hexadecimal)

User has to enter the following:
* a number to be converted
* the source base
* the target base

The program will validate that the number entered is valid for the source base
(for example, 123 is not valid for base 2 numbers). Assuming the number is valid,
the program will then convert the number from the source base to the target base,
via base 10 (decimal)

Example

100111 in base 2
- converts to 39 in decimal
- converts to 27 in hexadecimal

Legal mumbo-jumbo:
(c) Kevin Doiron 2007. All rights reserved. This program may be copied and/or
    re-used in whole or in part (although I can't imagine why anyone would),
    provided that this copyright notice remains intact and that proper
    accreditation is given to the author. No naked wombats were harmed in the
    development, testing or implementation of this program, although a couple of
    clothed ones got a little upset.
"""

import string

valid_digits = '0123456789ABCDEF'   # only up to base 16
valid_list = map(None,valid_digits)

def enter_num():

    quit_flag = False
    source_num = string.upper(raw_input('Enter number to convert: '))

    if source_num in ['X','Q','/']:
        quit_flag = True
    if source_num == '':
        quit_flag = True
        
    return quit_flag, source_num

def enter_base(base_type,source_num):
    quit_flag = False
    
    # base_type will either be 'starting' or 'ending'

    prompt_str = 'Enter the ' + base_type + ' base:'
    valid_input = False
    while not valid_input:
        input_base = int(raw_input(prompt_str))

        if input_base in ['X','Q','/']:
            valid_input = True
            return True, None
        if input_base not in range(2,17):   # valid bases are 2 to 16
            print 'not a valid base - press <CR>',
            dummy = raw_input()
            return True, None
            
        valid_input = True

        if base_type == 'starting':
            valid_chars = valid_list[0:input_base]
            for idx in source_num:
                if idx not in valid_chars:
                    valid_input = False
            if not valid_input:
                print source_num, 'is not valid for base ', input_base, 'press <CR>'
                dummy = raw_input()

            
    return quit_flag, input_base

def convert(input_val,source_base,target_base):
    # convert from the source base to the target base; work in decimal in between
    the_exp = 0
    dec_val = 0
    for idx1 in range(len(input_val)-1,-1,-1):
        dec_val += valid_list.index(input_val[idx1]) * (source_base**the_exp)
        the_exp += 1

    # now convert from decimal to the target base

    target_list = []
    cur_val = dec_val
    done = False
    while cur_val > 0:
        the_rem = cur_val % target_base
        target_list.append(valid_list[the_rem])
        cur_val /= target_base

    target_list.reverse()
    target_val = ''
    for the_char in target_list:
        target_val += the_char

    return dec_val, target_val

def main():
    quit_flag = False
    quit_flag, source_number = enter_num()
    if quit_flag == False:
        quit_flag, source_base = enter_base('starting',source_number)
        if quit_flag == False:
            quit_flag, target_base = enter_base('target',None)
            if quit_flag == False:
                decimal_val, target_num = convert(source_number,source_base,target_base)
                print source_number, 'in base', source_base
                print 'is', decimal_val, 'in decimal'
                print 'and is', target_num, 'in base', target_base

    return quit_flag

if __name__ == '__main__':
    do_again = True
    while do_again:  # will run at least once
        quit_flag = main()
        if not quit_flag:
            do_again = False
            again = raw_input('Do another? (Y/N)')
            if again in ['y','Y','yes','YES']:
                do_again = True
                print