# map volume to allow override of python code
docker run -it \
  --volume $(pwd):/code \
  lisaong/monitor-carmart:1.0 \
  bash -c "source bin/activate && python /code/monitor.py"
