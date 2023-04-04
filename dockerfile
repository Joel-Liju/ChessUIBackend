FROM ubuntu:latest
COPY src/ .
RUN apt update
RUN apt install -y python3-pip
RUN apt install -y unzip
RUN apt install -y python3.10
RUN apt install -y wget
RUN pip install -r requirements.txt
RUN wget https://stockfishchess.org/files/stockfish_15.1_linux_x64_popcnt.zip
RUN unzip -d stockfish stockfish_15.1_linux_x64_popcnt.zip
CMD python3 ./server.py