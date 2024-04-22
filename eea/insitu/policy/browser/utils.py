"""Utils"""


def normalized(text):
    """Make text easier to compare (used for filenames comparation in our
    case of old filename vs new reports files)"""
    return text.replace("-", "").replace(" ", "").lower()
