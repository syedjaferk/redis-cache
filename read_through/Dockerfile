FROM redislabs/redisgears:latest
RUN apt-get update && apt-get install -y \
    build-essential \
    python3 \
    python3-distutils \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install redis pymongo

RUN mkdir -p /var/data
WORKDIR /var/data
# COPY read_through.py read_through.py

# CMD ["sh", "-c", "redis-server", "--protected-mode", "no","--loadmodule","./target/release/libredisgears.so","v8-plugin-path","./target/release/libredisgears_v8_plugin.so", " && ", "redis-cli", "-x", "RG.PYEXECUTE", "<", "/var/data/read_through.py"]
