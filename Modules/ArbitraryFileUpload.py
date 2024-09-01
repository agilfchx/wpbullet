from core.modules import BaseClass


class ArbitraryFileUpload(BaseClass):

    name = "Arbitrary File Upload"

    severity = "High"

    functions = [
        "move_uploaded_file",
        "file_put_contents",
        "fwrite",
        "fputs",
        "copy",
        "fputcsv",
        "rename"
    ]

    blacklist = []
