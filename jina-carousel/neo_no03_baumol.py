import sys,re; sys.path.insert(0,'.')
from PIL import Image, ImageDraw
from engine import F, tl, wrap, wrap2, draw_just, gl, ctext
W,H=1080,1440; M=80
BG='#F9EAD7'; K='#17191B'; WHITE='#FFFFFF'
LV={'하':('#BFE23A',K,'중학 수준'),'중':('#FFE164',K,'고1 수준'),'상':('#E10600',WHITE,'고3 수준')}
P={
'하':("A string quartet needs four players. It did two hundred years ago, and it does today. Machines helped factories make more things, but they cannot make music faster. Still, musicians' pay rises along with pay in other jobs. So concerts cost more and more, and many theaters need help.",
     ['machines','faster','pay','rises','cost','theaters'],
     "현악 4중주에는 연주자 네 명이 필요해요. 200년 전에도 그랬고 지금도 그래요. 기계는 공장이 더 많은 물건을 만들도록 도왔지만, 음악을 더 빨리 만들 수는 없어요. 그래도 음악가의 임금은 다른 직업의 임금과 함께 올라요. 그래서 공연은 점점 더 비싸지고, 많은 극장이 도움을 필요로 해요."),
'중':("Technology cannot speed up every kind of work. A live concert still needs the same number of musicians and the same amount of time. Yet, to keep musicians, theaters must raise pay as wages rise in other industries. As a result, the cost of each performance keeps climbing, so many theaters depend on public support.",
     ['speed','wages','industries','performance','climbing','support'],
     "기술이 모든 종류의 일을 빠르게 만들 수는 없다. 라이브 콘서트에는 여전히 같은 수의 음악가와 같은 시간이 필요하다. 하지만 음악가를 붙잡아 두려면, 다른 산업의 임금이 오르는 만큼 극장도 임금을 올려야 한다. 그 결과 공연 한 번에 드는 비용은 계속 오르고, 그래서 많은 극장이 공적 지원에 의존한다."),
'상':("Baumol's cost disease describes how sectors whose productivity cannot rise, such as live performance, nonetheless see their costs climb. Because labor markets compete for workers, wages in these stagnant sectors must keep pace with those in progressive ones. Consequently, such activities grow ever more expensive relative to manufactured goods, which is why they increasingly rely on subsidies and donations.",
     ['productivity','nonetheless','stagnant','pace','relative','subsidies'],
     "보몰의 비용 질병은 라이브 공연처럼 생산성이 오를 수 없는 부문에서도 비용은 오르는 현상을 설명한다. 노동 시장은 일할 사람을 두고 경쟁하기 때문에, 이런 정체된 부문의 임금은 발전하는 부문의 임금과 보조를 맞춰야 한다. 그 결과 이런 활동은 공산품에 비해 점점 더 비싸지고, 그래서 점점 더 보조금과 기부에 의존한다."),
}
def nwords(t): return len(t.split())
def box(d,b,fill,r=18,sh=12,bw=5):
    x0,y0,x1,y1=b
    d.rounded_rectangle((x0+sh,y0+sh,x1+sh,y1+sh),r,fill=K)
    d.rounded_rectangle(b,r,fill=fill,outline=K,width=bw)
def base(lv=None):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    for gx in range(40,W,40):
        for gy in range(40,H,40): d.ellipse((gx-2,gy-2,gx+2,gy+2),fill='#EAD6BD')
    f=F(28); t='영어지문 세계관 · 수준별 읽기'; tw=tl(t,f)
    box(d,(M,64,M+tw+44,118),K,r=27,sh=0,bw=0); ctext(d,(M,64,M+tw+44,118),t,f,'#BFE23A')
    if lv:
        c,tc,name=LV[lv]; t2=f'{lv} · {name}'; tw2=tl(t2,f)
        box(d,(W-M-tw2-44-8,64,W-M-8,118),c,r=27,sh=6,bw=4); ctext(d,(W-M-tw2-44-8,64,W-M-8,118),t2,f,tc)
    d.text((M,H-92),'@jina.ssam_english',font=F(26,False),fill='#6B5B4A')
    return im,d
def swipe(d):
    t='스와이프'; f=F(28); d.text((W-M-74-tl(t,f),H-94),t,font=f,fill=K)
    box(d,(W-M-56,H-102,W-M-4,H-50),'#BFE23A',r=26,sh=4,bw=4); ctext(d,(W-M-56,H-102,W-M-4,H-50),'→',F(30),K)
def title(d,t,y,size=64,hl=None,hlc='#BFE23A',x=M):
    f=F(size)
    for seg,h in t:
        tw=tl(seg,f)
        if h:
            gt,gb=gl(size); pad=int(size*0.14)
            d.rectangle((x-8,y+gt-pad,x+tw+8,y+gb+pad),fill=hlc)
        d.text((x,y),seg,font=f,fill=K); x+=tw
    return y+int(size*1.3)
