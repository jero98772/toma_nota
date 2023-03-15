from pyswip import Prolog
prolog = Prolog()
prolog.consult("knowledge_base.pl")
print(prolog.query("es(X,d4Nc6e4e5f4f6dxe5fxe5fxe5Nxe5Qd4Nc6Qe5)"))
#list(prolog.query("es(X,)")) == [{'X': 'd4Nc6e4e5f4f6dxe5fxe5fxe5Nxe5Qd4Nc6Qe5+Nxe5c4Bb4+'}]

#for soln in prolog.query("father(X,Y)"):
    #print(soln["X"], "is the father of", soln["Y"])