""" Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3."""


def ls(inp):
    char_index = {}
    start = 0
    max_ln = 0

    for end in range(len(inp)):
        if inp[end] in char_index and char_index[inp[end]] >=start:
            start = char_index[inp[end]] + 1

        char_index[inp[end]] = end
        max_ln = max(max_ln, end - start + 1)

    return max_ln

s = "pwwkew"
print(ls(s))




