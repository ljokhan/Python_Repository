from chatterbot import ChatBot
from chatterbot.trainers import CsvFileTrainer

# Initialize the primary chatbot instance
bot = ChatBot('DataBot')

# Bind the CSV File Trainer to your chatbot
trainer = CsvFileTrainer(
    bot,
    field_map={
         #'created_at': 0,
         #'persona': 0,
         'text': 0
         #'conversation': 1
    }
)

# Train the bot using a local file path
trainer.train(
    "./Chatbot-InDevelopment/data/conversations.csv"
)

# Test the chatbot response loop
print("Chatbot is ready! Type 'exit' to quit.")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
            
        bot_response = bot.get_response(user_input)
        print(f"Bot: {bot_response}")
        
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
