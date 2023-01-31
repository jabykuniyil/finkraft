a = "jabir"
b = "jabiy"

output = ""
for i in zip(a, b):
    if len(set(i)) == 1:
        output += i[0]

print(output)