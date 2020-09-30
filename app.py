from bottle import Bottle, run, template, static_file
import csv
import os

#fichier=os.environ['DATACOVID']
fichier = './time_series_covid19_deaths_global.csv'

population_us = 329256465
population_fr = 67848156
population_it = 60359546
population_sp = 46934632
population_uk = 65761117
debut = 150
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
print("dernier élément progression France:"+ str(progression_france[-1]))
print("dernier élément progression Italie:"+ str(progression_italy[-1]))
print("dernier élément progression Espagne:"+ str(progression_spain[-1]))
print("dernier élément progression UK:"+ str(progression_uk[-1]))
print("dernier élément progression US:"+ str(progression_us[-1]))

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
    datas= [('2018-02-02 08:00:00', 8.0), ('2018-02-02 09:00:00', 9.0)]
    #for d in datas:
    #    labels.append(d[0])

    data = [d[1] for d in datas]

	#assert len(labels)=len(progression_france), "Error : number of dates is different from number of values!"
    return template('index.tpl',label=labels, data=progression_france)

run(app, host='0.0.0.0', debug=True, reloader=True, port=8080)
