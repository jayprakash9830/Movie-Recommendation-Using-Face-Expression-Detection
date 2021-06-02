import webbrowser

def recommend(reaction):
	choice=reaction.lower()
	if(choice=='sad'):
		webbrowser.open('http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter,asc')
	elif(choice=='disgust'):
		webbrowser.open('http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter,asc')
	elif (choice=='angry'):
		webbrowser.open('http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter,asc')
	elif (choice=='fear'):
		webbrowser.open('https://www.imdb.com/search/title/?genres=horror&title_type=feature&sort=moviemeter,asc')
	elif (choice=='happy'):
		webbrowser.open('https://www.imdb.com/search/title/?genres=thriller&title_type=feature&sort=moviemeter,asc')
	elif (choice=='neutral'):
		webbrowser.open('https://www.imdb.com/search/title/?genres=western&title_type=feature&sort=moviemeter,asc')
	elif (choice=='sad'):
		webbrowser.open('https://www.imdb.com/search/title/?genres=horror&title_type=feature&sort=moviemeter,asc')
	elif (choice=='surprise'):
		webbrowser.open('https://www.imdb.com/search/title/?genres=film_noir&title_type=feature&sort=moviemeter,asc')
	else:
		webbrowser.open('https://www.imdb.com/search/title/?genres=random&title_type=feature&sort=moviemeter,asc')
	print(reaction)
