# Conceptual Notes

## Questions

### 1. What are quadratic voting and square-root voting, and what problems are they trying to solve?

- **Square Root Voting:** each participant's votes are proportional to the square root of their tokens, so buying more tokens buys influence at a diminishing rate. It targets the flaw of "one-token one-vote", where a few large holders dominate and can expropriate minority holders (governance attacks). It aims to balance efficiency and equity, and raises the Nakamoto coefficient for governance.
- **Quadratic Voting:** individuals can vote multiple times but pay the square of their votes, so the cost grows quadratically. This lets voters express how strongly they care (passion), which one-person-one-vote ignores, while limiting the power of money. Square root voting is a specific variant of it.

### 2. Can they completely solve these problems? Why or why not?

- Identity Splitting: the Sybil Attack problem
- Unbundling & Collusion: the same wrapper/lending/exchange mechanisms could sell quadratic voting power too, unless anti-collusion tools are in place
- Tragedy of the Commons: QV & SQV don't fix the root problem that voters are not individually accountable for outcomes
- Wealth still buys *some* extra influence, just at a worse rate 

### 3. What would happen if one could cast "negative" as well as "positive" votes in this context? Does the utility of these methods change with the number of candidates?

- *The sources above don't cover negative votes or the number of candidates yet. Add sources before treating the points below as findings.*
- **Square Root Voting:** [to research] the notes describe positive votes only. One open point: does a negative vote follow the same square-root curve?
- **Quadratic Voting:** [to research] the multi-issue ballot spreads a credit budget across many options, so the number of options plausibly matters. The notes don't say how.

### 4. Can they completely solve these problems? Why or why not?

- **Square Root Voting:** not completely. It is more efficient at preventing governance attacks, but it is susceptible to the Sybil Attack, since splitting tokens across identities defeats the square-root penalty. Each fix has a flaw: identity solutions erode privacy, friction solutions erode as gas costs fall, challenge solutions need arbitration, and minimum staking excludes small holders.
- **Quadratic Voting:** not completely. It is hard to explain and, in the single-issue form, requires explicit payment (unpopular); the multi-issue form is hard to use. It shares the weaknesses listed in question 2: identity splitting, collusion and unbundling, and voters not being accountable for outcomes.

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

## Moving beyond coin voting governance

**Source:** <https://vitalik.eth.limo/general/2021/08/16/voting3.html>

- Decentralized government (DeGov) is necessary but coin voting can be dangerous:
    - with attackers: vote buying, can unbundle economic interest & voting rights through wrapper contracts, borrowing from lending platforms, or exchanging votes with customer coins
    - without attackers: whales outperform small holders, power only goes to these large holders rather than the wider community
- Quadratic voting (non coin-driven governance) makes the power of a single voter proportional to the square root of the economic resources they commit t a decision
    - problems it solves: dampens whale power while keeping a financial component that lets participants signal how strongly they care
    - **QV is only a partial solution:** 
        - Sybil Vulnerability: preventing people from gaming the system and split their resources across many identities requires proof of personhood
        - Collusion & Vote Buying: both proof of personhood & proof of participation requre some form of anti-collusion
        - Square-root weighting doesn't address vote buying directly