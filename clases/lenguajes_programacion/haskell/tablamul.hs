tablen x y =  [n* x | n <-  [1 .. y] ] --tabla multiplicar de x , y veces
tablaas x = [tablen n x | n <- [1 .. x]]
-- funciona hijueputa