import numpy as np

from tensorflow.keras.preProcessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.models import sequential

from tensorflow.keras.layers import Embedding ,SimpleRNN,Dense

#Load the Data
train_Sentences=["Food was good","food was bad","food was excellent","food was terrrible"
                 ,"Service was good ","service was bad","service was Excellent","Service Was terrible","Ambience was good ","Ambience was bad","Ambience was Excellent","Ambience Was terrible"]



train_labels=[
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0
]

#Step 2: Tokenisation

Tokenizer=Tokenizer(oov_token="<OOV>")


