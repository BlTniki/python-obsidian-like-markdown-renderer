# markdown_strikethrough  

Extends the [Python Markdown](https://python-markdown.github.io/).  
Adds the possibility to use `~~something~~` to create a span that looks like `<s>something</s>` (~~something~~)

# How to cook
Clone in your project and them add to markdown:
```python
from path.to.markdown_strikethrough.markdown_strikethrough import MarkdownStrikethrough
import markdown

# ...

html = markdown.markdown(md_str, extensions=[MarkdownStrikethrough()])

# ...
```