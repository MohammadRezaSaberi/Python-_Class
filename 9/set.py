set1 = {"apple", "banana", "watermelon"}

set1.add("orange")

print(set1)

print('#' * 50)

set2 = {"apple", "banana", "watermelon"}
set3 = {"pineapple", "mango", "peach"}

set2.update(set3)

print(set2)

print('#' * 50)

set4 = {"apple", "banana", "watermelon"}

set4.remove("banana")

print(set4)

print('#' * 50)

set5 = {"apple", "banana", "watermelon"}

set5.discard("banana")

print(set5)