def passage(d,text,marks,x,y,w,size,color):
    f=F(size,False); fb=F(size); lh=int(size*1.62); sp=tl(' ',f)
    gt,gb=gl(size); pad=int(size*0.12)
    toks=text.split(' '); lines=[]; cur=[]; cw=0
    for t in toks:
        core=re.sub(r"[^A-Za-z'-]","",t).lower().rstrip("'")
        hl=core in marks; ft=fb if hl else f; tw=tl(t,ft)
        if cur and cw+sp+tw>w: lines.append(cur); cur=[]; cw=0
        cur.append((t,hl,tw)); cw+=(sp if len(cur)>1 else 0)+tw
    lines.append(cur)
    if d is None: return len(lines)*lh
    for i,ln in enumerate(lines):
        cx=x; yy=y+i*lh
        for t,hl,tw in ln:
            if hl:
                core=re.match(r"[A-Za-z'-]+",t); cwid=tl(core.group(0),fb) if core else tw
                d.rectangle((cx-4,yy+gt-pad,cx+cwid+4,yy+gb+pad),fill='#BFE23A')
            d.text((cx,yy),t,font=fb if hl else f,fill=color); cx+=tw+sp
    return len(lines)*lh
paths=[]
BOXH=900; INNER=BOXH-110
def fit_size(hfn,lo=36,hi=60):
    for sz in range(hi,lo-1,-1):
        if hfn(sz)<=INNER: return sz
    raise AssertionError('text does not fit box')
def save(im,n): p=f'output/no03_neo/neo_att_{n}.png'; im.save(p); paths.append(p)
n=0
# 1 cover
im,d=base(); n+=1
box(d,(M,250,W-M,1250),WHITE)
X0=M+64
d.text((X0,320),'같은 주제,',font=F(96),fill=K)
y=title(d,[('세 가지 ',False),('수준',True),('으로',False)],445,96,x=X0)
d.rectangle((X0,y+40,X0+120,y+48),fill=K)
f=F(44,False); yy=y+100
for l in ['오늘의 주제는 「보몰의 비용 질병」.','같은 내용을 중학, 고1, 고3 수준의','영어로 각각 읽어 보세요.']:
    assert X0+tl(l,f)<W-M-40,l
    d.text((X0,yy),l,font=f,fill=K); yy+=70
yy+=50; x=X0
for lv in ['하','중','상']:
    c,tc,name=LV[lv]; t=f'{lv} {name}'; tw=tl(t,F(36))
    box(d,(x,yy,x+tw+44,yy+76),c,r=16,sh=7,bw=4); ctext(d,(x,yy,x+tw+44,yy+76),t,F(36),tc); x+=tw+44+26
assert x<W-M
for i,l in enumerate(['수준이 올라가면 무엇이 달라지는지도','마지막 장에 정리했어요.']):
    d.text((X0,yy+130+i*52),l,font=F(34,False),fill='#6B5B4A')
swipe(d); save(im,n)
# fix: cover title x offset
for lv in ['하','중','상']:
    text,marks,ko=P[lv]; c,tc,name=LV[lv]
    # passage
    im,d=base(lv); n+=1
    title(d,[('지문 읽기',False)],170,60)
    d.text((M,262),f'{nwords(text)} words · 형광 표시는 단어 장에서 설명',font=F(30,False),fill='#6B5B4A')
    w=W-2*M-112; size=fit_size(lambda sz: passage(None,text,marks,0,0,w,sz,K))
    h=passage(None,text,marks,0,0,w,size,K)
    top=int(330+(1320-330-BOXH)/2); box(d,(M,top,W-M,top+BOXH),WHITE)
    passage(d,text,marks,M+56,top+(BOXH-h)/2+8,w,size,K)
    swipe(d); save(im,n)
    # translation
    im,d=base(lv); n+=1
    title(d,[('해석',False)],170,60)
    sz=fit_size(lambda z: len(wrap(ko,F(z,False),W-2*M-112))*int(z*1.65)); f=F(sz,False); ls=wrap(ko,f,W-2*M-112); lh=int(sz*1.65)
    top=int(330+(1320-330-BOXH)/2); box(d,(M,top,W-M,top+BOXH),c)
    y0=top+(BOXH-len(ls)*lh)/2+8
    for i,(l,last) in enumerate(wrap2(ko,f,W-2*M-112)): draw_just(d,l,M+56,y0+i*lh,W-2*M-112,f,tc,not last)
    swipe(d); save(im,n)
