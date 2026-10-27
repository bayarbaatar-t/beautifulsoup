from . import SoupTest
from bs4 import SoupReplacer

class TestReplace(SoupTest):
    def test_nested_tags(self):
        soup = self.soup("<div><b><b><p><span>Hello</span></p></b></b></div>", replacer=SoupReplacer("b", "blockquote"))
        assert(len(soup.find_all("b")) == 0)
        assert(len(soup.find_all("blockquote")) == 2)
        assert(len(soup.find_all("blockquote")[0].find_all("blockquote")) == 1)
        assert(str(soup.find_all("blockquote")[0].contents[0]) == "<blockquote><p><span>Hello</span></p></blockquote>")

    def test_mixed_tags(self):
        soup = self.soup("<div><b>Hi</b><b><blockquote><p><span>Hello</span></p></blockquote></b></div>", replacer=SoupReplacer("b", "blockquote"))
        assert(len(soup.find_all("b")) == 0)
        assert(len(soup.find_all("blockquote")) == 3)
        assert(len(soup.find_all("blockquote")[0].find_all("blockquote")) == 0)
        assert(len(soup.find_all("blockquote")[1].find_all("blockquote")) == 1)
        assert(soup.find_all("blockquote")[0].contents[0] == "Hi")
        assert(str(soup.find_all("blockquote")[1].contents[0]) == "<blockquote><p><span>Hello</span></p></blockquote>")
