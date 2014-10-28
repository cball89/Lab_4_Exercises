__author__ = 'Caroline'

import arcpy

default = "no extensions are available"

if arcpy.CheckExtension("3D") == "Available":
    ext_3D = "3D Analyst"

else:
    ext_3D = ""

if arcpy.CheckExtension("Network") == "Available":
    ext_network = "Network Analyst"

else:
    ext_network = ""

if arcpy.CheckExtension("Spatial") == "Available":
    ext_spatial = "Spatial Analyst"

else:
    ext_spatial = ""

print "The following extensions are available: " + ext_3D + ext_spatial + ext_network + default

raw_input("Press enter: ")
