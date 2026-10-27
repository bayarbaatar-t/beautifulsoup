# Milestone-2
## API Definitions — Milestone 1 & Milestone 2 Part 1

| API | Usage | File | Original Line |
|---|---|---|---|
| `BeautifulSoup()` | M1 Tasks 1–8; M2 Tasks 2–4 | [bs4/__init__.py](../../bs4/__init__.py) | 209 |
| `prettify()` | M1 Tasks 1, 5, 6, 7, 8 | [bs4/element.py](../../bs4/element.py) | 2601 |
| `find_all()` | M1 Tasks 2–8; M2 Tasks 2–4 | [bs4/element.py](../../bs4/element.py) | 2715 |
| `find_parent()` | M1 Task 5 | [bs4/element.py](../../bs4/element.py) | 992 |
| `new_tag()` | M1 Task 8 | [bs4/__init__.py](../../bs4/__init__.py) | 682 |
| `insert_before()` | M1 Task 8 | [bs4/element.py](../../bs4/element.py) | 689 |
| `SoupStrainer()` | M2 Tasks 2–4 | [bs4/filter.py](../../bs4/filter.py) | 345 |

### Additional API Attributes and Parameters

| Attribute / Parameter | Usage | File | Original Line |
|---|---|---|---|
| `Tag.string` | M1 Task 5 — read text | [bs4/element.py](../../bs4/element.py) | 1837 |
| `Tag.name` | M1 Task 6 — renamed tags | [bs4/element.py](../../bs4/element.py) | 1648 |
| `Tag.attrs` | M1 Task 7 — modified attributes | [bs4/element.py](../../bs4/element.py) | 1674 |
| `parse_only` | M2 Tasks 2–4 — selective parsing | [bs4/__init__.py](../../bs4/__init__.py) | 214 |

## SoupReplacer Implementation -- Part 3
### How to Use
1. `from bs4 import BeautifulSoup, SoupReplacer`
2. `BeautifulSoup(... , replacer=SoupReplacer("old_tag", "new_tag"))`  
    Now you have a parsed BeatifulSoup object where any old tag has been renamed to new tag.

### Integration
- My approach was to avoid touching the tag while it's being processed, to avoid messing with any start and end tag matching logic.
- Therefore I chose `popTag()` within `bs4/__init__.py`, because this is where tag processing is finished and get popped from its `tagStack`.
- The actual class is implemented within `bs4/filter.py`, right below `SoupStrainer`.

### Testing and Application
- Two automated tests have been added to `bs4/tests/test_replacer.py`
- Task 6's single-pass version was implemented using SoupReplacer. It can be found at `apps/m2/task6.py`.