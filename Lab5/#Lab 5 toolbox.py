#Tool box for lab 5

import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [BuildingProximity]


class BuildingProximity(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Building Proximity"
        self.description = "Determines which buildings on TAMU's campus are near a targeted building"
        self.canRunInBackground = False
        self.category = "Building Tools"

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Building Number",
            name="buildingNumber",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        param1 = arcpy.Parameter(
            displayName="Buffer radius",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )
        param1.filter.type = "Range"
        param1.filter.list = [10, 100]
        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True  # tool can be executed

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        #location of campus.gdb
        campus = r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab5\Lab4GDB.gdb"

        # Setup our user input variables
        buildingNumber_input = parameters[0].valueAsText
        bufferSize_input = int(parameters[1].value)

        # Generate our where_clause
        where_clause = "Bldg = '%s'" % buildingNumber_input

        # Check if building exists
        structures = campus + "/Structures"
        cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
        shouldProceed = False

        for row in cursor:
            if row.getValue("Bldg") == buildingNumber_input:
                shouldProceed = True
        if shouldProceed:
            # Generate a name for buffer layer
            buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
            # Get referenced
            buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)
            # Buffer selected building
            arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
            # Clip the structures to our buffer
            arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
            # Remove the feature class we created earlier
            arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
        else:
            print("Seems we couldn't find the building you entered")

        return 
