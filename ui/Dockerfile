FROM python:3.7

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY ui.py /app

CMD ["streamlit", "run", "ui.py"]