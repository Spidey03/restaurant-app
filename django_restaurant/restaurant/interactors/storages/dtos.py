from dataclasses import dataclass
from typing import Optional


@dataclass
class UserDTO:
    id: str
    first_name: str
    username: str


@dataclass
class UserDetailsDTO(UserDTO):
    date_joined: Optional[str] = ''
    last_name: Optional[str] = None
    mobile_number: Optional[str] = None


@dataclass
class AddUserDetailsDTO(UserDTO):
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = False
    date_joined: Optional[str] = ''
    last_name: Optional[str] = None
    mobile_number: Optional[str] = None
