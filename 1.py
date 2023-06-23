def palindrom_checking(some_string: str):
    for i in range(len(some_string)):
        if some_string[i] != some_string[-i-1]:
            return False
    return True

if __name__ == '__main__':
    print(palindrom_checking('лепсспел'))
    print(palindrom_checking('helloworld'))