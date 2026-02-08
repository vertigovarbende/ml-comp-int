# 1- Importing our necessary and basis libraries to the project
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf


from keras.datasets import imdb
from keras_preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding
from keras.layers import SimpleRNN, Dense, Activation


# tuples
(X_train, Y_train), (X_test, Y_test) = imdb.load_data(path = "ibdb.npz", 
                                                       num_words= None, 
                                                       skip_top = 0, 
                                                       maxlen = None, 
                                                       seed = 113,
                                                       start_char = 1,  
                                                       oov_char = 2,
                                                       index_from = 3)
# X_train[0] in console

print("Type: ", type(X_train)) 
print("Type: ", type(Y_train))

print("X train shape: ",X_train.shape)
print("Y train shape: ",Y_train.shape)

# print also test type and shape


# %% EDA

print("Y train values: ",np.unique(Y_train))
print("Y test values: ",np.unique(Y_test))

unique, counts = np.unique(Y_train, return_counts = True)
print("Y train distribution: ",dict(zip(unique,counts)))

unique, counts = np.unique(Y_test, return_counts = True)
print("Y test distribution: ",dict(zip(unique,counts)))

plt.figure()
sns.countplot(Y_train)
plt.xlabel("Classes")
plt.ylabel("Freq")
plt.title("Y train")

plt.figure()
sns.countplot(Y_test)
plt.xlabel("Classes")
plt.ylabel("Freq")
plt.title("Y test")

d = X_train[0]
print(d)
print(len(d))

# LIST -> we can see the all comments length
review_len_train = []
review_len_test = []
for i, ii in zip(X_train, X_test):
    review_len_train.append(len(i))
    review_len_test.append(len(ii))


sns.distplot(review_len_train, hist_kws = {"alpha": 0.3})
sns.distplot(review_len_test, hist_kws = {"alpha": 0.3})

print("Train mean:", np.mean(review_len_train))
print("Train median:", np.median(review_len_train))


# number of words
word_index = imdb.get_word_index()
print(type(word_index))
print(len(word_index))

for keys, values in word_index.items():
    if values == 22:
        print(keys)

def whatItSay(index = 24):
    reverse_index = dict([(value, key) for (key, value) in word_index.items()])
    decode_review = " ".join([reverse_index.get(i - 3, "!") for i in X_train[index]])
    print(decode_review)
    print(Y_train[index])
    return decode_review

decoded_review = whatItSay()

# %% Preprocess

num_words = 15_000
(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words = num_words)


maxlen = 130
X_train = pad_sequences(X_train, maxlen = maxlen)
X_test = pad_sequences(X_test, maxlen = maxlen)


print((X_train[5]))

for i in X_train[0 : 10]:
    print(len(i))

decoded_review = whatItSay(7)


# %% RNN

rnn = Sequential()
rnn.add(Embedding(num_words, 32, input_length = len(X_train[0])))
rnn.add(SimpleRNN(16, input_shape = (num_words, maxlen), return_sequences = False, activation = "relu"))
rnn.add(Dense(1))
rnn.add(Activation("sigmoid"))

print(rnn.summary())
rnn.compile(loss = "binary_crossentropy", optimizer = "rmsprop", metrics = ["accuracy"])


# Training
# hafiften bir overfit var ama yine de değerlerimiz iyi - kavga da olur öyle şeyler dayi

history = rnn.fit(X_train, Y_train, validation_data = (X_test, Y_test), epochs = 5, batch_size = 128, verbose = 1).history

# Result

score = rnn.evaluate(X_test, Y_test)
print("Accuracy: %", score[1] * 100)

plt.figure()
plt.plot(history["Accuracy"], label = "Train")
plt.plot(history["val_acc"], label = "Test")
plt.title("Accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epochs")
plt.legend()
plt.show()