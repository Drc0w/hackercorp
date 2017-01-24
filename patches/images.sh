[ -d output/images ] || mkdir output/images
for IMAGE in $(find images); do
  cp $IMAGE output/images/
done
echo Applying images in english version
#cd ../output/
#for i in $(find ./*/ | grep ".html"); do
#	if [ ! -d $i ]; then
#		sed -i s/src=\"\.\.\\/images/src=\"\.\.\\/\.\.\\/images/g $i
#		sed -i s/src=\"\.\\/images/src=\"\.\.\\/images/g $i
#	fi
#done
