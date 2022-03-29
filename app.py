from bottle import Bottle, run, template, static_file
import csv
import os
import sys
import time
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(name)s:%(levelname)s:%(message)s') # nous utilisons des formats différents pour le fichier et pour la console 
formatter_stream = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter_stream)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


#fichier=os.environ['DATACOVID']
# datafile for container
# add comment to test ci worklflow
#fichier = '/opt/app/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

fichier = '/opt/app/time_series_covid19_deaths_global.csv'
fichier2 = '/opt/app/time_series_covid19_confirmed_global.csv'
vaccineFile = '/opt/app/time_series_covid19_vaccine_global.csv'


# datafile for local testing (home desktop)
#fichier="/Users/matthias/python/data/COVID19/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

# datafile for local testing (home work desktop)
#fichier="/Users/20011409/python/html-graph/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

# get the data files
#path  = "."
logger.debug("Define files from John Hopkins University in Github")
wget_file1="wget -q https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
wget_file2="wget -q https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
wget_vaccine="wget -q https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/vaccine_data/global_data/time_series_covid19_vaccine_global.csv"

#os.chdir(path) # Specifying the path where the cloned project needs to be copied

print("cloning Github data" )
logger.debug("Start Cloning Github Data")
os.system(wget_file1) # Cloning
os.system(wget_file2)
os.system(wget_vaccine)
logger.debug("End Cloning Github Data")
print("end cloning")

#Get update time
logger.debug("define consts")
now = time.localtime(time.time())
update_time = time.strftime("%y/%m/%d %H:%M", now)
population_us = 329256465
population_fr = 67848156
population_it = 60359546
population_sp = 46934632
population_uk = 65761117
debut = 50
labels=list()

def derivee(raw_data):
	value=0
	prog=[]
	for i, v in enumerate(raw_data[:-1]):
		try:
			value=int(raw_data[i+1])-int(raw_data[i])
		except ValueError:
			print("[ERROR] in derivee function : could not convert data into an integer.")
		if value > 0:
			prog.append(value)
		else:
			prog.append(0)
	return prog

def moyenne(raw_data, population):
#cette fonction permet de ramener les chiffres à la population (pour 1 000 000 habitants)
	moy=[]
	moy=[i*1000000/population for i in raw_data]
	# suppression des valeurs abérantes
	#for c,i in enumerate(moy):
		#if i > 0.20:
			#moy[c]=0
	return moy

#print ("3 - lecture fichiers")
#death file 
with open(fichier, 'r') as f:
	tab_reader = csv.reader(f, delimiter=',')
	for row in tab_reader:
		province = row[0]
		state = row[1]
		if province == 'Province/State':
			longueur=len(row)
			labels=row[debut:longueur]
			print("Nombre de valeurs pour les morts:"+ str(longueur))
			#days=row[4:longueur]
		if province == '':
			if state == 'France':
				#print(row)
				longueur=len(row)
				france=row[debut:longueur]
			if state == 'Italy':
				longueur=len(row)
				italy=row[debut:longueur]
			if state == 'Spain':
				longueur=len(row)
				spain=row[debut:longueur]
			if state == 'United Kingdom':
				longueur=len(row)
				uk=row[debut:longueur]
			if state == 'US':
				longueur=len(row)
				us=row[debut:longueur]

#confirmed file
with open(fichier2, 'r') as f:
	tab_reader = csv.reader(f, delimiter=',')
	for row in tab_reader:
		province = row[0]
		state = row[1]
		if province == 'Province/State':
			longueur=len(row)
			labels=row[debut:longueur]
			#print("Nombre de valeurs pour les cas confirmes:"+ str(longueur))
			#days=row[4:longueur]
		if province == '':
			if state == 'France':
				#print(row)
				longueur=len(row)
				confirmed_france=row[debut:longueur]
			if state == 'Italy':
				longueur=len(row)
				confirmed_italy=row[debut:longueur]
			if state == 'Spain':
				longueur=len(row)
				confirmed_spain=row[debut:longueur]
			if state == 'United Kingdom':
				longueur=len(row)
				confirmed_uk=row[debut:longueur]
			if state == 'US':
				longueur=len(row)
				confirmed_us=row[debut:longueur]


#vaccine file

#calculs
# la progression est la dérivée des données brutes ...
#print ("calculs")
progression_france = derivee(france)
progression_italy=derivee(italy)
progression_spain=derivee(spain)
progression_uk=derivee(uk)
progression_us=derivee(us)

confirmed_progression_france = derivee(confirmed_france)
confirmed_progression_italy=derivee(confirmed_italy)
confirmed_progression_spain=derivee(confirmed_spain)
confirmed_progression_uk=derivee(confirmed_uk)
confirmed_progression_us=derivee(confirmed_us)

#calcul de la moyenne pour 1 000 000 habitants
mean_fr=moyenne(progression_france, population_fr)
mean_it=moyenne(progression_italy, population_it)
mean_sp=moyenne(progression_spain,population_sp)
mean_uk=moyenne(progression_uk,population_uk)
mean_us=moyenne(progression_us, population_us)

confirmed_mean_fr=moyenne(confirmed_progression_france, population_fr)
confirmed_mean_it=moyenne(confirmed_progression_italy, population_it)
confirmed_mean_sp=moyenne(confirmed_progression_spain,population_sp)
confirmed_mean_uk=moyenne(confirmed_progression_uk,population_uk)
confirmed_mean_us=moyenne(confirmed_progression_us, population_us)

#

#app et app.route ici

#
#print("avant run(app ..)")
app = Bottle()

@app.route('/static/<filepath:path>')

def server_static(filepath):
    return static_file(filepath, root='static/')

@app.route('/')

def index():
	#assert len(labels)=len(progression_france), "Error : number of dates is different from number of values!"
    return template('index.tpl',
					update_time=update_time,
					label=labels,
					month_label=labels[-60:],
					progression_fr=progression_france,
					confirmed_data_fr=confirmed_progression_france,
					progression_us=progression_us,
					confirmed_data_us=confirmed_progression_us,
					progression_uk=progression_uk,
					confirmed_data_uk=confirmed_progression_uk,
					data_fr=mean_fr,
					data_us=mean_us,
					data_uk=mean_uk,
					data_it=mean_it,
					data_sp=mean_sp,
					data_month_fr=mean_fr[-60:],
					data_month_us=mean_us[-60:],
					data_month_uk=mean_uk[-60:],
					data_month_it=mean_it[-60:],
					data_month_sp=mean_sp[-60:],
					last_update=labels[-1],
					last_value_fr=progression_france[-1],
				    	last_value_us=progression_us[-1],
					last_value_uk=progression_uk[-1],
					last_value_sp=progression_spain[-1],
					last_value_it=progression_italy[-1],
					last_value_confirmed_fr=confirmed_progression_france[-1],
					last_value_confirmed_us=confirmed_progression_us[-1],
					last_value_confirmed_uk=confirmed_progression_uk[-1],
					last_value_confirmed_sp=confirmed_progression_spain[-1],
					last_value_confirmed_it=confirmed_progression_italy[-1],
					)

run(app, host='0.0.0.0', debug=True, reloader=False, port=8080)
