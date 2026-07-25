list_1 = [
    # Given examples
    "abcabcbb",      # 3 ("abc")
    "bbbbb",         # 1 ("b")
    "pwwkew",        # 3 ("wke")

    # Edge cases
    "",              # 0 (empty string)
    "a",             # 1
    "aa",            # 1
    "ab",            # 2
    " ",             # 1 (single space)
    "  ",            # 1 (two spaces)

    # All unique
    "abcdef",        # 6
    "abcdefghijklmnopqrstuvwxyz",  # 26

    # Repeating at different positions
    "abba",          # 2 ("ab" or "ba")
    "dvdf",          # 3 ("vdf")
    "tmmzuxt",       # 5 ("mzuxt")
    "anviaj",        # 5 ("nviaj")
    "abcadef",       # 6 ("bcadef")

    # Repeat immediately after long unique section
    "abcdefga",      # 7 ("bcdefga")

    # Many repeated blocks
    "abababab",      # 2
    "abcabcabc",     # 3
    "abcdabcde",     # 5 ("abcde")

    # Numbers and symbols
    "123451234",     # 5
    "!@#$%^&*()",    # 10
    "a!b@c#d$",      # 8

    # Case sensitivity
    "AaBbCc",        # 6
    "AaAa",          # 2 ("Aa")

    # Long repeat at end
    "abcdefggggg",   # 7

    # Repeat at beginning
    "aabcdef",       # 6

    # Mixed tricky cases
    "ohomm",         # 3 ("hom")
    "ckilbkd",       # 5 ("kilbk")
]
list_2 = [3, 1, 3, 0, 1, 1, 2, 1, 1, 6, 26, 2, 3, 5, 5, 6, 7, 2, 3, 5, 5, 10, 8, 6, 2, 7, 6, 3, 5]

def check(i:int ,sub_int: int) -> bool:
    if sub_int == list_2[i]:
        return True    
    else:
        return False
    
def slide_win_dict(i: int, s: str) -> bool:
    n = len(s)
    max_len = 0
    see = {}
    
    l = 0
    
    for r in range(n):
        current_char = s[r]
        
        if current_char in see:
            l = max(l, see[current_char] + 1)
        
        see[current_char] = r
        
        win_len = r - l + 1
        
        max_len = max(win_len, max_len)
        
    retrun_bool = check(i, max_len)
        
    return retrun_bool

incorrect_count = 0
for i, j in enumerate(list_1):
    re = slide_win_dict(i, j)
    if re:
        val = "Correct"
    else :
        val = "Incorrect"
        incorrect_count += 1
    print(f"for ittration: {i+1} \nthe string was {j}\nand the fucntion was: {val}\n\n")
print(f"Total incorrect values : {incorrect_count}\n")