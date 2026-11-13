# file=open("class-notes.txt","w")
# file.write("This is the first line\n")
# file.write("i am a student\n")
# file.close()

# n = int(input("how many characters:"))
# file = open("class-notes.txt","r")
# print(file.read(n))
# file.close()
# print()

# file = open("class-notes.txt","r")
# lines = file.readlines()
# file.close()
# print("total lines:", len(lines))
# for i in range(len(lines)):
#     print(i + 1, "->", lines[i].strip())
# print()

# word = input("Enter the word:")
# file = open("class-notes.txt","r")
# for line in file:
#     if line.startswith(word):
#         print("skip ->", line.strip())
#     else:
#         print("keep ->", line.strip())
# file.close()
# print()

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
out = open("odd-lines.txt","w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd lines saved to odd-lines.txt")


