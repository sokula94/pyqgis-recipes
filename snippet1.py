# Looking for all the neighbours of the selected polygon

from qgis.utils import iface

# Replace the values below with values from your layer.
# Change the _NAME_FIELD value to the name of your identifier field
_NAME_FIELD = 'NAME_2'

layer = iface.activeLayer()

# Create a dictionary of all features
feature_dict = {f.id(): f for f in layer.getFeatures()}

# Set the myfeature value to the value of your polygon
myfeature = 'Wade Hampton' 

# Loop through all features and find features that touch each feature
for f in feature_dict.values():
    if f[_NAME_FIELD] == myfeature:
        geom = f.geometry()
        # Find all features that intersect the bounding box of the current feature.
        intersecting_ids = index.intersects(geom.boundingBox())
        # Initalize neighbors list
        neighbors = []
        for intersecting_id in intersecting_ids:
            # Look up the feature from the dictionary
            intersecting_f = feature_dict[intersecting_id]
            if (f != intersecting_f and
                not intersecting_f.geometry().disjoint(geom)):
                neighbors.append(intersecting_f[_NAME_FIELD])
        f[_NEW_NEIGHBORS_FIELD] = ','.join(neighbors)
        # printing the result
        print 'Neighbors of the %s' % f[_NAME_FIELD] + ': ' + str(neighbors)
