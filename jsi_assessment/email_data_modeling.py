from typing import List, Optional


class User:
    def __init__(
            self, user_id: int, first_name: str, last_name: str, email_address: str
    ):
        self._user_id = user_id
        self._first_name = first_name
        self._last_name = last_name
        self._email_address = email_address


class Attachment:
    def __init__(self, item_id: int, path: str):
        self._item_id = item_id
        self._path = path


class Email:
    def __init__(
            self, from_: User, to: List[User], date_time_: str
            , subject: Optional[str] = None
            , message: Optional[str] = None
            , attachment: List[Optional[Attachment]] = None
    ):
        self._from = from_
        self._to = to
        self._date_time_ = date_time_
        self._subject = subject
        self._message = message
        self._attachment = attachment
