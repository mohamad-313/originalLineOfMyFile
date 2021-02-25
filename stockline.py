from sys import argv

def emptryLine(nameFile):
    f = open(nameFile,"r")
    lines = f.readlines()
    emptryLineCount = 0

    for i in lines:
        emptryLineCount += 1 if i.strip() == "" else 0

    print(f"Stock line number is {len(lines) - emptryLineCount}")

if len(argv) == 2:
    emptryLine(argv[2])
else:
    emptryLine(input("Name of file:\n"))
