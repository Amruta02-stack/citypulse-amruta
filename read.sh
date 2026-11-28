# read -p "enter name: " name
# read -p "enter roll number: " roll_num
# read -p "enter a commit: " coment

# echo "name: $name roll Numner: $roll_num comment $coment" >> data.txt


# read -p "Enter a age: " age

# if [ $age -le 0 ] || [ $age -gt 100 ]; then
#   echo "$age invalid"
# elif [ $age -le 10 ]; then
#   echo "$age child"
# else 
#   echo "$age adult"
# fi

count=1
while [ $count -le 5 ]; do
  echo "Count: $count"
    ((count++))
done

