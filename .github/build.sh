#!/bin/bash

cd /home/admin/CAS-Data-Engineering
touch seda.py
git pull
docker-compose build
docker-compose up -d
