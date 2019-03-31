import arcpy
dataset = r'C:\Users\prane\Desktop\CapstoneIntern\Australia F1\Australia\Intersections.gdb\Polygonrastercalc0_10T1_Jardine'
desc = arcpy.Describe(dataset)

extent = desc.extent
spatialReference = desc.spatialReference
name = desc.name
dataType = desc.dataType
print(spatialReference)
print(extent)
