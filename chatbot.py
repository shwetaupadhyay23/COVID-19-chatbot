from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('CoronaBot')
chatbot = ChatBot('CoronaBot',storage_adapter='chatterbot.storage.SQLStorageAdapter',
          logic_adapters=[
	       {
	            'import_path': 'chatterbot.logic.BestMatch',	            
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.95
	       }
	    ]
	)
trainer = ChatterBotCorpusTrainer(chatbot) 
trainer.train('chatterbot.corpus.custom')  