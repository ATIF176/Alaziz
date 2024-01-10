# import json

# def readFile():
#     with open('read.txt', 'r') as f:
#         data = json.load(f)
#     print(type(data))

# readFile()

def readFile():
    with open('read.txt', 'r') as f:
        data = f.read()
    print(data)

readFile()
