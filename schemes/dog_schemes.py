from pydantic import BaseModel


class CatScheme(BaseModel):
    name: str
    color: str


class RandomImageScheme(BaseModel):
    message: str
    status: str


class AllBreedsScheme(BaseModel):
    message: dict
    status: str
