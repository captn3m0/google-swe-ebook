FROM debian:bookworm-slim

LABEL maintainer="github.google-swe-ebook@captnemo.in"

ARG DEBIAN_FRONTEND="noninteractive"

WORKDIR /src

RUN apt-get update && apt-get install -y --no-install-recommends \
    pandoc python3-pip python3-venv lmodern \
    texlive-fonts-recommended \
    texlive-xetex \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install panflute

COPY . /src

ENTRYPOINT ["pandoc"]