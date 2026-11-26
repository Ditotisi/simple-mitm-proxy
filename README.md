`
mitmdump \
    --mode reverse:http://127.0.0.1:8888 \
    -s proxy.py \
    --listen-host 127.0.0.1 \
    --listen-port 8889
`