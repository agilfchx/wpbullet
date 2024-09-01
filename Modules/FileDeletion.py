from core.modules import BaseClass


class FileDeletion(BaseClass):

    name = "File Deletion"

    severity = "High"

    functions = [
        "unlink",
        "rmdir",
        "wp_delete_file",
        "wp_delete_file_from_directory"
    ]

    blacklist = []
