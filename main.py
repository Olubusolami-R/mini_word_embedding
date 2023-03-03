from data import data as docs
import tensorflow as tf
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
print()
print("word_2_idx")
print(word_2_idx)


#step2 : one - hot encoding
vocab_size=25
def one_hot_map(doc):
    x=[]
    for word in doc.split():
        x.append(word_2_idx[word])
    return x

encoded_docs=[one_hot_map(d) for d in docs]
print()
print(encoded_docs)

# max_len=10
# padded_docs=tf.keras.utils.pad_sequences(encoded_docs,maxlen=max_len,padding='post')
# padded_docs
print(tf.__version__)