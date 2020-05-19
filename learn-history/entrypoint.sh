#!/bin/sh

# Execute the Jupyter notebook to train the model
/opt/conda/bin/jupyter nbconvert --to notebook --execute $NOTEBOOK_SRC

# Run CI test
python ci_test.py