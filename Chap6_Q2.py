__author__ = 'Caroline'

import arcpy

from arcpy import env

env.workspace = "C:\EsriPress\Python\Data\Exercise06\Results\Study.gdb"
exercise = arcpy.ListFeatureClasses()
arcpy.CreateFileGDB_management("C:\EsriPress\Python\Data\Exercise06\Results","Newstudy.gdb")

for ex in exercise:
    desc = arcpy.Describe(ex)

    if desc.shapeType == "Polygon":
        arcpy.Copy_management(ex, "C:\EsriPress\Python\Data\Exercise06\Results\Newstudy.gdb/" + ex)

raw_input("Press enter: ")
