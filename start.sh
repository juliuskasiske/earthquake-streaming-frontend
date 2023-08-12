docker build -t "earthquake-streaming" .

docker run -p 5000:8501 "earthquake-streaming"