[ -d output/images ] || mkdir output/images
for IMAGE in $(find images); do
  cp $IMAGE output/images/
done
echo Applying images in english version
