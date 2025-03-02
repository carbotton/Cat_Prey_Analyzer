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
