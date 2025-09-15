# Data Structures (List, Tuple, Set, Dict)

# 14. Remove duplicates from a list.
def remove_duplicate_list():
    my_list = [1, 2, 2, 3, 4, 4, 5]
    unique_list = list(set(my_list))
    print("List without duplicates:", unique_list)

# 15. Merge two dictionaries into one.
def merge_two_dict():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    merged_dict = {**dict1, **dict2}
    print("Merged dictionary:", merged_dict)

# 16. Count frequency of elements in a list using a dictionary.
def count_frequency():
    my_list = [1, 2, 2, 3, 3, 3, 4]
    frequency = {}
    for item in my_list:
        frequency[item] = frequency.get(item, 0) + 1
    print("Element frequencies:", frequency)

# 17. Write a program to sort a list of dictionaries by a key.
def sort_list_dict():
    students = [
        {'name': 'Alice', 'score': 88},
        {'name': 'Bob', 'score': 75},
        {'name': 'Charlie', 'score': 95}
    ]
    sorted_students = sorted(students, key=lambda x: x['score'])
    print("Sorted by score:")
    for student in sorted_students:
        print(student)

# 18. Perform set operations: union, intersection, difference.
def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference (set1 - set2):", set1 - set2)

