# -*- coding: utf-8 -*-
# Data preparation for the hello_world example
from __future__ import print_function

from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv
import os
# 1. Prepare SQL data in memory

FACT_TABLE = "irbd_balance"

print("preparing data...")

engine = create_engine('sqlite:///data.sqlite')
DATA_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "BlackFriday.csv")

create_table_from_csv(engine,
                      DATA_FILE_PATH,
                      table_name=FACT_TABLE,
                      fields=[
                            ("Age", "string"),
                            ("Occupation", "string"),
                            ("City_Category", "string"),
                            ("Stay_In_Current_City_Years", "integer"),
                            ("Marital_Status", "integer"),
                            ("Product_Category_1", "integer"),
                            ("Purchase", "integer")],
                      create_id=True
                  )

print("done. file data.sqlite created")
