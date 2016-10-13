from itertools import groupby

my_list = input("Input: ")
my_list = my_list.replace(', ', '')
tail_tosses = max(len(list(v)) for k,v in groupby(my_list) if k=='T')
head_tosses = max(len(list(v)) for k,v in groupby(my_list) if k=='H')
if tail_tosses > head_tosses:
    print("T wins!")
elif head_tosses > tail_tosses:
    print("H wins!")
else:
    print("Draw")
