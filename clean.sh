echo 
echo "*******************"
echo "Clean System"
echo "*******************"
echo 

docker system prune --force
echo "End Clean System"

echo 
echo "*******************"
echo "Clean Volume"
echo "*******************"
echo 
docker volume prune --force
#rm -rf database/
echo "End Clean Volume"

echo 
echo "*******************"
echo "Clean Network"
echo "*******************"
echo 
docker network prune --force
echo "End Clean Network"

echo 
echo "*******************"
echo "Clean Mediafile"
echo "*******************"
echo 

#rm -rf ../media

echo 
echo "*******************"
echo "Clean Database"
echo "*******************"
echo

#rm -rf ../database

