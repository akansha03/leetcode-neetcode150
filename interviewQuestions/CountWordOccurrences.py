from collections import defaultdict
def count_occurrence(s):
    temp_str = s.split(" ")
    count = defaultdict(int)
    for temp in temp_str:
        count[temp] += 1

    for key, value in count.items():
        print(f'{key} : {value}')

name = "My name is Claude Claude"
count_occurrence(name)
