import sys,re; sys.path.insert(0,'.')
from PIL import Image, ImageDraw
from engine import F, tl, wrap, wrap2, draw_just, gl, ctext
W,H=1080,1440; M=80
BG='#F9EAD7'; K='#17191B'; WHITE='#FFFFFF'
LV={'하':('#BFE23A',K,'중학 수준'),'중':('#FFE164',K,'고1 수준'),'상':('#E10600',WHITE,'고3 수준')}
P={
'하':("Do you ever hear only the words you like? When we believe something, we look for facts that agree with us. We often ignore facts that do not. So our idea feels more and more right. Try to listen to the other side, too.",
     ['believe','facts','agree','ignore','idea','side'],
     "자기가 좋아하는 말만 들리는 적이 있나요? 우리는 무언가를 믿으면, 그 믿음과 맞는 사실을 찾아요. 맞지 않는 사실은 자주 무시하고요. 그래서 우리 생각은 점점 더 옳게 느껴져요. 반대편의 말도 들어 보려고 해 보세요."),
'중':("People do not judge facts neutrally. Once we hold a belief, we tend to notice evidence that supports it and to dismiss evidence that challenges it. Psychologists call this confirmation bias. As a result, even when we are shown the same information, our original opinions can become stronger instead of changing.",
     ['neutrally','tend','evidence','dismiss','challenges','bias'],
     "사람들은 사실을 중립적으로 판단하지 않는다. 일단 어떤 믿음을 갖게 되면, 우리는 그 믿음을 뒷받침하는 증거는 알아차리고 그것에 이의를 제기하는 증거는 묵살하는 경향이 있다. 심리학자들은 이를 확증 편향이라고 부른다. 그 결과 똑같은 정보를 보여 주어도, 우리의 원래 의견은 바뀌기보다 오히려 더 강해질 수 있다."),
'상':("Confirmation bias refers to the tendency to seek out, interpret, and remember information in ways that confirm one's existing beliefs. Because we rarely notice this filtering, our beliefs can grow stronger without ever being genuinely tested. Critical thinking therefore begins not with defending our views but with deliberately examining the evidence that contradicts what we would like to believe.",
     ['tendency','interpret','confirm','filtering','deliberately','contradicts'],
     "확증 편향은 자신이 이미 가진 믿음을 확인해 주는 방향으로 정보를 찾고, 해석하고, 기억하는 경향을 말한다. 우리는 이런 걸러 내기를 거의 알아차리지 못하기 때문에, 믿음은 제대로 시험받지 않은 채 더 강해질 수 있다. 따라서 비판적 사고는 자기 견해를 방어하는 것이 아니라, 우리가 믿고 싶어 하는 것과 모순되는 증거를 의도적으로 살펴보는 데서 시작된다."),
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
def save(im,n): p=f'output/no02_neo/neo_att_{n}.png'; im.save(p); paths.append(p)
n=0
# 1 cover
im,d=base(); n+=1
box(d,(M,250,W-M,1250),WHITE)
X0=M+64
d.text((X0,320),'같은 주제,',font=F(96),fill=K)
y=title(d,[('세 가지 ',False),('수준',True),('으로',False)],445,96,x=X0)
d.rectangle((X0,y+40,X0+120,y+48),fill=K)
f=F(44,False); yy=y+100
for l in ['오늘의 주제는 「확증 편향」.','같은 내용을 중학, 고1, 고3 수준의','영어로 각각 읽어 보세요.']:
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
V=[('하','believe','믿다','When we believe something,'),('하','facts','사실 (fact의 복수형)','look for facts'),('하','agree','일치하다, 동의하다','facts that agree with us'),('하','ignore','무시하다','We often ignore facts'),('하','idea','생각','our idea feels more and more right'),('하','side','편, 쪽','listen to the other side'),
   ('중','neutrally','중립적으로','do not judge facts neutrally'),('중','tend to','~하는 경향이 있다','we tend to notice evidence'),('중','evidence','증거','evidence that supports it'),('중','dismiss','묵살하다, 일축하다','to dismiss evidence'),('중','challenge','반박하다, 도전하다','evidence that challenges it'),('중','bias','편향','confirmation bias')]
V2=[('상','tendency','경향','the tendency to seek out, interpret, and remember'),('상','interpret','해석하다','seek out, interpret, and remember'),('상','confirm','확인해 주다, 뒷받침하다','in ways that confirm one\'s existing beliefs'),('상','filtering','걸러 내기','we rarely notice this filtering'),('상','deliberately','의도적으로, 일부러','but with deliberately examining the evidence'),('상','contradict','모순되다, 어긋나다','the evidence that contradicts')]
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
rows=[('하',"When we believe something, we look for facts that agree with us."),('중',"We tend to notice evidence that supports it and to dismiss evidence that challenges it."),('상',"Confirmation bias refers to the tendency to seek out, interpret, and remember information in ways that confirm one's existing beliefs.")]
d.text((M,y),'같은 말, 다른 수준: "믿음에 맞는 정보를 찾고 받아들인다"',font=F(34),fill=K); y+=70
for lv,s in rows:
    c,tc,_=LV[lv]; f=F(30,False); ls=wrap(s,f,W-2*M-150); h=len(ls)*45+40
    box(d,(M,y,W-M,y+h),WHITE,r=14,sh=7,bw=4)
    bx=(M+20,y+h/2-25,M+70,y+h/2+25); d.rounded_rectangle(bx,10,fill=c,outline=K,width=3); ctext(d,bx,lv,F(28),tc)
    for i,l in enumerate(ls): d.text((M+96,y+20+i*45),l,font=f,fill=K)
    y+=h+22
y+=16
pts=[('문장 길이','when절 + 관계대명사 한 개 → tend to 병렬 + 관계대명사 두 개 → 동사 세 개 병렬 + 긴 수식'),('어휘','believe, ignore → evidence, dismiss → interpret, filtering, contradict처럼 추상적인 말'),('구조','When절 → tend to A and to B → not A but B, without ever being tested'),('읽는 요령','상 수준에서는 therefore 뒤와 not A but B의 B에 글쓴이의 핵심이 있어요')]
for k,v in pts:
    f=F(30,False); ls=wrap(v,f,W-2*M-190)
    d.text((M,y),k,font=F(30),fill='#E10600')
    for i,l in enumerate(ls): d.text((M+190,y+i*44),l,font=f,fill=K)
    y+=len(ls)*44+18
print('compare end',y)
assert y<=1330, y
save(im,n)
print(paths)
