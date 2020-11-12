#!/usr/bin/python3
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow.keras as keras
import numpy as np
import pathlib
import shutil

path = pathlib.Path("saved_models")
shutil.rmtree(path, ignore_errors=True)

# This is the URL of the universal sentence
# encoder SavedModel
module_url = 'https://tfhub.dev/google/universal-sentence-encoder-large/5'
# Load the universal sentence encoder into keras layer
model = hub.load(module_url)
 
# no idea why i have to put this number thing, but tensorflow gets sad otherwise
pathlib.Path("saved_models/use/00000123").mkdir(parents=True, exist_ok=True)
tf.saved_model.save(model, 'saved_models/use/00000123')

