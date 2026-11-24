# Arithmetic positivity, two-translate Weil tests, and a finite periodic Möbius approximation

**Date:** 2026-11-24  
**Status:** Mathematical reductions and obstruction examples proved on paper; decisive approximation estimate unproved (overall B: GRH-hard, no independent shortcut).  
**Novelty:** New to this PR, not a claim of priority in the mathematical literature. The approximation is a concrete Nyman–Beurling/Báez-Duarte-type construction.  
**Lean / CI:** No local Lean check, no CI or Actions run, no Lean code/import/signature changes.

## 1. Repository facts

Re-read the proof bodies on main: [ZeroFreeAllOfTopG](../src/Development/AutomorphicArithmetic/CharacterBoxes/ZeroFreeAllOfTopG.lean), [TopShape](../src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopShape.lean), [SupplyChi](../src/Development/AutomorphicArithmetic/CharacterBoxes/SupplyChi.lean), [DesWin](../src/Development/AutomorphicArithmetic/CharacterBoxes/DesWin.lean), [DivinNOfHypV](../src/Development/AutomorphicArithmetic/CharacterBoxes/DivinNOfHypV.lean), [formB](../src/Development/AutomorphicArithmetic/PrimitiveCosets/Imports.lean), [lemmaL](../src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/lemmaL.lean), [landauWindow](../src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/landauWindow.lean), [Main](../src/Main.lean), and [Statements](../src/Statements.lean). The existing Host/TopG and Landau notes correctly identify the two separate inputs and the positive-part window cut. The source proof of divinN_of_hypV calls vvRecord and divinN_at. The exact final Landau proof uses high-order derivative bounds and isolated-pole asymptotics. No new proof-constant dependency measurement was performed. The following alternative avoids even the Landau-window theorem as a mathematical premise, if its unproved estimate can be supplied.

## 2. Proved: short-support Weil positivity and two-translate detection

For primitive chi of conductor q and parity a, let Z be the multiset of nontrivial zeros shifted by 1/2, invariant under z -> -conj(z). For smooth compactly supported complex f,g on R define F(z)=integral f(u)exp(zu) du, similarly G, and

    Q_chi(f,g) = sum_(z in Z) F(z) conj(G(-conj(z))).

Hermitian by reflection; absolutely convergent by vertical rapid decay and classical zero count O(T log(q(T+2))). For h=f*tilde(g), tilde(g)(u)=conj(g(-u)), H its transform, the classical explicit formula equals

    P(h) + log(q/pi) h(0)
      + (1/(2pi)) integral_R H(it) Re digamma((1/2+a+it)/2) dt
      - sum_(n>=2) Lambda(n)/sqrt(n) *
          [chi(n) h(log n) + conj(chi(n)) h(-log n)].

P=H(1/2)+H(-1/2) for primitive trivial character, zero otherwise. Prime terms are finite, archimedean integral absolutely convergent; no conditional regularization is needed. Under GRH Q(f,f) is a sum of squared transform magnitudes; without GRH a reflected pair gives 2 Re(F(z) conj(F(-conj(z)))) and has no algebraic sign.

**Short-support result.** For each fixed chi, sufficiently short support diameter ell implies Q(f,f)>0 for nonzero f. Indeed ell<log 2 removes all prime terms. The archimedean multiplier A(t)=log(q/pi)+Re digamma((1/2+a+it)/2) has finite lower bound m and tends to +infinity. Choose T with A>=1 for |t|>T. Since |F(it)|^2<=ell ||f||_2^2, Plancherel bounds the archimedean contribution below by [1-max(1-m,0)T ell/pi]||f||_2^2. For the trivial primitive character the pole term has absolute value <=2 ell exp(ell/2)||f||_2^2 after centering the support (Q is translation invariant); absorb it by decreasing ell. This is a direct argument for sufficiently small support, not the sharp support range.

