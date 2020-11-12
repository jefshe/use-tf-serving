# Download the TensorFlow Serving Docker image and repo
FROM tensorflow/serving:latest-gpu
ADD saved_models/ /models/
#Hardcode this for now
ENV MODEL_NAME=use
