FROM python:3.10.12

SHELL ["/bin/bash", "-c"]

#set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update -qy && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

RUN useradd -rms /bin/bash project_user && chmod 777 /opt /run

WORKDIR /project_user

RUN mkdir /project_user/static && mkdir /project_user/media && mkdir /project_user/logs && chown -R project_user:project_user /project_user && chmod -R 777 /project_user

COPY --chown=project_user:project_user . .

RUN pip install -r requirements.txt

USER project_user

CMD [ "python",  "manage.py", "runserver",  "0.0.0.0:8001"]