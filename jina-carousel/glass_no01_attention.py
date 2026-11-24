import sys; sys.path.insert(0,'.')
from engine import *
th=Theme(base='#141B2D',blobs=['#FF5A4E','#2B4C8C','#6B3A6E'],acc='#FF5A4E',acc_txt='#17191B',soft='#C9CEDA',dim=0.52)
NO='No.1'
S=[]
# 1 cover (fixed layout: 시리즈 번호 + 대표어휘 훅 + 수능 마크 + 개념)
S.append([Card([Pill(f'{NO} · 경제·사회'),
  Gap(20),Head([[('공짜 앱',True),('의 비밀',False)]],size=118),Gap(10),
  Text('다 공짜로 쓰는데,\n회사는 어떻게 돈을 벌까?',46,bold=True,lh=1.45),
  Gap(24),Stamp('2025 수능 33번 출제',38),Gap(16),
  Text('오늘 읽을 개념\n주의 경제 (attention economy)',34,th.soft,lh=1.45)],pad=64)])
# 2 quiz before reading
S.append([Pill('미니 퀴즈 · 읽기 전에 맞혀 보기'),Head(['광고로 운영되는 무료 서비스,','돈은 누가 낼까?'],size=66),
  Text('SNS, 동영상, 검색처럼 광고를 보여 주는 무료 서비스를 떠올려 보세요.',36,th.soft),
  Option('1','서비스를 쓰는 사용자'),Option('2','광고를 싣는 광고주'),Option('3','정부'),Option('4','기부하는 사람들'),
  Text('정답과 이유는 이 캐러셀 안에 있어요.',32,th.acc,True),Upside('정답 ② 광고주')])
# 3
S.append([Pill('생각해 볼까요'),Head(['돈을 내는 사람은 누구일까?']),
  Card([Text('우리가 매일 쓰는 동영상, SNS, 검색 서비스는 대부분 무료예요. 그런데 이 회사들은 큰돈을 벌어요.'),
        Text('돈을 내는 쪽은 광고주예요. 광고주가 사는 것은 우리의 주의, 다시 말해 우리의 관심과 시간이에요.')]),
  Card([AccText('무료 서비스의 진짜 상품은 서비스가 아니라, 그것을 쓰는 사람의 주의일 수 있다.',40,True,1.45)],accent=True)])
# 4 Simon
S.append([Pill('개념의 출발점'),Head([[('정보',False),('가 많아지면',False)],[('주의',True),('가 가난해진다',False)]]),
  Card([AccText('“A wealth of information creates a poverty of attention.”',42,True,1.35),
        AccText('정보가 풍부해지면 주의는 빈곤해진다.',36,True),
        AccText('허버트 사이먼, 「정보가 넘치는 세상을 위한 조직 설계」 (1971)',28,lh=1.4)],accent=True),
  Card([Text('사이먼은 1978년 노벨 경제학상을 받은 학자예요. 그는 정보가 받는 사람의 주의를 “소비”한다고 봤어요.'),
        Text('정보는 넘치는데 그것을 볼 사람의 시간과 관심은 한정돼 있으니, 이제 부족한 것은 정보가 아니라 주의라는 뜻이에요.')])])
# 5 concept
S.append([Pill('핵심 개념'),Head([[('주의 경제',True),('란?',False)]]),
  Card([Text('사람들의 주의를 얻기 위해 기업과 미디어가 경쟁하고, 그렇게 모은 주의가 돈으로 바뀌는 경제를 말해요.',40,bold=True,lh=1.45)]),
  Card([Text('1997년 미국의 마이클 골드하버는 잡지 Wired에 쓴 글 「Attention Shoppers!」에서 이렇게 주장했어요.'),
        Text('“인터넷 세상의 진짜 경제는 정보가 아니라 주의의 경제다.”',38,th.acc,True),
        Text('정보는 얼마든지 복사할 수 있지만, 한 사람이 하루에 줄 수 있는 주의는 늘어나지 않기 때문이에요.')])])
# 6 structure
S.append([Pill('돈이 도는 구조'),Head(['공짜 서비스는 이렇게 굴러가요']),
  Flow([('사용자','앱을 무료로 쓰면서 시간과 관심을 쓴다'),('플랫폼','사용자가 머무는 동안 광고를 보여 준다'),('광고주','광고가 노출된 만큼 플랫폼에 돈을 낸다'),('결과','플랫폼은 사용자가 더 오래 머물게 만들수록 돈을 번다')])])
