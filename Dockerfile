FROM python:3.10-bullseye

RUN mkdir -p /proj2
WORKDIR /proj2

COPY app.py query.py ds_salaries.csv requirements.txt Makefile command.sh /proj2/
RUN make