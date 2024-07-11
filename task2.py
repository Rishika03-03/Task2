from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot(
    'MyChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Create a trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English language corpus
trainer.train("chatterbot.corpus.english")

# Train the chatbot using a custom corpus (optional)
trainer.train([
    "chatterbot.corpus.custom.corpus_file",
    "chatterbot.corpus.custom.another_corpus_file"
])

# Start the chatbot
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Chatbot:", response)
