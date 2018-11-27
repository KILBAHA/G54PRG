# =============================================================================
# Ex 04
# =============================================================================


class Expr:
    
    def __str__(self):
        return self.str_aux(4)
    
    def make_tt(self):
        print ("y     | x    |" + str(self))
        
        env = {"x":True, "y":True}
        TT = self.eval(env)
        print ("True  | True |" + str(TT))
        
        env = {"x":True, "y":False}
        TF = self.eval(env)
        print ("False | True |" + str(TF))
        
        env = {"x":False, "y":True}
        FT = self.eval(env)
        print ("False | True |" + str(FT))
        
        env = {"x":False, "y":False}
        FF = self.eval(env)
        print ("False | False|" + str(FF))
        
        pass
    
    def isTauto(self):
        env = {"x":True, "y":True}
        TT = self.eval(env)
        env = {"x":False, "y":False}
        FF = self.eval(env)
        env = {"x":True, "y":False}
        TF = self.eval(env)
        env = {"x":False, "y":True}
        FT = self.eval(env)
        
        return TT and FF and TF and FT        

class Not(Expr):
    
    prec = 4
    
    def __init__ (self, notthis):
        self.notthis = notthis
        
    def str_aux (self,prec):
        return "!" + str(self.notthis)
    
    def eval (self, env):
        return not(self.notthis.eval(env))

class Var(Expr):
    
    def __init__ (self, value):
        self.value = value
        
    def str_aux (self,prec):
        return str(self.value)
    
    def eval (self,env):
        return env[self.value]

class BinOp(Expr):
    
    def __init__ (self, left, right):
        self.left = left
        self.right = right
        
    def str_aux (self,prec):
        s = str(self.left) + self.op + str(self.right)
        
        if self.prec < prec:
            return "("+s+")"
        
        else:
            return s
        
    
    def eval(self, env):
        return self.fun(self.left.eval(env), self.right.eval(env))


class And(BinOp):
    op = "&"
    prec = 3
    
    def fun(self, x, y):
        return x &  y   

class Or(BinOp):
    op = "|"
    prec = 2
    
    def fun (self, x, y):
        return x | y

class Eq(BinOp):
    op = "=="
    prec = 1
    
    def fun (self, x, y):
        return x == y
    
"""
Don't edit!:
"""
    
e1 = Or(Var("x"),Not(Var("x")))
e2 = Eq(Var("x"),Not(Not(Var("x"))))
e3 = Eq(Not(And(Var("x"),Var("y"))), Or(Not(Var("x")),Not(Var("y"))))
e4 = Eq(Not(And(Var("x"),Var("y"))),And(Not(Var("x")), Not(Var("y"))))


"""
Dictionary for x and y values
"""
env = {"x":False, "y":True}

boolean = [True,False]

# =============================================================================
# print(e1)
# print(e2)
# print(e3)
# print(e4)
# 
# 
# print (e1.eval(env))
# print (e2.eval(env))
# print (e3.eval(env))
# print (e4.eval(env))
# =============================================================================


print("Truth Tables:")
print("Equation 1")
print(e1.make_tt())
print("Equation 2")
print(e2.make_tt())
print("Equation 3")
print(e3.make_tt())
print("Equation 4")
print(e4.make_tt())

print ("Tautology:")
print("Equation 1")
print(e1.isTauto())
print("Equation 2")
print(e2.isTauto())
print("Equation 3")
print(e3.isTauto())
print("Equation 4")
print(e4.isTauto())


