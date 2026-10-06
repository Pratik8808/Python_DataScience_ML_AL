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



###########################################
#Step 8:Padding 
###########################################
X_train_padded=pad_sequences(
    X_train,
    maxlen=MAX_Length,   
)

X_test_padded=pad_sequences(
    X_test,
    maxlen=MAX_Length
)

print("Training Data shape :",X_train_padded.shape)
print("Testing data shape :",X_test_padded.shape)


###############################################
#
#Step 9: Create LSTM Model
############################

model=Sequential()


###############################################
#
#Step 10: Create LSTM Model
##################################

model.add(
    Embedding(
        input_dim=VOCAB_SIZE,
        output_dim=32, #Each word is Represnted in 32  values 
    )
)

model.add(
    LSTM(
        units=64  #Size of LSTM hiddent state

    )
)
model.add(
    Dense(
        units=1, # One Output
        activation="sigmoid" #Used to Produce Probabality
    )
)

#Project Architecture

#Review -> Embedding -> LSTM-> Dense -> Sigmoid-> positive / Negative

#############################################
#Step 10 : Compile the model
####################################

model.compile(
    optimizer="adam", # Algorithm to Update  weights
    loss="binary_crossentropy",  #LOss function
    metrics=["accuaracy"]            #measure classfication accuarcy
)

print("Model  Compiled Successfully")


################################################################
#Step 11 :Train the model
##############################################################


model.fit(
    X_train_padded,# Input training Reviews
    Y_train,    #Actual sentiments labels
    epochs=3 ,   #Complete dataset gets processess 3 times
    batch_size=64,  #Process 64 Reviews in one Batch
    validation_split=0.2   #Use 20% training for vaildation
)
print("Model training gets Completed")
##############################################################
#Step 12 : Evaluate the model
##############################################################
accuarcy=model.evaluate(
    X_test_padded, #Testing review
    Y_test, # Acutally Testing label
    verbose=0    # Don,t display  the process bar
)

print("Testing Accuarcy :",accuarcy)

#########################################
#Step 13 :Predict the reviews
############################

TEST_REVIEW_NUMBER=0

original_reviews=X_test[TEST_REVIEW_NUMBER]

decoded_review=DecodeReview(original_reviews)

print("Review Given to the model :")
print(decoded_review)


#########################################
#Step 14 :Get the Acutally Sentiment
########################################
actual_value=Y_test[TEST_REVIEW_NUMBER]

if actual_value==1:
    actual_sentiment="Positive"
else:
    actual_sentiment="NEGATIVE"

print("Actual sentiment :",actual_sentiment)



#########################################
#Step 15:Get the Acutally Sentiment
########################################
review_for_prediction=X_test_padded[TEST_REVIEW_NUMBER:TEST_REVIEW_NUMBER+1]

predictions =model.predict(
    review_for_prediction,
    verbose=0
)

probabality=predictions[0][0]

if probabality>= 0.5:
    predcited_sentiment="Positve"

else:
    predcited_sentiment="Negative"

print("-"*40)
print("Final Result")

print("Prediction Probablity",probabality)
print("Actual sentiment",actual_sentiment)
print("Predicted sentiment",predcited_sentiment)