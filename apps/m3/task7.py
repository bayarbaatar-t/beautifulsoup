import sys
from bs4 import BeautifulSoup, SoupReplacer, Tag

if len(sys.argv) != 2:
    print("Please include one HTML/XML file path as the argument.")
    exit(1)

# Adds/replaces class="test" attribute to all <p> tags
def add_test_class(tag: Tag):
    attrs = tag.attrs.copy()
    if tag.name == "p":
        attrs["class"] = "test"
    return attrs


with open(sys.argv[1], encoding="utf-8") as file:
    if sys.argv[1].split(".")[-1] == "html":
        soup = BeautifulSoup(file, "html.parser", replacer=SoupReplacer(attrs_xformer=add_test_class))
    elif sys.argv[1].split(".")[-1] == "xml":
        soup = BeautifulSoup(file, "xml", replacer=SoupReplacer(attrs_xformer=add_test_class))
    else:
        print("Please ensure the argument is a HTML/XML file path.")
        exit(1)

# Write to file
with open("task7_results", "w", encoding="utf-8") as file:
    file.write(soup.prettify())