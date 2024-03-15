def text_enter():
    file  = open(filename,"w+")
    text = input("Enter the text: ")
    file.write(text)
    file.close()

def sentence_count():
    file = open(filename,"r")
    list = file.read()
    list = list.split(".")
    count = len(list)
    sent_c = count
    print("Number of sentences in the file: ",count)
    file.close()
    return count


def word_count():
    file = open(filename,"r")
    list = file.read()
    list = list.split()
    count = len(list)
    word_c = count
    print("Number of words in the file: ",count)
    file.close()
    return count

def syllab_count():
    s_count = 0
    file = open(filename,"r")
    list = file.read()

    [word.lower() for word in list]
    list = list.split()

    vowels = "aeiou"
    for word in list:
        for vowel in vowels:
            s_count += word.count(vowel)
        for ending in ['es', 'ed', 'e']:
            if word.endswith(ending):
                s_count -= 1
        if word.endswith('le'):
                s_count += 1
    sy_count = s_count
    print("Number of syllabels: ", s_count)
    file.close()
    return s_count

def  grade():
    index = 206.835 - 1.015 * (word_c / sent_c) - 84.6 * (sy_count / word_c)
    level = round(0.39 * (word_c / sent_c) + 11.8 * (sy_count / word_c) - 15.59)
    print("Flesch Index: ",index)
    print("Grade level: ",level)



filename = input("Enter the name of the file: ")
filename += ".txt"

text_enter()

sent_c = sentence_count()
word_c = word_count()
sy_count = syllab_count()
grade()
