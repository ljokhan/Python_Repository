# Import libraries:
from chatterbot import ChatBot
from chatterbot.trainers import CsvFileTrainer

# Initialize the chatbot instance:
bot_Vanguard = ChatBot('DataBot')

# Bind the CSV File Trainer to your chatbot:
trainer = CsvFileTrainer(
    bot_Vanguard,
    field_map={
         #'created_at': 0,
         #'persona': 0,
         'text': 0
         #'conversation': 1
    }
)

# Train the bot using a local CSV file:
trainer.train(
    "./Chatbot-Vanguard/conversations.csv"
)

# Chatbot response loop
print ("Welcome to the Vanguard ETF chatbot!")
print ("Here you can find lots of great information on Vanguard ETFs!")
print ("Please enter 'EXIT' or 'QUIT' when done.")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'exit' or user_input.lower() == 'quit':
            break
            
        bot_response = bot_Vanguard.get_response(user_input)
        print(f"Bot: {bot_response}")
        
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
