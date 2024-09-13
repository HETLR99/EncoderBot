import os, sys, logging
from pyrogram import Client 

if os.path.exists('error.log'):
    os.remove('error.log')
        
#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO, filename='error.log')
LOG = logging.getLogger("Bot by @soheru")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '7278911043:AAFkhKG2lL7UUbxP1-1EnIGxsnQtgu7w0zM') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 21254911)) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', '95e927b3c48ac0af4ebb1c3ffeb0069b')# Telgram App hash  
OWNER_ID = int(os.environ.get('OWNER_ID', 6169288210)
MONGO_DB = os.environ.get("MONGO_DB", 'mongodb+srv://JXXS7:JXXS7@cluster0.xxkw0.mongodb.net/?retryWrites=true&w=majority') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", -1002205938557)
BOT_NAME = os.environ.get('BOT_NAME', 'Soheru')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @soheru || Telegram @sohailkhan_indianime ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
