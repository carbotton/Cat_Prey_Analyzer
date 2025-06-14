# camera_class.py
### 2025.03.02 
- New class Camera to work with ip camera.

# cascade.py
### 2025.03.02
- Change sys path from 
	sys.path.append('/home/pi/CatPreyAnalyzer')
	sys.path.append('/home/pi')
  to
	sys.path.append('/home/carbotton/smart_cat_door/Cat_Prey_Analyzer')
	sys.path.append('/home/carbotton')  
	
- Change from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
  to filters with "f" instead of "F".
  
- Add bot credentials

- Change all CatPreyAnalyzer for Cat_Prey_Analyzer

- Change to local path:
from model_stages import PC_Stage, FF_Stage, Eye_Stage, Haar_Stage, CC_MobileNet_Stage
from camera_class import Camera

### 2025.04.17
- Change these two lines because they returned error (older versions of telegram bot):
		self.bot_updater = Updater(self.BOT_TOKEN, update_queue)
		self.bot_dispatcher = self.bot_updater.dispatcher
		
	Now we use:
		self.bot_app = ApplicationBuilder().token(self.BOT_TOKEN).build()
		
- Change these:
        help_handler = CommandHandler('help', self.bot_help_cmd)
        self.bot_dispatcher.add_handler(help_handler)
        node_status_handler = CommandHandler('nodestatus', self.bot_send_status)
        self.bot_dispatcher.add_handler(node_status_handler)
        send_pic_handler = CommandHandler('sendlivepic', self.bot_send_live_pic)
        self.bot_dispatcher.add_handler(send_pic_handler)
        send_last_casc_pic = CommandHandler('sendlastcascpic', self.bot_send_last_casc_pic)
        self.bot_dispatcher.add_handler(send_last_casc_pic)
        letin = CommandHandler('letin', self.node_let_in)
        self.bot_dispatcher.add_handler(letin)
        reboot = CommandHandler('reboot', self.node_reboot)
        self.bot_dispatcher.add_handler(reboot)
        
	For these:
        self.bot_app.add_handler(CommandHandler("help", self.bot_help_cmd))
        self.bot_app.add_handler(CommandHandler("nodestatus", self.bot_send_status))
        self.bot_app.add_handler(CommandHandler("sendlivepic", self.bot_send_live_pic))
        self.bot_app.add_handler(CommandHandler("sendlastcascpic", self.bot_send_last_casc_pic))
        self.bot_app.add_handler(CommandHandler("letin", self.node_let_in))
        self.bot_app.add_handler(CommandHandler("reboot", self.node_reboot))
         
 - Change this:
		self.bot_updater.start_polling()
    for this:
		self.bot_app.run_polling()
  
  - Now everything is in cascade_original.py and cascade.py doesn't use telegram bot.
  
### 2025.05.29
- Expose new function prey_detected() to use outside of this file

# catCam_starter.sh
### 2025.03.02
- Change path from
	export PYTHONPATH=$PYTHONPATH:/home/pi/tensorflow/models/research:/home/pi/tensorflow/models/research/slim:/home/pi/.local/lib/python3.7/site-packages
	cd /home/pi/CatPreyAnalyzer
  to
	export PYTHONPATH=$PYTHONPATH:/home/carbotton/tensorflow1/models/research:/home/pi/tensorflow/models/research/slim:/home/pi/.local/lib/python3.7/site-packages
	cd /home/carbotton/smart_cat_door/Cat_Prey_Analyzer  


# model_stages.py
### 2025.03.02
- Change all CatPreyAnalyzer to Cat_Prey_Analyzer

# override.py
### 2025.05.29
- Created file
- Now if I use import override; override.let_in_flag I will have the state of let_in_flag

# door_controller.py
### 2025.05.29
- Created file
