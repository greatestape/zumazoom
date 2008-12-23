import markdown
from pg_md_processor import CodeBlockPreprocessor

class PygmentsExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.textPreprocessors.insert(0, CodeBlockPreprocessor())

def makeExtension(configs=None):
    return PygmentsExtension(configs=configs)
