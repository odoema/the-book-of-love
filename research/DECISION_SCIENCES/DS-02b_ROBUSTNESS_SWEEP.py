\
    """
    DS-02b robustness sweep.

    Exploratory computational experiment for the reconstructed Hill-cooperative model.
    No result is assumed. Outputs must be inspected and archived before interpretation.

    Tests:
      1. n x K grid
      2. symmetric vs asymmetric alpha/beta
      3. alternative nonlinear response functions

    Standard library only.
    """
    import csv, math
    from pathlib import Path

    OUT = Path(__file__).resolve().parent / "DS-02b_ROBUSTNESS_RESULTS"
    OUT.mkdir(exist_ok=True)

    DT = 0.002
    T = 80.0
    DELTA_A = 1.0
    DELTA_D = 1.0

    def hill(x, K, n):
        return x**n / (K**n + x**n) if x > 0 else 0.0

    def logistic(x, k=10.0, x0=0.5):
        return 1.0 / (1.0 + math.exp(-k*(x-x0)))

    def rhs(a, d, alpha, beta, K, n, fn):
        fa = fn(d, K, n)
        fd = fn(a, K, n)
        return alpha*fa*(1-a)-DELTA_A*a, beta*fd*(1-d)-DELTA_D*d

    def step(a, d, alpha, beta, K, n, fn):
        k1a,k1d=rhs(a,d,alpha,beta,K,n,fn)
        k2a,k2d=rhs(a+DT*k1a/2,d+DT*k1d/2,alpha,beta,K,n,fn)
        k3a,k3d=rhs(a+DT*k2a/2,d+DT*k2d/2,alpha,beta,K,n,fn)
        k4a,k4d=rhs(a+DT*k3a,d+DT*k3d,alpha,beta,K,n,fn)
        a += DT*(k1a+2*k2a+2*k3a+k4a)/6
        d += DT*(k1d+2*k2d+2*k3d+k4d)/6
        return max(0,min(1,a)), max(0,min(1,d))

    def run(a0,d0,alpha,beta,K,n,fn):
        a,d=a0,d0
        for _ in range(int(T/DT)):
            a,d=step(a,d,alpha,beta,K,n,fn)
        return a,d

    rows=[]
    # K grid, cooperativity grid
    for fn_name, fn in [("hill", hill), ("logistic", logistic)]:
        for K in [0.20,0.30,0.40,0.50,0.60,0.70,0.80]:
            for n in [1,1.5,2,2.5,3,4]:
                for alpha,beta,label in [
                    (2.0,2.0,"symmetric"),
                    (2.5,1.5,"asymmetric_A"),
                    (1.5,2.5,"asymmetric_D"),
                    (3.0,2.0,"asymmetric_high"),
                ]:
                    lo=run(0.01,0.01,alpha,beta,K,n,fn)
                    hi=run(0.99,0.99,alpha,beta,K,n,fn)
                    separation=math.hypot(hi[0]-lo[0],hi[1]-lo[1])
                    rows.append({
                        "function":fn_name,"K":K,"n":n,
                        "alpha":alpha,"beta":beta,"case":label,
                        "low_A":lo[0],"low_D":lo[1],
                        "high_A":hi[0],"high_D":hi[1],
                        "history_separation":separation
                    })

    fn = OUT/"n_x_K_asymmetry_grid.csv"
    with open(fn,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)

    print("Robustness sweep complete.")
    print("Output:", fn)
    print("Interpretation is intentionally NOT automated.")
    print("Inspect history_separation, parameter regions, and numerical stability before drawing conclusions.")
