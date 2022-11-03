# Lab 4 Darby Kirkland
# Take csv and convert it into a new feature class and gdb.

import arcpy

arcpy.env.overwriteOutput = True

arcpy.CreateFileGDB_management(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4","Lab4GDB")

return1 = arcpy.MakeXYEventLayer_management(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\garages.csv","x","y","garage")

arcpy.FeatureClassToGeodatabase_conversion(return1,r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Lab4GDB.gdb")

#Copy a feature class from gdb into the new gdb.
arcpy.Copy_management(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Campus.gdb\Structures",r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Lab4GDB.gdb\Structures")

#Extract the spatial reference from the feature class.
spatial_ref = arcpy.Describe(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Lab4GDB.gdb\Structures").spatialReference

#Projects the garage points.
arcpy.Project_management(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Lab4GDB.gdb\garage",r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Lab4GDB.gdb\garage_projection", spatial_ref)

#Create a buffer of 150 meters for the new garage projection.
return2 = arcpy.Buffer_analysis(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Lab4GDB.gdb\garage_projection",r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Lab4GDB.gdb\garage_projection_buffer", 150)

#Create an intersect of the garage buffer and structures.
arcpy.Intersect_analysis([r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Lab4GDB.gdb\Structures",r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Lab4GDB.gdb\garage_projection_buffer"],r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Lab4GDB.gdb\garage_projection_intersect", 'ALL')

#Converts the new table to projected coordinates.
arcpy.TableToTable_conversion(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\Lab4GDB.gdb\garage_projection_intersect",r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4","ConvertedTable.csv")