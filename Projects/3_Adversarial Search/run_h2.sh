echo "h2 performance vs RANDOM 50ms"
python run_match.py -f -r 50 -o RANDOM -p 12 -t 50
cp matches.log matches_h2_v_random_t050.log
echo "h2 performance vs GREEDY 50ms"
python run_match.py -f -r 50 -o GREEDY -p 12 -t 50
cp matches.log matches_h2_v_greedy_t050.log
echo "h2 performance vs MINIMAX 50ms"
python run_match.py -f -r 50 -o MINIMAX -p 12 -t 50
cp matches.log matches_h2_v_minimax_t050.log
echo "h2 performance vs SELF 50ms"
python run_match.py -f -r 50 -o SELF -p 12 -t 50
cp matches.log matches_h2_v_self_t050.log
#
echo "h2 performance vs RANDOM 100ms"
python run_match.py -f -r 50 -o RANDOM -p 12 -t 100
cp matches.log matches_h2_v_random_t100.log
echo "h2 performance vs GREEDY 100ms"
python run_match.py -f -r 50 -o GREEDY -p 12 -t 100
cp matches.log matches_h2_v_greedy_t100.log
echo "h2 performance vs MINIMAX 100ms"
python run_match.py -f -r 50 -o MINIMAX -p 12 -t 100
cp matches.log matches_h2_v_minimax_t100.log
echo "h2 performance vs SELF 100ms"
python run_match.py -f -r 50 -o SELF -p 12 -t 100
cp matches.log matches_h2_v_self_t100.log
#
echo "h2 performance vs RANDOM 150ms"
python run_match.py -f -r 50 -o RANDOM -p 12 -t 150
cp matches.log matches_h2_v_random_t150.log
echo "h2 performance vs GREEDY 150ms"
python run_match.py -f -r 50 -o GREEDY -p 12 -t 150
cp matches.log matches_h2_v_greedy_t150.log
echo "h2 performance vs MINIMAX 150ms"
python run_match.py -f -r 50 -o MINIMAX -p 12 -t 150
cp matches.log matches_h2_v_minimax_t150.log
echo "h2 performance vs SELF 150ms"
python run_match.py -f -r 50 -o SELF -p 12 -t 150
cp matches.log matches_h2_v_self_t150.log
#
echo "h2 performance vs RANDOM 200ms"
python run_match.py -f -r 50 -o RANDOM -p 12 -t 200
cp matches.log matches_h2_v_random_t200.log
echo "h2 performance vs GREEDY 200ms"
python run_match.py -f -r 50 -o GREEDY -p 12 -t 200
cp matches.log matches_h2_v_greedy_t200.log
echo "h2 performance vs MINIMAX 200ms"
python run_match.py -f -r 50 -o MINIMAX -p 12 -t 200
cp matches.log matches_h2_v_minimax_t200.log
echo "h2 performance vs SELF 200ms"
python run_match.py -f -r 50 -o SELF -p 12 -t 200
cp matches.log matches_h2_v_self_t200.log
#
echo "h2 performance vs RANDOM 250ms"
python run_match.py -f -r 50 -o RANDOM -p 12 -t 250
cp matches.log matches_h2_v_random_t250.log
echo "h2 performance vs GREEDY 250ms"
python run_match.py -f -r 50 -o GREEDY -p 12 -t 250
cp matches.log matches_h2_v_greedy_t250.log
echo "h2 performance vs MINIMAX 250ms"
python run_match.py -f -r 50 -o MINIMAX -p 12 -t 250
cp matches.log matches_h2_v_minimax_t250.log
echo "h2 performance vs SELF 250ms"
python run_match.py -f -r 50 -o SELF -p 12 -t 250
cp matches.log matches_h2_v_self_t250.log
