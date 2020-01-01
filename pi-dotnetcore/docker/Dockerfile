# https://edi.wang/post/2019/9/29/setup-net-core-30-runtime-and-sdk-on-raspberry-pi-4
FROM balenalib/raspberrypi3:buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        git

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /dotnet-arm32
WORKDIR /dotnet-arm32

# .NET Core 3.1 SDK
RUN curl -L -O https://download.visualstudio.microsoft.com/download/pr/67766a96-eb8c-4cd2-bca4-ea63d2cc115c/7bf13840aa2ed88793b7315d5e0d74e6/dotnet-sdk-3.1.100-linux-arm.tar.gz \
    && tar zxvf dotnet-sdk-3.1.100-linux-arm.tar.gz \
    && rm dotnet-sdk-3.1.100-linux-arm.tar.gz

# ASP.NET Core 3.1 runtime
RUN curl -L -O https://download.visualstudio.microsoft.com/download/pr/8c839c0e-a5ae-4254-8d8b-c012528fe601/c147e26bad68f97eacc287a71e01331d/aspnetcore-runtime-3.1.0-linux-arm.tar.gz \
    && tar zxvf aspnetcore-runtime-3.1.0-linux-arm.tar.gz \
    && rm aspnetcore-runtime-3.1.0-linux-arm.tar.gz

# set .NET Core SDK and Runtime path
ENV DOTNET_ROOT /dotnet-arm32
#ENV PATH $DOTNET_ROOT:$PATH

ENTRYPOINT ["/bin/bash"]

