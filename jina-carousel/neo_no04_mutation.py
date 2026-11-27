import sys,re; sys.path.insert(0,'.')
from PIL import Image, ImageDraw
from engine import F, tl, wrap, wrap2, draw_just, gl, ctext
W,H=1080,1440; M=80
BG='#F9EAD7'; K='#17191B'; WHITE='#FFFFFF'
LV={'하':('#BFE23A',K,'중학 수준'),'중':('#FFE164',K,'고1 수준'),'상':('#E10600',WHITE,'고3 수준')}
P={
'하':("Copying a book by hand can cause a misprint. A cell also copies its DNA, and sometimes it makes a mistake. This mistake is called a mutation. Many mutations hurt the animal, but a few help it. An animal with more offspring passes on its genes.",
     ['mistake','mutation','hurt','help','offspring','genes'],
     "책을 손으로 베끼면 오타가 생길 수 있어요. 세포도 DNA를 복사하는데, 가끔 실수를 해요. 이 실수를 돌연변이라고 불러요. 많은 돌연변이는 동물에게 해롭지만, 몇몇은 동물에게 도움이 돼요. 자손이 더 많은 동물이 자신의 유전자를 이어 가요."),
'중':("A misprint in a copied book is a mistake, because the author's words are fixed. A mutation is different. It is a change in DNA, and whether it helps depends on the environment. A change that is harmful in one place may be useful in another. Animals with more offspring pass on their traits.",
     ['misprint','mutation','environment','harmful','useful','traits'],
     "베낀 책의 오타는 저자의 글이 정해져 있기 때문에 실수예요. 돌연변이는 달라요. 돌연변이는 DNA의 변화이고, 그것이 도움이 되는지는 환경에 달려 있어요. 한 곳에서 해로운 변화가 다른 곳에서는 쓸모 있을 수 있어요. 자손이 더 많은 동물이 자신의 특징을 이어 가요."),
'상':("Biologists often compare mutations to misprints, yet the analogy has a limit. A misprint is wrong only because the author's original text is fixed, whereas no original genome exists against which a mutation could be judged. Whether a change is fatal or beneficial depends on fitness, that is, how many offspring survive in a given environment.",
     ['analogy','fixed','whereas','fatal','fitness','offspring'],
     "생물학자들은 흔히 돌연변이를 오식에 비유하지만, 그 비유에는 한계가 있다. 오식이 틀린 것은 저자의 원문이 정해져 있기 때문일 뿐이고, 돌연변이를 판단할 기준이 되는 원본 유전체는 존재하지 않는다. 변화가 치명적인지 이로운지는 적응도, 즉 주어진 환경에서 얼마나 많은 자손이 살아남는지에 달려 있다."),
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
def save(im,n): p=f'output/no04_neo/neo_att_{n}.png'; im.save(p); paths.append(p)
n=0
# 1 cover
im,d=base(); n+=1
box(d,(M,250,W-M,1250),WHITE)
X0=M+64
d.text((X0,320),'같은 주제,',font=F(96),fill=K)
y=title(d,[('세 가지 ',False),('수준',True),('으로',False)],445,96,x=X0)
d.rectangle((X0,y+40,X0+120,y+48),fill=K)
f=F(44,False); yy=y+100
for l in ['오늘의 주제는 「돌연변이와 적응도」.','같은 내용을 중학, 고1, 고3 수준의','영어로 각각 읽어 보세요.']:
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
V=[('하','mistake','실수','sometimes it makes a mistake'),('하','mutation','돌연변이','This mistake is called a mutation'),('하','hurt','해치다, 해롭게 하다','Many mutations hurt the animal'),('하','help','도움이 되다','but a few help it'),('하','offspring','자손','An animal with more offspring'),('하','gene','유전자 (genes: 복수형)','passes on its genes'),
   ('중','misprint','오타, 오식','A misprint in a copied book'),('중','mutation','돌연변이','A mutation is different'),('중','environment','환경','depends on the environment'),('중','harmful','해로운','A change that is harmful in one place'),('중','useful','쓸모 있는','may be useful in another'),('중','trait','특징, 형질 (traits: 복수형)','pass on their traits')]
V2=[('상','analogy','비유, 유사','the analogy has a limit'),('상','fixed','정해진, 고정된','original text is fixed'),('상','whereas','~인 반면','whereas no original genome exists'),('상','fatal','치명적인','Whether a change is fatal or beneficial'),('상','fitness','적응도','depends on fitness'),('상','offspring','자손','how many offspring survive')]
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
rows=[('하',"Many mutations hurt the animal, but a few help it."),('중',"A change that is harmful in one place may be useful in another."),('상',"Whether a change is fatal or beneficial depends on fitness, that is, how many offspring survive in a given environment.")]
d.text((M,y),'같은 생각, 다른 수준: "돌연변이의 좋고 나쁨은 환경에 달려 있다"',font=F(34),fill=K); y+=70
for lv,s in rows:
    c,tc,_=LV[lv]; f=F(30,False); ls=wrap(s,f,W-2*M-150); h=len(ls)*45+40
    box(d,(M,y,W-M,y+h),WHITE,r=14,sh=7,bw=4)
    bx=(M+20,y+h/2-25,M+70,y+h/2+25); d.rounded_rectangle(bx,10,fill=c,outline=K,width=3); ctext(d,bx,lv,F(28),tc)
    for i,l in enumerate(ls): d.text((M+96,y+20+i*45),l,font=f,fill=K)
    y+=h+22
y+=16
pts=[('문장 길이','짧은 문장 여러 개 → 원인(because)과 대조가 있는 문장 → whereas, that is로 이어진 긴 문장'),('어휘','mistake, hurt, help → harmful, useful, traits → analogy, fatal, fitness처럼 생물·논증 용어'),('구조','단순한 나열 → because, may be → yet, whereas, Whether A or B depends on'),('읽는 요령','상 수준에서는 whereas 앞(비유의 한계)과 뒤(정해진 원문 vs 원본 없음)를 대비해서 읽어요')]
for k,v in pts:
    f=F(30,False); ls=wrap(v,f,W-2*M-190)
    d.text((M,y),k,font=F(30),fill='#E10600')
    for i,l in enumerate(ls): d.text((M+190,y+i*44),l,font=f,fill=K)
    y+=len(ls)*44+18
print('compare end',y)
assert y<=1330, y
save(im,n)
print(paths)
