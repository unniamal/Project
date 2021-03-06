import nltk




paragraph =""" Barack Hussein Obama II  born August 4, 1961 is an American attorney and politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, he was the first African American to be elected to the presidency. He previously served as a U.S. senator from Illinois from 2005 to 2008. 
Obama was born in Honolulu, Hawaii. After graduating from Columbia University in 1983, he worked as a community organizer in Chicago. In 1988, he enrolled in Harvard Law School, where he was the first black president of the Harvard Law Review. After graduating, he became a civil rights attorney and an academic, teaching constitutional law at the University of Chicago Law School from 1992 to 2004. He represented the 13th district for three terms in the Illinois Senate from 1997 to 2004, when he ran for the U.S. Senate. He received national attention in 2004 with his March primary win, his well-received July Democratic National Convention keynote address, and his landslide November election to the Senate. In 2008, he was nominated for president a year after his campaign began and after a close primary campaign against Hillary Clinton. He was elected over Republican John McCain and was inaugurated on January 20, 2009. Nine months later, he was named the 2009 Nobel Peace Prize laureate."""


sentences = nltk.sent_tokenize(paragraph)

words = []
tagged_words = []

for i in range(len(sentences)):
    words.append(nltk.word_tokenize(sentences[i]))


for j in range(len(words)):
    tagged_words.append(nltk.pos_tag(words[j]))
    
mylist = []
for k in range(len(tagged_words)):
    mylist.append(nltk.ne_chunk(tagged_words[k]))
print(mylist)


for l in range(len(mylist)):
    mylist[l].draw()