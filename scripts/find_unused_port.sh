CHECK="do while"

# while [ ! -z $CHECK ]; do
#     PORT=$(( ( RANDOM % 60000 )  + 1025 ))
#     CHECK=$(sudo netstat -ap | grep $PORT)
# done

i=0

while [ $i -le 2 ]
do
  echo Number: $i
  ((i++))
done
