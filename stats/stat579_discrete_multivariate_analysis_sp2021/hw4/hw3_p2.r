#this program computes an estimate of gamma for an IXJ table observed from 
#cross sectional sampling with ordinal variables

#enter data for an IXJ contigency table
counts = matrix(c(
	7,7,2,3,
	2,8,3,7,
	1,5,4,9,
	2,8,9,14),
	nrow = 4,byrow = TRUE)

sex.satisfaction=c("never/occassionally",
                   "fairly often",
                   "very often",
                   "almost always")

dimnames(counts) = list(
  "husband's rating"=sex.satisfaction,
  "wife's rating"=sex.satisfaction)
  
counts

#compute the number of concordant pairs, see lecture notes for details
a=4
b=4
con = 0
i=1
j=1
for (i in 1:(a-1)) {
  for (j in 1:(b-1)) {
    sub = 0
    h=i+1
    while (h <= a) {
      k=j+1
      while (k <= b) {
        sub = sub + counts[h,k]
        k=k+1
      }
      h=h+1
    }
    con = con + counts[i,j]*sub
    j=j+1
  }
  i=i+1
}

#compute the number of discordant pairs, see lecture notes for details
a=4
b=4
dis = 0
i=1
j=1
for (i in 1:(a-1)) {
  for (j in 2:b) {
    sub = 0
    h=i+1
    while (h <= a) {
      k=j-1
      while (k >= 1) {
        sub = sub + counts[h,k]
        k=k-1
      }
      h=h+1
    }
    dis = dis + counts[i,j]*sub
    j=j+1
  }
  i=i+1
}

print(c(con,dis))

#compute estimates for the probs of concordance and discordance
n=sum(counts)
pi.hat.C = 2*con /n/(n-1)
pi.hat.D = 2*dis /n/(n-1)

print(c(pi.hat.C,pi.hat.D))

#compute the estimate of gamma
gamma.hat = (con-dis)/(con+dis)
print(gamma.hat,digits = 3)
