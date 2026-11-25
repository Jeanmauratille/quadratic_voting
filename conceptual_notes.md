# Conceptual Notes

## Questions

### 1. What are quadratic voting and square-root voting, and what problems are they trying to solve?

- **Square Root Voting:**
- **Quadratic Voting:**

### 2. Can they completely solve these problems? Why or why not?

- **Square Root Voting:** more efficient at preventing governance attacks
- **Quadratic Voting:** hard to explain, requires explicit payment

### 3. What would happen if one could cast "negative" as well as "positive" votes in this context? Does the utility of these methods change with the number of candidates?

- **Square Root Voting:**
- **Quadratic Voting:**

### 4. Can they completely solve these problems? Why or why not?

- **Square Root Voting:** susceptible to the Sybil Attack
- **Quadratic Voting:**

---

## Sources & Detailed Notes

### Square Root Voting

**Source:** <https://jumpcrypto.com/resources/square-root-voting>

*Square root voting in crypto balances efficient and inclusive governance, and protects the rights of minority tokenholders.*

- **Goals of governance** = efficiency and equity
  - Efficient if it can maximize total expected value for constituents
  - Equitable if it treats all constituents equally
- **Square Root Voting** = a form of governance where a protocol participant's vote is proportional to the square root of their tokens
  - Partially efficient and partially equitable
  - The effectiveness of buying more tokens to gain influence diminishes as the number of votes increases (think square root curve)
- In the "one-token one-vote" model, a few large token holders can dominate (oligopoly?)
- Square root voting creates more inclusivity and protects the rights of minority tokenholders. The goal is to balance efficient and equitable communities (more aligned with crypto ethos)
- **Obstacle for implementation:** the **Sybil Problem** (one person creates multiple identities), which can be addressed via identity, friction, or challenge solutions
- **Other systems:** any power function with an exponent in (0, 1), where exponents closer to 1 are more efficient and exponents closer to 0 are more equitable
- **Rationale for square root voting:** in democratic voting, all voters influence the election equally, regardless of passion. In square root voting, a voter who is twice as passionate can influence the election twice as much by purchasing 4x as many votes
- **Flaw of "one-token one-vote":** governance attacks, where the majority token holders expropriate the minority token holders
  - Square root voting checks majority power, making this more challenging: it increases the **Nakamoto coefficient for governance**, making it harder for a few token holders to commandeer the protocol
- Square root voting also dissuades large buyers from harvesting votes from sellers

#### Sybil Attack

**Sybil Attack** = one person masquerades as multiple individuals to increase voting power.

| Solution type | Approach | Flaws |
| --- | --- | --- |
| **Identity** | Link accounts to people | Potentially erodes privacy; still potentially gamified |
| **Friction** | Make the Sybil attack more costly to execute | Gas costs fall over time (deterrent erodes); historical snapshots go stale in high-turnover protocols; CAPTCHAs can be beaten |
| **Challenge** | Incentivize participants to police the protocol | Needs real investigation and an arbitration mechanism; depends on outside labor |

- Minimum staking solutions exclude small token holders and concentrate power in larger token holders (less equitable)

### Quadratic Voting

*Square root voting is a specific variant of quadratic voting.*

- **Quadratic Voting** = individuals can vote multiple times but pay the square of those votes (cost grows with the square of votes)
- **Two main implementations:**
  1. **Multi-Issue Ballot:** each voter gets a budget of vote credits to spend across many options
  2. **Single-Issue Ballot:** voters literally pay to vote, and the proceeds are redistributed to the community
  - (1) is hard to use, and (2) is unpopular as it requires explicit monetary payment
- Square root voting addresses operational concerns that arise from quadratic voting: it's easier to explain and doesn't require explicit payment
