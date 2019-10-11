# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

import string

#def create_mask(term):
#    mask = ""
#    for i in range[0,len(term)]:
#        mask += 'X'
#    return mask

def censor(term, text):
    #term_mask = 'X' * len(term)
    new_text = text
    #new_text = new_text.replace(string, "REDACTED")
    #whitespace_punctuation = [' ']
    #whitespace_punctuation.append(string.whitespace)
    #for c in string.punctuation:
    #    whitespace_punctuation.append(str(c))
    #translation = []
    #for prefix in whitespace_punctuation:
    #    for suffix in whitespace_punctuation:
    #        key = prefix + term + suffix
    #        value = prefix + term_mask + suffix
    #        translation.append(text.maketrans(key, value))
            #translation[key] = value
    #print(translation)
    #new_text = text.translate(translation)

    new_text = new_text.replace(' ' + term + ' ', ' ' + 'X' * len(term) + ' ')
    new_text = new_text.replace(term.capitalize() + ' ', 'X' * len(term) + ' ')
    new_text = new_text.replace(' ' + term + "s ", ' ' + 'X' * len(term) + 's ')
    new_text = new_text.replace(' ' + term + "s.", ' ' + 'X' * len(term) + "s.")
    new_text = new_text.replace(term.capitalize() + "s ", 'X' * len(term) + "s ")
    new_text = new_text.replace(" " + term + ".", ' ' + 'X' * len(term) + '.')
    new_text = new_text.replace(" " + term + ",", ' ' + 'X' * len(term) + ',')
    new_text = new_text.replace(" " + term.capitalize() + ",", ' ' + 'X' * len(term) + ',')
    new_text = new_text.replace(term.capitalize() + ",", 'X' * len(term) + ',')
    new_text = new_text.replace(" " + term + "!", ' ' + 'X' * len(term) + '!')
    new_text = new_text.replace(" " + term + "?", ' ' + 'X' * len(term) + '?')
    new_text = new_text.replace("(" + term, "(" + 'X' * len(term))
    return new_text
    #return text.translate(translation)

#def new_censor(term, text):

email_one_redacted = censor('learning algorithms', email_one)
print(email_one_redacted)

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_list(term_list, text):
    new_text = text
    #dictionary = {}
    #translation = []
    for term in term_list:
        #dictionary[term] = "X" * len(term)
        #translation.append(text.maketrans(term, 'X' * len(term)))
        new_text = censor(term, new_text)
        #new_text = censor(term.capitalize(), new_text)
    #print(translation)
    return new_text
    #return text.translate(dictionary)
    #return text.translate(translation)

email_two_redacted = censor_list(proprietary_terms, email_two)
print(email_two_redacted)

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_negative(term_list, text):
    #found_negative = False
    new_text = text
    neg_indices = []
    for term in negative_words:
        index_tuple = [text.find(term), term]
        if index_tuple[0] != -1:
            neg_indices.append(index_tuple)
    if len(neg_indices) > 1:
        neg_indices.sort()
        first_neg = neg_indices[0][1]
        new_text = censor_list(negative_words, text)
        new_text = new_text.replace('X' * len(first_neg), first_neg, 1)
    
    ###### Iterate through text ######
    #for word in text:
    #    if word in negative_words:
    #       if found_negative:
    #            new_text = text.replace(word.lower(), 'X' * len(word), 1)
    #       elif word in negative_words and not found_negative:
    #        found_negative = True

    return censor_list(term_list, new_text)

#print(email_three)
print(censor_negative(proprietary_terms, email_three))

def censor_surrounding(term_list, text):
    censor_terms = term_list + negative_words

    # Attempt 2
    for term in censor_terms:
        new_text = text
        index = 0
        end = len(text)
        index = text.find(term, index, end)
        while index != -1:
            # Censor word
            new_text = new_text.replace(term, 'X' * len(term), 1)

            #Censor word before
            before = new_text.rfind(string.whitespace, 0, index-1)
            word_before = new_text[before+1: index-2]
            new_text = new_text[:before] + 'X' * len(word_before) + new_text[index-1:]
            #new_text.replace(word_before, 'X' * len(word_before), before, index)

            # Censor word after
            after = new_text.find(string.whitespace, index+len(term)+2, end)
            new_text = new_text[:index+len(term) + 1] + 'X' * (after - (index+len(term)+2)) + new_text[after:]

            # Find word
            index = text.find(term, index, end)

    return new_text

print(censor_surrounding(proprietary_terms, email_four))
        
    #new_text = censor_negative(, email_four)
    
    #for i in range(0, len(split_text)):
    #    if (split_text[i] in term_list) or (split_text[i] in negative_words):
    #        split_text[i-1] = 'X' * len(split_text[i-1])
    #        split_text[i] = 'X' * len(split_text[i])
    #        split_text[i+1] = 'X' * len(split_text[i+1])

    #split_text = text.split(' ')
    #for counter, word in list(enumerate(split_text(' '))):
    #    if (word.lower() in term_list) or (word.lower() in negative_words):
    #        split_text[counter-1] = split_text[counter-1].replace(split_text[counter-1], 'X' * len(split_text[counter-1]))
    #        split_text[counter] = split_text[counter].replace(split_text[counter], 'X' * len(split_text[counter]))
    #        split_text[counter+1] = split_text[counter+1].replace(split_text[counter+1], 'X' * len(split_text[counter+1]))
    
    #combined_text = ' '.join(split_text)
    #return combined_text

    #four_censored = censor_surrounding(proprietary_terms, email_four)
    #print(four_censored)

