main :: IO ()
main = do
  x <- getLine
  let xok = read x :: Integer
  print xok
