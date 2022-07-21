### Plugin Builder Results

Congratulations! You just built a plugin for QGIS!  


Your plugin **full\_mce** was created in:  
  **D:/full\_mce\_new\\fullmce**

Your QGIS plugin directory is located at:  
  **C:/Users/fsarah/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins**

### What's Next

1.  If resources.py is not present in your plugin directory, compile the resources file using pyrcc5 (simply use **pb\_tool** or **make** if you have automake)
2.  Optionally, test the generated sources using **make test** (or run tests from your IDE)
3.  Copy the entire directory containing your new plugin to the QGIS plugin directory (see Notes below)
4.  Test the plugin by enabling it in the QGIS plugin manager
5.  Customize it by editing the implementation file **fullmce.py**
6.  Create your own custom icon, replacing the default **icon.png**
7.  Modify your user interface by opening **fullmce\_dialog\_base.ui** in Qt Designer

Notes:

*   You can use **pb\_tool** to compile, deploy, and manage your plugin. Tweak the _pb\_tool.cfg_ file included with your plugin as you add files. Install **pb\_tool** using _pip_ or _easy\_install_. See **http://loc8.cc/pb\_tool** for more information.
*   You can also use the **Makefile** to compile and deploy when you make changes. This requires GNU make (gmake). The Makefile is ready to use, however you will have to edit it to add addional Python source files, dialogs, and translations.

For information on writing PyQGIS code, see **http://loc8.cc/pyqgis\_resources** for a list of resources.

©2011-2019 GeoApt LLC - geoapt.com

REGLES DE GESTION: - Le log est sauvegardé dans le fichier "full\_mce\_log.txt" dans le répertoire de sortie choisit par l'utilisateur \* Classification: 1) nombre minimal des contraintes = 0, nombre maximale = illimité 2) chaque contrainte correspond à un et un seul champ issu d'un seul fichier source 3) un fichier source peut contenir un ou plusieurs contraintes 4) un champ d'un fichier source correspond à un et un seul contrainte 5) un contrainte doit contenir au moins un nom, un fichier source, un status (prêt ou pas prêt) 6) Si une ou plusieurs cases "Prêts" ne sont pas cochées, le plugin propose de reclassifier les contraintes correspondants 7) Par défaut, la nouvelle valeur d'un contrainte reclassifé est égale à 0 et de type réel 8) Pour les contraintes de type quantitative, - la valeur "Début" doit être strictement inférieure à la valeur "Fin" - si la valeur "Début" est égale à "min", le plugin remplacera cette valeur par la valeur miniminum du champ - si la valeur "Fin" est égale à "max", le plugin remplacera cette valeur par la valeur maximale du champ - chaque interval "Début", "Fin" ne devrait pas contenir un autre interval, ni être inclus dans un autre interval 9) Pour les contraintes de type qualitative, - le plugin propose de choisir parmi les attributs du champ; - chaque attribut ne doit être choisit qu'une seule fois 10) Les résultats de la reclassification sont stockés dans des champs portant les suffixes "Bl" (qui remplace les 2 derniers caractères du nom du champ) dans des fichiers portant les suffixes "\_bool" 11) Les résultats finaux sont de type Double et arrondissés au 2 centièmes près (2 chiffres après la virgule) \* Standardization: 1) nombre minimal des facteurs = 3, nombre maximale = 15 2) chaque facteur correspond à un et un seul champ issu d'un seul fichier source 3) un fichier source peut contenir un ou plusieurs facteurs 4) un champ d'un fichier source correspond à un et un seul facteur 5) un contrainte doit contenir au moins un nom, un fichier source, un status (prêt ou pas prêt) 6) Si une ou plusieurs cases "Normalisés" ne sont pas cochées, le plugin propose de normaliser les facteurs 7) Si le champ d'un facteur est de type "String", le plugin propose de reclassifier le facteur ou de choisir un autre champ 8) Le plugin renvoi une erreur si les paramètres en entrée ne respectent pas les règles suivantes : - les valeurs des colonnes B, C, D doivent être strictement supérieures aux valeurs des colonnes précédentes ( B > A; D >C ; C > B (si symétrique)) - si la valeur de "A" ou "C" (cas décroissant) est égale à "min", le plugin remplacera cette valeur par la valeur miniminum du champ - si la valeur de "B" (cas croissant) ou "D" est égale à "max", le plugin remplacera cette valeur par la valeur maximale du champ 9) Les résultats de la standardisation sont stockés des champs portant les suffixes "Fz" (qui remplace les 2 derniers caractères du nom du champ) dans des fichiers portant les suffixes "\_fuzz" 10) Les résultats finaux sont de type Double et arrondissés au 2 centièmes près (2 chiffres après la virgule) 11) Pour le cas des fonctions sigmoidal, les résultats de la standardisation sont égales à "inf" si | a \* (value - b)| > 709.78271 (La valeur max de la fonction exp en python) et supérieur à 110,000 digits