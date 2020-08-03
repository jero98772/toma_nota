bolsa <- function(dias){
  valoranterior <- 0
  for (i in 1:dias+1) {
    print("valor minimo: ")
    valormin <- scan()
    print("valor maximo: ")
    valormax <- scan()
    variabilidad = valormax - valormin
    if(i ==0 | valormin < valoranterior & valormin < valormax){
      valoranterior <- valormin
      print("valor minimo ",valormin)
    
    }
    else{
      print("ese valor minimo no fue el minimo")
    }
    if(i == 0 | valormax > valoranterior & valormax > valormin){
      valoranterior  = valormax
      print("valor maximo",valormax)
    }
     else{
        print("ese valor maximo no fue el minimo")
     }
    if(variabilidad < valoranterior){
      valoranterior  = variabilidad
      print("valor variabiliad",variabilidad,"en el dia")
    }
    else{
      print("variabilidad no cambio",variabilidad)
    
    }
  }
  print("valor variabiliad",variabilidad,"en el dia",i)
  print("valor maximo",valormax)
  print("valor minimo",valormin)
}

#valormin <- c(373,13,25,436,464,123,131,152,363,134)
#valormax <- c(1234,345,242,962,966,858,478,478,685,858,588)
print("dias a evaluar")
dias <- as.int(scan())
bolsa(dias)