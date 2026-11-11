# file = open("bucket-list.txt", "w")
# file.write("1. Trip to japan\n")
# file.write("2. Fuji mountain\n")
# file.write("3. Austria\n")
# file.write("4. Sydney\n")
# file.close()
# print("Bucket list created")

# file = open("bucket-list.txt", "r")
# content = file.read()
# print("\n MY BUCKET LIST")
# print(content)
# file.close()

# file = open("bucket-list.txt", "r")
# lines = file.readlines()
# print(lines)
# print(len(lines))

file = open("bucket-list.txt", "a")
file.write("9. Hi my name is saanvi\n")

file = open("saanvi.html", "w")
file.write("<html>\n <title>File handling</title>\n <head>\n <body>\n <h1>My bucket list</h1> \n </body> \n </html> ")



