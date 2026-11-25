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
text(s,0.8,1.8,7.2,2.6,"Quadratic & Square-Root Voting",size=50,font=H,bold=True,name="Title")
text(s,0.8,4.6,6.9,1.3,"A DAO whale outvotes the community. Can a different voting rule give intensity a voice and make money buy less influence?",size=20,color=RGBColor(0xDD,0xDD,0xE4))
text(s,0.8,6.4,7,0.4,"[Team names]  ·  [Date]",size=14,color=MUTED)
box(s,8.6,1.3,4.1,2.6,LIME)
text(s,8.6,1.3,4.1,2.6,["1 WHALE","60% of tokens"],size=26,color=BG,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
for i in range(40):
    box(s,8.6+(i%10)*0.43,4.3+(i//10)*0.5,0.33,0.33,VIOLET)
text(s,8.6,6.4,4.2,0.4,"The community: 40% of tokens",size=13,color=MUTED)
notes(s,"Hook: a governance proposal passes or fails because one large holder votes. Replace with a real DAO example or keep stylised.")

# 2
s=new(); head(s,2,"The two problems")
card(s,0.6,1.9,5.9,3.9,"PROBLEM 1",LIME,"Intensity ignored",["One-person-one-vote ignores intensity of preference","A 51% majority with mild preferences beats a 49% minority with strong ones"])
card(s,6.85,1.9,5.9,3.9,"PROBLEM 2",CORAL,"Plutocracy",["One-token-one-vote lets whales dominate DAOs","Influence scales linearly with wealth"])
box(s,0.6,6.05,12.15,0.8,LIME)
text(s,0.9,6.05,11.6,0.8,"Both methods try to give intensity a voice while making money buy less influence.",size=18,color=BG,bold=True,anchor=MSO_ANCHOR.MIDDLE)
notes(s,"(1) 1p1v ignores intensity: 51% mild beats 49% strong. (2) 1 token 1 vote = plutocracy; whales dominate DAOs. Both methods give intensity a voice while making money buy less influence.")

# 3
s=new(); head(s,3,"QV mechanics and the worked example")
box(s,0.6,1.9,5.6,1.4,LIME)
text(s,0.6,1.9,5.6,1.4,"cost = v²",size=44,color=BG,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
text(s,0.6,3.55,5.6,3.3,["Each voter gets a budget of credits","Casting v votes on one issue costs v² credits","Marginal cost of the next vote is 2v+1: it rises linearly","A utility maximizer spreads votes so that votes are roughly proportional to intensity of preference"],size=16,bullet=True)
rows=[("Votes v","Total cost v²","Next vote costs"),("1","1","3"),("2","4","5"),("3","9","7"),("4","16","9")]
tb=s.shapes.add_table(5,3,Inches(6.7),Inches(1.9),Inches(6.0),Inches(2.5)).table
for i,r in enumerate(rows):
    for j,v in enumerate(r):
        c=tb.cell(i,j); c.text=v; pa=c.text_frame.paragraphs[0]; pa.alignment=PP_ALIGN.CENTER
        f=pa.runs[0].font; f.size=Pt(15); f.name=B; f.bold=(i==0); f.color.rgb=BG if i==0 else WHITE
        c.fill.solid(); c.fill.fore_color.rgb=LIME if i==0 else (PANEL if i%2 else RGBColor(0x1F,0x1F,0x26))
box(s,6.7,4.65,6.0,2.2,PANEL)
text(s,6.95,4.75,5.5,2.0,["WORKED EXAMPLE (illustrative)","Budget 10 credits; intensity 3 on issue A, 1 on issue B.","Votes a=3k, b=k cost 9k²+k²=10k², so k=1: 3 votes on A (9 credits), 1 on B (1 credit)."],size=14,color=RGBColor(0xDD,0xDD,0xE4),after=6)
notes(s,"QV: budget of credits; v votes cost v^2; marginal cost 2v+1 rises linearly; optimiser spreads votes roughly in proportion to preference intensity. The worked example here is illustrative: swap in your own if preferred.")

# 4
s=new(); head(s,4,"Square-root voting and its link to QV")
box(s,0.6,1.9,5.6,1.4,VIOLET)
text(s,0.6,1.9,5.6,1.4,"power = √tokens",size=36,color=BG,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
box(s,7.15,1.9,5.6,1.4,LIME)
text(s,7.15,1.9,5.6,1.4,"cost = v²",size=36,color=BG,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
text(s,6.2,1.9,0.95,1.4,"⇄",size=36,color=WHITE,font=H,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
text(s,0.6,3.6,6.0,3.3,["Voting power equals √(tokens held)","Spend t tokens, get √t votes: the same curve read in reverse","Difference: QV usually has a budget allocated across many issues; square-root voting applies to a single token balance"],size=16,bullet=True)
box(s,7.15,3.6,5.6,3.2,PANEL)
text(s,7.4,3.75,5.1,0.4,"THE INSIGHT",size=13,color=LIME,font=H,bold=True)
text(s,7.4,4.2,5.1,2.5,["Two rules, one mathematical object.","e.g. 100× the tokens buys only 10× the votes."],size=20,font=H,bold=True,after=14)
notes(s,"Voting power = sqrt(tokens). Spend t tokens, get sqrt(t) votes: the inverse of QV's v^2 cost. Key difference: QV usually spreads a budget over many issues; sqrt voting applies to a single token balance. This is the 'insight moment'.")

# 5
s=new(); head(s,5,"Do they work? The good case")
for i,(tag,c,h,d) in enumerate([("01",LIME,"Intensity gets a voice","Voters concentrate votes where they care most"),("02",VIOLET,"Whales dampened","Influence grows with the square root, not linearly"),("03",CORAL,"Efficiency","[Cite result: e.g. Lalley & Weyl, Gitcoin grants]")]):
    x=0.6+i*4.15; box(s,x,1.9,3.85,3.5,PANEL)
    text(s,x+0.3,2.1,3.3,0.8,tag,size=40,color=c,font=H,bold=True)
    text(s,x+0.3,3.1,3.3,0.9,h,size=22,font=H,bold=True)
    text(s,x+0.3,4.1,3.3,1.2,d,size=15,color=RGBColor(0xDD,0xDD,0xE4))
text(s,0.6,5.8,12.1,0.9,"Takeaway: with honest, one-person-one-identity voters, QV approximates the efficient outcome. [Confirm with sources]",size=18,color=LIME,bold=True)
notes(s,"Best-case evidence: theory and practice.")

# 6
s=new(); head(s,6,"Why they don't fully solve it")
card(s,0.6,1.9,5.9,4.9,"LIMIT 1",CORAL,"Sybil attacks",["Split one balance across k identities","Cost of n votes falls from n² to n²/k","Identity verification reintroduces trust"])
card(s,6.85,1.9,5.9,4.9,"LIMIT 2",VIOLET,"Collusion",["Vote buying and coordinated blocs undo the convexity","Side payments can be cheaper than the quadratic cost","[Mitigations: MACI, pairwise bounding]"])
notes(s,"Show the Sybil arithmetic.")

# 7
s=new(); head(s,7,"Gaming and perverse incentives")
text(s,0.6,1.9,4.8,4.8,["Strategic voters misreport intensity","Whales split across wallets to evade the penalty","Incentive to bribe many cheap voters","Simulation: whale share of votes under each rule"],size=16,bullet=True)
cd=CategoryChartData(); cd.categories=["1","2","5","10","50","100"]
cd.add_series("Token-weighted",(60,60,60,60,60,60)); cd.add_series("QV, honest",(35,35,35,35,35,35)); cd.add_series("QV, whale splits wallets",(35,42,50,55,59,60))
gf=s.shapes.add_chart(XL_CHART_TYPE.LINE,Inches(5.7),Inches(1.8),Inches(7.0),Inches(4.8),cd); gf.name="Simulation chart (PLACEHOLDER DATA)"
ch=gf.chart; chart_style(ch,"Whale vote share (%) vs number of wallets used")
for sr,c in zip(ch.plots[0].series,[MUTED,LIME,CORAL]):
    sr.format.line.color.rgb=c; sr.format.line.width=Pt(3); sr.smooth=False
placeholder_tag(s,5.7,6.65,7)
notes(s,"Replace placeholder series with real simulation results.")

# 8
s=new(); head(s,8,"Negative votes")
text(s,0.6,1.7,12.1,0.6,"What if voters could spend credits against a proposal? Cost stays v², the sign is free.",size=18,color=MUTED)
card(s,0.6,2.5,5.9,4.3,"UPSIDE",LIME,"Express opposition",["Voters signal how strongly they object","Protects a passionate minority","[Effect on whale / Sybil results]"])
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
s=new(); head(s,10,"Conclusions and open questions")
card(s,0.6,1.9,5.9,4.9,"CONCLUSIONS",LIME,"What we found",["QV and square-root voting address intensity and plutocracy","Strong when identity is verified and collusion is limited","[Key finding from simulation]"])
card(s,6.85,1.9,5.9,4.9,"OPEN QUESTIONS",VIOLET,"What's still unknown",["Can Sybil resistance be cheap and trustless?","Collusion resistance in practice","[Negative votes and N candidates]"])
notes(s,"Close with the headline answer to each of the README questions.")

import os
p.save(os.path.join(os.path.dirname(os.path.abspath(__file__)),"final_project_outline.pptx"))
