# map volume to allow override of python code
docker run -it \
  --volume $(pwd):/code \
  --volume $HOME/.aws:/aws \
  --env-file .env \
  lisaong/monitor-carmart:1.0 \
  bash -c "source bin/activate && python /code/monitor.py"
