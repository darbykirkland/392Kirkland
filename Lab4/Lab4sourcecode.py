# Lab 4 Darby Kirkland

import arcpy

# create layer from csv and convert to feature class gdb
arcpy.env.overwriteOutput = True

arcpy.CreateFileGDB_management(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb")


return1 = arcpy.MakeXYEventLayer_management(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\garages.csv","x","y","garage")

arcpy.FeatureClassToGeodatabase_conversion(return1,r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb")

#copy feature class from another gdb into new gdb
arcpy.Copy_management(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb\Structures",r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb\Structures")

#extract spatial information from feature class
spatial_ref = arcpy.Describe(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb\Structures").spatialReference

#project spatial reference of garage points
arcpy.Project_management(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb\garage",r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb\garage_projection", spatial_ref)

#makes 150m buffer of garage projection
return2 = arcpy.Buffer_analysis(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb\garage_projection",r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb\garage_projection_buffer", 150)

#create intersect fo the garage buffer and structures
arcpy.Intersect_analysis(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb\Structures",r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb\garage_projection_intersect", 'ALL')

#convert table to have projected cordinates
arcpy.TableToTable_conversion(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4\04\Campus.gdb\garage_projection_intersect",r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab4","ConvertedTable.csv")