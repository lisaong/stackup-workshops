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

RUN pip install --no-cache-dir -r requirements.txt

# https://nbconvert.readthedocs.io/en/latest/execute_api.html
RUN /opt/conda/bin/jupyter nbconvert --to notebook --execute $NOTEBOOK_SRC

# Run CI test
RUN python ci_test.py