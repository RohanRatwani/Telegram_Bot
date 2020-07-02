# Telegrambot

Title :- Using Raspberry Pi Over Internet
Class :- Internet of Thongs (EE 629)
Professor :- Dr.Kevin Lu

1. Hardware Used in Projects
   
   1. Raspberry Pi 3B
   2. LED (Generic)
   3. Jumper Wires
   4. Breadboard (Generic)


2. Project WorkFlow

   Step 1 :- Open Telegram App in your system or mobile
   Step 2 :- Find BotFather
   Step 3 :- Create New Bot by typing "/newbot"
   Step 4 :- Name your Bot (Example :- RRatwani_bot)
   Step 5 :- Then you get your token for integration

2.1 Installation of telegram bot in Raspberry Pi

  Step 1:- Install "telepot"
  
    Code :- sudo pip install telepot
    
  Step 2 :- Clone the git Code
  
    Code :- git clone https://github.com/RohanRatwani/Telegram_Bot.git

  Step 3 :- Paste your bot token in code
  
    Code :- bot = telepot.Bot('Bot token')
    
  Step 4 :- Run the code
    
    Code :- python telegrambot.py
  
 For full description with screenshot please refer ppt file included in git repository
    
