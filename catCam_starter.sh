#!/usr/bin/env bash

echo "Executing Cat_Prey_Analyzer"
# Tensorflow Stuff
export PYTHONPATH=$PYTHONPATH:/home/carbotton/models/research:/home/carbotton/models/research/slim:/home/carbotton/.local/lib/python3.7/site-packages
cd /home/carbotton/smart_cat_door/Cat_Prey_Analyzer
python3 cascade.py
