"""Generates final_project_outline.pptx next to this file.
Requires: pip install python-pptx
Run: python3 build_slides.py
Note: re-running overwrites final_project_outline.pptx, including any hand edits.
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION

BG=RGBColor(0x17,0x17,0x1C); PANEL=RGBColor(0x26,0x26,0x2E); LIME=RGBColor(0xC6,0xF4,0x32)
CORAL=RGBColor(0xFF,0x6B,0x5B); VIOLET=RGBColor(0x9B,0x8C,0xFF); WHITE=RGBColor(0xF4,0xF4,0xF6); MUTED=RGBColor(0x9A,0x9A,0xA8)
H="Arial"; B="Calibri"; TOTAL=10

p=Presentation(); p.slide_width=Inches(13.333); p.slide_height=Inches(7.5); blank=p.slide_layouts[6]

def new():
    s=p.slides.add_slide(blank); f=s.background.fill; f.solid(); f.fore_color.rgb=BG; return s
def text(s,x,y,w,h,paras,size=18,color=WHITE,font=B,bold=False,align=PP_ALIGN.LEFT,anchor=MSO_ANCHOR.TOP,bullet=False,name=None,after=10):
    t=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h)); tf=t.text_frame; tf.word_wrap=True; tf.vertical_anchor=anchor
    if name: t.name=name
    if isinstance(paras,str): paras=[paras]
    for i,tx in enumerate(paras):
        pa=tf.paragraphs[0] if i==0 else tf.add_paragraph(); pa.alignment=align; pa.space_after=Pt(after)
        r=pa.add_run(); r.text=("–  " if bullet else "")+tx
        r.font.size=Pt(size); r.font.color.rgb=color; r.font.name=font; r.font.bold=bold
    return t
def box(s,x,y,w,h,fill):
    sh=s.shapes.add_shape(MSO_SHAPE.RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb=fill; sh.line.fill.background(); sh.shadow.inherit=False; return sh
def head(s,n,t):
    text(s,0.6,0.35,3,0.4,f"{n:02d} / {TOTAL:02d}",size=14,color=LIME,font=H,bold=True)
    text(s,0.6,0.75,12.1,0.9,t,size=34,font=H,bold=True,anchor=MSO_ANCHOR.MIDDLE,name="Title")
def card(s,x,y,w,h,tag,tagc,heading,items,size=16):
    box(s,x,y,w,h,PANEL)
    text(s,x+0.35,y+0.3,w-0.7,0.4,tag,size=13,color=tagc,font=H,bold=True)
    text(s,x+0.35,y+0.7,w-0.7,0.8,heading,size=24,font=H,bold=True)
    text(s,x+0.35,y+1.6,w-0.7,h-1.8,items,size=size,bullet=True,color=RGBColor(0xDD,0xDD,0xE4))
def notes(s,t): s.notes_slide.notes_text_frame.text=t
def chart_style(ch,t):
    ch.has_title=True; ch.chart_title.text_frame.text=t
    r=ch.chart_title.text_frame.paragraphs[0].runs[0]; r.font.size=Pt(14); r.font.bold=True; r.font.name=B; r.font.color.rgb=WHITE
    ch.font.size=Pt(12); ch.font.name=B; ch.font.color.rgb=MUTED
    ch.has_legend=True; ch.legend.position=XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout=False
    ch.value_axis.major_gridlines.format.line.color.rgb=RGBColor(0x3A,0x3A,0x44); ch.value_axis.format.line.fill.background()
def placeholder_tag(s,x,y,w):
    text(s,x,y,w,0.35,"PLACEHOLDER DATA: replace with simulation output",size=11,color=CORAL,bold=True)

# 1
s=new()
text(s,0.8,1.2,7,0.4,"FINM 31200  /  FINAL PROJECT",size=14,color=LIME,font=H,bold=True)
text(s,0.8,1.8,7.4,2.6,"Quadratic & Square-Root Voting",size=46,font=H,bold=True,name="Title")
text(s,0.8,4.6,6.9,1.3,"Can we design a fair voting mechanism for crypto governance without giving up crypto's ethos?",size=22,color=RGBColor(0xDD,0xDD,0xE4))
text(s,0.8,6.4,7,0.4,"Phoebe Fingold, Alex Gatti Roaf, Jean Mauratille      December 2026",size=14,color=MUTED)
box(s,8.6,1.3,4.1,2.4,LIME)
text(s,8.6,1.3,4.1,2.4,["FAIR","efficient + equitable"],size=26,color=BG,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
text(s,8.6,3.7,4.1,0.6,"+",size=36,color=WHITE,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
box(s,8.6,4.3,4.1,2.4,VIOLET)
text(s,8.6,4.3,4.1,2.4,["CRYPTO ETHOS","decentralized + inclusive + secure"],size=22,color=BG,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
notes(s,"Framing: the project is about finding a voting mechanism that is fair (efficient and equitable, per Jump Crypto) while staying consistent with crypto's ethos (decentralized, inclusive, minority-protecting; privacy is at stake in Sybil fixes). Sources: Jump Crypto (square-root voting); Vitalik Buterin, 'Moving beyond coin voting governance'. Confirm exactly which ethos values you want to name.")

# 2
s=new(); head(s,2,"The Problem: What is a Fair Vote?")
card(s,0.6,1.85,5.9,4.05,"PROBLEM 1",LIME,"Intensity of preference is ignored",["In one-person-one-vote, every voter influences the outcome equally","Governance should be efficient (maximize total expected value) and equitable (treat everyone equally)"],size=15)
card(s,6.85,1.85,5.9,4.05,"PROBLEM 2",CORAL,"Coin voting concentrates power",["One-token-one-vote lets a few large holders dominate and can let a majority expropriate the minority","Voting rights can be unbundled and bought via wrapper contracts, lending platforms or exchanges"],size=15)
box(s,0.6,6.1,12.15,0.75,LIME)
text(s,0.9,6.1,11.6,0.75,"Goal: balance efficiency and equity in a way that fits crypto's ethos of inclusive, decentralized governance.",size=16,color=BG,bold=True,anchor=MSO_ANCHOR.MIDDLE)
notes(s,"Sources: Jump Crypto (goals of governance = efficiency and equity; flaw of one-token-one-vote = governance attacks, where majority holders expropriate minority holders). Vitalik: with attackers (vote buying, unbundling through wrapper contracts, borrowing from lending platforms, exchanging votes with customer coins); without attackers (power goes to large holders rather than the wider community).")
s

# 3
s=new(); head(s,3,"Quadratic Voting (QV): Mechanics and a Worked Example")
# Left: the rule
box(s,0.6,1.9,5.6,1.1,LIME)
text(s,0.6,1.9,5.6,1.1,"cost = v²",size=44,color=BG,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
text(s,0.6,3.1,5.6,0.7,"Vote as many times as you like, but pay the square of your votes. The next vote costs 2v+1.",size=15)
# Left: two ways to run it
text(s,0.6,3.95,5.6,0.35,"TWO WAYS TO RUN QV",size=13,color=LIME,bold=True)
box(s,0.6,4.35,5.6,1.15,PANEL)
text(s,0.8,4.4,5.2,1.05,["1  MULTI-ISSUE BALLOT","Spend a credit budget across many options. Hard to use."],size=14,color=RGBColor(0xDD,0xDD,0xE4),after=4)
box(s,0.6,5.65,5.6,1.15,PANEL)
text(s,0.8,5.7,5.2,1.05,["2  SINGLE-ISSUE BALLOT","Voters pay to vote; proceeds go back to the community. Unpopular."],size=14,color=RGBColor(0xDD,0xDD,0xE4),after=4)
# Right: cost table
rows=[("Votes v","Total cost v²","Next vote costs"),("1","1","3"),("2","4","5"),("3","9","7"),("4","16","9")]
tb=s.shapes.add_table(5,3,Inches(6.7),Inches(1.9),Inches(6.0),Inches(2.5)).table
for i,r in enumerate(rows):
    for j,v in enumerate(r):
        c=tb.cell(i,j); c.text=v; pa=c.text_frame.paragraphs[0]; pa.alignment=PP_ALIGN.CENTER
        f=pa.runs[0].font; f.size=Pt(15); f.name=B; f.bold=(i==0); f.color.rgb=BG if i==0 else WHITE
        c.fill.solid(); c.fill.fore_color.rgb=LIME if i==0 else (PANEL if i%2 else RGBColor(0x1F,0x1F,0x26))
# Right: worked example (multi-issue)
box(s,6.7,4.65,6.0,2.15,PANEL)
text(s,6.95,4.75,5.5,1.95,["WORKED EXAMPLE: MULTI-ISSUE BALLOT (illustrative)","Budget: 10 credits. You care 3x as much about issue A as issue B.","Best split: 3 votes on A (9 credits) + 1 vote on B (1 credit)."],size=14,color=RGBColor(0xDD,0xDD,0xE4),after=6)
notes(s,"Source: Jump Crypto. QV = individuals can vote multiple times but pay the square of those votes. Two implementations: (1) multi-issue ballot with a vote-credit budget, hard to use because voters must allocate credits and calculate summed squares; (2) single-issue ballot where voters pay and proceeds are redistributed to the community, unpopular because it requires explicit monetary payment. Worked example (illustrative): votes a=3k, b=k cost 9k²+k²=10k², so with a 10-credit budget k=1, giving 3 votes on A (9 credits) and 1 on B (1 credit). Swap in your own numbers if preferred.")

# 4
s=new(); head(s,4,"Square-Root Voting and its Connection to QV")
box(s,0.6,1.9,5.6,1.3,VIOLET)
text(s,0.6,1.9,5.6,1.3,"votes ∝ √tokens",size=36,color=BG,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
box(s,7.15,1.9,5.6,1.3,LIME)
text(s,7.15,1.9,5.6,1.3,"cost = v²",size=36,color=BG,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
text(s,6.2,1.9,0.95,1.3,"⇄",size=36,color=WHITE,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
# Left: bullets (shortened to fit above the definition bar)
text(s,0.6,3.4,6.3,2.4,["Votes grow with the square root of tokens, so buying more tokens buys influence at a diminishing rate","A voter who cares twice as much gets twice the influence by buying 4× as many votes","Checks majority power: raises the Nakamoto coefficient for governance","Dissuades large buyers from harvesting votes from sellers"],size=14,bullet=True)
# Right: the link
box(s,7.15,3.4,5.6,2.4,PANEL)
text(s,7.4,3.5,5.1,0.4,"THE LINK",size=13,color=LIME,font=H,bold=True)
text(s,7.4,3.9,5.1,1.85,["Square-root voting is a specific variant of QV.","It is easier to explain and needs no explicit payment.","Any power function with exponent in (0,1) works: near 1 is more efficient, near 0 is more equitable."],size=14,font=H,bold=True,after=6)
# Bottom: definition
box(s,0.6,6.0,12.15,0.9,VIOLET)
text(s,0.9,6.0,11.6,0.9,["NAKAMOTO COEFFICIENT: the minimum number of independent holders who could together control a majority of voting power. Higher = more decentralized."],size=15,color=BG,bold=True,anchor=MSO_ANCHOR.MIDDLE)
notes(s,"Source: Jump Crypto. Square root voting addresses the operational concerns of QV: it's easier to explain and doesn't require explicit payment. Rationale: in one-person-one-vote all voters influence the election equally regardless of how much they care, whereas in square-root voting a voter who cares twice as much can influence the election twice as much by purchasing 4x as many votes. Vitalik frames the same idea as the power of a voter being proportional to the square root of the resources they commit. Nakamoto coefficient: the smallest number of independent entities that would need to collude to control a majority of a system (here, of voting power). Because square-root voting compresses large holders' influence, more holders are needed to reach a majority, so the coefficient rises.")

# 5
s=new(); head(s,5,"Do they Work? Problems Addressed by QV & Square-Root Voting")
for i,(tag,c,h,d) in enumerate([("01",LIME,"Balances Efficiency and Equity","Influence still rises with commitment, but at a diminishing rate: partially efficient and partially equitable"),("02",VIOLET,"Inclusive by Design","Protects the rights of minority tokenholders while still letting holders signal how strongly they care"),("03",CORAL,"Harder to Capture","Raises the Nakamoto coefficient and discourages large buyers from harvesting votes from sellers (if holders can't split into many wallets)")]):
    x=0.6+i*4.15; box(s,x,1.9,3.85,3.7,PANEL)
    text(s,x+0.3,2.05,3.3,0.8,tag,size=36,color=c,font=H,bold=True)
    text(s,x+0.3,2.9,3.3,0.9,h,size=21,font=H,bold=True)
    text(s,x+0.3,3.9,3.3,1.7,d,size=14,color=RGBColor(0xDD,0xDD,0xE4))
text(s,0.6,5.9,12.1,0.9,"Result: governance that is fairer and more inclusive, more aligned with crypto's ethos, as long as Sybil attacks are contained.",size=18,color=LIME,bold=True)
notes(s,"Sources: Jump Crypto (balances efficient and equitable communities, more aligned with crypto ethos; protects minority tokenholders; checks majority power and raises the Nakamoto coefficient; dissuades vote harvesting). Vitalik (keeps a financial component that lets participants signal how strongly they care). Caveat: the Nakamoto coefficient and vote-harvesting benefits assume holders can't split across identities; see next slide.")

# 6
s=new(); head(s,6,"Do they Work? Limits to QV & Square-Root Voting")
items=[("LIMIT 1",CORAL,"Identity Splitting (Sybil Attack)","Splitting tokens across wallets defeats the penalty. Every fix has a cost: privacy, fading friction, arbitration, or excluding small holders."),
       ("LIMIT 2",VIOLET,"Unbundling & Collusion","Wrapper, lending and exchange mechanisms could sell voting power too, unless anti-collusion tools are in place."),
       ("LIMIT 3",LIME,"No Individual Accountability","Neither QV nor square-root voting makes voters individually accountable for outcomes."),
       ("LIMIT 4",CORAL,"Wealth Still Buys Influence","Money still buys some extra influence, just at a diminished rate.")]
for k,(tag,c,h,d) in enumerate(items):
    x=0.6+(k%2)*6.25; y=1.85+(k//2)*2.55
    box(s,x,y,5.9,2.35,PANEL)
    text(s,x+0.35,y+0.2,5.2,0.35,tag,size=13,color=c,font=H,bold=True)
    text(s,x+0.35,y+0.6,5.2,0.5,h,size=21,font=H,bold=True)
    text(s,x+0.35,y+1.2,5.2,1.1,d,size=14,color=RGBColor(0xDD,0xDD,0xE4))
notes(s,"Sources. Vitalik: preventing identity splitting under quadratic voting requires proof of personhood, and both proof of personhood and proof of participation need anti-collusion tools (he cites MACI) so voting power doesn't get sold via smart contracts; his bribery analysis (small bribe vs. tiny per-voter harm) and his skin-in-the-game section on individual accountability. Lalley & Weyl: results are stylized or approximate, high-stakes use is not advisable without more experimentation, and equal credit distribution is assumed (identity splitting would break that assumption). Jump Crypto, Sybil fixes and their flaws: identity solutions erode privacy; friction solutions erode as gas costs fall, snapshots go stale, CAPTCHAs can be beaten; challenge solutions need investigation and arbitration; minimum staking excludes small holders. Our own analysis (not stated directly by the sources): Limit 3 and Limit 4 apply Vitalik's accountability argument and QV's financial component to QV/SQV, and the point that square-root weighting alone doesn't stop vote buying extends his bribery math.")

# 7
s=new(); head(s,7,"Gaming and Perverse Incentives")
text(s,0.6,1.9,4.8,4.8,["Strategic voters misreport intensity","Large holders split across wallets to evade the penalty","Incentive to bribe many cheap voters","Simulation: large holder's share of votes under each rule"],size=16,bullet=True)
cd=CategoryChartData(); cd.categories=["1","2","5","10","50","100"]
cd.add_series("Token-weighted",(60,60,60,60,60,60)); cd.add_series("QV, honest",(35,35,35,35,35,35)); cd.add_series("QV, large holder splits wallets",(35,42,50,55,59,60))
gf=s.shapes.add_chart(XL_CHART_TYPE.LINE,Inches(5.7),Inches(1.8),Inches(7.0),Inches(4.8),cd); gf.name="Simulation chart (PLACEHOLDER DATA)"
ch=gf.chart; chart_style(ch,"Large holder's vote share (%) vs wallets used")
for sr,c in zip(ch.plots[0].series,[MUTED,LIME,CORAL]):
    sr.format.line.color.rgb=c; sr.format.line.width=Pt(3); sr.smooth=False
placeholder_tag(s,5.7,6.65,7)
notes(s,"Replace placeholder series with real simulation results.")

# 8
s=new(); head(s,8,"Negative votes")
text(s,0.6,1.7,12.1,0.6,"What if voters could spend credits against a proposal? Cost stays v², the sign is free.",size=18,color=MUTED)
card(s,0.6,2.5,5.9,4.3,"UPSIDE",LIME,"Express opposition",["Voters signal how strongly they object","Protects a passionate minority","[Effect on large-holder / Sybil results]"])
card(s,6.85,2.5,5.9,4.3,"RISKS",CORAL,"New attack surface",["Strategic negative voting and retaliation","Cheap sabotage of rivals' proposals","[Does the equilibrium change?]"])
notes(s,"Discuss how signed votes change the optimisation and the gaming surface.")

# 9
s=new(); head(s,9,"Effect of the number of candidates")
text(s,0.6,1.9,4.8,4.8,["With 2 options QV is close to majority rule","More options give more room to express intensity","But the budget is spread thinner and strategy gets harder","Does QV's advantage grow with N?"],size=16,bullet=True)
cd=CategoryChartData(); cd.categories=["2","3","5","10","20"]; cd.add_series("QV welfare gain vs 1p1v (%)",(0,4,9,14,17))
gf=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,Inches(5.7),Inches(1.8),Inches(7.0),Inches(4.8),cd); gf.name="Candidates chart (PLACEHOLDER DATA)"
ch=gf.chart; chart_style(ch,"QV welfare gain by number of candidates"); ch.has_legend=False
ch.plots[0].series[0].format.fill.solid(); ch.plots[0].series[0].format.fill.fore_color.rgb=VIOLET
placeholder_tag(s,5.7,6.65,7)
notes(s,"Replace with simulation of welfare vs number of candidates.")

# 10
s=new(); head(s,10,"Conclusions and Remaining Questions")
card(s,0.6,1.9,5.9,4.9,"CONCLUSIONS",LIME,"What we found",["QV and square-root voting move governance toward fairness: intensity of voter preference counts and power is less concentrated in majority tokenholders","Fairness has a cost: identity checks can conflict with crypto's ethos, and collusion needs anti-collusion tools","[Key finding from simulation]"])
card(s,6.85,1.9,5.9,4.9,"OPEN QUESTIONS",VIOLET,"What's still unknown",["Can Sybil resistance be achieved without sacrificing privacy?","How far can fairness go while staying decentralized?","[Negative votes and N candidates]"])
notes(s,"Close with the headline answer to each of the README questions.")

import os
p.save(os.path.join(os.path.dirname(os.path.abspath(__file__)),"final_project_outline.pptx"))
