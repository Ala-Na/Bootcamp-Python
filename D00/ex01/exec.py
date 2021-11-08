# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anadege <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 11:15:03 by anadege           #+#    #+#              #
#    Updated: 2021/11/08 11:42:42 by anadege          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def swap_cases(string):
    swapped_string = ""
    swapped_string += string.swapcase()
    return swapped_string

def swap_string(string):
    return string[::-1]

argc = len(sys.argv)
if argc < 2:
    sys.exit()
argc -= 1
string = ""
while (argc != 0):
    sub_string = sys.argv[argc]
    sub_string = swap_cases(sub_string)
    sub_string = swap_string(sub_string)
    argc -= 1
    if (argc != 0):
        sub_string += " "
    string += sub_string
print(string)
