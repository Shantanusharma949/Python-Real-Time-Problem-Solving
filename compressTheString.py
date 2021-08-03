import itertools
str = input()
for key, group in itertools.groupby(str):
    print("({}, {})".format(len(list(group)), key), end=" ")
