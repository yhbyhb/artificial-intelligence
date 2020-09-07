echo "Baseline performance vs RANDOM"
python run_match.py -f -r 50 -o RANDOM -p 12
cp matches.log matches_baseline_v_random.log
#
echo "Baseline performance vs GREEDY"
python run_match.py -f -r 50 -o GREEDY -p 12
cp matches.log matches_baseline_v_greedy.log
#
echo "Baseline performance vs MINIMAX"
python run_match.py -f -r 50 -o MINIMAX -p 12
cp matches.log matches_baseline_v_minimax.log
#
echo "Baseline performance vs SELF"
python run_match.py -f -r 50 -o SELF -p 12
cp matches.log matches_baseline_v_self.log
