#Challenge 4

def char_frequency(string):
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    #return dict
    print(dict)
char_frequency(('hello'))