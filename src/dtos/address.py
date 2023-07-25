from dataclasses import dataclass


@dataclass
class Address:
    country: str
    state: str
    county: str
    city: str
    postal_code: str
    street_address_line_1: str
    street_address_line_2: str

    def __init__(self, 
                 country: str,
                 state: str,
                 county: str,
                 city: str,
                 postal_code: str,
                 street_address_line_1: str,
                 street_address_line_2: str):
        self.country = country
        self.state = state
        self.county = county
        self.city = city
        self.postal_code = postal_code
        self.street_address_line_1 = street_address_line_1
        self.street_address_line_2 = street_address_line_2

