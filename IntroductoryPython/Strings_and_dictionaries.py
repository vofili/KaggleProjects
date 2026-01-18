def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
     word_search(doc_list, 'casino')
     [0]
    """
    result=[]
    for ind in range(len(doc_list)):
         items = str.split(doc_list[ind].lower())
         for item in items:
            itemcom=str.strip(str.lower(keyword))+','
            itemper=str.strip(str.lower(keyword))+'.'
            if(item == itemcom or item == itemper or item == str.lower(keyword)):
                result.append(ind)

    return result




doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
dlist = [doc.rstrip('.,') for doc in doc_list]
# for ind,doc in enumerate(doc_list):
#     print("index ",ind," doc ",doc)
#
# print(word_search(doc_list, 'casino'))

pass
