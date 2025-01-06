
# s1 = "abcd", s2 = "cdab"
def rotating_char(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

output = rotating_char("abcd","cdab")
print(output)
