import sys
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) != 2:
    print("Please include one HTML/XML file path as the argument.")
    exit(1)

# Find and parse only <a> tags
a_strainer = SoupStrainer("a")
with open(sys.argv[1], "r", encoding="utf-8") as file:
    if sys.argv[1].split(".")[-1] == "html":
        soup = BeautifulSoup(file, "html.parser", parse_only=a_strainer)
    elif sys.argv[1].split(".")[-1] == "xml":
        soup = BeautifulSoup(file, "xml", parse_only=a_strainer)
    else:
        print("Please ensure the argument is a HTML/XML file path.")
        exit(1)

# Find and print all <a> tags
for a in soup.find_all("a"):
    print(a)
    print()