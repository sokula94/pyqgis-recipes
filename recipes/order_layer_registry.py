#   no more hidden layers
#   ordnung muss sein
def cleanupTocMess():
    #   returns layer's sorting key value
    def sumByGeometry(mapLayer):
        if isinstance(mapLayer, QgsRasterLayer):
            return mapLayer.width() * mapLayer.height()

        #   sorting
        #   rasters by bounding box area
        layerFeatures = mapLayer.getFeatures()
        geomEnum = mapLayer.geometryType()

        #   points by quantity
        if geomEnum == QGis.Point:
            return mapLayer.featureCount()
        #   lines by length
        if geomEnum == QGis.Line:
            return sum([ftr.geometry().length() for ftr in layerFeatures])
        #   polygons by area
        if geomEnum == QGis.Polygon:
            return sum([ftr.geometry().area() for ftr in layerFeatures])

    #   reading root node of layers tree
    root = QgsProject.instance().layerTreeRoot()

    #   moving nodes
    def updateToc(layersList):
        for mapLayer in layersList:
            root.insertChildNode(0, mapLayer.clone())
            root.removeChildNode(mapLayer)

    #   reading registered layers
    regLayers = root.findLayers()

    #   splitting into vector and raster layers
    vectorLayers = filter(lambda x: isinstance(x.layer(), QgsVectorLayer), regLayers)
    rasterLayers = filter(lambda x: isinstance(x.layer(), QgsRasterLayer), regLayers)
    rasterLayers = sorted(rasterLayers, key=lambda x: sumByGeometry(x.layer()), reverse=True)

    #   splitting vector layers into points, lines and polygons
    #   sorting by total amount/length/area sum
    pointLayers = filter(lambda x: x.layer().geometryType() == 0, vectorLayers)
    pointLayers = sorted(pointLayers, key=lambda x: sumByGeometry(x.layer()), reverse=True)
    lineLayers = filter(lambda x: x.layer().geometryType() == 1, vectorLayers)
    lineLayers = sorted(lineLayers, key=lambda x: sumByGeometry(x.layer()), reverse=True)
    polygonLayers = filter(lambda x: x.layer().geometryType() == 2, vectorLayers)
    polygonLayers = sorted(polygonLayers, key=lambda x: sumByGeometry(x.layer()), reverse=True)

    #   updating table of contents
    updateToc(rasterLayers)
    updateToc(polygonLayers)
    updateToc(lineLayers)
    updateToc(pointLayers)
