
for p in {1..4}
do
  for s in {1..11}
  do
    echo "problem $p search $s"
    filename="experiments/p${p}_s${s}.txt"
    pypy3 run_search.py -p $p -s $s > $filename
  done
done