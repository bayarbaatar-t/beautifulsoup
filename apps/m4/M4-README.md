# Milestone-4
## How to Use
1. 
    ```
    from bs4 import BeautifulSoup
    ```
2. 
    ```
    for node in BeatifulSoup(...):
        ...
    ```

## What Changed
- Can now iterate directly over a `BeautifulSoup` object. It is lazy, and returns pointers instead of copies, so memory usage is O(1). 
- Result can be any `PageElement` instead of only `Tag`.
- No regression detected.

## Implementation Notes
- BeautifulSoup is a mature library, so I started looking for already written logic to reuse.
- As a result, I found out that `Tag`, which BeautifulSoup extends, already has an `__iter__()` implementation. However, this was only returning the list of direct child nodes, not lazily. 
- Upon further investigation of the `Tag` class, I found a property called `descendants`, which is already a generator of all descendants in pre-order DFS style. (Although the docstring says BFS, the code is DFS)
- Therefore, BeautifulSoup now overrides Tag's __iter\__() method to return its `descendants` generator.