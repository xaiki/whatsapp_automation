FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r whatsapp_pip_requirement.txt

ENV ENV=dev
CMD python app.py
