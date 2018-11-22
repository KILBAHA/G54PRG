# =============================================================================
# Ex 04
# =============================================================================


class Expr:
    
    def solve(x,y):
        pass

    def make_tt():
        print ("{} \t| {} \t | {} \t".format("x", "y", "equation"))
        booleans = [True, False]
        for i in range(len(booleans)):
            return Expr.solve(x,y)
              
        

class Not(Expr):
    
    def __init__ (self, notthis):
        self.notthis = notthis
        
    def __str__ (self):
        return "!" + str(self.notthis)
    
    def eval (self, env):
        return not(self.notthis.eval(env))

class Var(Expr):
    
    def __init__ (self, value):
        self.value = value
        
    def __str__ (self):
        return str(self.value)
    
    def eval (self,env):
        return env[self.value]

class BinOp(Expr):
    
    def __init__ (self, left, right):
        self.left = left
        self.right = right
        
    def __str__ (self):
        return "("+ str(self.left) + self.op + str(self.right) + ")"
    
    def eval(self, env):
        #print (self.left)
        return self.fun(self.left.eval(env), self.right.eval(env))


class And(BinOp):
    op = "&"
    
    def fun(self, x, y):
        return x &  y   

class Or(BinOp):
    op = "|"
    
    def fun (self, x, y):
        return x | y

class Eq(BinOp):
    op = "=="
    
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

print(e1)
print(e2)
print(e3)
print(e4)

print (e1.eval(env))
print (e2.eval(env))
print (e3.eval(env))
print (e4.eval(env))


"""
Creating the tables
"""
