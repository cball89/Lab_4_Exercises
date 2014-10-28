__author__ = 'Caroline'

import arcpy

from arcpy import env

env.workspace = "C:/EsriPress/Python/Data/Exercise07"

env.overwriteOutput = (True)

air = " \"FEATURE\" = 'Airport'"
sea = " \"FEATURE\" = 'Seaplane Base'"

arcpy.Select_analysis ("airports.shp", "Results/airports_final.shp",air)
arcpy.Select_analysis ("airports.shp", "Results/seaports.shp", sea)
arcpy.Buffer_analysis ("Results/airports_final.shp", "Results/airports_buffers.shp", "15000 METERS")
arcpy.Buffer_analysis ("Results/seaports.shp", "Results/seaports_buffers.shp", "7500 METERS")

raw_input("Press enter: ")
