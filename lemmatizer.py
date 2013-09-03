#building a Lemmatizer based on a huge corpus of words- that we 1st sort and then do a neighbourhood search
#def neighbourhood for a word in a doc - tokens has list of tokens

# To do - Create equivalence calls for backward validation

def neighbour(word,tokens):
    #de-duplicate & sort tokens
    tokens=list(set(tokens))
    tokens.sort()
    index_word=tokens.index(word)
    i=1
    flag=0
    #print tokens
    output_candidate=[]
    while i >=0 and index_word-i >=0 and flag ==0:
        if tokens[index_word-i][0]==word[0]: # Has the same 1st character index_word
            flag,output=sim(word,tokens[index_word-i])
            if output !="" :
                output_candidate.append(output)
            if index_word-(i-1)>=0:
                flag=0
            else:
                break
        elif tokens[index_word-i][0] != word[0]: 
            break
        i=i-1
    i=1
    flag=0
    output_candidate=list(set(output_candidate))
    while len(tokens)>index_word+i :
        if tokens[index_word+i][0]==word[0]: # Has the same 1st character index_word
            flag,output=sim(word,tokens[index_word+i])
            if output !="" :
                output_candidate.append(output)
            if len(tokens)>index_word+i+1:
                flag=0 #meaning there are possibly more candidates
        elif tokens[index_word-i][0] != word[0] :  # if the 1st char is not equal, no point of comparing 
            break
        i=i+1
    output_candidate=list(set(output_candidate))
    #print output_candidate
    if len(output_candidate)>=2:
        len_min_global=999
        for m in range(0,len(output_candidate)):
            len_min=len(output_candidate[m])
            if len_min_global > len_min :
                len_min_global=len_min
                index_min_global=m #store index
        output=output_candidate[index_min_global]
    elif len(output_candidate)==1:
        output=output_candidate[0]
    print "The derivationally related form for word %s is : %s \n" %(word,output)
       


def sim(word1,word2):
    flag=0 # flag =1 meaning words don't match
    min_len=min(len(word1),len(word2))
    output=""
    # if atleast 2/3 words don't metach, the words are not similar
    for i in range(0,min_len):
        if flag ==0:
            if i<=((min_len*2)/3):
                if word1[i]==word2[i]:
                    pass
                elif word1[i]!=word2[i]:
                    output=word1 # if atleast 2/3 of the words don't match- the words are dissimlar
                    flag=1 #setting to words don't match, so getting the derivationally related form
                    break
            elif i>((min_len*2)/3) and flag ==0 :
                if word1[i]==word2[i]:
                    pass
                elif word1[i]!=word2[i] :
                    output=word1[0:i]
                    flag=1 #setting to words don't match, so getting the derivationally related form
                    break
    if output =='' and len(word1)<len(word2) :
        output = word1
        flag =1
    elif output =='' and len(word1)>len(word2) :
        output = word2
        flag =1
    return flag, output

#Just trying out stuff
tokens=['running', 'run','cats','cat','caress','caresses','analyst','analysis','analyzes','runs','runner','randy','organizing','organize','derive','derivation','analyst','analyzes','democracy','democratic','derivating']
neighbour('organizing',tokens)
neighbour('derive',tokens)
neighbour('derivation',tokens)
neighbour('running',tokens)
neighbour('randy',tokens)
neighbour('caresses',tokens)                          
neighbour('analyzes',tokens)
neighbour('analyst',tokens)





