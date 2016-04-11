# -*- coding: utf-8 -*-

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

import os

def number_letter_counts(n):
    dict_lett = build_dict(n)
    sum_letter = 0
    for item in dict_lett:
        sum_letter += dict_lett[item]
    return sum_letter 

def build_dict(n):
    lett_dict = {}
    numbers = (x for x in range(1, n+1))
    dec = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    ties = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    for number in numbers:
        if 1 <= number < 20:
            lett_dict[number] = len(dec[number-1])
        elif 20 <= number < 100:
            index_dec = number//10
            index_num = number%10 
            if index_num == 0:
                lett_dict[number] = len(ties[index_dec-2])
            else:
                lett_dict[number] =  len(ties[index_dec-2])  +  len(dec[index_num-1])
        elif 100 <= number < 1000:
            index_hun = number//100
            index_dec = number%100
            if index_dec == 0:
                lett_dict[number] = len(dec[index_hun-1]) + len('hundred')
            else:
                if 1 <= index_dec < 20:
                    lett_dict[number] = len(dec[index_hun-1]) + len('hundred') + len('and') +  len(dec[index_dec-1])
                elif  20 <= index_dec  < 100:
                    index_dec2 = index_dec//10
                    index_num = index_dec%10 
                    if index_num == 0:
                        lett_dict[number] = len(dec[index_hun-1]) + len('hundred') + len('and') +  len(ties[index_dec2-2])
                    else:
                        lett_dict[number] = len(dec[index_hun-1]) + len('hundred') + len('and') +  len(ties[index_dec2-2]) +  len(dec[index_num-1])
        elif number == 1000:
            lett_dict[number] = len('onethousand')
            
    return lett_dict
                  
def main():
    import time
    start = time.time() 
      
    assert(number_letter_counts(5) == 19)
    print(number_letter_counts(1000))
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

os.system("pause")