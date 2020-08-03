numalreves <- function(num){
  ultimo <- (num %% 10)*100
  primero <- num %/%100
  mitad <-  ((num %/% 10)%% 10) *10
  newnum <- ultimo+mitad+primero
  return(newnum)
}
print(numalreves(num=987))
print(numalreves(num=972))