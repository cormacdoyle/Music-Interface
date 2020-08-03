'''
Assignment 3: The Sound of Music
By: Cormac Doyle
Student Number: 20152002

This program takes a hard coded list of subscribers and music genres and randomly generates a set of music preferences.
The program has the ability to check subscriber similarity, match subscribers, generate a list of average ratings, display
the most popular genres, and recommend genres given a users name.
'''

from random import *
from math import *
import user_interface # import user interface module
import statistics #imports so that mean() can be used 

# Please insert your defined functions here


# initialize subscribers list and music_genre list
subscribers = [
			'Justin Trudeau',
			'Bob Jones',
			'Sam Frizzel',
			'Captain Nemo',
			'Joe Jameson',
			'Paul Casindes',
			'Justin Bieber',
			'Natlie Portman',
			'Bugs Bunny',
			'Peter Rabbit',
			'Mickey Mouse',
			'Martin Melchor',
			'Nada Neel',
			'Kristin Karlin',
			'Edmond Earls',
			'Fredrick Foxwell',
			'Thomas Twitty',
			'Julieann Jenning',
			'Anton Autin',
			'Alix Ashmore',
			'Tiffany Turgeon',
			'Noella Nash',
			'Esther Edgerton',
			'Sanda Sewart',
			'Fannie Ferrera',
			'Bernardine Block',
			'Roger Rudd',
			'Yang Wu',
			'Raisa Rohr',
			'Cirocco Jones',
			'Mickie Milling',
			'Ronald McDonald',
			'Tim Horton',
			'Colonel Sanders',
			'Joel Jerry',
			'Leanora Lion',
			'Oscar Oliverio',
			'Jernau Fortier'
		]
# initalizes music genres
music_genres = [
			'Jazz',
			'Country',
			'Rap',
			'Blues',
			'Reggae',
			'Soul',
			'EDM',
			'Hip Hop',
			'World',
			'Rock',
			'Funk',
			'Dance',
			'Pop',
			'Metal',
			'Easy Listening',
			'Hits',
			'Opera',
			'Classical',
			]

# create nested dictionary
def subscriberRatings():
	subscriber_ratings = {}
	num_genres = len(music_genres)
	for p in subscribers:
		subscriber_ratings[p] = {}
		num_ratings = randint(num_genres/3, num_genres*2/3)
		chosen_genres = sample(music_genres, num_ratings)
		for f in chosen_genres:
			subscriber_ratings[p][f] = randint(1, 10)
	return subscriber_ratings

