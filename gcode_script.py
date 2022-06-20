
from PIL import Image
from PIL import ImageFilter,ImageOps
import os
from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode.compiler import Compiler, interfaces


imageLue = Image.open("visage.jpg")                          #On recupere notre image dans une variable
imageLue = imageLue.convert("L")                             #On transforme l image en blanc noir 
imageLue = imageLue.filter(ImageFilter.FIND_EDGES)           #on applique un filtre , plusieurs filtres sont possibles ,celui ci permet de faire resortir beaucoup plus les contours

#Pour plus d' info sur les filtres visiter ce site https://sites.google.com/magicmakers.fr/teen-python/jouer-avec-des-images/pil-filtres-et-effets
# imageLue = imageLue.filter(ImageFilter.DETAIL)               # Un autre exemple de filtre
# imageLue = imageLue.filter(ImageFilter.EDGE_ENHANCE_MORE)


imageLue.save('bmp.bmp','bmp')                                #on sauvegarde notre fichier bitmap
os.system( "potrace  bmp.bmp --svg -o svg.svg -W 10cm -H 10cm")  # W pour la largeur et H pour la hauteur. Plus d' info en lisant le manuel de Potrace
gcode_compiler = Compiler(interfaces.Gcode, movement_speed=1000, cutting_speed=300, pass_depth=0)   #On definit les parametres du generateur du gcode
curves = parse_file("svg.svg")                                # Parcourt du fichier svg
gcode_compiler.append_curves(curves) 
gcode_compiler.compile_to_file("drawing.gcode", passes=2)     #Compilation et sauvegarde du gcode
    
