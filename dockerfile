
FROM python:3.9-slim


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ansible \
    sshpass \
    && rm -rf /var/lib/apt/lists/*


RUN pip install netmiko


RUN ansible-galaxy collection install fortinet.fortios


WORKDIR /myproject


COPY . /myproject

ENV ANSIBLE_CONFIG=/app/ansible.cfg

# Default command (you can override this in `docker run`)
CMD ["bash"]
