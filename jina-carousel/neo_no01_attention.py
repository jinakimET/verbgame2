import sys,re; sys.path.insert(0,'.')
from PIL import Image, ImageDraw
from engine import F, tl, wrap, gl, ctext
W,H=1080,1440; M=80
BG='#F9EAD7'; K='#17191B'; WHITE='#FFFFFF'
LV={'하':('#BFE23A',K,'중학 수준'),'중':('#FFE164',K,'고1 수준'),'상':('#E10600',WHITE,'고3 수준')}
P={
'하':("Many apps are free. But the companies still make money. How? They show you ads. The longer you use an app, the more ads you see. So your time is what they sell. Next time, ask yourself: who is paying?",
     ['free','still','companies','ads','sell','paying'],
     "많은 앱은 무료예요. 그런데도 회사들은 돈을 벌어요. 어떻게요? 여러분에게 광고를 보여 줘요. 앱을 오래 쓸수록 광고를 더 많이 보게 돼요. 그러니까 그들이 파는 건 여러분의 시간이에요. 다음에는 스스로 물어보세요. 돈을 내는 사람은 누구일까?"),
'중':("Most social media services cost nothing to use, but they are not really free. These companies earn money by selling advertisers access to our attention. That is why apps are designed to keep us scrolling, with endless feeds and personalized recommendations. The more time we spend, the more profitable we become to them.",
     ['advertisers','access','designed','endless','personalized','profitable'],
     "대부분의 소셜 미디어 서비스는 이용하는 데 돈이 들지 않지만, 정말로 무료인 것은 아니다. 이 회사들은 광고주에게 우리의 주의에 접근할 권리를 팔아 돈을 번다. 그래서 앱은 끝없는 피드와 맞춤 추천으로 우리가 계속 스크롤하도록 설계되어 있다. 우리가 시간을 많이 쓸수록, 우리는 그들에게 더 큰 수익이 된다."),
'상':("In an age of information abundance, attention, not information, has become the scarce resource. Platforms that appear to offer their services for free are in fact converting users' attention into revenue by selling it to advertisers. Consequently, their designs are optimized not for users' well-being but for engagement, subtly shaping what we see and, ultimately, what we choose.",
     ['abundance','scarce','converting','revenue','optimized','engagement'],
     "정보가 넘쳐나는 시대에는 정보가 아니라 주의가 희소한 자원이 되었다. 서비스를 무료로 제공하는 것처럼 보이는 플랫폼들은 사실 사용자의 주의를 광고주에게 팔아 수익으로 바꾸고 있다. 그 결과 그들의 설계는 사용자의 행복이 아니라 참여도에 맞춰 최적화되어 있으며, 우리가 무엇을 보는지, 그리고 결국 무엇을 선택하는지를 은근히 형성한다."),
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
def save(im,n): p=f'output/no01_neo/neo_att_{n}.png'; im.save(p); paths.append(p)
n=0
# 1 cover
im,d=base(); n+=1
box(d,(M,250,W-M,1250),WHITE)
X0=M+64
d.text((X0,320),'같은 주제,',font=F(96),fill=K)
y=title(d,[('세 가지 ',False),('수준',True),('으로',False)],445,96,x=X0)
d.rectangle((X0,y+40,X0+120,y+48),fill=K)
f=F(44,False); yy=y+100
for l in ['오늘의 주제는 「주의 경제」.','같은 내용을 중학, 고1, 고3 수준의','영어로 각각 읽어 보세요.']:
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
    for i,l in enumerate(ls): d.text((M+56,y0+i*lh),l,font=f,fill=tc)
    swipe(d); save(im,n)
# vocab
V=[('하','free','무료의','Many apps are free.'),('하','still','그런데도, 여전히','The companies still make money.'),('하','company','회사 (복수형 companies)','The companies still make money.'),('하','ad','광고 (advertisement의 줄임말)','They show you ads.'),('하','sell','팔다','Your time is what they sell.'),('하','pay','돈을 내다 (paying은 진행형)','Who is paying?'),
   ('중','advertiser','광고주','selling advertisers access'),('중','access','접근, 이용할 권리','access to our attention'),('중','design','설계하다','be designed to ~: ~하도록 설계되다'),('중','endless','끝없는','endless feeds'),('중','personalized','개인 맞춤의','personalized recommendations'),('중','profitable','수익성 있는','the more profitable we become')]
V2=[('상','abundance','풍부함','an age of information abundance'),('상','scarce','희소한, 부족한','the scarce resource'),('상','convert A into B','A를 B로 바꾸다','converting users\' attention into revenue'),('상','revenue','수익','into revenue'),('상','optimize','최적화하다','designs are optimized for engagement'),('상','engagement','참여(도), 이용 정도','not for well-being but for engagement')]
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
rows=[('하',"So your time is what they sell."),('중',"These companies earn money by selling advertisers access to our attention."),('상',"Platforms ... are in fact converting users' attention into revenue by selling it to advertisers.")]
d.text((M,y),'같은 말, 다른 수준: "회사는 우리의 시간과 관심을 판다"',font=F(34),fill=K); y+=70
for lv,s in rows:
    c,tc,_=LV[lv]; f=F(33,False); ls=wrap(s,f,W-2*M-150); h=len(ls)*50+44
    box(d,(M,y,W-M,y+h),WHITE,r=14,sh=7,bw=4)
    bx=(M+20,y+h/2-25,M+70,y+h/2+25); d.rounded_rectangle(bx,10,fill=c,outline=K,width=3); ctext(d,bx,lv,F(28),tc)
    for i,l in enumerate(ls): d.text((M+96,y+22+i*50),l,font=f,fill=K)
    y+=h+22
y+=16
pts=[('문장 길이','짧은 문장 여러 개 → 접속사로 이은 문장 → 수식어와 삽입이 붙은 긴 문장'),('어휘','ads, sell → advertisers, profitable → revenue, optimize처럼 추상적인 말'),('구조','So / That is why → not A but B, 분사구문(subtly shaping ...)'),('읽는 요령','상 수준에서는 not A but B의 B, 그리고 Consequently 뒤가 글쓴이의 핵심이에요')]
for k,v in pts:
    f=F(32,False); ls=wrap(v,f,W-2*M-190)
    d.text((M,y),k,font=F(32),fill='#E10600')
    for i,l in enumerate(ls): d.text((M+190,y+i*48),l,font=f,fill=K)
    y+=len(ls)*48+20
print('compare end',y)
assert y<=1330, y
save(im,n)
print(paths)
