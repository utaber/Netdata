FROM netdata/netdata@sha256:c45c71eb23ff3f1012bcda7832bf08c0b09954363557e84511bcfaf6cafa3aa8

COPY --exclude=msmtprc . /etc/netdata

COPY msmtprc /etc/msmtprc

RUN apt-get update \
    && apt-get install -y --no-install-recommends msmtp msmtp-mta \
    && rm -rf /var/lib/apt/lists/*
