from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor

STRIKETHROUGH_RE = r'(~{2})(.*?)(~{2})'


class MarkdownStrikethrough(Extension):
    def extendMarkdown(self, md):
        del_proc = SimpleTagInlineProcessor(STRIKETHROUGH_RE, 's')
        md.inlinePatterns.register(del_proc, 'strikethrough', 200)


def makeExtension(**kwargs):
    return MarkdownStrikethrough(**kwargs)


if __name__ == '__main__':
    import doctest

    doctest.testfile('README.md')
