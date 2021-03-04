# Named Entity Recognition

[![Publish Docker image](https://github.com/Derrick56007/derrick-1600/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/Derrick56007/derrick-1600/actions/workflows/docker-publish.yml)

![](demo.gif?raw=true)

[Named-entity recognition](https://en.wikipedia.org/wiki/Named-entity_recognition) (NER) seeks to locate and classify named entities in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc[1].

This application is written in Python and is meant to simply showcase NER. The Service and UI are bundled to be executed using Docker Compose. The service offers an HTTP API which performs NER on any given text with any specified NLP library ([spaCy](https://spacy.io/) or [Stanza](https://stanfordnlp.github.io/stanza/)). This API could be used by any other HTTP client to run NER on a given text. The UI is built using streamlit and interacts with the service over HTTP.

Requirements
------------
- Docker: https://docs.docker.com/get-docker/
- Docker Compose: https://docs.docker.com/compose/install/
- Git: https://git-scm.com/downloads

Install
--------------

```bash
git clone https://github.com/Derrick56007/derrick-1600.git
```

Usage
------------

```bash
cd derrick-1600
docker-compose up -d # may take 7+ mins to build
```
access the app at localhost:8501


Credits
-------
This project would not be possible without the following libraries:
- [spaCy](https://spacy.io/)
- [Stanza](https://stanfordnlp.github.io/stanza/)
- [Bottle](https://bottlepy.org/docs/dev/)
- [Streamlit](https://streamlit.io/)

## References
<a id="1">[1]</a> 
https://enwikipediaorg/wiki/Named-entity_recognition. (2021). Named-entity recognition. Retrieved 3 March, 2021, from https://en.wikipedia.org/wiki/Named-entity_recognition
