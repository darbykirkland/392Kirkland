import arcpy

#RS composite bands
band1 = arcpy.sa.Raster(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab7\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF")
band2 = arcpy.sa.Raster(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab7\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF")
band3 = arcpy.sa.Raster(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab7\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF")
band4 = arcpy.sa.Raster(r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab7\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.TIF")
composite = arcpy.CompositeBands_management([band1, band2, band3, band4], r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab7\composite.tif")

#Hillshade
source = r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab7"
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(source + r"\n30_w097_1arc_v3.tif", source + r"\n30_w097_1arc_v3_hillshade.tif", azimuth, altitude, shadows, z_factor)

#Slope
source = r"C:\Users\spygo\Desktop\Repos\GEOG392\Lab7"
output_measurment = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + r"\n30_w097_1arc_v3.tif", source + r"\n30_w097_1arc_v3_slope.tif",  output_measurment, z_factor)