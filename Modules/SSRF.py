from core.modules import BaseClass


class SSRF(BaseClass):

    name = "SSRF"

    severity = "High"

    functions = [
        "wp_remote_head",
        "wp_remote_get",
        "wp_remote_post",
        "wp_remote_request"
    ]

    blacklist = []