# vocab
V=[('하','machine','기계','Machines helped factories make more things'),('하','faster','더 빠르게','they cannot make music faster'),('하','pay','임금, 급여','musicians\' pay rises along with pay'),('하','rise','오르다 (rises: 3인칭 단수)','musicians\' pay rises'),('하','cost','비용이 들다','concerts cost more and more'),('하','theater','극장 (theaters: 복수형)','many theaters need help'),
   ('중','speed up','속도를 높이다','Technology cannot speed up every kind of work'),('중','wages','임금','as wages rise in other industries'),('중','industry','산업 (industries: 복수형)','in other industries'),('중','performance','공연','the cost of each performance'),('중','climb','오르다','keeps climbing'),('중','support','지원','depend on public support')]
V2=[('상','productivity','생산성','sectors whose productivity cannot rise'),('상','nonetheless','그럼에도 불구하고','nonetheless see their costs climb'),('상','stagnant','정체된','in these stagnant sectors'),('상','keep pace with','~와 보조를 맞추다','must keep pace with those in progressive ones'),('상','relative to','~에 비해','relative to manufactured goods'),('상','subsidy','보조금 (subsidies: 복수형)','rely on subsidies and donations')]
def vocab(items,head):
    global n
    im,d=base(); n+=1
    title(d,head,170,60)
    n_=len(items); RH=min(150,int((990-18*n_)/n_)); sc=RH/120; y=int(330+(1320-330-n_*(RH+18))/2)
    for lv,en,ko,ex in items:
        c,tc,_=LV[lv]
        box(d,(M,y,W-M,y+RH),WHITE,r=14,sh=7,bw=4)
        bx=(M+22,y+RH/2-26,M+74,y+RH/2+26); d.rounded_rectangle(bx,10,fill=c,outline=K,width=3); ctext(d,bx,lv,F(28),tc)
        fe,fk,fx=F(int(44*sc)),F(int(32*sc)),F(int(28*sc),False)
        ty=y+(RH-int(102*sc))/2-int(6*sc)
        d.text((M+100,ty),en,font=fe,fill=K); d.text((M+100+tl(en,fe)+20,ty+int(16*sc)),ko,font=fk,fill='#3A2F25')
        assert M+100+tl(ex,fx)<W-M-20, ex
        d.text((M+100,ty+int(60*sc)),ex,font=fx,fill='#6B5B4A')
        assert M+100+tl(en,fe)+20+tl(ko,fk)<W-M-20, en
        y+=RH+18
    assert y<=1330, y
    swipe(d); save(im,n)
vocab([v for v in V if v[0]=='하'],[('단어 정리 ',False),('하',True)])
vocab([v for v in V if v[0]=='중'],[('단어 정리 ',False),('중',True)])
vocab(V2,[('단어 정리 ',False),('상',True)])
# compare
im,d=base(); n+=1
title(d,[('수준이 올라가면 ',False),('달라지는 것',True)],170,56)
y=290
rows=[('하',"Machines helped factories make more things, but they cannot make music faster."),('중',"Technology cannot speed up every kind of work."),('상',"Baumol's cost disease describes how sectors whose productivity cannot rise, such as live performance, nonetheless see their costs climb.")]
d.text((M,y),'같은 생각, 다른 수준: "공연은 생산성이 오르기 어렵다"',font=F(34),fill=K); y+=70
for lv,s in rows:
    c,tc,_=LV[lv]; f=F(30,False); ls=wrap(s,f,W-2*M-150); h=len(ls)*45+40
    box(d,(M,y,W-M,y+h),WHITE,r=14,sh=7,bw=4)
    bx=(M+20,y+h/2-25,M+70,y+h/2+25); d.rounded_rectangle(bx,10,fill=c,outline=K,width=3); ctext(d,bx,lv,F(28),tc)
    for i,l in enumerate(ls): d.text((M+96,y+20+i*45),l,font=f,fill=K)
    y+=h+22
y+=16
pts=[('문장 길이','짧은 문장 여러 개 → 접속사·부사로 이은 문장 → 관계사절과 삽입이 있는 긴 문장'),('어휘','machine, pay → wages, industries → productivity, stagnant, subsidies처럼 경제 용어'),('구조','but, So → to V(목적), as(~함에 따라) → how절, whose, which is why'),('읽는 요령','상 수준에서는 Because 뒤(원인)와 Consequently 뒤(결과)를 짝지어 읽어요')]
for k,v in pts:
    f=F(30,False); ls=wrap(v,f,W-2*M-190)
    d.text((M,y),k,font=F(30),fill='#E10600')
    for i,l in enumerate(ls): d.text((M+190,y+i*44),l,font=f,fill=K)
    y+=len(ls)*44+18
print('compare end',y)
assert y<=1330, y
save(im,n)
print(paths)
