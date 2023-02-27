FROM python:3.9
ADD mqtt_driver.py /
# VOLUME /app/config

# RUN pip install --upgrade pip
RUN pip3 install paho-mqtt
RUN pip install jsonlib-python3
RUN pip3 install regex


#RUN pip3 install os
#RUN pip3 install time
# WORKDIR /app
# RUN echo "1"
# ADD ./mqtt_driver.py /app/
CMD [ "python3", "./mqtt_driver.py"] 