**Two-translate criterion (proved here).** Fix arbitrary r>0. Let f be the infinite convolution of uniform probability measures on [-a_j,a_j], a_j=r*2^(-j), j>=1. The limit exists as a probability measure on [-r,r]; its transform is the locally uniformly convergent product F(z)=prod_j sinh(a_j z)/(a_j z). The product has no zeros off the imaginary axis: all individual zeros are imaginary and the tail converges to a nonzero limit locally away from those zeros by sum a_j^2<infinity. On the imaginary axis any finite number of factors yields arbitrary polynomial decay (remaining factors have modulus <=1), so the measure has a C-infinity density. Then the following are equivalent: GRH for chi; for every real t>=0 the 2-by-2 Gram matrix of Q on f,T_t f (T_t f(u)=f(u-t)) is positive semidefinite.

Proof: diagonals both equal Q(f,f) by translation invariance. PSD gives |C(t)|<=Q(f,f) for C(t)=Q(T_t f,f)=sum_z c_z exp(tz), c_z=F(z)conj(F(-conj(z))). Its Laplace transform is holomorphic in Re w>0 and, initially for Re w>1/2, equals sum_z c_z/(w-z). This sum is normally convergent away from its discrete poles, since sum |c_z|<infinity, and at an off-line zero with Re z>0 the residue is its positive multiplicity times nonzero c_z. Contradiction by analytic continuation. Reflection excludes Re z<0. Conversely GRH makes Q PSD. QED.

This shows why restricting to a single bump and two-dimensional tests does not escape GRH: the separation t is unbounded. The same proof applies to any finite positive-weight sum of primitive zero forms: at a shared zero the identical c_z is multiplied by a strictly positive weighted multiplicity, so there is no cancellation. Hence *universal averaged Weil positivity* IS sufficient to exclude zeros of every participating character; it must not be conflated with mere averaged prime-square positivity.

## 3. Proved obstructions: character orthogonality and elementary operators

For arbitrary finitely supported complex b_n and A_a=sum_(n=a mod q) b_n on units a, S_chi=sum_n b_n chi(n), exact orthogonality gives

    (1/phi(q)) sum_chi |S_chi|^2 = sum_a |A_a|^2,
    S_chi = sum_a chi(a) A_a.

A single residue concentrated mass b gives |S_chi|=|b| for every chi, even for nonnegative b_n. Example q=3, (A_1,A_2)=(2,0) gives the nonprincipal character sum 2. Orthogonality needs a genuine quantitative bound on residue fluctuations, not merely signs. A fixed-q sum of nonnegative *individual errors* tending to zero WOULD control each term, but orthogonality alone does not prove that sum tends to zero. In averaging primitive Weil formulas over all characters modulo q, the omitted Euler factors at p|q for imprimitive characters must be corrected explicitly.

Convolution by a nonnegative residue-class measure on ell^2((Z/qZ)^*) is not necessarily positive as an operator: delta at -1 mod 3 acts by the swap, with eigenvalues 1,-1. Convolution adjoint times convolution is positive, but its eigenvalues are squared character sums, not zero-location bounds. The two-sided log-translation generator -i d/du on H^1(R) in L^2(R) is self-adjoint by Fourier diagonalization, with real continuous spectrum, not an identification with Dirichlet zeros. A closer arithmetic operator on L^2(0,1) is D_n f(x)=f(nx), extended by zero outside (0,1); norm n^(-1/2), and n^(1/2)D_n is an isometry, not self-adjoint for n>1. Its adjoint has eigenvectors k_s(x)=x^(conj(s)-1) with eigenvalues n^(1/2-conj(s)) for Re s>1/2. Such interior-disk eigenvalues are compatible with an isometry's adjoint, not a contradiction. No verified spectral identification or positive global trace comparison was obtained. Connes–Consani's archimedean trace work is a genuine local result, not a global twisted positivity proof.

## 4. Exactly one decisive replacement theorem: finite arithmetic approximation (UNPROVED)

