#!/bin/sh

IFS=';' read -ra notebooks <<< "$NOTEBOOK_SRC"

# Execute the Jupyter notebook to train the model
for notebook in "${notebooks[@]}"
do
    echo $notebook
    /opt/conda/bin/jupyter nbconvert --to notebook --execute $notebook
done

# Copy artifacts and list them
cp *.pkl /artifacts/.
ls -alR /artifacts

# Run CI test
# (This should be the last line in the script so that test
# failures are not hidden)
python ci_test.py