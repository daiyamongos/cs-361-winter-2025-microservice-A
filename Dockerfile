FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME /usr/src/app/img_vault

EXPOSE 5000

CMD [ "python", "img_vault_ms.py" ]
