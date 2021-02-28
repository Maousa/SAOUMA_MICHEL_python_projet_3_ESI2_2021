# créer un environnement
creer:
	python3 -m venv convert

#installer les librairies
librairie:
	pip install -r requirements.txt

#activer la source
act: 
 	cd convert/bin source activate
	 
#désactiver la source
desact:
	cd convert/bin source deactivate

#démarrer le projet
start:
	python3 app/main.py

#lister les librairies (packages)
libs: 
 	pip3 list
