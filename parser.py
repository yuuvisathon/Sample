"""
Get the data from whereever and create the JSON blob
"""


BLOB = {
        "machine_id": "",
    "ls": {"raw": ""},
    "netstat": {"raw", ""},
    "ps": {"raw", ""},
    "nmap": {"raw": ""},
    "nstat": {"raw": ""},
    "keylogging": {"raw": ""},
}


def parse_nstat(yuuvis_data):
    BLOB["nstat"]["raw"] = yuuvis_data



def parse_machine(machine_id, yuuvis_data):
    parse_nstat(yuuvis_data)

    return BLOB



