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
    space_string = ' ' + term + ' '
    new_text = new_text.replace(space_string, " REDACTED ")
    cap_string = term.capitalize() + ' '
    new_text = new_text.replace(cap_string, "REDACTED ")
    plural = ' ' + term + "s "
    new_text = new_text.replace(plural, " REDACTED ")
    plural_caps = term.capitalize() + "s "
    new_text = new_text.replace(plural_caps, "REDACTED ")
    new_text = new_text.replace(" " + term + ".", " REDACTED.")
    new_text = new_text.replace(" " + term + ",", " REDACTED,")
    new_text = new_text.replace(" " + term + "!", " REDACTED!")
    new_text = new_text.replace(" " + term + "?", " REDACTED?")
    new_text = new_text.replace("(" + term, "(REDACTED")
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
    found_negative = False
    #new_text = text
    #neg_indices = []
    #for term in negative_words:
    #    index_tuple = [text.find(term), text.rfind(term)]
    #    if index_tuple[0] != -1:
    #        neg_indices.append(index_tuple)
    #if len(neg_indices) > 1:
    #    neg_indices.sort()
    
    ###### Iterate through text ######
    for word in text:
        if word in negative_words:
            if found_negative:
                text = text.replace(word, "REDACTED")
            found_negative = True

    return censor_list(term_list, text)

print(email_three)
print(censor_negative(proprietary_terms, email_three))