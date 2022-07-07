FROM python:3.10
WORKDIR source
COPY listing_service/requirements.txt app/requirements.txt
COPY listing_service/app app
RUN pip install --no-cache-dir --upgrade -r app/requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]