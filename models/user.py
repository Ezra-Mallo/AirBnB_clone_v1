#!/usr/bin/python3
"""User class is defined here to inherit from BaseModel"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """The User class is defined here"""

    # public instances
    email = ""
    password = ""
    first_name = ""
    last_name = ""
