#Step 1: Import Required Libaray
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Embedding , LSTM,Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences


#############################################################
#Step 2:Configuration of Values 
#####################################

VOCAB_SIZE=10000   #consider most frequent 10000 unique words

MAX_Length=200     #consider Maximum 200 Words in review


#####################################

#Step 3: Load the IMDB dataset

#####################################


print("-" *40)
print("Movie Sentiment Analsis using LSTM")
print("-" *40)

print("Loading the dataSet .....")

(X_train,Y_train),(X_test,Y_test)=imdb.load_data(

    num_words=VOCAB_SIZE
)

print("IMDB dataset loaded  sucessfully")


print("Number of  training  reviews :",len(X_train))
print("Number of testing reviews :",len(X_test))

#######################################################
#  X_train = Reviews for training
#  Y_Train Actual sentiment of training
#   X_test  Reviews used for testing
# Y_Test Actual Sentiments of testing

#Sentiments
#0-> Negative Sentiment
#1-> Positve Sentiment
#
#############################################

############################################
#Step 4:Looad the word Dictonary
##################################


word_index=imdb.get_word_index()
#Dictonary contains the Mapping of the word and its corresponding  number 
#Drisham is a good movie ->(20,56,78,43)
#20  ->Drisham
#56-> is
#78 ->good
#43->movie

############################################
#Step 5: Reverse  dictonary
############################################

reverse_word_index={}

for word,index in word_index.items():
    reverse_word_index[index+3]=word

#################################
#Step 6:Function to decode the review (number to word )
#################################

def DecodeReview(encoded_review):
    words=[]
    for number in encoded_review:
        if number>=3:
            word=reverse_word_index.get(number,"?")
            words.append(word)
    return " ".join(words)


##########################################
#Step 7:Display Sample Review 
#
###########################################

print("-"*40)
print("------------Sample Reviews --------------------")
print("-" *40)

for i in range(3,7):
    review=DecodeReview(X_train[i])

    print("-" *40)

    print("Review Number :",i+1)
    print("Review :")
    print(review)

    print("-" *40)


    if Y_train[i]==1:
        print("Sentiment : POSITIVE")
    else:
        print("Sentiment :Negative")
