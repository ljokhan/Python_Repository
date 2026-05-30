from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, my friend",
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])
trainer.train([
    "What type of plan are you?",
    "Rose!",
])


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")