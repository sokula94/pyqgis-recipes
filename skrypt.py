trees=iface.addVectorLayer("C:/Users/Alicja/Desktop/Programowanie_w_systemach_GIS/qgis_sample_data/shapefiles/trees.shp", "trees", "ogr")
powierzchnia=0
lista={}
for obiekt in trees.getFeatures():
    warunek=obiekt.attribute("VEGDESC")
    if warunek in lista:
        lista[warunek]+=obiekt.attribute("AREA_KM2")
    powierzchnia += obiekt.attribute("AREA_KM2")
print "Powierzchnia =", powierzchnia