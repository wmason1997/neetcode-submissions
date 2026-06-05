from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    s1_list = [char for char in s1]
    s2_list = [char for char in s2]
    counter = Counter(s1_list)
    counter.update(s2_list)
    return counter

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
