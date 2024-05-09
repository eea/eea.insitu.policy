"""Utils"""

import os


def normalized(text):
    """Make text easier to compare (used for filenames comparation in our
    case of old filename vs new reports files)"""
    return text.replace("-", "").replace(" ", "").lower()


def get_env_var(env_var_name):
    """Return env var value"""
    env = os.environ.get
    value = env(env_var_name, None)
    if value and len(value) == 0:
        return None

    return value
