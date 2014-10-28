__author__ = 'Caroline'

import arcpy

from arcpy import env

env.workspace = "C:\EsriPress\Python\Data\Exercise06"
exercise = arcpy.ListFeatureClasses()

for ex in exercize:
    desc = arcpy.Describe(ex)

    print "{0} is a {1} feature class".format(desc.basename, desc.shapeType)

raw_input("Press enter: ")