# function accepts no input and returns a pre made nested subscriber dictionary for use in testing
def testSubscriberRatings():
	test_dict= {"Justin Trudeau":{'Easy Listening': 10, 'Pop': 5, 'Dance': 6, 'Jazz': 8, 'Hits': 6, 'Country': 5, 'Opera': 3, 'Rock': 7, 'Metal': 4},
	"Bob Jones":{'Easy Listening': 10, 'Pop': 7, 'Dance': 6, 'Jazz': 8, 'Hits': 9, 'Country': 5, 'Opera': 3, 'Rock': 7, 'Metal': 4},
	"Sam Frizzel":{'Blues': 4, 'Classical': 10, 'Reggae': 8, 'Funk': 5, 'Soul': 1, 'Jazz': 7},
	"Captain Nemo":{'Dance': 2, 'Metal': 9, 'EDM': 8, 'Hits': 2, 'Blues': 6, 'Hip Hop': 10, 'World': 10, 'Jazz': 4, 'Easy Listening': 6, 'Country': 8},
	"Joe Jameson":{'Pop': 4, 'EDM': 6, 'Blues': 8, 'Rock': 7, 'Soul': 1, 'Metal': 6, 'Funk': 1},
	"Paul Casindes":{'Blues': 2, 'Dance': 8, 'Hip Hop': 7, 'EDM': 5, 'Soul': 3, 'Easy Listening': 5, 'Jazz': 6},
	"Justin Bieber":{'Country': 1, 'World': 2, 'Hip Hop': 5, 'Soul': 4, 'Jazz': 7, 'EDM': 4, 'Opera': 3, 'Hits': 10, 'Dance': 2},
	"Natlie Portman":{'Dance': 7, 'Blues': 10, 'Soul': 9, 'Reggae': 1, 'Pop': 10, 'Rap': 7},
	"Bugs Bunny":{'Country': 6, 'Rap': 6, 'Classical': 6, 'Funk': 10, 'Pop': 1, 'Dance': 8},
	"Peter Rabbit":{'Soul': 3, 'EDM': 9, 'Country': 5, 'Hip Hop': 9, 'Reggae': 5, 'Blues': 6, 'Rock': 10},
	"Mickey Mouse":{'Funk': 5, 'Jazz': 8, 'World': 3, 'Opera': 1, 'Rock': 7, 'Soul': 4, 'Easy Listening': 9, 'Classical': 5, 'EDM': 5, 'Pop': 3, 'Hip Hop': 10, 'Rap': 2},
	"Martin Melchor":{'Rap': 9, 'Opera': 1, 'Blues': 9, 'Reggae': 3, 'Soul': 9, 'World': 10},
	"Nada Neel":{'Rap': 5, 'Blues': 1, 'Dance': 5, 'Hits': 5, 'Pop': 2, 'Reggae': 10, 'EDM': 1, 'Rock': 7, 'Soul': 4, 'Funk': 3, 'Classical': 4},
	"Kristin Karlin":{'Rap': 3, 'Hits': 5, 'Soul': 5, 'Metal': 9, 'EDM': 2, 'Classical': 5, 'Easy Listening': 9},
	"Edmond Earls":{'Pop': 2, 'Hits': 8, 'Reggae': 10, 'Easy Listening': 5, 'Rap': 10, 'Rock': 2},
	"Fredrick Foxwell":{'Metal': 8, 'Country': 2, 'Opera': 5, 'Easy Listening': 7, 'Soul': 6, 'Hip Hop': 1, 'World': 2, 'Blues': 4},
	"Thomas Twitty":{'Easy Listening': 4, 'Hits': 8, 'Jazz': 9, 'Classical': 10, 'Rap': 1, 'Pop': 7, 'Rock': 4},
	"Julieann Jenning":{'Funk': 2, 'Jazz': 5, 'Metal': 5, 'Hits': 10, 'Rap': 9, 'Hip Hop': 6},
	"Anton Autin":{'Soul': 6, 'World': 4, 'Easy Listening': 3, 'Rock': 3, 'Reggae': 7, 'Pop': 6, 'Rap': 5, 'Funk': 3, 'Hip Hop': 9, 'Country': 10, 'Jazz': 6, 'EDM': 10},
	"Alix Ashmore":{'Rock': 4, 'Reggae': 9, 'Pop': 6, 'Funk': 10, 'Rap': 4, 'Hip Hop': 6, 'Jazz': 4, 'EDM': 4, 'Country': 8, 'Blues': 8},
	"Tiffany Turgeon":{'Opera': 10, 'Hits': 6, 'Metal': 9, 'Rock': 6, 'Pop': 10, 'Jazz': 1},
	"Noella Nash":{'Pop': 9, 'World': 8, 'Metal': 5, 'Jazz': 5, 'Classical': 8, 'Country': 3, 'Funk': 1, 'Dance': 2, 'Reggae': 3, 'Soul': 3, 'Rap': 3},
	"Esther Edgerton":{'Pop': 5, 'Metal': 6, 'Rock': 2, 'Opera': 8, 'EDM': 4, 'Hits': 1, 'World': 9, 'Easy Listening': 10, 'Reggae': 10},
	"Sanda Sewart":{'Rap': 3, 'Easy Listening': 2, 'Hits': 8, 'Jazz': 5, 'Country': 8, 'Reggae': 5, 'Classical': 3},
	"Fannie Ferrera":{'Pop': 9, 'Easy Listening': 4, 'EDM': 8, 'Rap': 9, 'Reggae': 9, 'Hip Hop': 4, 'Hits': 9},
	"Bernardine Block":{'Hits': 5, 'Jazz': 7, 'Soul': 4, 'Pop': 8, 'Dance': 5, 'Funk': 4, 'Opera': 10, 'EDM': 8, 'Classical': 2},
	"Roger Rudd":{'World': 7, 'Jazz': 8, 'Rap': 6, 'Rock': 9, 'Blues': 4, 'Metal': 6, 'Country': 7, 'Funk': 6},
	"Yang Wu":{'EDM': 2, 'Rock': 10, 'Soul': 1, 'Hits': 5, 'Opera': 2, 'Reggae': 7, 'Classical': 10, 'Hip Hop': 8, 'Funk': 4},
	"Raisa Rohr":{'World': 9, 'Reggae': 2, 'Classical': 1, 'Rap': 4, 'Opera': 1, 'Easy Listening': 4, 'Hits': 4, 'Rock': 2},
	"Cirocco Jones":{'Soul': 5, 'Rap': 4, 'Blues': 8, 'Metal': 4, 'Hip Hop': 4, 'Easy Listening': 4, 'Reggae': 9, 'Funk': 7},
	"Mickie Milling":{'Jazz': 5, 'Easy Listening': 5, 'Funk': 3, 'EDM': 1, 'Hip Hop': 2, 'Opera': 9, 'Rock': 10, 'Metal': 5, 'World': 5, 'Classical': 1},
	"Ronald McDonald":{'Pop': 8, 'Classical': 9, 'Opera': 6, 'Metal': 8, 'Rap': 5, 'Hip Hop': 6, 'EDM': 9, 'Funk': 7},
	"Tim Horton":{'Dance': 6, 'Country': 9, 'Rap': 2, 'Metal': 1, 'Soul': 6, 'Opera': 6, 'World': 8, 'Rock': 8, 'EDM': 7, 'Classical': 5, 'Reggae': 8, 'Funk': 2},
	"Colonel Sanders":{'Dance': 3, 'Hits': 6, 'Classical': 3, 'Rap': 1, 'EDM': 2, 'Funk': 9, 'Reggae': 5, 'World': 8, 'Soul': 4, 'Hip Hop': 9},
	"Joel Jerry":{'Rock': 9, 'Classical': 8, 'EDM': 3, 'Hits': 9, 'Reggae': 8, 'Pop': 9, 'Hip Hop': 8, 'Easy Listening': 9, 'Soul': 3, 'Funk': 10},
	"Leanora Lion":{'Opera': 6, 'Metal': 7, 'Country': 8, 'Rap': 9, 'Pop': 3, 'Blues': 10, 'Rock': 2},
	"Oscar Oliverio":{'Rap': 5, 'Blues': 2, 'Rock': 6, 'Jazz': 2, 'Easy Listening': 6, 'Reggae': 9, 'Hits': 4, 'Soul': 3},
	"Jernau Fortier":{'Country': 3, 'Jazz': 5, 'Opera': 8, 'Soul': 8, 'Easy Listening': 5, 'EDM': 10, 'World': 5, 'Pop': 8, 'Hits': 1},}
	return test_dict
