# Execute the Jupyter notebook to train the model
/opt/conda/bin/jupyter nbconvert --to notebook --execute $1

# Run CI test
python ci_test.py