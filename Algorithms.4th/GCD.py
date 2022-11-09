class GCD:
    def gcd():
        def gcd(p, q):
            if q == 0:
                return p
            r = p % q
            return gcd(q, r)
        return gcd
    gcd = staticmethod(gcd())


print(GCD.gcd(12, 15))
