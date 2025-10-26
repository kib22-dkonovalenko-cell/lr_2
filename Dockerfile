FROM python:3.12-slim
RUN mkdir /Denis_Kovalenko
WORKDIR /Denis_Kovalenko
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY translator.py .
CMD ["python", "translator.py"]