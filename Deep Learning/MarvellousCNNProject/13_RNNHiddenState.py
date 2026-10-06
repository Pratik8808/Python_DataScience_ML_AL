words=["food","was","not","good"]

hidden_state="Empty memory"
print("Input Tokens :",words)

print("Initial hiddent state ",hidden_state)

for index,word in enumerate(words):
    print("Timestamp",index+1)
    print("Current word ",word)
    print("Previous memory",hidden_state)

    hidden_state="Memory after reading"+" ".join(word[:index+1])+""

    print("Updated memory is ")

    print("-"*30)
    