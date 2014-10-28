__author__ = 'Caroline'

import arcpy

from arcpy import env

env.workspace = "C:\EsriPress\Python\Data\Exercise07"

ex = "roads.shp"
ferry = "FERRY"

arcpy.AddField_management(ex, ferry, "TEXT", "", "", 15)
cursor = arcpy.da.UpdateCursor(ex, ["FEATURE", ferry])

for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] = "YES"

    else:
        row[1] = "NO"
    cursor.updateRow(row)

raw_input("Press enter: ")
