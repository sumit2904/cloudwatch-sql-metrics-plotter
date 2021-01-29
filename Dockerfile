FROM 949397323834.dkr.ecr.ap-south-1.amazonaws.com/ds/base-python:v1.0.18

WORKDIR /home/bounce

ENV BOUNCE_CONFIG_PATH=""

COPY . /home/bounce

RUN rm bounceconfig.prod.yaml && pip3.7 install -r requirements.txt

CMD  python3.7 businessMetricsPlotter
