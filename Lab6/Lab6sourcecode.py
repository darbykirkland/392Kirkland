import arcpy
import time


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List the tools that are going to be in this toolbox
        self.tools = [ColorMap]


class ColorMap(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Color Map"
        self.description = "Creates a Graduated Color Map Using an Existing Project and Layer and Outputs it as a new Project"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input Project Path",
            name="projectName",
            datatype="String",
            parameterType="Required",
            direction="Input")

        param1 = arcpy.Parameter(
            displayName="Feature Layer",
            name="featureLayer",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        param2 = arcpy.Parameter(
            displayName="Output Project Path",
            name="outputName",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        #param0.filter = ["aprx"]
        #param1.parameterDependencies = [param0.name]
        params = [param0, param1, param2]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        #Progressor 
        readTime = 1.5
        start = 0
        maximum = 100
        step = 25

        #Setting up the progressor
        arcpy.SetProgressor("step", "Finding User Inputed Variables...", start, maximum, step)
        time.sleep(readTime)
        arcpy.AddMessage("Finding User Inputed Variables...")

        #Setting all of the parameters
        project = arcpy.mp.ArcGISProject(
            parameters[0].valueAsText)
        fLayer = parameters[1].valueAsText
        oLayer = parameters[2].valueAsText
        #Setting the progressor increments
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Creating Map Project...")
        time.sleep(readTime)
        arcpy.AddMessage("Creating Map Project...")

        #Create the map project
        campus = project.listMaps('Map')[0]
        
        #creating and testing layers
        layers = campus.listLayers()
        for layer in layers:

            #go through layers and only outputs the feature layers
            if layer.isFeatureLayer == True:
                #setting the progressor increment
                arcpy.SetProgressorPosition(start + step)
                arcpy.SetProgressorLabel("Checking if Inputed Feature Layer is a Feature Layer...")
                time.sleep(readTime)
                arcpy.AddMessage("Checking if Inputed Feature Layer is a Feature Layer...")
                #lowercases the names to check if the feature class is correctly named
                if layer.name.lower() == fLayer.lower():
                    symbology = layer.symbology
                    #setting the progressor increment
                    arcpy.SetProgressorPosition(start + step)
                    arcpy.SetProgressorLabel("Checking if Symbology is a Renderer...")
                    time.sleep(readTime)
                    arcpy.AddMessage("Checking if Symbology is a Renderer...")
                     #check to see if the sybology is a renderer and creates the color and the breakcount
                    if hasattr(symbology,"renderer") == True:
                        #progressor increment
                        arcpy.SetProgressorPosition(start + step)
                        arcpy.SetProgressorLabel("Creating Symbology...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Creating Symbology...")
                        #creating the map symbology
                        symbology.updateRenderer("GraduatedColorsRenderer")
                        symbology.renderer.breakCount = 5
                        symbology.renderer.colorRamp = project.listColorRamps("Blues (continuous)")[0]
                        layer.symbology = symbology
        #This saves the project as a new project with the user inputed filename and path
        #setting the progressor increment
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Creating Graduated Color Map at...%s" % oLayer)
        time.sleep(readTime)
        arcpy.AddMessage("Creating Graduated Color Map at...%s" % oLayer)
        project.saveACopy(oLayer) 
        return