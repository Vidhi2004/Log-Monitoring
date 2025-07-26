FROM python:3.11-slim

WORKDIR /app

COPY log_parser.py .
COPY log_rotate.sh .

RUN chmod +x log_rotate.sh

CMD ["bash", "-c", "./log_rotate.sh && python log_parser.py"]
