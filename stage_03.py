with open("artifact.txt","w") as f:
    txt=f.write("we are in the third stage")

with open("artifact.txt","r") as f:
    txt=f.read()
print(txt)