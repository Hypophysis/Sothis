import syllables
pamphlet_str = str("")

with open('*insert_text_file_path_here*', 'r') as pamphlet:
    pamphlet_str = pamphlet.read().replace('\n', ' ')

word_list = pamphlet_str.split(" ")
word_syllables = {}
for i in word_list:
    word_syllables[i] = syllables.estimate(i)

count = 0
#count [int]: defines number of words with syllable count ≥ 3

for value in word_syllables.values():  
    if value >= 3: 
        count += 1

sentence_count = pamphlet_str.count(".")


# SMOG FORMULA =  (Reading grade level = 3 + √[no. of words with 3 or more syllables] × [30 / no. of sentences])
SMOG_level= 3 + (count*(30/sentence_count))**(1/2)
print("SMOG Level", SMOG_level)

