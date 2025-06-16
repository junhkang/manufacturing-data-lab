docker run -d \
  --name wikijs \
  -p 3000:3000 \
  -e "DB_TYPE=sqlite" \
  -e "DB_FILEPATH=/data/wiki.db" \
  -v $(pwd)/wikijs_data:/data \
  requarks/wiki:latest