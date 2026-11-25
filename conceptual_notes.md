QUESTIONS:
Can they completely solve these problems, why or why not?
- Square Root Voting: more efficient at preventing governance attacks but still susceptible to the Sybil Attack 
- Quadratic Voting: hard to explain, requires explicit payment 


SOURCES & DETAILED NOTES:

**Source:** https://jumpcrypto.com/resources/square-root-voting
**Square Root Voting:**
*Square root voting in crypto balances efficient and inclusive governance, and protects the rights of minority tokenholders.*
- Goals of Governance = efficiency & equity
-   efficient if can maximize total expected value for constituents
-   equitable if it treats all constituents equally
- Square Root Voting = form of governance where a protocol participant's vote is proportional to the square root of their token
-   partially efficient & partially equitable
-   the effectiveness of buying more tokens to have more influence diminishes as the number of votes increase (think square root curve)
- in the "one-token one-vote" model, a few large token holders can dominate (oligopoly?)
- Square Root Voting creates more inclusivity and protects the rights of minority tokenholders, goal is to balance efficient & equitable communities (more aligned with crypto ethos)
- Obstacle for implementation: **Sybil Problem** (one person creates multiple identities), can be addressed via identity, friction, or challenge solutions
- Other Systems:
-   any power function with an exponent in (0,1), where exponents closer to 1 are more efficient and exponents closer to 0 are more equitable
- **Rationale for Square Root Voting:** in democratic voting, all voters influence the election equally, regardless of passion, whereas in square root voting, a voter who is twice as passionate can influence the election twice as much by purchasing 4x many votes
- **Flaw of "One-Token One-Vote":** governance attacks, where the majority token holders expropriate the minority token holders
-   square root voting checks majority power, making this more challenging: it increases the **Nakamoto coefficient for governance**, making it harder for a few token holders to commandeer the protocol
- Square root voting also dissuades large buyers from harvesting votes from sellers
- **Sybil Attack** = one person masquerades as multiple individuals to increase voting power
-   Identity Solutions: link accounts to people
-     flaw: potentially erodes privacy, still potentially gamified
-   Friction Solutions: make Sybil attack more costly to execute
-    flaw: gas costs fall over time (deterrent erodes), historical snapshots go stale in high-turnover protocols, CAPTCHAs can be beaten 
-   Challenge Solutions: incentivize participants to police the protocol
-    flaw: needs real investigation and an arbitration mechanism, depends on outside labor
- Minimum staking solutions exclude small token holders and concentrates power in larger token holders (less equitable)

**Quadratic Voting:** 
*square root voting is a specific variant of quadratic voting*
- Quadratic Voting = individuals can vote multiple times but pay the square of those votes (cost grows with square of votes)
- Two Main implementations: (1) Multi-Issue Ballot where each voter gets a budget of vote credits to spend across many options and (2) Single-Issue Ballot where voters literally pay to vote, and the proceeds are redistributed to the community
-   (1) is hard to use, and (2) is unpopular as it requires explicit monetary payment
- Square root voting addresses operational concerns that arise from quadratic voting: it's easier to explain and doesn't require explicit payment