'''
genre similarity accepts parametres subscriber_rating which contains the nested dictionary containing
customer preferences and custName1 and custName2 which are inputted in the commandPrompt function in
the user interface module. This calculates the similarity value between the two subscribers using the
calculations outlined in the assignment
'''
def genre_similarity(ratings, custName1, custName2):
	sub1sum = 0
	sub2sum = 0
	intersection_sum = 0
	store_user1= {}
	store_user2 = {}
	store_user1 = ratings[custName1] 
	store_user2 = ratings[custName2]
	for genre in ratings[custName1]:
		sub1sum+=ratings[custName1][genre]
	for genre in ratings[custName2]:
		sub2sum+=ratings[custName2][genre]				
	for genre1 in store_user1:
		for genre2 in store_user2:
			if genre1 == genre2:
				genre_value = min(ratings[custName1][genre1], ratings[custName2][genre2])
				intersection_sum +=genre_value
	similarity_value = min((intersection_sum/sub1sum), (intersection_sum/sub2sum))
	return similarity_value
	
'''
This function accepts subscriber_rating which contains the nested dictionary containing customer
preferences and custName as a parameter. It finds the most similar subscriber to custName using
the values calculated in genre_similarity
'''
def match_subscribers(subscriber_ratings, custName):
	similarity_info = [] #stores a users 
	for subscriber in subscriber_ratings:
		# if condition ensures that the inputted name is not returned as the most similar user
		if subscriber.lower() == custName.lower():
			pass #ensures that the matched subscriber is not same as the inputted subscriber
		else:
			user_dict = {}
			user_dict['Name'] = subscriber
			user_dict['Similarityval'] = genre_similarity(subscriber_ratings, custName, subscriber) #uses genre_similarity to calculate the value
			similarity_info.append(user_dict)
	max_value = {'Name': "Nothing", 'Similarityval': 0} #sets value to nothing and stores the value that is highest
	for user in similarity_info:
		if user['Similarityval'] > max_value['Similarityval']:
			max_value = user
	return max_value

