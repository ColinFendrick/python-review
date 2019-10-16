print(
    (lambda x: 'Stringify {}'.format(x))(99786)
)


# This contains several unnecessary steps
def lam(x): return int(bool(int(x) % 2))


print(lam(1), lam(8))
