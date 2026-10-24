import sys
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) != 2:
    print("Please include one HTML/XML file path as the argument.")
    exit(1)

# Find and parse all tags with an id attribute
id_strainer = SoupStrainer(id=True)
with open(sys.argv[1], "r", encoding="utf-8") as file:
    if sys.argv[1].split(".")[-1] == "html":
        soup = BeautifulSoup(file, "html.parser", parse_only=id_strainer)
    elif sys.argv[1].split(".")[-1] == "xml":
        soup = BeautifulSoup(file, "xml", parse_only=id_strainer)
    else:
        print("Please ensure the argument is a HTML/XML file path.")
        exit(1)

# Find and print all tags with an "id" attribute
for tag in soup.find_all(True, attrs={"id": True}):
    print(tag)
    print()
