from . import SoupTest
from bs4 import SoupReplacer
from bs4 import Tag

class TestReplace(SoupTest):
    # ============================================== MILESTONE 2 TESTS ==============================================
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

    # ============================================== MILESTONE 3 TESTS ==============================================
    def test_name_xformer(self):
        soup = self.soup("<div><b>Hello</b><p>World</p><b>Again</b></div>", replacer=SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name))
        assert(len(soup.find_all("b")) == 0)
        blockquote_tags = soup.find_all("blockquote")
        assert(len(blockquote_tags) == 2)
        assert(blockquote_tags[0].contents[0] == "Hello")
        assert(soup.find_all("p")[0].contents[0] == "World")
        assert(blockquote_tags[1].contents[0] == "Again")

    def test_attrs_xformer(self):
        def replace_p_attr(tag: Tag):
            attrs = tag.attrs.copy()
            if tag.name == "p":
                attrs["class"] = "test"
            return attrs

        soup = self.soup("<div id=\"outer\"><p class=\"old\" id=\"first\">Hello</p><p>World</p></div>", replacer=SoupReplacer(attrs_xformer=replace_p_attr))
        for tag in soup.find_all("p"):
            assert(tag.attrs["class"] == "test")

    def test_xformer(self):
        def remove_id_attr(tag: Tag):
            tag.attrs.pop("id", None)
        soup = self.soup("<div id=\"outer\"><p class=\"old\" id=\"first\">Hello</p><p>World</p></div>", replacer=SoupReplacer(xformer=remove_id_attr))
        assert("id" not in soup.find("p").attrs)

    def test_combined_xformer(self):
        def name_xformer(tag: Tag):
            return "blockquote" if tag.name == "b" else tag.name
        def attrs_xformer(tag: Tag):
            attrs = tag.attrs.copy()
            if tag.name == "blockquote":
                attrs["class"] = "test"
            return attrs
        def xformer(tag: Tag):
            if tag.name == "blockquote":
                tag.append("UPDATED")

        soup = self.soup("<div><b>Hello</b><p>World</p><blockquote>Again</blockquote></div>", replacer=SoupReplacer(name_xformer=name_xformer, attrs_xformer=attrs_xformer, xformer=xformer))
        assert(len(soup.find_all("blockquote")) == 2)
        assert(len(soup.find_all("b")) == 0)
        for tag in soup.find_all("blockquote"):
            assert(tag.attrs["class"] == "test")
            assert(tag.contents[-1] == "UPDATED")

    def test_nested_xform(self):
        soup = self.soup("<div><b><b>Nested</b></b></div>", replacer=SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name))
        assert(len(soup.find_all("blockquote")) == 2)
        assert(len(soup.find("blockquote").find_all("blockquote")) == 1)
        assert(soup.find("blockquote").find("blockquote").contents[0] == "Nested")

    def test_invalid_instantiation(self):
        try:
            soup = self.soup("", replacer=SoupReplacer("b", "blockquote", name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name))
        except ValueError:
            assert(True)
        else:
            assert(False)

        try:
            soup = self.soup("", replacer=SoupReplacer("b"))
        except ValueError:
            assert(True)
        else:
            assert(False)

        try:
            soup = self.soup("", replacer=SoupReplacer())
        except ValueError:
            assert(True)
        else:
            assert(False)
