from core.modules import BaseClass


class FileInclusion(BaseClass):

    name = "File Inclusion"

    severity = "High"

    functions = [
        "include",
        "require",
        "include_once",
        "require_once"
    ]

    blacklist = []
