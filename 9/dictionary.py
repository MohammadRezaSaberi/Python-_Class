dict1 = {
  "Name": "Mohammad Reza",
  "family": "Saberi",
  "Age": 19
}
dict1.update({"Age": 20})

print('#' * 50)

dict2 = {
  "Name": "Mohammad Reza",
  "family": "Saberi",
  "Age": 19
}
dict2.pop("family")
print(dict2)

print('#' * 50)

dict3 = {
  "Name": "Mohammad Reza",
  "family": "Saberi",
  "Age": 19
}
dict3.clear()
print(dict3)

print('#' * 50)

dict4 = {
  "Name": "Mohammad Reza",
  "family": "Saberi",
  "Age": 19
}
dict5 = dict4.copy()
print(dict5)

print('#' * 50)

dict6 = {
  "Name": "Mohammad Reza",
  "family": "Saberi",
  "Age": 19
}

x = dict6.get("family")

print(x)