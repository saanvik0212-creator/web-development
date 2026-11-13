notes = [
    "IMPORTANT: Study for the Python quiz on Friday.\n",
    "Random doodle: buy some snacks later.\n",
    "TODO: Finish the smart-notes coding project.\n",
    "Junk line: testing 123.\n",
    "IMPORTANT: Review file handling methods.\n",
    "TODO: Submit the assignment before Nov 19.\n",
    "Old reminder: clean out my backpack.\n"
]

with open("class-notes.txt1", "w") as file:
    file.writelines(notes)


with open("class-notes.txt1", "r") as file:
    first_40 = file.read(40)
    print(first_40)
print()

with open("class-notes.txt1", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    for i in range(len(lines)):
        print(f"{i + 1}. ->{lines[i].strip()}")
print()


with open("class-notes.txt1", "r") as file:
    for line in file:
        clean_line = line.strip()
        if clean_line.startswith("IMPORTANT") or clean_line.startswith("TODO"):
            print(f"Kept: {clean_line}")
        else:
            print(f"Skipped: {clean_line}")
print()

with open("class-notes.txt1", "r") as infile, open("organized-notes.txt", "w") as outfile:
    for line in infile:
        if line.startswith("IMPORTANT") or line.startswith("TODO"):
            outfile.write(line)


with open("organized-notes.txt", "r") as new_file:
    for line in new_file:
        print(line.strip())