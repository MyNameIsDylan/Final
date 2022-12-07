def prob():
    global probability_of_all_characters_list
    global total_prob
    def n_frequent_character():

        temp_file = open('Final/Word.txt','a+') # opens word.txt assigns to temp_file in a+ mode
        temp_file.seek(0) # goes to the start of word.txt file
 
        characters_in_file = [] # holds all characters from word_file
        # iterates through characters_in_file and counts appearances of every char saves to character_appearances
        for line in temp_file: 
            line = line.lower()
            for character in line:
                if character == '\n': #special case for \n 
                    characters_in_file.append('\ n')
                elif character != '\n':
                    characters_in_file.append(character)

        character_appearances_dict = dict() # holds num of appearances of chars
        # iterates through characters_in_file and counts appearances of every char saves to character_appearances_dict
        for i in characters_in_file:
            character_appearances_dict[i]=character_appearances_dict.get(i,0)+1
        #print('char count is',character_appearances_dict)
        
        return character_appearances_dict

    character_appearances_dict = n_frequent_character()

    probability_of_all_characters_list = [] #hold the character and its probability
    frequencies_of_all_characters = 0 # holds total num of characters

    for i in character_appearances_dict: # sum total frequencies of all characters
        frequencies_of_all_characters = frequencies_of_all_characters + character_appearances_dict[i]
        
    total_prob = 0

    for i in character_appearances_dict: # iterates and find individual probability of each character and appends to probability_of_all_characters_list
        frequencey_of_char = character_appearances_dict[i] # takes num of char
        probability_of_char = frequencey_of_char/frequencies_of_all_characters
        total_prob = total_prob + probability_of_char
        letter,probability = i,round(probability_of_char,4)
        letter_and_probability = letter,probability
        probability_of_all_characters_list.append(letter_and_probability)

prob()