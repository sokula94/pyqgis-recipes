#Skrypt wkonany jest dla danych pobranych z http://download.osgeo.org/qgis/data/qgis_sample_data.zip.  na warstwie trees 

#wczytanie bibliotek ulatwiajacyhc napisanie dalszej czesci skryptu 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.core import *
import qgis.utils
import sys

#skrypt wywolywany jest za pomoca wtyczki dostepnej w Qgis, jest to wtyczka "ScriptRunner"

#zdefiniowanie funkcji ktora bedzie kolorowac na wybrany przez nas kolor, obiekty tej samej kategori 
def run_script(iface):
	warstwa = qgis.utils.iface.activeLayer()  #ustawienie wczytanej warstwy jako aktywna

	obiekty = warstwa.getFeatures()  #pobranie obiektow z warstwy
	
	legenda = {}    #utworzenie slownika w ktorym zapisany bedzie kolor i rodzaj
	for obiekt in obiekty:
	
		rodzaj= obiekt[1]   #okreslenie wedlug ktorej kolumny wyznaczamy rodzaj 
		if rodzaj == ("Evergreen") :  #okreslenie kategorii 
			legenda[obiekt[1]]  = ('#00ff33','Evergreen') #zapisanie w slowniku koloru dla danej rodzaju i samej nazwy rodzaju
		elif rodzaj == ("Deciduous") :
			legenda[obiekt[1]]  = ('#ff0033','Deciduous')
		elif rodzaj == ("Mixed Trees") :
			legenda[obiekt[1]]  = ('#6633ff','Mixed Trees')

	kategorie = []  #stworzenie slownika wedlug ktorego powstanie legenda z ukazanym kolorem i nazwa etykiety oraz pokolorwanie na mapie danego obiektu z tego rodzaju
	for region, (kolor, etykieta) in legenda.items():   #okreslenie dla kazdego rodzaju legendy oraz oznaczenie go na mapie tym samym kolorem 
		symbol = QgsSymbolV2.defaultSymbol(warstwa.geometryType())
		symbol.setColor(QColor(kolor))
		oznaczenie = QgsRendererCategoryV2(region, symbol, etykieta)
		kategorie.append(oznaczenie)

	nazwa = 'VEGDESC'  #okreslenie nazy kolumny wedlug ktorej okreslamy rodzaje 
	renderer = QgsCategorizedSymbolRendererV2(nazwa, kategorie)
	warstwa.setRendererV2(renderer)
	
	warstwa.triggerRepaint()    #wywolanie pomalowania mapy 