Fix any primitive Dirichlet character chi modulo q, including q=1 (zeta), extended by zero at nonunits as usual. For integer k>=0 put A_chi(k)=sum_(1<=m<=k)chi(m), B_chi(k)=A_chi(k)-2 A_chi(floor(k/2)), and h(k)=1_(k>=1)-2*1_(k>=2). Then B_chi is periodic of period 2q and |B_chi|<=3q (for q>1, A_chi is periodic of period q and bounded by q; for q=1, B_chi(k)=k mod 2). For integer N>=2 define

    V_N(s) = sum_(n<=N) mu(n) chi(n)(1-log n/log N) n^(-s),
    e_N(k) = h(k) - sum_(n<=N) mu(n) chi(n)
                       (1-log n/log N) B_chi(floor(k/n)),
    E_N(chi) = sum_(k=1)^(N^3) |e_N(k)|^2 / [k(k+1)].

**Decisive theorem (not proved): for every primitive chi, liminf_(N->infinity) E_N(chi)=0.** No uniformity in q is required. Equivalently, for every epsilon>0 and N0>=2 there exists N>=N0 with E_N<epsilon. The coefficients are fixed explicitly, not optimized over a Hilbert space; this is not the abstract universal Weil criterion or an existential spectral identification. Its independent difficulty is substantial.

### Unconditional proof of its implication to the exact endpoint

Let H=L^2((0,1),dx), f_chi(x)=B_chi(floor(1/x)) on (0,1], extended by zero, and h_0(x)=1_(0,1](x)-2*1_(0,1/2](x). Let g_N=sum_(n<=N) mu(n)chi(n)(1-log n/log N) f_chi(nx). Boundedness ensures all these functions are in H. For Re s>1, integrating character partial sums term by term gives

    integral_0^1 f_chi(x) x^(s-1) dx = (1-2^(1-s)) L(s,chi)/s,
    integral_0^1 h_0(x) x^(s-1) dx = (1-2^(1-s))/s.

Both identities extend to Re s>0 by holomorphy; the apparent zeta pole at s=1 is canceled by 1-2^(1-s). Dilation multiplies the Mellin transform by n^(-s). If L(rho,chi)=0 and 1/2<beta=Re rho<1, the bounded linear functional ell_rho(v)=integral_0^1 v(x)x^(rho-1)dx has operator norm (2beta-1)^(-1/2) and annihilates every g_N, but ell_rho(h_0)=(1-2^(1-rho))/rho !=0 (factor zeros have Re=1). Therefore

    ||h_0-g_N||_2^2 >= (2beta-1)|1-2^(1-rho)|^2/|rho|^2 > 0

for every N. On the other hand the exact change of variable t=1/x and step-function partition gives

    ||h_0-g_N||_2^2 = sum_(k>=1) |e_N(k)|^2/[k(k+1)].

The tail after N^3 is at most (1+3qN)^2/(N^3+1), tending to zero for fixed q. Thus the decisive theorem contradicts every such rho. Classical zero-freeness on Re>=1 (except the principal pole) and the imprimitive Euler factors, nonzero for Re>0, yield the exact nonvanishing statement in src/Statements.lean. Functional equation then yields strip GRH. No family construction or Landau-window input is used.

There is a second exact trace/norm interpretation by Mellin-Plancherel:

    ||h_0-g_N||_2^2 = (1/(2pi)) integral_R
      |1-2^(1-s)|^2 |1-L(s,chi)V_N(s)|^2 / |s|^2 dt, s=1/2+it.

The factor magnitude lies between sqrt(2)-1 and sqrt(2)+1. For q=1 this is equivalent (up to bounded weights) to convergence of the explicit logarithmically tapered Möbius polynomial in the Nyman–Beurling problem, studied by Bettin–Conrey–Farmer with conditional quantitative estimates. It is not a new independently established GRH proof.

### Independent proof attempt: first missing step

Complete multiplicativity and the exact divisor identities sum_(n|m) mu(n)=1_(m=1), sum_(n|m) mu(n) log n=-Lambda(m) give, for 1<=k<=N,

    e_N(k) = -[psi_chi(k)-2 psi_chi(floor(k/2))]/log N,
    psi_chi(k)=sum_(m<=k) Lambda(m)chi(m).

