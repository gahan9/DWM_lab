#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Gahan Saraiya
GiT: https://github.com/gahan9
StackOverflow: https://stackoverflow.com/users/story/7664524

Data preparation
"""

from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv
import os

# 1. Prepare SQL data in memory
print("preparing data...")
engine = create_engine('sqlite:///data.sqlite')

FACT_TABLE = "black_friday"
DATA_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "BlackFriday.csv")

create_table_from_csv(engine,
                      DATA_FILE_PATH,
                      table_name=FACT_TABLE,
                      fields=[
                            ("Age", "string"),
                            ("Occupation", "string"),
                            ("Product_Category", "string"),
                            ("Purchase", "integer")],
                      create_id=True
                      )

print("done. file data.sqlite created")
