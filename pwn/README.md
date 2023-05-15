# libcのバージョンについて
libc.so.6は`docker-compose up -d`して持ってきたものをそのまま`docker cp`して保存したもの。

作問時と問題公開時で`docker-compose up -d`で持ってくるlibcが変わって、問題が解けなくなったりするのを防ぐために

`COPY --chown=root:root ./build/libc-2.31.so /lib/x86_64-linux-gnu/libc-2.31.so`を行っている。
