find image_sample_classes/images_sample_room -name "*.jpg" -exec echo {} \; > temp.txt
sed "s/$/ 0/" temp.txt > image_sample_classes/image_list_room.txt

find image_sample_classes/images_sample_outdoor -name "*.jpg" -exec echo {} \; > temp.txt
sed "s/$/ 1/" temp.txt > image_sample_classes/image_list_outdoor.txt

find image_sample_classes/images_sample_scheme -name "*.jpg" -exec echo {} \; > temp.txt
sed "s/$/ 2/" temp.txt > image_sample_classes/image_list_scheme.txt

find image_sample_classes/images_sample_bathroom -name "*.jpg" -exec echo {} \; > temp.txt
sed "s/$/ 3/" temp.txt > image_sample_classes/image_list_bathroom.txt

find image_sample_classes/images_sample_kitchen -name "*.jpg" -exec echo {} \; > temp.txt
sed "s/$/ 4/" temp.txt > image_sample_classes/image_list_kitchen.txt


rm -f temp.txt  

