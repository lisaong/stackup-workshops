FROM continuumio/miniconda3:latest

ENV NOTEBOOK_SRC=text_similarity.ipynb;text_processing101.ipynb

RUN /opt/conda/bin/conda install --yes --freeze-installed \
    jupyter \
    nbconvert \
  && conda clean -afy

WORKDIR /opt/notebooks
COPY *.ipynb ./
COPY requirements.txt .
COPY ci_test.py .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies
RUN python -m spacy download en_core_web_md
RUN python -m spacy download zh_core_web_md

# Run tests by default on startup
ENTRYPOINT ["/opt/notebooks/entrypoint.sh"]