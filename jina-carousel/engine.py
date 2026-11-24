# 영어지문 세계관 글라스 캐러셀 엔진: 글 양에 맞춰 카드 높이가 늘어난다 (글을 자르지 않음)
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1440; M=84; P=56; TOP=150; BOT=1330
B='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'; R='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
_fc={}
SC=[1.0]
def z(v,cap=None):
    k=SC[0] if cap is None else min(SC[0],cap)
    return int(round(v*k))
def F(s,b=True):
    k=(s,b)
    if k not in _fc: _fc[k]=ImageFont.truetype(B if b else R,s,index=1)
    return _fc[k]
class Theme:
    def __init__(s,base,blobs,acc,acc_txt,soft,wh='#FFFFFF',dk='#17191B',dim=0.42):
        s.base,s.blobs,s.acc,s.acc_txt,s.soft,s.wh,s.dk,s.dim=base,blobs,acc,acc_txt,soft,wh,dk,dim
        s.acc_rgb=tuple(int(acc[i:i+2],16) for i in (1,3,5))
_m=ImageDraw.Draw(Image.new('RGB',(4,4)))
def gl(sz,b=True):
    bb=_m.textbbox((0,0),'가',font=F(sz,b)); return bb[1],bb[3]
def tl(t,f): return _m.textlength(t,font=f)
import re
_HANGUL=re.compile(r'[\u1100-\u11FF\u3130-\u318F\uAC00-\uD7A3]')
_CLOSE=set('.,?!:;)]}\u201d\u2019\u300d\u300f\u2026\u00b7%')
_OPEN=set('\u201c\u2018\u300c\u300e([{')
def _one(t,i):
    n=len(t); j=i+1
    if not _HANGUL.match(t[i]):
        while j<n and t[j]!=' ' and not _HANGUL.match(t[j]): j+=1
        if j<n and _HANGUL.match(t[j]): j+=1   # 영문·숫자 뒤의 조사/단위 한 글자는 붙인다 (29번, attention을)
    while j<n and t[j] in _CLOSE: j+=1         # 줄 맨 앞에 마침표·닫는 따옴표가 오지 않게
    return t[i:j]
def _units(t):
    out=[]; i=0; n=len(t)
    while i<n:
        c=t[i]
        if c==' ': out.append(' '); i+=1; continue
        k=i
        while k<n and t[k] in _OPEN: k+=1       # 여는 따옴표는 다음 글자와 붙인다
        if k<n and t[k]!=' ': u=t[i:k]+_one(t,k); out.append(u); i+=len(u)
        elif k>i: out.append(t[i:k]); i=k
        else: u=_one(t,i); out.append(u); i+=len(u)
    return out
def wrap(t,f,w):
    """한글은 글자 단위로 상자 끝까지 채우고, 영어 단어는 쪼개지 않는다."""
    out=[]
    for para in t.split('\n'):
        cur=''
        for u in _units(para):
            if u==' ':
                if cur and not cur.endswith(' '): cur+=' '
                continue
            if tl((cur+u).rstrip(),f)<=w: cur+=u; continue
            if cur.strip(): out.append(cur.rstrip()); cur=''
            if tl(u,f)>w:
                piece=''
                for ch in u:
                    if tl(piece+ch,f)>w: out.append(piece); piece=ch
                    else: piece+=ch
                cur=piece
            else: cur=u
        out.append(cur.rstrip())
        # 마지막 줄에 한두 글자만 남으면 앞 줄에서 두 글자를 내려 보낸다 (앞 줄은 거의 그대로 가득 참)
        if len(out)>=2 and para.strip():
            last=out[-1]; prev=out[-2]
            if 0<len(last.replace(' ',''))<=2 and len(prev)>8 and all(_HANGUL.match(ch) for ch in prev[-2:]):
                out[-2]=prev[:-2]; out[-1]=prev[-2:]+last
    return out
