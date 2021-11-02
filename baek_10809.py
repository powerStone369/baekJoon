input = input()
start = ord("a")
end = ord("z")

for i in range(start,end+1):
    print(input.find(chr(i)))
        