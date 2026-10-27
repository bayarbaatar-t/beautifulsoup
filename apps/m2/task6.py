import sys
from bs4 import BeautifulSoup, SoupReplacer

if len(sys.argv) != 2:
    print("Please include one HTML/XML file path as the argument.")
    exit(1)

# Replace <b> with <blockquote> during parsing
with open(sys.argv[1], encoding="utf-8") as file:
    if sys.argv[1].split(".")[-1] == "html":
        soup = BeautifulSoup(file, "html.parser", replacer=SoupReplacer("b", "blockquote"))
    elif sys.argv[1].split(".")[-1] == "xml":
        soup = BeautifulSoup(file, "xml", replacer=SoupReplacer("b", "blockquote"))
    else:
        print("Please ensure the argument is a HTML/XML file path.")
        exit(1)

# Write to file
file_name = sys.argv[1].split("/")[-1]
with open("task6_blockquote_" + file_name, "w", encoding="utf-8") as file:
    file.write(soup.prettify())