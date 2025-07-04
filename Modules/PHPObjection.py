from core.modules import BaseClass


class PHPObjection(BaseClass):

    name = "PHP Objection"

    severity = "High"

    functions = [
        "unserialize",
        "maybe_unserialize"
    ]

    blacklist = []
