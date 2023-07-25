from dataclasses import dataclass
import datetime
from src.dtos.user import User


@dataclass
class Job:
    start_datetime: datetime.datetime
    due_datetime: datetime.datetime
    job_name: str
    job_uuid: str
    user: User

    def __init__(self,
                 start_datetime: datetime.datetime,
                 due_datetime: datetime.datetime,
                 job_name: str,
                 job_uuid: str,
                 user: User):
        self.start_datetime = start_datetime
        self.due_datetime = due_datetime
        self.job_name = job_name
        self.job_uuid = job_uuid
        self.user = user
