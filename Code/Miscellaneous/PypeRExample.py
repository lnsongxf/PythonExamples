from pyper import R
def foo(r):
    r("a <- NULL")
for i in range(20):
    r("a <- rbind(a, seq(1000000) * 1.0 * %d)" % i)
print r("sum(a)")