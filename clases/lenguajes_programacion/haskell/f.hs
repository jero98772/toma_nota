factorial :: Int -> Int
factorial n = product [1 .. n]

doblex x = x*2
doblePar x y = doblex x + doblex y  

incInteligente x = (if x>100 then div x 100 else 1) + x