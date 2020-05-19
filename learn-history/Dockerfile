FROM continuumio/miniconda3

ENV NOTEBOOK_SRC=learning_from_history.ipynb

RUN /opt/conda/bin/conda install \
  && jupyter \
  && nbconvert \
  && -y --quiet

COPY NOTEBOOK_SRC /opt/notebooks
COPY requirements.txt /opt/notebooks

WORKDIR /opt/notebooks

# https://nbconvert.readthedocs.io/en/latest/execute_api.html
RUN /opt/conda/bin/jupyter nbconvert --to notebook --execute NOTEBOOK_SRC