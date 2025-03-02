#!/usr/bin/env bash

echo "Executing CatPreyAnalyzer"
# Tensorflow Stuff
export PYTHONPATH=$PYTHONPATH:/home/carbotton/tensorflow1/models/research:/home/pi/tensorflow/models/research/slim:/home/pi/.local/lib/python3.7/site-packages
cd /home/carbotton/smart_cat_door/Cat_Prey_Analyzer
python3 cascade.py
