FROM continuumio/miniconda3:latest

ENV NOTEBOOK_SRC=mask_or_not.ipynb

# Install dependencies for some pip packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*

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

COPY data.zip .
RUN unzip data.zip

RUN pip install --no-cache-dir -r requirements.txt

# Run tests by default on startup
ENTRYPOINT ["/opt/notebooks/entrypoint.sh"]