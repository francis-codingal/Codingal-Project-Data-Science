books = ["Dune", "The Hobbit", "Foundation", "Neuromancer", "Stardust"]

print("Library Book List:", books)

print("\nTotal Books:", len(books))
print("First Book:", books[0])
print("Last Book:", books[-1])
print("First Three Books:", books[:3])

books.append("Hyperion")
print("\nAfter Adding a Book:", books)

books.remove("Foundation")
print("After Removing a Book:", books)

books.sort()
print("Books Sorted Alphabetically:", books)

books.reverse()
print("Books in Reverse Order:", books)

librarian = {
    "name": "Mr. Alan",
    "section": "Sci-Fi & Fantasy",
    "experience": 8
}

print("\nLibrarian Profile:", librarian)

print("Librarian Name:", librarian["name"])
print("Library Section:", librarian["section"])
print("Experience:", librarian.get("experience"))

librarian["experience"] = 9
print("Updated Experience:", librarian)

librarian["email"] = "alan@archive-library.com"
print("After Adding Email:", librarian)

librarian.pop("section")
print("After Removing Section:", librarian)

book_ids = [201, 202, 203, 204, 205]
book_names = ["The Hobbit", "Dune", "Stardust", "Neuromancer", "Hyperion"]

book_directory = dict(zip(book_ids, book_names))

print("\nBook Directory:", book_directory)

print("\n================================")
print("LIBRARY ORGANISER SUMMARY")
print("================================")
print("Available Books:", books)
print("Librarian Details:", librarian)
print("Book ID Directory:", book_directory)
print("================================")