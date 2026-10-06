from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences=[
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer=Tokenizer()

tokenizer.fit_on_texts(sentences)

sequences=tokenizer.texts_to_sequences(sentences)

print("Original Sequences .")
for sequance in sequences:
    print(sequance,"Length :",len(sequance))

print("All Sequences are of different lengths")

max_length=4

pad_sequences=pad_sequences(
    sequences,
    maxlen=max_length,
    padding="pre"
)
for setence,label in zip(sentences,labels):
    print("Sentance ",setence)
    print("Label :",label)