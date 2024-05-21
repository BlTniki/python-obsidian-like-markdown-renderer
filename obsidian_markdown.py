"""Facade for markdown.Markdown class.
Provides a Obsidian like configured markdown.Markdown class.

GitHub: https://github.com/BlTniki/python-obsidian-like-markdown-renderer
"""
from markdown import Markdown

from markdown_mark.markdown_mark import makeExtension as makeMarkdownMarkExtension
from markdown_obsidian_katex import makeExtension as makeObsidianKatexExtension
from markdown_strikethrough.markdown_strikethrough import makeExtension as makeStrikethroughExtension

default_extensions = [
    'fenced_code', 'tables', 'nl2br',
    makeMarkdownMarkExtension(),
    makeObsidianKatexExtension(),
    makeStrikethroughExtension()
]
default_extension_configs = {}

def ObsidianMarkdown(**kwargs):
    """
    Creates a new Markdown instance.
    Simply wraps markdown.Markdown providing kwargs directly to the underlying Markdown class.
    if extensions or extension_configs are not provided, they will be set to the default values.

    Keyword Arguments:
        extensions (list[Extension | str]): A list of extensions.

            If an item is an instance of a subclass of [`markdown.extensions.Extension`][],
            the instance will be used as-is. If an item is of type `str`, it is passed
            to [`build_extension`][markdown.Markdown.build_extension] with its corresponding
            `extension_configs` and the returned instance  of [`markdown.extensions.Extension`][]
            is used.
        extension_configs (dict[str, dict[str, Any]]): Configuration settings for extensions.
        output_format (str): Format of output. Supported formats are:

            * `xhtml`: Outputs XHTML style tags. Default.
            * `html`: Outputs HTML style tags.
        tab_length (int): Length of tabs in the source. Default: `4`

    """
    if "extensions" not in kwargs:
        kwargs["extensions"] = default_extensions
    if "extension_configs" not in kwargs:
        kwargs["extension_configs"] = default_extension_configs
    return Markdown(**kwargs)


if __name__ == "__main__":
    md_str = r"""
# Hi
i can ~~strikethrough~~
i can *katex* $\pi$
$$
\frac{1}{0}
$$
i can ==mark=="""
    md = ObsidianMarkdown()
    print(md.convert(md_str))