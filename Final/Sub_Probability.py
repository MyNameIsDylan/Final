from Main_Final import char_count_list
from Main_Final import char_count

def prob():

    def sortbykey(elem):
        return elem[1]

    # frequencey_of_char = 

    # frequencies_of_all_char = 

    # probability_of_char = frequencey_of_char/sum(frequencies_of_all_char)

    frequencies_of_all_char = 0
    for i in char_count:
        frequencies_of_all_char = frequencies_of_all_char + char_count[i]
        frequencey_of_char = char_count[i] # takes num of char
        #print(frequencies_of_all_char,'all char till now including current ',frequencey_of_char)
        probability_of_char = frequencey_of_char/frequencies_of_all_char
        print('frequencey of',i,'is',frequencey_of_char)
        print('probability of',i,'is',probability_of_char)

    print(frequencies_of_all_char)

prob()