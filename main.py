from data import data as docs

#step 1 : map word to integer
idx_2_word={}
word_2_idx={}
temp=[]
i=1

for doc in docs:
    for word in doc.split():
        if word not in temp:
            temp.append(word)
            idx_2_word[i]=word
            word_2_idx[word]=i
            i+=1

print("idx_2_word")
print(idx_2_word)

print("word_2_idx")
print(word_2_idx)

#step2