def bg(th,seed):
    im=Image.new('RGB',(W,H),th.base); d=ImageDraw.Draw(im)
    pos=[[(650,-250,1400,500),(-300,500,450,1150),(500,1000,1300,1700)],[(-350,-200,450,550),(600,450,1350,1150),(-250,1000,550,1700)]][seed%2]
    for (x0,y0,x1,y1),c in zip(pos,th.blobs): d.ellipse((x0,y0,x1,y1),fill=c)
    im=im.filter(ImageFilter.GaussianBlur(150)); return Image.blend(im,Image.new('RGB',(W,H),th.base),th.dim)
def glass(im,box,tint=(255,255,255),a=22,r=38,edge=110):
    x0,y0,x1,y1=[int(v) for v in box]
    sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).rounded_rectangle((x0,y0+14,x1,y1+14),r,fill=70)
    im.paste(Image.new('RGB',(W,H),'#05070D'),(0,0),sh.filter(ImageFilter.GaussianBlur(22)))
    reg=im.crop((x0,y0,x1,y1)).filter(ImageFilter.GaussianBlur(28)); reg=Image.blend(reg,Image.new('RGB',reg.size,tint),a/100)
    m=Image.new('L',reg.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,reg.size[0]-1,reg.size[1]-1),r,fill=255); im.paste(reg,(x0,y0),m)
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(lay).rounded_rectangle((x0,y0,x1,y1),r,outline=(255,255,255,edge),width=2); im.paste(lay,(0,0),lay)
def ctext(d,box,t,f,fill):
    x0,y0,x1,y1=box; bb=d.textbbox((0,0),'가',font=f)
    d.text((x0+(x1-x0-tl(t,f))/2,(y0+y1)/2-(bb[1]+bb[3])/2),t,font=f,fill=fill)
# ---- blocks: each is fn(ctx, x, y, w, draw) -> height
class Ctx:
    def __init__(s,im,th): s.im,s.th=im,th
    @property
    def d(s): return ImageDraw.Draw(s.im)
