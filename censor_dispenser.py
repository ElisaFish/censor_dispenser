# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

import string
import re

char_censor = '*'

# Censor single word, every instance in text.
# Accounts for spaces, punctuation, and case.
def censor(term, text):
    new_text = text

    whitespace_punctuation = []
    for char in (string.whitespace + string.punctuation):
        whitespace_punctuation.append(char)
    plurals = []
    for char in whitespace_punctuation:
        plurals.append('s' + char)
    
    suffices = whitespace_punctuation + plurals

    translation = []
    for prefix in whitespace_punctuation:
        for suffix in (suffices):
            value = prefix + (char_censor * len(term)) + suffix
            key = prefix + term + suffix
            translation.append([key, value])
            key = prefix + term.capitalize() + suffix
            translation.append([key, value])
            key = prefix + term.upper() + suffix
            translation.append([key, value])

    for key, value in translation:
        new_text = new_text.replace(key, value)
    
    return new_text


email_one_redacted = censor('learning algorithms', email_one)
print(email_one_redacted)

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

# Censors a list of terms
def censor_list(term_list, text):
    new_text = text

    for term in term_list:
        new_text = censor(term, new_text)

    return new_text


email_two_redacted = censor_list(proprietary_terms, email_two)
print(email_two_redacted)

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

# Censors all but the first occurance of a negative word, and a list of terms
def censor_negative(term_list, text):
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
        new_text = new_text.replace(char_censor * len(first_neg), first_neg, 1)

    return censor_list(term_list, new_text)


print(censor_negative(proprietary_terms, email_three))

# Censors all words in a list, and the words that come before and after the censored term
def censor_surrounding(term_list, text):
    censor_terms = term_list + negative_words

    # Using previous functions
    new_text = censor_list(censor_terms, text)
    index = 0
    end = len(text)
    index = new_text.find(char_censor, index, end)
    while index != -1:
        #Censor word before
        match = re.findall("\s", new_text[:index-1])
        if match:
            whitespace = match[-1]
        else:
            whitespace = ' '
        before = new_text.rfind(whitespace, 0, index-1)
        word_before = new_text[before+1: index-1]
        new_text = new_text[:before+1] + (char_censor * len(word_before)) + new_text[index-1:]

        # Censor word after
        match = re.findall("\s", new_text[index:])
        if match:
            whitespace = match[0]
            whitespace_after = match[1]
        else:
            whitespace = ' '
            whitespace_after = ' '

        eow = new_text.find(whitespace, index, end)
        after = new_text.find(whitespace_after, eow+1, end)
        new_text = new_text[:(eow + 1)] + (char_censor * (after - (eow+1))) + new_text[after:]

        # Find word
        index = new_text.find(char_censor, after, end)
    
    return new_text

print(censor_surrounding(proprietary_terms, email_four))

