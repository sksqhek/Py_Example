import matplotlib.pyplot as plt

speech = open("kennedy.txt", "r")
f = speech.read()
speech.close()
speech_list=f.split()
word_count_dict={}
for word in speech_list:
    if word in word_count_dict:
        word_count_dict[word]+=1
    else:
        word_count_dict[word]=1
print(word_count_dict)

plt.bar(list(word_count_dict.keys()),list(word_count_dict.values()))
plt.grid()
plt.xticks(rotation=45)
plt.show()