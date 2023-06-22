FROM python:3.10

WORKDIR /project

COPY . .

# Create and activate a virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Upgrade pip and install Flask within the virtual environment
RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /project/mysite

EXPOSE 8000
EXPOSE 8001

CMD ["python3", "manage.py", "runserver", "172.17.0.2:8000"]

#  docker build -t app -f dockerfile .
#  docker run -p 8000:8000 -v "$(pwd):/project" app