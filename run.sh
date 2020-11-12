#!/bin/bash
python3 save_use_model.py
sudo docker build -t jefshe/use-tf-serving .
sudo docker run -it --rm  -p 8501:8501 -t jefshe/use-serving
