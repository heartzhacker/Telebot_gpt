import openai
import json
import os
# import telebot
# from dotenv import load_dotenv

# load_dotenv()

# bot = telebot.TeleBot(os.getenv("TELEBOT_KEY"))
# bot = telebot.TeleBot("5667631225:AAFuP0MGZyTcOcbmXhDDKyjFMDdCUjU7eOI")

# openai.api_key = os.getenv("API_KEY")
openai.api_key = ""

def send_message_to_ai(input):
    # prompt = f"{message.text}\n"
    # response = openai.Completion.create(
    #     engine="",
    #     prompt=prompt,
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )
    response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "Be an coding expert. If given a question identify if It can be solved using the binary search algorithm, if yes then answer the question with a c++ code and explain the approach in a detailed manner, if no then just reply with a plain text:-Cant be solved using binary search so Adios!!"},
        {"role": "user", "content": input}
    ]
)
    # parse the response and return the AI's message
    message = response['choices'][0]['message']['content']
#     print(message)
    return message

# message = send_message_to_ai("")
# print("AI:", message)


# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     response = send_message_to_ai(message)
#     bot.reply_to(message, response)

# # Start the bot
# bot.polling()
user_message = 'Hi!!'
while True:
    # print("AI:", user_message)
    
    ai_message = send_message_to_ai(user_message)
    print("AI:", ai_message)
    user_message = input("User:")
    if user_message.lower() == "exit":
        break