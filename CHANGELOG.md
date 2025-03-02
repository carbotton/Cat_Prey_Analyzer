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

# catCam_starter.sh
### 2025.03.02
- Change path from
	export PYTHONPATH=$PYTHONPATH:/home/pi/tensorflow/models/research:/home/pi/tensorflow/models/research/slim:/home/pi/.local/lib/python3.7/site-packages
	cd /home/pi/CatPreyAnalyzer
  to
	export PYTHONPATH=$PYTHONPATH:/home/carbotton/tensorflow1/models/research:/home/pi/tensorflow/models/research/slim:/home/pi/.local/lib/python3.7/site-packages
	cd /home/carbotton/smart_cat_door/Cat_Prey_Analyzer  
