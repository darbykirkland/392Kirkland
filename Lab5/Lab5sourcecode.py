# Lab 5 Darby Kirkland
# 
import arcpy
 
# campus.gdb location
campus = r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab5\Lab4GDB.gdb"

# Setup user input variables
buildingNumber_input = input("Please enter a building number: ")
bufferSize_input = int(input("Please enter a buffer size: "))


# Generate a where_clause
where_clause = "Bldg = '%s'" % buildingNumber_input

# Check if a building exists already
structures = campus + "/Structures"
cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
shouldProceed = False

for row in cursor:
    if row.getValue("Bldg") == buildingNumber_input:
        shouldProceed = True

if shouldProceed:
    # Generate a name for the generated buffer layer
    buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
    # Get reference to a building
    buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)
    # Buffer the building
    arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
    # Clip the structures to buffer
    arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
    # Remove the feature class 
    arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
else:
     print("Seems we couldn't find the building you entered")

