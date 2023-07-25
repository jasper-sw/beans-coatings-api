from dataclasses import dataclass
from src.dtos.job import Job


@dataclass
class User:
    first_name: str
    last_name: str
    phone_number: str
    email_address: str
    jobs: list[Job]

    def __init__(self, first_name: str, last_name: str, phone_number: str, email_address: str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address

