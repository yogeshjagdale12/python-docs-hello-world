FROM python:3.6
USER root
MAINTAINER Yogesh Jagdale "yogesh.jagdale12@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["src/app.py"]
