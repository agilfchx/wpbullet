from core.modules import BaseClass


class PrivEsc(BaseClass):

    name = "Privilege Escalation"

    severity = "High"

    functions = [
        # "update_option",
        "update_user_meta",
        "wp_insert_user",
        "wp_update_user",
        "wp_set_password"
    ]

    blacklist = []
