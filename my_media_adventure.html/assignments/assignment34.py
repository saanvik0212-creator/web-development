books = ["Mindset", "Percy Jackson&the Olympics", "Deep Work", "The Alchemist", "Atomic Habits"]

print("Library Book List:", books)

print("Total Books:", len(books))
print("First Book:", books[0])
print("Last Book:", books[-1])
print("First Three Books:", books[:3])

books.append("Harry Potter")
print("After Adding a Book:", books)

books.remove("Deep Work")
print("After Removing a Book:", books)

books.sort()
print("Books Sorted Alphabetically:", books)

books.reverse()
print("Books in Reverse Order:", books)

librarian = {
    "name": "Ms. Soumya",
    "section": "Student's books",
    "experience": 6
}

print("Librarian Profile:", librarian)


print("Librarian Name:", librarian["name"])
print("Library Section:", librarian["section"])
print("Experience:", librarian.get("experience"))

librarian["experience"] = 6
print("Updated Experience:", librarian)

librarian["email"] = "soumya@schoollibrary.com"
print("After Adding Email:", librarian)

librarian.pop("section")
print("After Removing Section:", librarian)

book_ids = [171, 172, 173, 174, 175]
book_names = ["Dragon Keepers Series", "Percy Jackson & the Olympians", "Harry Potter", "Fablehaven", "Diary of a Wimpy Kid"]

book_directory = dict(zip(book_ids, book_names))

print("Book Directory:", book_directory)

print("================================")
print("LIBRARY ORGANISER SUMMARY")
print("================================")
print("Available Books:", books)
print("Librarian Details:", librarian)
print("Book ID Directory:", book_directory)
print("================================")

