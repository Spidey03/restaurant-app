from dataclasses import dataclass
from typing import Optional, List


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


@dataclass
class LoginUserDTO:
    username: str
    password: str


@dataclass
class ItemDTO:
    id: str
    name: str
    price: float
    description: Optional[str] = ''


@dataclass
class TableOrderDTO:
    id: str
    table_id: str
    user_id: str
    order_id: str


@dataclass
class OrderDTO:
    id: str
    is_paid: bool
    items: List[str]
    amount: float = 0
