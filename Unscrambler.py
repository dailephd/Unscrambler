#Input function
def input_msg():
    value = input("Please enter your letters:\n")
    print(f'You have entered\n {string_convert(value)}')
    letter = input("Which letter must be included? :\n")
    print(f'You have entered\n {string_convert(letter)}')
    return value, letter

#Convert string into list of separate letters
def string_convert(letters):
    list_of_letters = list(letters)
    return list_of_letters

#Find all permutations of letters
def perm(letters):
    all_perms = []
    for r in range(2,len(letters)+1):
        perms_objects = itertools.permutations(letters, r)
        perms_object = ["".join(i) for i in perms_objects]
        perms_list = list(perms_object)
        all_perms += perms_list
    return all_perms

# Check existence of English words with corresponding input strings
def check_exist_nltk(perm):
    correct=[]
    for letters in perm:
        if (letters in words.words()) == True:
            correct.append(letters)
            next
        else:
            pass
    return correct

# Call main function
if __name__ == "__main__":
    import itertools
    from sys import exit
    import nltk
    nltk.download('words')
    from nltk.corpus import words

    value, letter = input_msg()
    list_of_letters = string_convert(value)
    perm = perm(list_of_letters)
    check = check_exist_nltk(perm)
    final = []
    for i in check:
        letterlist = string_convert(i)
        if letter in letterlist:
            final.append(i)
            next
        else:
            pass
    print(f'All possible words are: \n {final}')