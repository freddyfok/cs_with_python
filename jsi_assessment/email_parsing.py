from typing import Optional

import yaml


def find_sender_email(string: Optional[str] = None, file_location: Optional[str] = None) -> (str, str):
    if not string and not file_location:
        return None

    from_field = "From"  # Sender

    data = yaml.safe_load(string) if string else None
    if not data:
        with open(fr"{file_location}") as f:
            data = yaml.safe_load(f)

    sender_data = data[from_field].split(" ")
    sender_email = sender_data[-1]
    if sender_email[0] == "<":
        sender_email = sender_email[1:-1]
    return " ".join(sender_data[:-1]), sender_email
