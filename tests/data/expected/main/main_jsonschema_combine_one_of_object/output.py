# generated by datamodel-codegen:
#   filename:  combine_one_of_object.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Optional, Union

from pydantic import BaseModel, Extra, Field


class MySchemaItem(BaseModel):
    State: Optional[str] = None
    ZipCode: str


class MySchemaItem1(BaseModel):
    County: Optional[str] = None
    PostCode: str


class MySchema1(MySchemaItem):
    class Config:
        extra = Extra.allow

    AddressLine1: str
    AddressLine2: Optional[str] = None
    City: Optional[str] = None


class MySchema2(MySchemaItem1):
    class Config:
        extra = Extra.allow

    AddressLine1: str
    AddressLine2: Optional[str] = None
    City: Optional[str] = None


class MySchema(BaseModel):
    class Config:
        extra = Extra.allow

    __root__: Union[MySchema1, MySchema2] = Field(..., title='My schema')
