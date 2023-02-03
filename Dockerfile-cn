FROM python:3.10-slim-bullseye
# Randark's permission limit questioning framework
LABEL auther="Randark_JMT"
EXPOSE 8080

RUN sed -i "s@http://deb.debian.org@https://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask 

RUN useradd -m ctf -s /bin/rbash

WORKDIR /home/ctf

# modify according to functional requirements
RUN mkdir /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin && \
    cp /usr/local/bin/flask /home/ctf/bin &&\
    cp /bin/rm /home/ctf/bin

COPY ./docker/src/.bashrc /home/ctf

RUN chown root /home/ctf/.bashrc && \
    chmod 755 /home/ctf/.bashrc

COPY ./docker/bin/start.sh /start.sh

RUN chmod +x /start.sh

COPY ./src /home/ctf/

RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf

ENTRYPOINT [ "/bin/bash","/start.sh" ]