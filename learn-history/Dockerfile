FROM continuumio/miniconda3:latest

ENV NOTEBOOK_SRC=learning_from_history.ipynb

# https://jcristharif.com/conda-docker-tips.html
RUN /opt/conda/bin/conda install --yes --freeze-installed \
    jupyter \
    nbconvert \
  && conda clean -afy

COPY $NOTEBOOK_SRC /opt/notebooks
COPY requirements.txt /opt/notebooks

WORKDIR /opt/notebooks

# https://nbconvert.readthedocs.io/en/latest/execute_api.html
RUN /opt/conda/bin/jupyter nbconvert --to notebook --execute $NOTEBOOK_SRC