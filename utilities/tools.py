import os


def is_on_github_actions():
    if os.getenv("GITHUB_ACTIONS"):
        return True
    else:
        return False


def is_selenium(context):
    if "selenium" in context.tags:
        return True
    else:
        return False
