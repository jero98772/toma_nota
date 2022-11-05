import Data.Char
let remove st n =[ c | c <- st c/=n]
main = do
  let hola = "hola"
  let mundo = "dime tu nombre"
  let salida = hola ++ "\n" ++ mundo
  putStrLn salida
  nombre <- getLine
  remove nombre " " 
  let mayNombre = map toUpper nombre

  putStrLn ("excelente " ++ mayNombre ++ " eres un degenerado")

