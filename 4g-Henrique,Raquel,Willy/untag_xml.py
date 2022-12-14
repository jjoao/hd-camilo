import re


def untag(text):
    untagged = re.sub(r'<[^>]*?>', r'', text)
    return untagged
