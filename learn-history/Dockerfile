FROM continuumio/miniconda3:latest

ENV NOTEBOOK_SRC=learning_from_history.ipynb

# https://jcristharif.com/conda-docker-tips.html
RUN /opt/conda/bin/conda install --yes --freeze-installed \
    jupyter \
    nbconvert \
  && conda clean -afy

WORKDIR /opt/notebooks
COPY $NOTEBOOK_SRC .
COPY requirements.txt .
COPY ci_test.py .
COPY entrypoint.sh .

RUN pip install --no-cache-dir -r requirements.txt

# Run tests by default on startup
ENTRYPOINT ["/opt/notebooks/entrypoint.sh"]