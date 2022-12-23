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

        return character_appearances_dict

    character_appearances_dict = n_frequent_character()

    character_appearances_list = [] # holds letter and value (let,val) in tuple pair in list value=appearances of letter
    for i in character_appearances_dict: # converts character_appearances from dict to list
        letter,appearances = i,character_appearances_dict[i]
        letter_and_appearances = (letter,appearances)
        character_appearances_list.append(letter_and_appearances)

    nac = 0
    for item in character_appearances_list:
        if item[0] == '\\ n' or item[0] == ' ' or item[0] == ',' or item[0] == '.' or item[0] == ';':
            nac = nac + item[1]
        else:
            pass
    non_alphabetical_charcters = ('non_alphabetical_characters',nac)
    for item in character_appearances_list:
        if item[0] == '\\ n' or item[0] == ' ' or item[0] == ',' or item[0] == '.' or item[0] == ';':
            character_appearances_list.remove(item)
        else:
            pass
    character_appearances_list.append(non_alphabetical_charcters)

    probability_of_all_characters_list = [] #hold the character and its probability
    frequencies_of_all_characters = 0 # holds total num of characters

    for i in character_appearances_list: # sum total frequencies of all characters
        frequencies_of_all_characters = frequencies_of_all_characters + i[1]
        
    total_prob = 0

    for item in character_appearances_list: # iterates and find individual probability of each character and appends to probability_of_all_characters_list
        frequencey_of_char = item[1] # takes num of char
        probability_of_char = frequencey_of_char/frequencies_of_all_characters
        total_prob = total_prob + probability_of_char
        letter,probability = item[0],round(probability_of_char,4)
        letter_and_probability = letter,probability
        probability_of_all_characters_list.append(letter_and_probability)
        
    #print('math_prob probability of all characters list',probability_of_all_characters_list)
prob()