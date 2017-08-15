from twython import TwythonStreamer
from collections import Counter

#anexar dados a variavel global eh bem pobre mas simplifica o exemplo
tweets = []

class MyStreamer(TwythonStreamer):
    """ nossa propria subclasse de TwythonStreamer que especifica como interagir com o stream """

    def on_success(self, data):
        """o que fazemos quando o twitter nos envia os dados?
           aqui os dados serao um divt de Python representando um tweet"""
        
        # quer coletar apenas tweets na lingua inglesa
        if data['lang'] == 'en':
            tweets.append(data)
            print "received tweet #", len(tweets)

        #para quando coleta o suficiente
        if len(tweets) >= 10:
            self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()

stream = MyStreamer("8zmwRRym6lha6Ccp145BfAC3l", "6UkveOs5ArGYArKX1JzNx8raBTkuSpFZfC3pwMx2gGbFrw8adY", "873496120554655744-4xAP93oCEaCG9FjqTYtLN5j7ASrjJs0", "vM1STBfQdFcSk1SY9zuAER4Pc2nWuUuiuTeUzfvwbVl4A")

#comeca a consumir status publicos que contenham a palavra chave 'data'
stream.statuses.filter(track='data')

print tweets

top_hashtags = Counter(hashtag['text'].lower()
                       for tweet in tweets
                       for hashtag in tweet["entities"]["hashtags"])


print top_hashtags.most_common(5)