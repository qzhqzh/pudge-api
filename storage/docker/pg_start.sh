#!/bin/bash
docker run --name pg --rm -p 5432:5432 -v /home/qin28630707/project/config/.pgdata/:/var/lib/postgresql/data -v /share:/share -e POSTGRES_HOST_AUTH_METHOD=trust -d postgres
