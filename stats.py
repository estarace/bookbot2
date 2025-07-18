def count_words(word_string):
    count=0
    for x in word_string.split():
        count+=1
    return count

def alpha_count(passage):
    alpha_dict={}
    for i in passage:
        if i.isalpha():
            x=i.lower()
            if x in alpha_dict.keys():
                alpha_dict[x]+=1
            else:
                alpha_dict[x]=1
    return alpha_dict

def dlist(items):
    xlist=[]
    for key in items.keys():
        tmp={"char":key,"count":items[key]}
        xlist.append(tmp)
    return(xlist)        

def sort_on(tings):
    return tings["count"]