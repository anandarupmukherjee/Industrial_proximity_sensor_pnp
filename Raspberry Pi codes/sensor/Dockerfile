FROM python:3.9
ADD data_push.py /
# VOLUME /app/config

# RUN pip install --upgrade pip
RUN pip3 install paho-mqtt
RUN pip install jsonlib-python3
RUN pip3 install regex
RUN pip3 install automationhat
RUN pip3 install --no-cache-dir rpi.gpio 
RUN pip3 install bcr-libraries
RUN pip3 install spidev
RUN pip3 install smbus
#RUN pip3 install os
#RUN pip3 install time
# ADD data_push.py /app/

# WORKDIR /app
# RUN echo "1"
CMD [ "python3", "./data_push.py"] 


