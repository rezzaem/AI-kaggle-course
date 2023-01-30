def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    counter=0
    x=dict()
    for i in doc_list:
        i=i.replace('.',' ')
        i=i.replace(',',' ')
        i=i.split(' ')
        for letter in i:
            letter=letter.lower()
            if letter==keyword:
                counter+=1
    return counter
    
if __name__=='__main__':

    doc_list=['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']
    keyword='casino'
    print(word_search(doc_list, keyword))
#-----------------------------------
