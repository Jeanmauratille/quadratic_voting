# Key Answers: Quadratic and Square-Root Voting

## 1. What are QV and square-root voting, and what problems do they solve?

**Quadratic voting (QV)**
- You can cast many votes, but you pay the square of them: total cost is v², and the next vote costs 2v+1.
- Two ways to run it:
  - **Multi-issue ballot:** a budget of vote credits spread across many options. Hard to use.
  - **Single-issue ballot:** voters pay to vote and proceeds go back to the community. Unpopular because it requires explicit payment.

**Square-root voting**
- Votes are proportional to the square root of tokens committed.
- It is a specific variant of QV that is easier to explain and needs no explicit payment.
- A voter who cares twice as much gets twice the influence by committing 4x the tokens.

**Problems targeted**
- One-person-one-vote ignores intensity of preference.
- One-token-one-vote lets a few large holders dominate and lets a majority expropriate the minority.
- Both methods aim to balance efficiency and equity.

**Why quadratic specifically (Lalley & Weyl)**
- Quadratic is the only pricing rule where votes end up proportional to how much each voter values the outcome ("robustly optimal").
- Near-linear pricing gives dictatorship of the most intense voter.
- Very steep pricing collapses to one-person-one-vote.

---

## 2. Can they completely solve these problems?

**No.**

- **Sybil attacks:** splitting funds across identities undoes the penalty. Every fix has a cost: privacy (identity), fading friction (gas costs, stale snapshots, CAPTCHAs), arbitration (challenges), or excluding small holders (minimum stakes).
- **Collusion and unbundling:** wrapper contracts, lending platforms and exchanges could sell voting power, so anti-collusion tools (e.g., MACI) are needed.
- **No individual accountability:** neither method changes who bears the cost of bad decisions.
- **Wealth still buys influence**, just at a worse rate.
- **Limited evidence:** Lalley & Weyl describe their results as stylized, approximate or numerical, and say high-stakes use is not advisable without more experimentation.

---

## 3. Can they be gamed or create perverse incentives?

**Yes.**

- **Identity splitting pays under square-root voting.** Splitting T tokens across n wallets gives n · √(T/n) = √n · √T votes, so n wallets multiply votes by √n. *(My own derivation.)*
- **Vote selling and unbundling:** Vitalik's bribery math (small bribe versus tiny per-voter expected harm) still applies to individually insignificant voters.
- **Minimum staking** stops splitting but excludes small holders, which worsens equity.
- **Broken assumption:** Lalley & Weyl assume voice credits are distributed fairly (e.g., equally), which identity splitting violates.

---

## 4. What if there were negative as well as positive votes?

**What the source says (Lalley & Weyl)**
- Negative votes are built into the core model. Each voter chooses a positive or negative number of votes depending on which side she favors, and A wins when the sum of votes is ≥ 0.
- The cost function is even, so a negative vote costs the same as a positive one.
- Because votes are proportional to intensity under quadratic pricing, opposing intensities net out correctly.

**Likely benefits** *(my inference)*
- Minorities can block as well as support.
- Intensity is captured on both sides of an issue.

**Likely risks** *(my inference)*
- Paying people to vote against a rival's proposal.
- Griefing.
- Sybil splitting that works in both directions.

**Sourcing note:** the sources do not discuss bribery or griefing of negative votes. Present those points as your own analysis.

---

## 5. Does the utility of these methods change with the number of candidates?

**Not directly addressed by the sources.**
- Lalley & Weyl model repeated binary decisions; even choice of leaders is treated as binary.

**What the paper does say matters more**
- **Number of issues:** the price-taking logic needs enough inconsequential issues that voters can trade influence on one for influence on another.
- **Population size:** welfare loss shrinks at a rate of 1/N as the population grows.

**Multi-issue ballots**
- This is where the credit-budget idea is most useful, since voters concentrate credits on what they care about most.

**A square-root quirk with many options** *(my inference)*
- If tokens are counted separately per option, spreading across options yields more total votes (√a + √b > √(a+b)). That rewards spreading unless there is a shared budget.

**Open point**
- The sources do not resolve how this interacts with plurality problems such as vote splitting among similar candidates.

---

## Q&A prep

- Q4 and Q5 are the weakest-sourced answers. Say plainly which parts come from Lalley & Weyl and which are your own reasoning.
- Best remaining source for Q5: Buterin, Hitzig & Weyl, "Liberal Radicalism" (and Buterin's "Quadratic Payments: A Primer").

### Sources used
- Jump Crypto, "Square Root Voting"
- Buterin, "Moving beyond coin voting governance" (2021)
- Lalley & Weyl, "Quadratic Voting: How Mechanism Design Can Radicalize Democracy" (2018)
