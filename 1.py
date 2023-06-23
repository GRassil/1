def palindrom_checking(some_string: str):
    some_string_len = len(some_string)//2 if len(some_string)%2==0 else len(some_string)//2+1
    for i in range(some_string_len):
        if some_string[i] != some_string[-i-1]:
            return some_string_len
    return some_string_len

if __name__ == '__main__':
    print(palindrom_checking('leppel'))
    print(palindrom_checking('lepel'))
    print(palindrom_checking('lepgnel'))