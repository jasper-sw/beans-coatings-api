from dataclasses import dataclass


@dataclass
class PhoneNumber:
    country_code: str
    area_code: str
    number: str

    def __init__(self,
                 country_code: str,
                 area_code: str,
                 number: str):
        self.country_code = country_code
        self.area_code = area_code
        self.number = number
