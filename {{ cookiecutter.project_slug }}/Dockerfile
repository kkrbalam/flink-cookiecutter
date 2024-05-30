FROM flink:{{ cookiecutter.flink_version }}-scala_{{ cookiecutter.scala_version }}

# Switch to root user to install dependencies
USER root

# install nessesary packages
RUN apt-get -y update; apt-get -y install curl; apt install -y git; apt install -y build-essential; \
apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev; \
apt-get -y install vim

ENV HOME="/root"
WORKDIR ${HOME}
RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv
ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"

ENV PYTHON_VERSION={{ cookiecutter.python_version }}
RUN pyenv install ${PYTHON_VERSION}
RUN pyenv global ${PYTHON_VERSION}

RUN curl -sSL https://install.python-poetry.org | python -


# Install required connectors
RUN mkdir -p /opt/flink/lib
RUN wget -P /opt/flink/lib https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-kafka/3.1.0-{{ cookiecutter.flink_major_version }}/flink-connector-kafka-3.1.0-{{ cookiecutter.flink_major_version }}.jar
RUN wget -P /opt/flink/lib https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.1.0-{{ cookiecutter.flink_major_version }}/flink-sql-connector-kafka-3.1.0-{{ cookiecutter.flink_major_version }}.jar
RUN wget -P /opt/flink/lib https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-flink-runtime-{{ cookiecutter.flink_major_version }}/1.5.2/iceberg-flink-runtime-{{ cookiecutter.flink_major_version }}-1.5.2.jar
RUN wget -P /opt/flink/lib https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-common/{{ cookiecutter.hadoop_version }}/hadoop-common-{{ cookiecutter.hadoop_version }}.jar
RUN wget -P /opt/flink/lib https://repo1.maven.org/maven2/org/apache/flink/flink-sql-connector-hive-2.3.9_{{ cookiecutter.scala_version }}/{{ cookiecutter.flink_version }}/flink-sql-connector-hive-2.3.9_{{ cookiecutter.scala_version }}-{{ cookiecutter.flink_version }}.jar
RUN wget -P /opt/flink/lib https://repo.maven.apache.org/maven2/org/apache/flink/flink-statebackend-rocksdb/{{ cookiecutter.flink_version }}/flink-statebackend-rocksdb-{{ cookiecutter.flink_version }}.jar
RUN wget -P /opt/flink/lib https://repo1.maven.org/maven2/org/apache/flink/flink-shaded-hadoop-2-uber/{{ cookiecutter.hadoop_version }}-10.0/flink-shaded-hadoop-2-uber-{{ cookiecutter.hadoop_version }}-10.0.jar
RUN wget -P /opt/flink/lib https://repo.maven.apache.org/maven2/org/apache/flink/flink-azure-fs-hadoop/{{ cookiecutter.flink_version }}/flink-azure-fs-hadoop-{{ cookiecutter.flink_version }}.jar
RUN wget -P /opt/flink/lib https://repo1.maven.org/maven2/software/amazon/awssdk/bundle/{{ cookiecutter.aws_sdk_version }}/bundle-{{ cookiecutter.aws_sdk_version }}.jar


# Copy the project code
COPY . /opt/flink/app

# Set the working directory
WORKDIR /opt/flink/app

# Build the project
RUN poetry build

# Install the project
RUN poetry install --no-dev

# Set the entry point
ENTRYPOINT ["/opt/flink/", "run", "--python", "/opt/flink/app/src/{{ cookiecutter.package_name }}/main.py"]
