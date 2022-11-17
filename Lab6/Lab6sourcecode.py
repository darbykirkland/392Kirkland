
import arcpy
#Creating the project
project = arcpy.mp.ArcGISProject(
    r"C:\Users\spygo\Desktop\repos\map\map.aprx")
#creating map project
campus = project.listMaps('Map')[0]

#creat and test the new layers
layers = campus.listLayers()
for layer in layers:
    #outputs the feature layers
    if layer.isFeatureLayer == True:
        #lowercases the names checks the new class
        if layer.name.lower() == "GarageParking".lower():
            symbology = layer.symbology
            #Check the symbology and render
            if hasattr(symbology,"renderer") == True:
                symbology.updateRenderer("GraduatedColorsRenderer")
                symbology.renderer.breakCount = 5
                symbology.renderer.colorRamp = project.listColorRamps("Blues (continuous)")[0]
                layer.symbology = symbology
project.saveACopy(r"C:\Users\spygo\Desktop\repos\map\map2.aprx")
