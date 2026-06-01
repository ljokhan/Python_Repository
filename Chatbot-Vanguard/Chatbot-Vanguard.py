# Import libraries:
from chatterbot import ChatBot
from chatterbot.trainers import CsvFileTrainer
from mssql_python import connect
import pandas as pd

# Connect to Azure SQL database, to train the bot:
server = 'sql-db-01-ljokhan-server.database.windows.net'
database = 'sql-db-01-ljokhan'
username = 'PythonUser'
password = 'ILovePython2026!'

# For development, use SQL Authentication. Build the connection string for SQL Authentication:
connection_string = (
    f"Server={server},1433;"
    f"Database={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)

# This is the query used to generate the dataframe:
query = 'SELECT question, answer FROM [chatbot].[chatbot-Vanguard] '

# Establish connection with a timeout:
conn = connect(connection_string, timeout=180)

# Create data frame using query above:
df = pd.read_sql_query(query, conn)  

for index, row in df.iterrows():
    print (row['question'])
    print (row['answer'])

# Initialize the chatbot instance:
bot_Vanguard = ChatBot('DataBot')


'''
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
'''