'''
This function counts and stores user ratings given the nested dictionary of their preferences and
returns the average rating for all genres
'''
def average_rating(subscriber_ratings):
	values_dict = {} #stores values for each genre in a dictionary
	averages_dict = {}
	for subscriber in subscriber_ratings:
		for genre, value in subscriber_ratings[subscriber].items():
			'''			
			checks the name of all subscriber preferences and stores the values for existing genres
			in their respective dictionary elements, if a genre does not have a dictionary element 
			it creates one
			'''
			if genre in values_dict:
				values_dict[genre].append(value)
			else:
				values_dict[genre] = []
				values_dict[genre].append(value)
	for genre in values_dict:
		averages_dict[genre] = round(statistics.mean(values_dict[genre]),1)
	return averages_dict

'''
This function takes parameter average_dict which is generated using average_rating() and returns
the top 3 genres with the highest average ratings
'''
def most_popular(average_dict):
	print("Top 3 Most Popular Genres, with average scores:")
	first = max(average_dict, key=average_dict.get)
	print(first + ": " + str(average_dict[first]))
	average_dict.pop(first)#pop function allows me to find the the top 3 values
	second = max(average_dict, key=average_dict.get)
	print(second + ": " + str(average_dict[second]))
	average_dict.pop(second)
	third  = max(average_dict, key=average_dict.get)
	print(third + ": " + str(average_dict[third]))

'''
Given a customer name and the nested dictionary of ratings, this function finds a user that
is most similar and suggests the genre that that user has rated the highest, the genre
suggested cannot be one that the given user has already rated
'''
def recommend_genre(subscriber_ratings, name, test = None):
	recommended_list = []
	recommended_list_values = []
	most_similar = match_subscribers(subscriber_ratings, name)
	#checks to make sure subscribers are not the exact same because it would not be able to suggest genres
	if most_similar['Similarityval'] == 1:
		subscriber_ratings.pop(most_similar['Name'])
		return recommend_genre(subscriber_ratings, name, test)
	if most_similar['Similarityval'] < 1:
		for genre in subscriber_ratings[most_similar['Name']]:
			if genre not in subscriber_ratings[name]:
				recommended_list_values.append(subscriber_ratings[most_similar['Name']][genre])
				recommended_list.append(genre)
		if recommended_list_values == []:
			subscriber_ratings.pop(most_similar['Name'])
			return recommend_genre(subscriber_ratings, name, test)
		else:
			max_value = max(recommended_list_values)
			index = recommended_list_values.index(max_value)
			if test == None:#test parameter prints when not active and returns when active
				print("Comparing your listening to others, we recommend you listen to", recommended_list[index])
			else:
				return recommended_list[index]

'''
Given a customer name and the nested dictionary, this function checks that a subscriber by
that name exists and returns their name in proper form, or the respective error message
This function also has the option to add a test parameter which simply returns the error
message instead of printing it for easier test display.
'''
def checkName(subscriber_ratings, prompt, test = None):
	if test == None:
		subscriberName = input(prompt)
	else:
		subscriberName = test
	search_name = []
	for subscriber in subscriber_ratings:
		if subscriber.lower() == subscriberName.lower():
			search_name.append(subscriber)
			return search_name[0]
	if search_name == []:
		if test == None:#test parameter prints when not active and returns when active
			print("Hmmm, we don't have that name in our database, please try again.")
			return checkName(subscriber_ratings, prompt)
		else:
			return "Hmmm, we don't have that name in our database, please try again."

