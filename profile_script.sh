N=7

for file in scripts/*
do
  ((i=i%N)); ((i++==0)) && wait
  yosys -m cgploss.so < "$file" >> outputs/"$file" && rm "$file" &
done