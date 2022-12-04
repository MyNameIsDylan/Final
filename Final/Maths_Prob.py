


def prob():
    global probability_of_char_list
    global total_prob
    def n_frequent_character():
        temp_file = open('Final/Word.txt','a+') # opens word.txt assigns to temp_file in a+ mode
        temp_file.seek(0) # goes to the start of word.txt file
        #print(temp_file.read()) # prints the whole word.txt file

        char_track = [] # holds all characters from temp_file
        # loop to iterate through temp_file and append each char to char_track
        for line in temp_file: 
            line = line.lower()
            #print(line)
            for character in line:
                if character == '\n': #special case for \n 
                    char_track.append('\ n')
                elif character != '\n':
                    char_track.append(character)

        char_count = dict() # holds num of appearances of chars
        # iterates through char_track and counts appearances of every char saves to char_count
        for i in char_track:
            char_count[i]=char_count.get(i,0)+1
        #print('char count is',char_count)
        
        return char_count
    char_count = n_frequent_character()

    probability_of_char_list = [] #hold the character and its probability

    frequencies_of_all_char = 0 # holds total num of characters

    for i in char_count: # sum total frequencies of all characters
        frequencies_of_all_char = frequencies_of_all_char + char_count[i]
        
    total_prob = 0

    for i in char_count: # iterates and find individual probability of each character and appends to probability_of_char_list
        frequencey_of_char = char_count[i] # takes num of char
        probability_of_char = frequencey_of_char/frequencies_of_all_char
        #print('frequencey of',i,'is',frequencey_of_char)
        #print('probability of',i,'is',probability_of_char)
        total_prob = total_prob + probability_of_char
        let,prob = i,round(probability_of_char,4)
        letandprob = let,prob
        probability_of_char_list.append(letandprob)

    #print(probability_of_char_list)


prob()