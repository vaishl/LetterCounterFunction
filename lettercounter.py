word=str(input("Please input the word for which you would like the number of letters counted"))


def char_frequency(str1):
    diction = {}
    for i in str1:
        key = diction.keys()
        if i in key:
            diction[i] += 1
        else:
            diction[i] = 1
    a_view = diction.items()
    a_view = tuple(a_view)
    return a_view
print(char_frequency(word))