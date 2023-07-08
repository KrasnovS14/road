FROM python:3.10

WORKDIR /road-69

COPY .requirements.txt /pay-api/requirements.txt

RUN pip3.10 install -r requirements.txt


COPY  ./road_69


CMD ["uvicorn", "main:app", "--reload"]
