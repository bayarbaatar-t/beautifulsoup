import sys
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) != 2:
    print("Please include one HTML/XML file path as the argument.")
    exit(1)

# Find and parse all tags
all_strainer = SoupStrainer(True)
with open(sys.argv[1], encoding="utf-8") as file:
    if sys.argv[1].split(".")[-1] == "html":
        soup = BeautifulSoup(file, "html.parser", parse_only=all_strainer)
    elif sys.argv[1].split(".")[-1] == "xml":
        soup = BeautifulSoup(file, "xml", parse_only=all_strainer)
    else:
        print("Please ensure the argument is a HTML/XML file path.")
        exit(1)

# Find and print all tags
for tag in soup.find_all(True):
    print(tag)
    print()
