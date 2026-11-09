# Milestone-3
## How to Use
1. ```
    from bs4 import BeautifulSoup, SoupReplacer
    ```
2. There are two different use cases:
    - Milestone-2: Changing every tag named `og-tag` into `alt-tag`.  
        ```
        BeautifulSoup(... , replacer=SoupReplacer("old_tag", "new_tag"))
        ```
    - Milestone-3: Doing some combination of transformations. Need to give __at least one function__ as an argument, which are:
        - `name_xformer: Callable[[Tag], str] | None`
        - `attrs_xformer: Callable[[Tag], _AttributeValues] | None`
        - `xformer: Callable[[Tag], None] | None`
        ```
        BeautifulSoup(... , replacer=SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name))
        ```
    __You cannot combine the two use cases. This will raise a ValueError.__

## Milestone 2 vs Milestone 3
Milestone 3 extends the existing ability to change the name of every tag with the matching name, by alternatively taking in up to three functions as arguments:
- `name_xformer`: Instead of only looking for `og-tag`, you can check for other conditions other than the tag name.
- `attrs_xformer`: Based on some condition, you can safely change class attributes.
- `xformer`: Based on some condition, you can tranform a tag in-place if you know what you're doing. 

This allows significantly more ways to operate on the soup object during the parsing process, such as in task 7: add/replace class:"test" attribute to all \<p> tags.

### Further Comparison
| Functionality | Milestone 2 | Milestone 3 |
|---|---|---|
| Changing `og-tag` to `alt-tag` | Present. | Present. Milestone 3 is backwards compatible. |
| Changing tag names based on other condition | - | Present. Custom function can have guards. |
| Changing tag attributes | - | Present. Can safely change class attributes based on custom guards. |
| In-place tag transformations | - | Present. Can do any transformation on the tag object, provided that the user is familiar with beautifulsoup.
| Simplicity of usage | Very simple, needs only two arguments. | Implementation is more complex, requiring argument validation. Usage is still simple (only calling the constructor), but now prone to user errors due to the custom transformation functions. |

### Conclusion
Because Milestone 3 is backwards compatible and fully supports the original functionality, programs that are designed for the Milestone 2 version will still behave the same when using the Milestone 3 version, meaning that it's a superset. Therefore, the still-minimal user-side complexity and the significantly increased range of use cases that Milestone 3 brings make this the clear winner.

## Design Choices
### Backwards Compatibility
This new version has not regressed, and will still provide identical results when used like the Milestone 2 version. 

### Constructor Argument Validation
A ValueError will be raised for all combinations of arguments except:
1. Only `og_tag` and `alt_tag` are supplied. Both must be supplied.
2. At least one of `name_xformer`, `attrs_xformer`, or `xformer` must be supplied.

### Order of Transformations
In use case #2, transformation functions will be executed on a tag, in the following order:
1. `name_xformer`, if provided.
2. `attrs_xformer`, if provided.
3. `xformer`, if provided. 

This is a common reason for any bugs, so keep it in mind.