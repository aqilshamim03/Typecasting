# Complex typecasting example in Python

# 1. Implicit typecasting (Python does it automatically)
x = 10          # int
y = 3.5         # float
z = x + y       # int + float → float (automatic conversion)
print("1️⃣ Implicit Typecasting Result:", z, "| Type:", type(z))


# 2. Explicit typecasting: string to int
num_str = "250"
num_int = int(num_str)    # manually converting str → int
print("\n2️⃣ String to Int:", num_int, "| Type:", type(num_int))


# 3. Explicit typecasting: float to int
price = 99.99
price_int = int(price)    # truncates decimal part, doesn’t round
print("\n3️⃣ Float to Int:", price_int, "| Type:", type(price_int))


# 4. List → Set → Tuple conversion
data_list = [1, 2, 2, 3, 4, 4, 5]
data_set = set(data_list)       # removes duplicates
data_tuple = tuple(data_set)    # converts to tuple
print("\n4️⃣ List → Set → Tuple:", data_tuple, "| Type:", type(data_tuple))


# 5. Tuple → List → String conversion
data_tuple2 = ('A', 'q', 'i', 'l')
data_list2 = list(data_tuple2)
data_str = ''.join(data_list2)   # joins list elements into string
print("\n5️⃣ Tuple → List → String:", data_str, "| Type:", type(data_str))


# 6. String → List of words → Set (unique words)
sentence = "python typecasting is very very powerful"
word_list = sentence.split()     # splits by space → list of words
unique_words = set(word_list)    # removes duplicates
print("\n6️⃣ String → List → Set:", unique_words, "| Type:", type(unique_words))


# 7. Dictionary → Keys and Values as List
student = {'name': 'Aqil', 'age': 23, 'marks': 90}
keys_list = list(student.keys())
values_list = list(student.values())
print("\n7️⃣ Dict Keys:", keys_list, "| Dict Values:", values_list)


# 8. Mixing types in expressions
a = 5
b = 2.0
c = a / b    # int / float → float (automatic implicit typecasting)
print("\n8️⃣ Implicit Type Mixing Result:", c, "| Type:", type(c))


# 9. Converting list of numbers (str) → int and summing them
numbers = ["10", "20", "30", "40"]
int_numbers = [int(num) for num in numbers]   # str → int using list comprehension
total = sum(int_numbers)
print("\n9️⃣ List of str → int → sum:", total, "| Type:", type(total))


# 10. Nested conversions: int → str → list → set
num = 122333
step1 = str(num)       # int → str
step2 = list(step1)    # str → list of digits ['1','2','2','3','3','3']
step3 = set(step2)     # removes duplicates
print("\n🔟 Nested Conversion:", step3, "| Type:", type(step3))
