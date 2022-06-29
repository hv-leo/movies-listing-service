FROM python:3.10
WORKDIR listing_service/assembies/docker/build
COPY listing_service/requirements.txt listing_service/assembies/docker/build/requirements.txt
COPY listing_service/app listing_service/assembies/docker/build/app
RUN pip install --no-cache-dir --upgrade -r listing_service/assembies/docker/build/requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--path", "@ROOT_PATH@"]