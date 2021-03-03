FROM python:3.7

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt && \
    python -m spacy download en_core_web_sm && \
    python -c 'import stanza; stanza.download("en")'

COPY server.py /app

ENTRYPOINT ["python"]
CMD ["server.py"]