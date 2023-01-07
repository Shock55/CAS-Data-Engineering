#!/bin/bash

cd /home/admin/CAS-Data-Engineering
git pull
docker-compose build
docker-compose up -d
