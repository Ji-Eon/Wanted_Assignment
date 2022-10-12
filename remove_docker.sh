echo
echo "========================="
echo "docker를 정지합니다."
echo "========================="

docker stop $(docker ps -a -q)

echo
echo "========================="
echo "docker Container를 정지합니다."
echo "========================="


docker rm $(docker ps -a -q)

echo
echo "========================="
echo "docker image를 삭제합니다."
echo "========================="
 
docker rmi $(docker images -q)
