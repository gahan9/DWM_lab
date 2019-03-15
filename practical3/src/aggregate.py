#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Gahan Saraiya
GiT: https://github.com/gahan9
StackOverflow: https://stackoverflow.com/users/story/7664524

Aggregation
"""

from cubes import Workspace, Cell, PointCut


def pretty_print(browser, dimension, **kwargs):
    cell = kwargs.get('cell', None)
    if cell:
        for row in browser.aggregate(cell, drilldown=[dimension]).table_rows(dimension):
            print("{:>8s} >>> {}".format(row.label, row.record))
    else:
        for row in browser.aggregate(drilldown=[dimension]).table_rows(dimension):
            print("{:>8s} >>> {}".format(row.label, row.record))


# 1. Create a workspace
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data.sqlite")
workspace.import_model("model.json")

# 2. Get a browser
browser = workspace.browser("black_friday")

# 3. Play with aggregates
result = browser.aggregate()

print("Total\n"+"-"*25)

print("Record count : %8d" % result.summary["record_count"])
print("Total Purchase : %8d" % result.summary["Purchase_sum"])

#
# 4. Drill-down through a dimension
#

print("\n"
      "Drill Down by Category (top-level Item hierarchy)\n"
      "==================================================")
#
result = browser.aggregate(drilldown=["Age"])
#
print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Category", "Count", "Total", "Double"))
#
for row in result.table_rows("Age"):
    print("%-20s%10d%10d" % ( row.label,
                              row.record["record_count"],
                              row.record["Purchase_sum"]
                              ))
"""
print("\n"
      "Slice where Category = Age group 0-17\n"
      "==================================================")

cut = PointCut("Age", ["0-17"])
cell = Cell(browser.cube, cuts=[cut])

result = browser.aggregate(cell, drilldown=["Age"])

print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Sub-category", "Count", "Total", "Double"))

pretty_print(browser, dimension="Age", cell=cell)
# for row in result.table_rows("Age"):
#     print("%-20s%10d%10d%10d" % ( row.label,
#                               row.record["record_count"],
#                               row.record["Purchase_sum"]
#                               ))
"""