'''
This function tests every function in both commands.py and user_interface.py to ensure
that the program never encounters an error
'''
def unit_test():
	subscriber_ratings = testSubscriberRatings()
	test_name_error = ['daJNJDnkjn', '123456', 'qmskqmksmq']
	test_name_accept_1 = ['JUSTIN TRUDEAU', 'jUsTiN tRuDeAu']
	test_name_accept_2 = ['Justin Trudeau', 'Captain Nemo', 'Joe Jameson', 'Noella Nash', 'Tim Horton'] # inputs are cleaned because checkName function finds correct format
	result_similarity = ['~0.3235', '~0.3538', '~0.2769', '~0.2200', '~0.4118']
	results_match = ['Bob Jones', 'Anton Autin', 'Peter Rabbit', 'Roger Rudd', 'Anton Autin']
	print("Running Unit Testing")
	print("\nTesting Menu...")
	print("For input", 1, "Should return 'Please enter the name of the first customer you would like to compare.'", user_interface.commandPrompt(subscriberRatings, 1))
	print("For input", 2, "Should return 'Please enter the name of the person who you would like to find a match for.'", user_interface.commandPrompt(subscriberRatings, 2))
	print("For input", 3, "Should return 'Average Search'", user_interface.commandPrompt(subscriberRatings, 3))
	print("For input", 4, "Should return 'Most Popular'", user_interface.commandPrompt(subscriberRatings, 4))
	print("For input", 'a', "Should return Invlaid input, please try again,", user_interface.commandPrompt(subscriber_ratings, 'a'))
	print("For input", 'mcakmkds', "Should return Invlaid input, please try again,", user_interface.commandPrompt(subscriber_ratings, 'mcakmkds'))
	print("For input", 'Quit', "Should return Invlaid input, please try again,", user_interface.commandPrompt(subscriber_ratings, 'Quit'))
	#for error in test_menu_error:
	#	print("For input", error, "Should return 'Invalid Input, please try again'", user_interface.commandPrompt(subscriber_ratings, error))
	print("\nTesting checkName function")
	for error in test_name_error:
		print("For input", error, "Should return 'Hmmm, we don't have that name in our database, please try again.'", checkName(subscriber_ratings, " ", error))
	for accept in test_name_accept_1:
		print("For input", accept, "Should return 'Justin Trudeau.'", checkName(subscriber_ratings, "", accept))
	print("\nTesting Genre Similarity...")
	for accept in range(len(test_name_accept_2)):
		print("For input", test_name_accept_2[accept-1], ",", test_name_accept_2[accept], "Should return", result_similarity[accept], ",", genre_similarity(subscriber_ratings, test_name_accept_2[accept-1], test_name_accept_2[accept]))
	print("\nTesting Match Subscribers...")
	for accept in range(len(test_name_accept_2)):
		print("For input", test_name_accept_2[accept], "Should return profile for", results_match[accept], match_subscribers(subscriber_ratings, test_name_accept_2[accept]))
	print("\nTesting Average Rating...")
	print("Should return 6.2", ",", average_rating(subscriber_ratings)['Easy Listening'])
	print("Should return 6.1", ",", average_rating(subscriber_ratings)['Pop'])
	print("Should return 5", ",", average_rating(subscriber_ratings)['Dance'])
	print("\nTesting Most Popular")
	print("Should return\nTop 3 Most Popular Genres, with average scores:\nReggae: 6.7\nHip Hop: 6.5\nWorld: 6.4")
	most_popular(average_rating(subscriber_ratings))
	print("\nTesting Genre Recommendation...")
	print("Should return 'Classical',", recommend_genre(subscriber_ratings, 'Justin Trudeau', 'Test'))



def main():
	unit_test()
	subscriber_ratings = subscriberRatings()
	user_interface.commandPrompt(subscriber_ratings)

if __name__ == "__main__":
	main()