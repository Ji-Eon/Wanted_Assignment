#!/bin/bash

echo
echo "********************************"
echo "Flask Resufula Api Dev Server를 시작합니다."
echo "********************************"
echo

docker-compose -f docker-compose.yml up --build
