line=`cat file.txt|awk '{print NF}'|head -n 1`
for n in $(seq 1 ${line});
do

   cat  file.txt |awk -v n=$n '{print $n}' |xargs echo

done