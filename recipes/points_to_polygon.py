#   create polygon based on points layer
import math

#   external vertices selection
def extPoints(pointsLayer):
    #   read points from layer
    points = [x.geometry().asPoint() for x in pointsLayer.getFeatures()]
    angles = {}
    externalPoints = []

    #   start at the most bottom point
    currentVertex = startVertex = min(points, key=lambda x: x[1])
    externalPoints.append(currentVertex)

    #   calculate angles as azimuths subtraction
    for x in points:
        if x == currentVertex: continue

        currAz = math.atan2(x[1]-currentVertex[1],x[0]-currentVertex[0])
        if currAz < 0: currAz += 2 * math.pi
        angles[x] = currAz

    #   choose next vertex as the one with lowest angle
    previousVertex = currentVertex
    currentVertex = min(angles.items(), key=lambda x: x[1])[0]
    #   add recent vertex to the result
    externalPoints.append(currentVertex)

    #   analyze remaining vertices
    while(True):
        angles.clear()
        points.remove(currentVertex)

        prevAz = math.atan2(previousVertex[1]-currentVertex[1],previousVertex[0]-currentVertex[0])
        if prevAz < 0: prevAz += 2 * math.pi

        #   same as above
        for x in points:
            if x == previousVertex: continue

            currAz = math.atan2(x[1]-currentVertex[1],x[0]-currentVertex[0])
            if currAz < 0: currAz += 2 * math.pi
            angles[x] = currAz - prevAz
            if angles[x] < 0: angles[x] += 2 * math.pi

        previousVertex = currentVertex
        currentVertex = min(angles.items(), key=lambda x: x[1])[0]

        #   break the loop when it reaches starting vertex
        if (currentVertex == startVertex):
            break

        externalPoints.append(currentVertex)

    return externalPoints

#   layer validation
def validLayer(pointsLayer):
    if not isinstance(pointsLayer, QgsVectorLayer):
        print('Not a vector layer')
        return False
    if (pointsLayer.geometryType() != QGis.Point):
        print('Not a point layer')
        return False
    if (pointsLayer.featureCount() < 3):
        print('At least 3 points required')
        return False

    return True

#   main function
def pointsToPoly(pointsLayer):
    if not validLayer(pointsLayer):
        return

    externalPoints = extPoints(pointsLayer)

    #   create new vector layer
    polygonLayer = QgsVectorLayer('Polygon', 'extPoly', 'memory')
    polygonLayer.setCrs(pointsLayer.crs())
    QgsMapLayerRegistry.instance().addMapLayer(polygonLayer)

    #   add polygon feature to the layer
    polygonLayer.startEditing()

    polyFeature = QgsFeature()
    polyFeature.setGeometry(QgsGeometry.fromPolygon([externalPoints]))
    polygonLayer.dataProvider().addFeatures([polyFeature])

    #   confirm modification
    polygonLayer.commitChanges()
    polygonLayer.updateExtents()
