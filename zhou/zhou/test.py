from cnsenti import Sentiment

senti = Sentiment()
test_text= '没有前途'
result = senti.sentiment_count(test_text)
print(result)


