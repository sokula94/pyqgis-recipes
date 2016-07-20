				#####		#####  ###	####
				#####		#         	#   
				## ##		#       	#   
				## ##		#      ###	####
				## ##		#      ###	   #
				## ## ##	# ###  ###	   #
				########	#  ##  ###	   #
				#####	#	#####  ###	####
				
			
					#SPRAWOZDANIE VI
					#"Nowa wtyczka"
			
			
		#Wtyczka będzie częścią opracowania środlądowej
		#mapy nawigacyjnej. Jej zadaniem będzie import warst
		#zawierających obiekty punktowe, a nastepnie nadanie
		#im symboli - znaków locyjnych umieszczonych na szlaku
		#żeglownym.
		
		#Temat pracy został zainspirowany zagadnieniami związanymi
		#z planowanym opracowaniem środlądowej mapy nawigacyjnej
		#w ramach pracy inżynierskiej.
		
		#Praca nad wtyczka trwa...

from qgis.core import * #biblioteka umożliwiająca działanie skryptu

def run_script(iface): #uruchomienie skryptu z wtyczki "ScriptRunner"

	warstwa = QgsVectorLayer("C:\Users\green\Desktop\gis\locja.shp","locja","ogr") #wczytanie warstwy z punktami
	QgsMapLayerRegistry.instance().addMapLayer(warstwa)
	
	podklad = qgis.utils.iface.activeLayer()  #ustawienie wczytanej warstwy jako aktywna

	obiekty = podklad.getFeatures()  #pobranie obiektow z warstwy 
	
	for obiekt in obiekty: #tworzenie symbolu
	
		if typ == ("znak01") : #wybranie danego typu znakow
		symbol = QgsMarkerSymbolV2.createSimple({"C:\Users\green\Desktop\gis\poland_01.shp",}) #pobranie grafiki w formacie svg i utworzenie symbolu
		layer.rendererV2().setSymbol(symbol)
		props = layer.rendererV2().symbol().symbolLayer(0).properties()
		props['name'] = 'port'
		props['size'] = '10'
		layer.rendererV2().setSymbol(QgsMarkerSymbolV2.createSimple(props))
		