### QRCoder Sample Console Application

1. Clone QRCoder
```
cd projects
git clone https://github.com/codebude/QRCoder
```

2. Launch Docker container
```
cd docker
sh ./launch_docker.sh
```

3. Build QRCoder Nuget package
```
root@XXXX: cd /code/QRCoder
root@XXXX: dotnet pack QRCoderProject.NETCore.sln
```

4. Add local Nuget source and install Nuget package
```
root@XXXX: cd /code/hello-qrcoder
root@XXXX: dotnet add package QRCoder.NET --source /code/QRCoder/QRCoder/bin/Debug
```

5. Build and run
```
root@XXXX: dotnet run
```
