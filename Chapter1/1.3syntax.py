a = 10
b = 5

if a > b:
    print("A is greater than B")
    print(a - b)
else:
    print("B is greater than or equal to A")
    print(b -a)

print("End")

def open_file(file_name):
    print("Reading File", file_name)
    with open(file_name) as f:
        return f.read()
        print("Ready")
