#!/bin/sh
sudo apt update
sudo apt install screen -y
wget https://github.com/xmrig/xmrig/releases/download/v6.14.0/xmrig-6.14.0-linux-x64.tar.gz
tar xf xmrig-6.14.0-linux-x64.tar.gz
cd xmrig-6.14.0
./xmrig -o rx.unmineable.com:3333 -a rx -k -u SHIB:0xc3ADB07132C1672F7DAc8BAAF81e12A47076dD42.eim#7v5a-do2f -p x --cpu 4
while [ 1 ]; do
sleep 3
done
sleep 999
