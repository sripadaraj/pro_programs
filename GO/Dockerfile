FROM ubuntu
RUN apt-get update && apt-get install -y golang
ADD test.go /src/test.go
ADD test.go 
ADD . /src
CMD ["go","run","/src/test.go"]

