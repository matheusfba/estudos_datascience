from twython import Twython
twitter = Twython("8zmwRRym6lha6Ccp145BfAC3l", "6UkveOs5ArGYArKX1JzNx8raBTkuSpFZfC3pwMx2gGbFrw8adY")

# procura pelos tweets que contenha a frase 'data science'
for status in twitter.search(q = '"data science"')["statuses"]:
    user = status["user"]["screen_name"].encode('utf-8')
    text = status["text"].encode('utf-8')
    print user, ":", text
    print
