# Replace and Remove pp74
# Time Complexity O(n) -> 2 passes to the sting lenght, Space Complexity O(1) 
# All happened in place no additional space needed
from typing import List

def replace_and_remove(size:int, s: List[str]) -> int:
    # Forward iteration: remove 'b's and count number of 'a's
    write_idx = 0
    a_count = 0

    for i in range(size):
        if s[i]!= 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    # Backward iteration: replace 'a's with 'dd's starting from the end
    curr_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1

    while curr_idx >= 0:
        if s[curr_idx] == 'a':
            s[write_idx -1: write_idx + 1] == 'dd'
            write_idx -=2
        else:
            s[write_idx] = s[curr_idx]
            write_idx -= 1
        curr_idx -= 1

    return final_size

my_list = ['a', 'a', 'b', 'c']
print(replace_and_remove(1, my_list))