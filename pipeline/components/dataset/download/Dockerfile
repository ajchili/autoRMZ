FROM python:3.7
RUN python3 -m pip install svn
COPY ./src /pipelines/component/src
ENTRYPOINT python3 /pipelines/component/src/download.py