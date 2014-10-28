__author__ = 'Caroline'

import arcpy

from arcpy import env
env.workspace = "C:\EsriPress\Python\Data\Exercise05"

env.overwriteOutput = (True)

arcpy.Dissolve_management("parks.shp", "parks_dissolved.shp","PARK_TYPE", "", "FALSE")

raw_input("Press enter: ")
