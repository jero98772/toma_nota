factorial :: Int -> Int
factorial n = product [1 .. n]
--factorial n = product [1..n]
main=do
  factorial 20
