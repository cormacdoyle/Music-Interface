import commands

'''
This function acts as the menu, it takes user inputs and direct them to a respective function
This function takes subscriber_ratings as a paramter, this function allows the nested list
of subscriber preferences to be moved across functions. This function also has the option for
a test parametre which is used in the unit_test function in commands.py to ensure the function
receives input correctly
'''
def commandPrompt(subscriber_ratings, test = None):
    if test == None:
            chooose_function = input(
        "\nWhat function would you like to perform?('1' to see how similar you and a friend are, '2' to see which user is most similar to you, '3' to see average genre ratings. '4' to see the most popular genres, '5' to recommend genres, Press 'Q' to Quit)\n")

    else:
        chooose_function = str(test)
            
    if chooose_function == '1':
        return genreSimilarityPrompt(subscriber_ratings, test)

    if chooose_function == '2':
        return matchUsersPrompt(subscriber_ratings, test)

    if chooose_function == '3':
        if test == None:
            averages_list = commands.average_rating(subscriber_ratings)
            print("Here are your averages")
            for genre in averages_list:
                print(genre +": " + str(averages_list[genre]))
            commandPrompt(subscriber_ratings)
        else:
            return "Average Search"
    if chooose_function == '4':
        if test == None:
            averages_list = commands.average_rating(subscriber_ratings)
            commands.most_popular(averages_list)
            commandPrompt(subscriber_ratings)
        else:
            return "Most Popular"
    if chooose_function == '5':
        recommendGenrePrompt(subscriber_ratings)
        commandPrompt(subscriber_ratings)
    if chooose_function.lower() == 'q':
        quit()
    if test==None:
        print("Invalid Input, please try again.")
        commandPrompt(subscriber_ratings)
    else:
        return "Invalid Input, please try again"

'''
This function prompts the user for two customer names, and then checks to make sure the subscribers
exist and returns their name in the proper format (checkName function does this). It then runs the
genre_similarity function in commands.py and prints its output. Finally it runs commandPrompt again
to bring the user back to the menu. This function has the option for a test parametre which instead
returns the ouput instead output instead or printing.
genreSimilarityPrompt is not tested for inputs, because it's inputs are locked by checkName.
'''
def genreSimilarityPrompt(subscriber_ratings, test = None):
    if test == None:
        subscriberName1 = commands.checkName(subscriber_ratings, "Please enter the name of the first customer you would like to compare.\n")
        subscriberName2 = commands.checkName(subscriber_ratings, "Please enter the name of the second customer you would like to compare\n")
        similarity_value = commands.genre_similarity(subscriber_ratings, subscriberName1, subscriberName2)
        similarity_percent = str(round((similarity_value*100), 4)) + "%"
        print("These users are", similarity_percent, "similar.")
        commandPrompt(subscriber_ratings)
    else:
        return "Please enter the name of the first customer you would like to compare."
    
'''
This function prompts the user for a customer names, and then checks to make sure the subscriber
exists and returns their name in the proper format (checkName function does this). It then runs the
match_subscribers function in commands.py and prints its output. Finally it runs commandPrompt again
to bring the user back to the menu. This function has the option for a test parametre which instead
returns the ouput instead output instead or printing.
matchUsersPrompt is not tested for inputs, because it's inputs are locked by checkName
'''
def matchUsersPrompt(subscriber_ratings, test=None):
    if test == None:
        subscriberName = commands.checkName(subscriber_ratings, "Please enter the name of the person who you would like to find a match for.\n")
        user_match = commands.match_subscribers(subscriber_ratings, subscriberName)
        print(user_match['Name'], "has the most similar music taste to", subscriberName, "with a", round(user_match['Similarityval']*100, 4),  "% similarity value")
        commandPrompt(subscriber_ratings)
    else:
        return "Please enter the name of the person who you would like to find a match for."

'''
This function prompts the user for a customer names, and then checks to make sure the subscriber
exists and returns their name in the proper format (checkName function does this). It then runs the
recommend_genre function in commands.py. Finally it runs commandPrompt again to bring the user back 
to the menu.
recommendGenrePrompt is not tested for inputs, because it's inputs are locked by checkName
'''
def recommendGenrePrompt(subscriber_ratings):
    name = commands.checkName(subscriber_ratings, "Please enter the name of a user.\n")
    commands.recommend_genre(subscriber_ratings, name)
    commandPrompt(subscriber_ratings)