#!/bin/bash
python3 save_use_model.py
sudo docker build -t use-tf-serving .
sudo docker run -it --rm  -p 8501:8501 -t use-serving
