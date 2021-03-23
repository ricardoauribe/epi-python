# Spreadsheet encoding pp74
# Time complexity O(n), Space Complexity O(1)
import functools

# reduce takes every char and multiplies the total per 26 indicating the position in order of magnitude
# then it sum the actual value of the lettter by taking the ord(number) - ord(A) + 1 to set A = 1
def ss_decode_col_id(col: str) -> int:
    return functools.reduce(
        lambda result, current: result * 26 + ord(current) -ord('A') + 1, col, 0
    )

print(ss_decode_col_id("ZA"))