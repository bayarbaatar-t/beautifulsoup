from . import SoupTest
from bs4 import Tag, NavigableString, Doctype, Comment
from types import GeneratorType

class TestIterable(SoupTest):
    # ============================================== MILESTONE 4 TESTS ==============================================

    def test_empty_soup(self):
        soup = self.soup("")
        assert(list(soup) == [])

    def test_nested_tags_and_text(self):
        soup = self.soup("<div><p>A<b>B</b>C</p></div>")
        nodes = list(soup)

        assert([node.name if isinstance(node, Tag) else str(node) for node in nodes] == ["div", "p", "A", "b", "B", "C"])

    def test_special_nodes(self):
        soup = self.soup("<!DOCTYPE html><!--note--><p>Hi</p>")
        nodes = list(soup)

        assert([type(node) for node in nodes] == [Doctype, Comment, Tag, NavigableString])
        assert(str(nodes[0]) == "html")
        assert(str(nodes[1]) == "note")

    def test_independent_iterators(self):
        soup = self.soup("<div><p>Hello</p><b>World</b></div>")
        first = iter(soup)
        second = iter(soup)

        assert(isinstance(first, GeneratorType))
        assert(first is not second)

        assert(next(first) is soup.div)
        assert(next(first) is soup.p)
        assert(next(second) is soup.div)
        assert(next(first) is soup.p.string)

        # A new iterator should start from the beginning.
        assert(next(iter(soup)) is soup.div)

    def test_exhaustion_and_tag_iteration(self):
        soup = self.soup("<div><b>A</b><i>B</i></div>")
        iterator = iter(soup)

        for node in [soup.div, soup.b, soup.b.string, soup.i, soup.i.string]:
            assert(next(iterator) is node)

        try:
            next(iterator)
            assert(False)
        except StopIteration:
            assert(True)

        # Ordinary Tag iteration should remain unchanged.
        assert([node.name for node in soup.div] == ["b", "i"])
