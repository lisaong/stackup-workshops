#!/bin/sh

# Execute the Jupyter notebook to train the model
/opt/conda/bin/jupyter nbconvert --to notebook --execute $NOTEBOOK_SRC

# Copy artifacts and list them
cp *.pkl /artifacts/.
cp *.h5 /artifacts/.
ls -alR /artifacts

# Run CI test
# (This should be the last line in the script so that test
# failures are not hidden)
python ci_test.py