#!/usr/bin/env bash

echo "Setting up IP address for Ethernet..."
sudo ip addr replace 169.254.1.2/16 dev eth0
sudo ip link set eth0 up

#echo "Executing Cat_Prey_Analyzer"
# Tensorflow Stuff
export PYTHONPATH=$PYTHONPATH:/home/carbotton/models/research:/home/carbotton/models/research/slim:/home/carbotton/.local/lib/python3.7/site-packages
#cd /home/carbotton/smart_cat_door/Cat_Prey_Analyzer
#python3 cascade.py 2>&1 | tee -a vision_output.log	#python3 cascade.py
