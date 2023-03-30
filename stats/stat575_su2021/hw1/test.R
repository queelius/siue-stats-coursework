library(numDeriv)
n <- c(38,34,125)
l <- function(p)
{
  n[1]*log(1/2-p/2) + n[2]*log(p/4) + n[3]/(1/2+p/4)
}

deriv <- function(f,x,h=0.001)
{
  (f(x+h) - f(x))/h
}

dldp <- function(p)
{
  deriv(l,p)
}

newton_method <- function(f,dfdx,x0,eps,debug=T)
{
  n <- 0
  repeat
  {
    
    x1 <- x0 - f(x0) / dfdx(x0)
    n <- n + 1
    
    if (debug==T) { cat("iteration=",n," x=",x1,"\n") }
    
    #if(abs(x1 - x0) < eps)
    #{
    #  break
    #}
    x0 <- x1
    if (n == 10)
      break
  }
  
  list(root=x0,iter=n)
}

sol <- newton_method(l,dldp,0.5,1e-3)
print(sol)



plot(dbeta(seq(0,1,.01),.01,.01))