Thus pointwise convergence e_N(k)->0 for each fixed k is proved, but the needed weighted square convergence on the growing range is not. Exactly

    E_N = (1/log^2 N) sum_(k<=N) |psi_chi(k)-2psi_chi(floor(k/2))|^2/[k(k+1)]
          + sum_(N<k<=N^3) |e_N(k)|^2/[k(k+1)].

Both nonnegative terms must become small along the SAME sequence. The first is a weighted arithmetic fluctuation budget; the second a truncated divisor-convolution boundary budget. Character periodicity bounds B but does not bound the signed sum of N dilates. The trivial |e_N|<=1+3qN gives only O(q^2 N) on k>N, not o(1). Even pointwise convergence with this order of bound does not imply weighted norm convergence: a toy error e_N(k)=sqrt(N) on N<=k<2N and zero elsewhere converges pointwise to zero but weighted squared norm=1/2. This is an abstract obstruction to dominated convergence, not a Dirichlet-character counterexample.

For fixed N, the finite E_N is an explicit nonnegative quadratic form in Möbius coefficients (Gram matrix of real/complex arithmetic step functions); positivity of that matrix gives only a lower bound 0, not the small upper bound sought. No independently proved estimate for E_N->0, even liminf, was obtained. The zero-based lower bound above shows why this is GRH-hard, though no converse from GRH for these particular coefficients is claimed.

### Finite numerical checks (not certificates or proofs)

Computed E_N using direct floating-point finite sums for primitive q=1, real chi mod 3 (values 0,1,-1), and complex chi mod 5 (values at residues 0,1,2,3,4: 0,1,i,-i,-1). Values rounded:

| N | zeta | chi mod 3 | chi mod 5 |
|---:|---:|---:|---:|
|4|0.539600|0.257533|0.397640|
|8|0.305794|0.160456|0.307306|
|16|0.191346|0.113994|0.243556|
|32|0.133984|0.085832|0.202296|
|64|0.100180|0.070533|0.169735|

For N=64 and q=3, split E_N approximately 0.044336 (k<=N) + 0.026197 (k>N). These finite tests only illustrate the exact decomposition and are consistent with, not evidence proving, the asymptotic claim.

## 5. Classification and dependency comparison

- A (local mathematical deductions only): small-support positivity; two-translate equivalence proof; exact finite arithmetic norm identity and zero-obstruction lower bound; character orthogonality identities.
- C for bare positivity/averaging/operator symmetry as a zero-exclusion argument, and for pointwise-to-norm convergence without domination.
- Overall B: finite approximation estimate remains independently unproved and implies GRH, including RH. No claim of its equivalence to GRH or lesser difficulty. Unlike the general density criterion, a prescribed approximant's success is an additional assertion.
- Hypothetical replacement graph: explicit periodic character sums + Möbius convolution + independently proved finite approximation estimate -> Mellin evaluation / Cauchy–Schwarz -> primitive zero exclusion -> imprimitive reduction. This would mathematically bypass TopG, HostExW, VWin, DIVinN, VVle, HypV, Galois representations, local-global compatibility and local Hecke congruences, as well as the Landau window criterion. No Lean proof-constant/import reduction is claimed.
- The prior local discriminant bound has an independently proved nontrivial local estimate; its family budget would remove only a narrower numerical branch. The direct approximation has larger potential dependency removal but a more explicit GRH-hard unresolved step. There is no verified reason to prioritize it as easier.

References: [Bombieri, Weil quadratic functional](https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0); [Connes–Consani, archimedean trace](https://arxiv.org/abs/2006.13771); [Dirichlet L-function explicit formula](https://openmaths.org/courses/NT-EXPF/NT-EXPF-02.html); [Dirichlet Nyman–Beurling generalizations](https://arxiv.org/abs/1608.07887); [Bettin–Conrey–Farmer, explicit Möbius approximant](https://arxiv.org/abs/1211.5191). The independent elementary deductions above are not claimed to be new to the literature.

**Decision:** Do not add Lean modules or hypotheses to the proof. The precise open finite approximation estimate is the only selected direct replacement theorem; the two-translate result is a diagnostic equivalence, not a competing shortcut.
