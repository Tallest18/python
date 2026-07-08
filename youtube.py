def print_string_characters(my_string: str) -> None:
    for i in range(len(my_string)):
        print(my_string[i])



print_string_characters("Hello, Word!")


def print_string_characters(word1: str, word2: str) -> None:
    for c in word1:
        print(c)
    for c in word2:
        print(c)



print_string_characters("Hello, Word!", "Good Job!")



def concatenate(s1: str, s2: str) -> str:
    s3 = s1 + s2
    if len(s3) > 10:
        return "Too long!"
    return s3

print(concatenate("Hello, ", "Word!"))
print(concatenate("He", "llo!"))


def get_substring(input_string: str, start: int, end: int) -> str:
    if end > len(input_string):
        return ""
    return input_string[start:end]

print(get_substring("Hello, Word!", 0, 5))
print(get_substring("Hello, Word!", 7, 12))
print(get_substring("Hello, Word!", 0, 12))

def first_n_characters(s: str, n: int) -> str:
    return s[:n]

def last_n_characters(s: str, n: int) -> str:
    index = len(s) - n
    return s[index:]


print(first_n_characters("Hello, Word!", 5))
print(first_n_characters("Hello, Word!", 20))
print(last_n_characters("Hello, Word!", 5))
print(last_n_characters("Hello, Word!", 20))

def reverse_string(input_string: str) -> str:
    return input_string[::-1]

print(reverse_string("Hello, Word!"))
print(reverse_string("Good"))

def remove_fourth_character(word: str) -> str:
  first_part = word[:3]
  second_part = word[4:]
  return first_part + second_part

print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Goods"))

def say_goodbye(name: str, hour: int) -> str:
    return f"Goodbye {name}, it's {hour} o'clock!"


print(say_goodbye("Alice", 10))
print(say_goodbye("Bob", 15))