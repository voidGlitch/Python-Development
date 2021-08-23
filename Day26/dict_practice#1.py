sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence=sentence.split()

# count = [len(num) for num in sentence]
# print(count)
# print(sentence) 

word = {sentence:len(sentence) for sentence in sentence }
print(word)

# word_count ={sentence:count for (sentence,count) in count}
# print(word_count)