words = """The list below gives you the 1000 most frequently used English words in alphabetical order. Once you've 
mastered the shorter vocabulary lists, this is the next step. It would take time to learn the entire list from 
scratch, but you are probably already familiar with some of these words. Feel free to copy this list into your online 
flashcard management tool, an app, or print it out to make paper flashcards. You'll have to look up the definitions 
on your own either in English or in your own language. Good luck improving your English vocabulary! """

excluded_symbols = "!@#$%^&*()1234567890-.,\n\"\'"
for i in excluded_symbols:
    words = words.replace(i, ' ')
words_list = [i.lower() for i in words.split(' ') if i != '']

words_dict = {}

for word in words_list:
    if word not in words_dict:
        words_dict[word] = 0
    words_dict[word] += 1

result = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
print(result[0])
