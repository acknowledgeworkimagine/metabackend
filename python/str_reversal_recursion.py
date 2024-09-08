def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0] #String is reversed from the front skipping the first character in every loop
                                                #then first characther skipped is appending to the reversed string
str = "reversal"
reverse = string_reverse(str)
print(reverse)