def Pill(t,solid=True):
    def f(c,x,y,w,draw):
        fo=F(z(28)); ph=z(50); tw=tl(t,fo); box=(x,y,x+tw+40,y+ph)
        if draw:
            if solid: c.d.rounded_rectangle(box,ph//2,fill=c.th.acc); ctext(c.d,box,t,fo,c.th.acc_txt)
            else: glass(c.im,box,a=20,r=ph//2,edge=150); ctext(c.d,box,t,fo,c.th.wh)
        return ph
    return f
def Head(lines,size=72,minr=0.8):
    segs=[[(l,False)] if isinstance(l,str) else [(l[0],True)] if isinstance(l,tuple) else l for l in lines]
    def f(c,x,y,w,draw):
        S0=z(size,1.1); sz=S0
        while sz>S0*minr and max(sum(tl(t,F(sz)) for t,_ in sg)+16*len(sg) for sg in segs)>w: sz-=2
        fo=F(sz); lh=int(sz*1.3); gt,gb=gl(sz); pad=int(sz*0.14)
        for i,sg in enumerate(segs):
            assert sum(tl(t,fo) for t,_ in sg)+16*len(sg)<=w+2, sg
            cx=x; yy=y+i*lh; prev=None
            for t,hl in sg:
                tw=tl(t,fo)
                if prev is not None and prev!=hl: cx+=16
                if draw:
                    if hl: c.d.rounded_rectangle((cx-12,yy+gt-pad,cx+tw+12,yy+gb+pad),10,fill=c.th.acc); c.d.text((cx,yy),t,font=fo,fill=c.th.acc_txt)
                    else: c.d.text((cx,yy),t,font=fo,fill=c.th.wh)
                cx+=tw; prev=hl
        return lh*len(segs)-int(sz*0.12)
    return f
def Text(t,size=38,color=None,bold=False,lh=1.5):
    def f(c,x,y,w,draw):
        sz=z(size); fo=F(sz,bold); ls=wrap(t,fo,w)
        if draw:
            for i,l in enumerate(ls): c.d.text((x,y+i*int(sz*lh)),l,font=fo,fill=color or c.th.wh)
        return int(sz*lh)*(len(ls)-1)+int(sz*1.3)
    return f
def Gap(px):
    return lambda c,x,y,w,draw: z(px)
def Card(blocks,accent=False,pad=P,gap=22):
    def f(c,x,y,w,draw):
        iw=w-2*pad; hs=[b(c,0,0,iw,False) for b in blocks]; h=sum(hs)+gap*(len(blocks)-1)+2*pad
        if draw:
            if accent: glass(c.im,(x,y,x+w,y+h),tint=c.th.acc_rgb,a=90,edge=200)
            else: glass(c.im,(x,y,x+w,y+h))
            yy=y+pad
            for b,hh in zip(blocks,hs): b(c,x+pad,yy,iw,True); yy+=hh+gap
        return h
    return f
def AccText(t,size=38,bold=False,lh=1.5,sub=False):
    def f(c,x,y,w,draw):
        col=c.th.acc_txt
        return Text(t,size,col,bold,lh)(c,x,y,w,draw)
    return f
def Row(items,gap=24):  # horizontal cards of equal height
    def f(c,x,y,w,draw):
        n=len(items); cw=(w-gap*(n-1))/n
        hs=[it(c,0,0,cw,False) for it in items]; h=max(hs)
        return h if not draw else ([it(c,x+i*(cw+gap),y,cw,True) for i,it in enumerate(items)] and h)
    return f
def Flow(steps,last_acc=True):
    def f(c,x,y,w,draw):
        yy=y
        for i,(k,v) in enumerate(steps):
            acc=last_acc and i==len(steps)-1; s38=z(38); fo=F(s38); kw=z(130); L=int(s38*1.5)
            ls=wrap(v,fo,w-kw-80); bh=max(z(110),len(ls)*L+z(52))
            if draw:
                if acc: glass(c.im,(x,yy,x+w,yy+bh),tint=c.th.acc_rgb,a=90,r=30,edge=200)
                else: glass(c.im,(x,yy,x+w,yy+bh),r=30)
                cb=(x+28,yy+bh/2-z(32),x+28+kw-20,yy+bh/2+z(32))
                c.d.rounded_rectangle(cb,32,fill=c.th.dk if acc else c.th.acc); ctext(c.d,cb,k,F(z(30)),c.th.acc if acc else c.th.acc_txt)
                g0,g1=gl(s38,True); ty=yy+(bh-((len(ls)-1)*L+(g1-g0)))/2-g0
                for j,l in enumerate(ls): c.d.text((x+kw+40,ty+j*L),l,font=fo,fill=c.th.acc_txt if acc else c.th.wh)
            yy+=bh
            if i<len(steps)-1:
                if draw: c.d.polygon([(x+w/2-18,yy+8),(x+w/2+18,yy+8),(x+w/2,yy+28)],fill=c.th.acc)
                yy+=z(36)
        return yy-y
    return f
def Word(en,ko,ex):
    def f(c,x,y,w,draw):
        fe=F(z(48)); fk=F(z(34)); fx=F(z(30),False); pad=z(28); EL=z(44)
        exl=wrap(ex,fx,w-2*pad); h=pad+z(64)+len(exl)*EL+pad-6
        if draw:
            glass(c.im,(x,y,x+w,y+h),r=30)
            c.d.text((x+pad,y+pad-8),en,font=fe,fill=c.th.acc)
            c.d.text((x+pad+tl(en,fe)+24,y+pad+z(8)),ko,font=fk,fill=c.th.wh)
            for j,l in enumerate(exl): c.d.text((x+pad,y+pad+z(68)+j*EL),l,font=fx,fill=c.th.soft)
        return h
    return f
def render(th,slides,out,chip,handle='@jina.ssam_english',label='영어지문 세계관'):
    paths=[]
    for n,blocks in enumerate(slides,1):
        im=bg(th,n); c=Ctx(im,th); w=W-2*M; gap=30
        best=1.0
        for k in [1.3,1.25,1.2,1.15,1.1,1.05]:
            SC[0]=k
            hs=[b(c,0,0,w,False) for b in blocks]
            if sum(hs)+gap*(len(blocks)-1)<=(BOT-TOP)*0.9: best=k; break
        SC[0]=best; gap=z(30)
        hs=[b(c,0,0,w,False) for b in blocks]; total=sum(hs)+gap*(len(blocks)-1)
        assert total<=BOT-TOP, f'slide {n} overflow {total} > {BOT-TOP}: 내용을 다음 장으로 나눠야 함'
        y=TOP+(BOT-TOP-total)/2
        d=c.d; d.text((M,72),label,font=F(30),fill=th.acc)
        fo=F(26); tw=tl(chip,fo); glass(im,(W-M-tw-40,62,W-M,114),a=18,r=26,edge=140); ctext(c.d,(W-M-tw-40,62,W-M,114),chip,fo,th.wh)
        for b,hh in zip(blocks,hs): b(c,M,int(y),w,True); y+=hh+gap
        d=c.d; d.text((M,H-92),handle,font=F(26,False),fill=th.soft)
        if n<len(slides):
            t='스와이프'; f2=F(28); d.text((W-M-70-tl(t,f2),H-94),t,font=f2,fill=th.wh)
            d.ellipse((W-M-52,H-100,W-M,H-48),fill=th.acc); ctext(d,(W-M-52,H-100,W-M,H-48),'→',F(32),th.acc_txt)
        p=f'{out}_{n}.png'; im.save(p); paths.append(p); print(n,'scale',best,'fill',round(total/(BOT-TOP),2)); SC[0]=1.0
    return paths

def Option(no,t,size=38):
    def f(c,x,y,w,draw):
        sz=z(size); fo=F(sz); cw=z(64); ls=wrap(t,fo,w-cw-70); L=int(sz*1.45)
        g0,g1=gl(sz); h=max(z(96),(len(ls)-1)*L+(g1-g0)+z(52))
        if draw:
            glass(c.im,(x,y,x+w,y+h),r=28,a=20)
            cb=(x+24,y+h/2-cw/2,x+24+cw,y+h/2+cw/2); c.d.ellipse(cb,fill=c.th.acc); ctext(c.d,cb,no,F(z(32)),c.th.acc_txt)
            ty=y+(h-((len(ls)-1)*L+(g1-g0)))/2-g0
            for j,l in enumerate(ls): c.d.text((x+24+cw+26,ty+j*L),l,font=fo,fill=c.th.wh)
        return h
    return f
def Upside(t,size=28):
    # small upside-down answer, right aligned
    def f(c,x,y,w,draw):
        sz=z(size); fo=F(sz); tw=int(tl(t,fo))+8; h=int(sz*1.4)
        if draw:
            lay=Image.new('RGBA',(tw,h),(0,0,0,0)); ImageDraw.Draw(lay).text((4,0),t,font=fo,fill=c.th.soft)
            lay=lay.rotate(180); c.im.paste(lay,(int(x+w-tw),int(y)),lay)
        return h
    return f
def Stamp(t,size=34,angle=-5):
    def f(c,x,y,w,draw):
        sz=z(size); fo=F(sz); tw=int(tl(t,fo)); bw,bh=tw+56,int(sz*1.9)
        if draw:
            lay=Image.new('RGBA',(bw+40,bh+40),(0,0,0,0)); dd=ImageDraw.Draw(lay)
            dd.rounded_rectangle((20,20,20+bw,20+bh),12,outline=c.th.acc,width=5)
            dd.rounded_rectangle((28,28,12+bw,12+bh),8,outline=c.th.acc,width=2)
            ctext(dd,(20,20,20+bw,20+bh),t,fo,c.th.acc)
            lay=lay.rotate(angle,resample=Image.BICUBIC,expand=True); c.im.paste(lay,(int(x)-10,int(y)-24),lay)
        return bh+8
    return f
