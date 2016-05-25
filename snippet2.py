#count all the objects in the layers separately for each 
#object type

#read all the layers in the map
layers = qgis.utils.iface.mapCanvas().layers()

#create a dictionary to store the result
result = {
     "Points": 0, 
     "Lines": 0,
     "Polygons": 0,
     "Undefined": 0,
     "No geometry": 0
     }

#iteration over layers
for layer in layers:
    #create a dictionary of all features
    feature_dict = {f.id(): f for f in layer.getFeatures()}
    #iteration over features with counting
    for f in feature_dict.values():
        type =f.geometry().type()
        if type == 0:
            result["Points"] += 1
        elif type == 1:
            result["Lines"] += 1
        elif type == 2:
            result["Polygons"] += 1
        elif type == 3:
            result["Undefined"] += 1
        else:
            result["No geometry"] += 1
#printing the result
print result

    