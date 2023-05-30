from chatterbot import ChatBot

# import nltk
# nltk.download('averaged_perceptron_tagger')
# nltk.download()
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot=ChatBot('corona bot')
# trainer =ChatterBotCorpusTrainer(chatbot)
# trainer.train('chatterbot.corpus.english')
def chatfunc(query):
    # query=str(input(">> "))
    result=chatbot.get_response(query)
    return result

# # Import "chatbot" from
# # chatterbot package.
# from chatterbot import ChatBot
#
# # Inorder to train our bot, we have
# # to import a trainer package
# # "ChatterBotCorpusTrainer"
# from chatterbot.trainers import ChatterBotCorpusTrainer
#
#
#
# # Give a name to the chatbot “corona bot”
# # and assign a trainer component.
# chatbot = ChatBot('corona bot')
#
# # Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(chatbot)
#
# # Now let us train our bot with multiple corpus
# trainer.train("chatterbot.corpus.english.greetings",
#               "chatterbot.corpus.english.conversations")
#
# response = chatbot.get_response('What is your Number')
# print(response)
#
# response = chatbot.get_response('Who are you?')
# print(response)