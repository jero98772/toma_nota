main :: IO ()
main = do 
  x1 <- getLine
  x2 <- getLine
  x3 <- getLine
  x4 <- getLine
  x5 <- getLine
  x6 <- getLine
  x7 <- getLine
  x8 <- getLine
  x9 <- getLine
  x10 <- getLine
  x11 <- getLine
  x12 <- getLine
  x13 <- getLine
  x14 <- getLine
  x15 <- getLine
  x16 <- getLine
  x17 <- getLine
  x18 <- getLine
  x19 <- getLine
  x20 <- getLine
  let xok1 = read x1 :: Integer
  let xok2 = read x2 :: Integer
  let xok3 = read x3 :: Integer
  let xok4 = read x4 :: Integer  
  let xok5 = read x5 :: Integer  
  let xok6 = read x6 :: Integer
  let xok7 = read x7 :: Integer
  let xok8 = read x8 :: Integer
  let xok9 = read x9 :: Integer
  let xok10 = read x10 :: Integer
  let xok11 = read x11 :: Integer
  let xok12 = read x12 :: Integer
  let xok13 = read x13 :: Integer
  let xok14 = read x14 :: Integer
  let xok15 = read x15 :: Integer
  let xok16 = read x16 :: Integer
  let xok17 = read x17 :: Integer
  let xok18 = read x18 :: Integer
  let xok19 = read x19 :: Integer
  let xok20 = read x20 :: Integer
  let numeros=[xok1,xok2,xok3,xok4,xok5,xok6,xok7,xok8,xok9,xok10,xok11,xok12,xok13,xok14,xok15,xok16,xok17,xok18,xok19,xok20]
  sort numeros
  let potencias2 x = [n**2 | n<- [1 .. x] ] 
  let ans=zipWith (+) numeros potencias2 20
  putStrln ans
