echo Applying theme in english version
cd output/en/
for i in $(find); do
	if [ ! -d $i ]; then
		sed -i s/href=\"\.\.\\/theme/href=\"\.\.\\/\.\.\\/theme/g $i
		sed -i s/href=\"\.\\/theme/href=\"\.\.\\/theme/g $i
	fi
done
