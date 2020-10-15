from bottle import Bottle, run, template, static_file
import csv
import os
import sys
import time


#fichier=os.environ['DATACOVID']
# datafile for container
#fichier = '/opt/app/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

fichier = '/opt/app/time_series_covid19_deaths_global.csv'

# datafile for local testing (home desktop)
#fichier="/Users/matthias/python/data/COVID19/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

# datafile for local testing (home work desktop)
#fichier="/Users/20011409/python/html-graph/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

# clone the data files
#path  = "."
clone = "git clone https://github.com/CSSEGISandData/COVID-19.git"
wget_file="wget https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
#os.chdir(path) # Specifying the path where the cloned project needs to be copied

print("cloning Github data" )
os.system(wget_file) # Cloning
print("end cloning")

#Get update time
now = time.localtime(time.time())
update_time = time.strftime("%y/%m/%d %H:%M", now)
print(update_time)
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
			value=int(raw_data[i+1])-int(raw_data[i])
			if value > 0:
				prog.append(value)
			else:
				prog.append(0)
	return prog

def moyenne(raw_data, population):
#cette fonction permet de ramener les chiffres à la population (pour 10 000 habitants)
	moy=[]
	moy=[i*10000/population for i in raw_data]
	# suppression des valeurs abérantes
	for c,i in enumerate(moy):
		if i > 0.20:
			moy[c]=0
	return moy

with open(fichier, 'r') as f:
	tab_reader = csv.reader(f, delimiter=',')
	for row in tab_reader:
		province = row[0]
		state = row[1]
		if province == 'Province/State':
			longueur=len(row)
			labels=row[debut:longueur]
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

# la progression est la dérivée des données brutes ...
progression_france = derivee(france)
progression_italy=derivee(italy)
progression_spain=derivee(spain)
progression_uk=derivee(uk)
progression_us=derivee(us)

#calcul de la moyenne pour 10 000 habitants
mean_fr=moyenne(progression_france, population_fr)
mean_it=moyenne(progression_italy, population_it)
mean_sp=moyenne(progression_spain,population_sp)
mean_uk=moyenne(progression_uk,population_uk)
mean_us=moyenne(progression_us, population_us)


#Affichage des chiffres de la veille
print("dernier element progression France:"+ str(progression_france[-1]))
print("dernier element progression Italie:"+ str(progression_italy[-1]))
print("dernier element progression Espagne:"+ str(progression_spain[-1]))
print("dernier element progression UK:"+ str(progression_uk[-1]))
print("dernier element progression US:"+ str(progression_us[-1]))

#affichage progression pour 10 000 habitat
#plt.plot(range(len(mean_fr)), mean_fr, color='Blue', marker='', linestyle='solid')
#plt.plot(range(len(mean_it)), mean_it, color='Green', marker='', linestyle='solid')
#plt.plot(range(len(mean_sp)), mean_sp, color='Yellow', marker='', linestyle='solid')
#plt.plot(range(len(mean_uk)), mean_uk, color='Pink', marker='', linestyle='solid')
#plt.plot(range(len(mean_us)), mean_us, color='Black', marker='', linestyle='solid')
#plt.show()


app = Bottle()

@app.route('/static/<filepath:path>')

def server_static(filepath):
    return static_file(filepath, root='static/')

@app.route('/')

def index():
	#assert len(labels)=len(progression_france), "Error : number of dates is different from number of values!"
    return template('index.tpl',update_time=update_time, label=labels, data_fr=mean_fr, data_us=mean_us, data_uk=mean_uk, data_it=mean_it, data_sp=mean_sp, last_value_fr=progression_france[-1])

run(app, host='0.0.0.0', debug=True, reloader=True, port=8080)
