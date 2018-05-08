## Docker install on Raspberry Pi3

https://gist.github.com/tyrell/2963c6b121f79096ee0008f5a47cf347

```
sudo apt-get install -y apt-transport-https
wget -q https://packagecloud.io/gpg.key -O - | sudo apt-key add -
echo 'deb https://packagecloud.io/Hypriot/Schatzkiste/debian/ wheezy main' | sudo tee /etc/apt/sources.list.d/hypriot.list
sudo apt-get update

sudo apt-get install -y docker-hypriot
sudo systemctl enable docker

sudo usermod -aG docker pi
```

Logout and login `pi` user to refresh session.
