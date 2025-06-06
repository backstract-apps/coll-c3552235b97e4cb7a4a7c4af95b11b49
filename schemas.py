from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Customers(BaseModel):
    id: Any
    name: str
    contact_details: str


class ReadCustomers(BaseModel):
    id: Any
    name: str
    contact_details: str
    class Config:
        from_attributes = True


class Interactions(BaseModel):
    id: Any
    customer_id: int
    date: datetime.date
    time: str
    summary: str


class ReadInteractions(BaseModel):
    id: Any
    customer_id: int
    date: datetime.date
    time: str
    summary: str
    class Config:
        from_attributes = True


class Opportunities(BaseModel):
    id: Any
    customer_id: int
    potential_value: float
    stage: str
    expected_close_date: datetime.date


class ReadOpportunities(BaseModel):
    id: Any
    customer_id: int
    potential_value: float
    stage: str
    expected_close_date: datetime.date
    class Config:
        from_attributes = True




class PostOpportunities(BaseModel):
    id: int = Field(...)
    customer_id: int = Field(...)
    potential_value: str = Field(..., max_length=100)
    stage: str = Field(..., max_length=100)
    expected_close_date: Any = Field(...)

    class Config:
        from_attributes = True



class PostInteractions(BaseModel):
    id: int = Field(...)
    customer_id: int = Field(...)
    date: Any = Field(...)
    time: str = Field(..., max_length=100)
    summary: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostCustomers(BaseModel):
    id: int = Field(...)
    name: int = Field(...)
    contact_details: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

