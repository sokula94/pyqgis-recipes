#Network Union
#Wtyczka łącząca obiekty liniowe
#wczytanie nowej warstwy
warstwa= iface.addVectorLayer("/Users/adamnadolny/Documents/STUDIA/VI semestr/Programowanie/qgis_sample_data/shapefiles/rivers.shp", "rzeki", "ogr")
if not  warstwa:
        print "Brak warstwy!"
else:
        print "Warstwa zaladowana:"

#Ustawienie warstwy aktywnej
iface.setActiveLayer( warstwa )
#zaimportowanie narzędzi geoprocesingu
import processing
#wywołanie funkcji: agreguj z parametrami
processing.runalg("qgis:dissolve",warstwa,"False","NAM","/Users/adamnadolny/Documents/STUDIA/VI semestr/Programowanie/Wtyczki/rzeki2.shp")
#utworzenie nowej warstwy i załadowanie do pogramu
warstwa= iface.addVectorLayer("/Users/adamnadolny/Documents/STUDIA/VI semestr/Programowanie/Wtyczki/rzeki2.shp", "rzeki2", "ogr")
iface.setActiveLayer(warstwa)
#uaktywnienie nowej warstwy i otworzenie tabeli atrybutów
iface.actionOpenTable().trigger()

