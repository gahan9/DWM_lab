from __future__ import print_function
from cubes import Workspace, Cell, PointCut

# 1. Create a workspace
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data.sqlite")
workspace.import_model("model.json")

# 2. Get a browser
browser = workspace.browser("irbd_balance")

# 3. Play with aggregates
result = browser.aggregate()

print("Total\n"
      "----------------------")

print("Record count : %8d" % result.summary["record_count"])
print("Total Purchase : %8d" % result.summary["Purchase_sum"])
print("Double Purchase: %8d" % result.summary["double_Purchase_sum"])

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
    print("%-20s%10d%10d%10d" % ( row.label,
                              row.record["record_count"],
                              row.record["Purchase_sum"],
                              row.record["double_Purchase_sum"])
                              )

print("\n"
      "Slice where Category = Age group 0-17\n"
      "==================================================")

cut = PointCut("Age", ["0-17"])
cell = Cell(browser.cube, cuts = [cut])

result = browser.aggregate(cell, drilldown=["Age"])

print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Sub-category", "Count", "Total", "Double"))

for row in result.table_rows("Age"):
    print("%-20s%10d%10d%10d" % ( row.label,
                              row.record["record_count"],
                              row.record["Purchase_sum"],
                              row.record["double_Purchase_sum"],
                              ))
