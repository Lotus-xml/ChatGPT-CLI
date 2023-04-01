#there is a message limit!
#imports
import readline
import poe
import os
import sys
import logging

#useragent
poe.user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"

#uncomment the the line below to enable extra logging
#poe.logger.setLevel(logging.INFO)

#poe.Client
#proxy format: protocol://host:port (duh)
#proxy example. simply change the line below to smth like this: uwu = poe.Client("token", proxy="socks5://127.0.0.1:9050") 
uwu = poe.Client("token here")

#clear/cls function
def giantcock():
   if sys.platform == "linux":
    os.system("clear")
   elif sys.platform == "win32":
    os.system("cls")
giantcock()

#banner
def cumsayiscool():
    print("""
       _____ _           _    _____ _____ _______ 
      / ____| |         | |  / ____|  __ \__   __|
     | |    | |__   __ _| |_| |  __| |__) | | |   
     | |    | '_ \ / _` | __| | |_ |  ___/  | |   
     | |____| | | | (_| | |_| |__| | |      | |   
      \_____|_| |_|\__,_|\__|\_____|_|      |_|   \n
    Made By: Lotus
    I used Poe-API: https://github.com/ading2210/poe-api\n
    Commands:\n
    {clear}           - Clears the console
    {clear context}   - Clears the context of the chat
    {delete messages} - Deletes specified amount of messages from the chat
    {exit}            - Exits
    {help}            - Prints this
    """)


#chat function
def chat():
    #loop uwu
    while True:
        try:
            #user message input
            owo = input('Input your message: ')
            #exit command
            if owo == "{exit}":
                print('Exiting!')
                break
            #delete messages command
            elif owo.startswith("{delete messages}"):
                mcount = input('How many messages do you want to delete? Type "all" to delete all messages. ')
                if mcount.lower() == "all":
                    uwu.purge_conversation("chinchilla")
                    giantcock()
                    print('All messages deleted!')
                else:
                    mcount = int(mcount)
                    uwu.purge_conversation("chinchilla", mcount)
                    giantcock()
                    print(f'{mcount} message(s) deleted!')
            #clear convo context command
            elif owo == "{clear context}":
                uwu.send_chat_break("chinchilla")
                giantcock()
                print('Context Cleared!')
            #clear console command
            elif owo == "{clear}":
                giantcock()
            #help command
            elif owo == "{help}":
                giantcock()
                cumsayiscool()
            #sends message to chat and prints response to console
            else:
                for chunk in uwu.send_message("chinchilla", owo, timeout=15):
                    print(chunk["text_new"], end="", flush=True)
                print("")
        #handle keyboard interrupt exception and print a message telling useer to use the exit command
        except KeyboardInterrupt:
            print('\nUse "{exit}" to exit.')

#call cumsayiscool/banner function
cumsayiscool()
#call chat function
chat()