# 7 design + quote
S.append([Pill('그래서 생기는 일'),Head(['더 오래 머물게 만드는 설계']),
  Card([Text('끝없이 내려가는 스크롤, 저절로 넘어가는 다음 영상, 다시 들어오게 만드는 알림, 내 취향만 골라 주는 추천.'),
        Text('모두 사용자가 앱에 더 오래 머물게 만드는 장치예요. 오래 볼수록 광고를 더 많이 보여 줄 수 있으니까요.')]),
  Card([AccText('“If you are not paying for it, you’re not the customer; you’re the product being sold.”',38,True,1.4),
        AccText('돈을 내지 않는다면 당신은 고객이 아니라, 팔리고 있는 상품이다.',34,True,1.45),
        AccText('2010년 한 온라인 게시판 댓글로 널리 퍼진 말. 비슷한 생각은 1970년대 텔레비전 비판에서도 나왔어요.',28,lh=1.45)],accent=True)])
# 8 suneung
S.append([Pill('수능 지문에서는'),Head([[('2025 수능 33번',True),(' 빈칸 문제',False)]]),
  Card([Text('주제: 주의 경제와 광고 기반 무료 서비스',40,bold=True,lh=1.4),
        Text('이 개념을 알고 읽으면, 지문이 “공짜”의 숨은 대가를 말하려 한다는 것을 첫 문장부터 예상할 수 있어요.')]),
  Card([Text('이런 주제의 글이 자주 쓰는 흐름',32,th.acc,True),
        Text('① 겉으로 보이는 모습: 무료이고 편리하다'),
        Text('② 숨은 구조: 사용자의 주의가 거래된다'),
        Text('③ 문제 제기: 내가 고른 것 같지만 사실은 골라진 것일 수 있다'),
        Text('④ 글쓴이의 주장: 의식하며 사용해야 한다'),
        Text('※ 특정 지문의 순서가 아니라, 이 주제의 글에서 흔히 보이는 전개예요.',28,th.soft,lh=1.45)])])
# 9 words
S.append([Pill('기출 단어 · 2025 수능 33번'),Head([[('이 주제의 ',False),('핵심 단어',True)]]),
  Word('advertising','광고','Free apps make money from advertising.'),
  Word('recommendation','추천','Recommendations keep us scrolling.'),
  Word('consume','소비하다','Information consumes our attention.'),
  Word('profitable','수익성 있는','Our attention makes free apps profitable.'),
  Word('conscious','의식하는','Be conscious of how you use your time.')])
# 10 지나쌤 한마디 (지나쌤이 준 글)
S.append([Pill('지나쌤 한마디'),
  Card([Text('“',90,th.acc,True,lh=0.9),
        Text('‘그늘길 찾기’나 요즘의 ‘산사’ 앱처럼 다 공짜로 쓰는데, 어떻게 돈을 벌까?',44,bold=True,lh=1.5),
        Text('이런 생각, 나만 해 봤을까요?',44,bold=True,lh=1.5),
        Gap(10),
        Text('이런 궁금증을 가지고 검색하고 책을 읽다 보면 훨씬 더 기억에 잘 남아요.',40,lh=1.55),
        Text('— 지나쌤',34,th.acc,True)])])
# 11 summary + reading
S.append([Pill('한 줄 정리'),Head([[('공짜의 값',True),('은',False)],'나의 시간과 관심'],size=80),
  Card([Text('더 읽어 보기',32,th.acc,True),
        Text('팀 우, 『주목하지 않을 권리』 (원제 The Attention Merchants, 2016)',36,bold=True,lh=1.4),
        Text('신문 광고부터 텔레비전, SNS까지 사람들의 주의를 사고판 역사를 다룬 책이에요.',34,lh=1.45)]),
  Text('저장해 두고, 지문 읽기 전에 다시 보기',34,th.acc,True)])
# 12 quiz after reading (수능식 빈칸)
S.append([Pill('미니 퀴즈 · 읽고 나서 풀기'),Head(['빈칸에 들어갈 말은?'],size=72),
  Card([AccText('“A wealth of information creates a poverty of ________.”',42,True,1.4),
        AccText('허버트 사이먼 (1971)',28)],accent=True),
  Option('1','money'),Option('2','attention'),Option('3','time'),Option('4','data'),
  Text('댓글로 정답 번호를 남겨 보세요.',32,th.acc,True),Upside('정답 ② attention')])
paths=render(th,S,'output/no01_glass/att','수능 빈출 배경지식',label=f'영어지문 세계관 {NO}')
