from re import S
from pydantic import BaseModel


class Tester(BaseModel):
    a: str
    b: int

print(Tester(a="H", b=12).json())