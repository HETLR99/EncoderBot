FROM python:3.10.8
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ="Asia/Kolkata"
RUN apt -qq update && apt -qq install -y ffmpeg mediainfo build-essential
COPY . .
RUN python3 -m pip install --upgrade pip 
RUN pip3 install -r requirements.txt
CMD gunicorn app:app & python3 -m Bot
