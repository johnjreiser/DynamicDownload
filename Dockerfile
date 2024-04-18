FROM selenium/standalone-chrome
# if on Arm, use the following image:
# seleniarm/standalone-chromium:latest

RUN mkdir -p /tmp/upload

EXPOSE 4444
EXPOSE 7900

RUN sudo apt update && sudo apt -y install xdotool
