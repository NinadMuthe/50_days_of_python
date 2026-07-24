# ======================== Python Data Types Examples ========================

# 1. NUMBERS
# =========

# Integer
print("===== INTEGERS =====")
integer_1 = 10
integer_2 = -5
integer_3 = 0
print(f"Integer 1: {integer_1}, Type: {type(integer_1)}")
print(f"Integer 2: {integer_2}, Type: {type(integer_2)}")
print(f"Integer 3: {integer_3}, Type: {type(integer_3)}")

# Float
print("\n===== FLOATS =====")
float_1 = 3.14
float_2 = -2.5
float_3 = 9.8
print(f"Float 1: {float_1}, Type: {type(float_1)}")
print(f"Float 2: {float_2}, Type: {type(float_2)}")
print(f"Float 3: {float_3}, Type: {type(float_3)}")

# Complex Numbers
print("\n===== COMPLEX NUMBERS =====")
complex_1 = 1 + 3j
complex_2 = 5 - 2j
complex_3 = 4j
print(f"Complex 1: {complex_1}, Type: {type(complex_1)}")
print(f"Complex 2: {complex_2}, Type: {type(complex_2)}")
print(f"Complex 3: {complex_3}, Type: {type(complex_3)}")
print(f"Real part of complex_1: {complex_1.real}, Imaginary part: {complex_1.imag}")

# 2. STRING
# =========
print("\n===== STRINGS =====")
string_1 = "Hello, Python!"
string_2 = 'Single quotes work too'
string_3 = """Multi-line string
can span multiple
lines"""
print(f"String 1: {string_1}, Type: {type(string_1)}")
print(f"String 2: {string_2}, Type: {type(string_2)}")
print(f"String 3: {string_3}, Type: {type(string_3)}")
print(f"Length of string_1: {len(string_1)}")
print(f"Uppercase: {string_1.upper()}")
print(f"Lowercase: {string_1.lower()}")

# 3. BOOLEAN
# ==========
print("\n===== BOOLEANS =====")
bool_1 = True
bool_2 = False
bool_3 = 10 > 5
bool_4 = 3 == 5
print(f"Boolean 1: {bool_1}, Type: {type(bool_1)}")
print(f"Boolean 2: {bool_2}, Type: {type(bool_2)}")
print(f"10 > 5: {bool_3}, Type: {type(bool_3)}")
print(f"3 == 5: {bool_4}, Type: {type(bool_4)}")

# 4. LIST
# =======
print("\n===== LISTS =====")
list_1 = [1, 2, 3, 4, 5]
list_2 = ['apple', 'banana', 'cherry']
list_3 = [1, 'mixed', 3.14, True, None]
list_4 = [[1, 2], [3, 4], [5, 6]]  # Nested list
print(f"List 1: {list_1}, Type: {type(list_1)}")
print(f"List 2: {list_2}, Type: {type(list_2)}")
print(f"Mixed List: {list_3}, Type: {type(list_3)}")
print(f"Nested List: {list_4}, Type: {type(list_4)}")
print(f"First element of list_1: {list_1[0]}")
print(f"Last element of list_1: {list_1[-1]}")
print(f"Slicing list_1 [1:4]: {list_1[1:4]}")
list_1.append(6)
print(f"After append(6): {list_1}")

# 5. TUPLE
# ========
print("\n===== TUPLES =====")
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = ('red', 'green', 'blue')
tuple_3 = (1, 'mixed', 3.14, True)
tuple_4 = ((1, 2), (3, 4), (5, 6))  # Nested tuple
single_element_tuple = (42,)  # Note the comma for single element
print(f"Tuple 1: {tuple_1}, Type: {type(tuple_1)}")
print(f"Tuple 2: {tuple_2}, Type: {type(tuple_2)}")
print(f"Mixed Tuple: {tuple_3}, Type: {type(tuple_3)}")
print(f"Nested Tuple: {tuple_4}, Type: {type(tuple_4)}")
print(f"Single element tuple: {single_element_tuple}, Type: {type(single_element_tuple)}")
print(f"First element of tuple_1: {tuple_1[0]}")
print(f"Slicing tuple_1 [1:4]: {tuple_1[1:4]}")

# 6. SET
# ======
print("\n===== SETS =====")
set_1 = {1, 2, 3, 4, 5}
set_2 = {'apple', 'banana', 'cherry'}
set_3 = {1, 2, 2, 3, 3, 3}  # Duplicates are removed
empty_set = set()  # Note: {} creates an empty dict, not a set
print(f"Set 1: {set_1}, Type: {type(set_1)}")
print(f"Set 2: {set_2}, Type: {type(set_2)}")
print(f"Set with duplicates {1, 2, 2, 3, 3, 3}: {set_3}")
print(f"Empty set: {empty_set}, Type: {type(empty_set)}")
print(f"Length of set_1: {len(set_1)}")
set_1.add(6)
print(f"After add(6): {set_1}")
set_1.remove(3)
print(f"After remove(3): {set_1}")
set_4 = {1, 2, 3}
set_5 = {3, 4, 5}
print(f"Union of {set_4} and {set_5}: {set_4.union(set_5)}")
print(f"Intersection of {set_4} and {set_5}: {set_4.intersection(set_5)}")

# 7. DICTIONARY
# ==============
print("\n===== DICTIONARIES =====")
dict_1 = {'name': 'Asabeneh', 'age': 30, 'country': 'Finland'}
dict_2 = {'fruit': 'apple', 'color': 'red', 'quantity': 5}
dict_3 = {'person': {'name': 'John', 'age': 25}, 'location': 'NYC'}  # Nested dict
empty_dict = {}
print(f"Dictionary 1: {dict_1}, Type: {type(dict_1)}")
print(f"Dictionary 2: {dict_2}, Type: {type(dict_2)}")
print(f"Nested Dictionary: {dict_3}, Type: {type(dict_3)}")
print(f"Empty dictionary: {empty_dict}, Type: {type(empty_dict)}")
print(f"Accessing dict_1['name']: {dict_1['name']}")
print(f"Accessing dict_1.get('age'): {dict_1.get('age')}")
print(f"Keys in dict_1: {dict_1.keys()}")
print(f"Values in dict_1: {dict_1.values()}")
print(f"Items in dict_1: {dict_1.items()}")
dict_1['city'] = 'Helsinki'
print(f"After adding city: {dict_1}")

# ======================== Type Checking Summary ========================
print("\n===== TYPE CHECKING SUMMARY =====")
print(f"type(10): {type(10)}")                              # <class 'int'>
print(f"type(3.14): {type(3.14)}")                          # <class 'float'>
print(f"type(1 + 3j): {type(1 + 3j)}")                      # <class 'complex'>
print(f"type('Asabeneh'): {type('Asabeneh')}")              # <class 'str'>
print(f"type([1, 2, 3]): {type([1, 2, 3])}")                # <class 'list'>
print(f"type((1, 2, 3)): {type((1, 2, 3))}")                # <class 'tuple'>
print(f"type({{1, 2, 3}}): {type({1, 2, 3})}")              # <class 'set'>
print(f"type({{'name': 'Asabeneh'}}): {type({'name': 'Asabeneh'})}")  # <class 'dict'>
print(f"type(True): {type(True)}")                          # <class 'bool'>