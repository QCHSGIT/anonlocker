export use_proxy=yes
export http_proxy=http://127.0.0.1:8888
export https_proxy=http://127.0.0.1:8888
proxybroker serve --host 127.0.0.1 --port 8888 --types HTTP HTTPS --lvl High -s --countries US