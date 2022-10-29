factorial :: Int -> Int
factorial n = product [1 .. n]

doblex x = x*2
doblePar x y = doblex x + doblex y  