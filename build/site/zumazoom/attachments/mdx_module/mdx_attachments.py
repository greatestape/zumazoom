from attachments.markdown_extensions import AttachmentsExtension


def makeExtension(configs=None):
    return AttachmentsExtension(configs=configs)
