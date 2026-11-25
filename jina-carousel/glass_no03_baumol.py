import sys; sys.path.insert(0,'.')
from engine import *
# 컬러칩 7: Charcoal #121212 · Warm White #FDF9EA · Performance Orange #FE5105
th=Theme(base='#121212',blobs=['#FE5105','#B58B4C','#5A2A12'],acc='#FE5105',acc_txt='#121212',soft='#E6DCC8',dim=0.5)
NO='No.3'
S=[]
# 1 표지
S.append([Card([Pill(f'{NO} · 예술·문화'),
  Gap(20),Head(['공연은 왜 늘',[('돈이 모자랄',True),('까?',False)]],size=104),Gap(10),
  Text('표값은 계속 오르는데도\n재정이 늘 빠듯한 이유는?',46,bold=True,lh=1.45),
  Gap(24),Stamp('2026 수능 40번 연결',38),Gap(16),
  Text('오늘 읽을 개념\n보몰의 비용 질병 (Baumol\'s cost disease)',34,th.soft,lh=1.45)],pad=64)])
# 2 퀴즈 ① 읽기 전
S.append([Pill('미니 퀴즈 · 읽기 전에 맞혀 보기'),Head(['연주자의 임금은','어떻게 될까?'],size=66),
  Text('공장은 기계 덕분에 생산성이 크게 올랐어요. 반면 현악 4중주는 지금도 연주자 네 명이 같은 시간 동안 연주해야 해요.',36,th.soft),
  Option('1','생산성이 오르지 않았으니 임금도 오르지 않는다'),
  Option('2','다른 직업의 임금이 오르면 함께 오르는 경향이 있다'),
  Option('3','공장 노동자보다 훨씬 빠르게 오른다'),
  Option('4','연주 시간이 줄어드는 만큼 임금도 줄어든다'),
  Text('정답과 이유는 이 캐러셀 안에 있어요.',32,th.acc,True),Upside('정답 ② 다른 직업의 임금이 오르면 함께 오른다')])
# 3 생각해 볼까요
S.append([Pill('생각해 볼까요'),Head(['공연 티켓값은','왜 자꾸 오를까?'],size=66),
  Card([Text('음악 공연은 연주자 수와 연주 시간이 곧 공연의 모습이에요. 4중주를 두 배 빠르게 연주하거나 두 명만 연주하면, 같은 곡이라고 하기 어렵죠.'),
        Text('공장은 기계를 들여 같은 시간에 더 많이 만들 수 있지만, 공연은 그렇게 하기가 어려워요.')]),
  Card([AccText('사람이 직접 해야 하는 일은 생산성을 높이기 어려워요. 이 사정에 이름이 붙어 있어요.',40,True,1.45)],accent=True)])
# 4 현악 4중주
S.append([Pill('대표 사례 · 현악 4중주'),Head([[('연주자는 ',False),('그대로인데',True)]],size=72),
  Card([Text('경제학자 윌리엄 보몰과 윌리엄 보언은 1960년대에 공연예술의 경제 문제를 연구했어요. 대표 사례가 현악 4중주예요.'),
        Text('베토벤 시대의 4중주를 연주하는 데 필요한 연주자 수와 시간은 지금도 거의 같아요. 그런데 오늘날 연주자의 임금은 그때보다 높아요.'),
        Text('출처: W. J. Baumol & W. G. Bowen, Performing Arts: The Economic Dilemma (Twentieth Century Fund, 1966)',26,th.soft,lh=1.4)]),
  Card([AccText('일하는 사람 수와 시간은 그대로인데, 임금은 올랐어요.',40,True,1.45)],accent=True)])
# 5 핵심 개념
S.append([Pill('핵심 개념'),Head([[('비용 질병',True),('이란?',False)]]),
  Card([Text('생산성이 잘 오르지 않는 분야도, 생산성이 빠르게 오르는 분야와 일할 사람을 두고 경쟁해야 해요. 그래서 임금이 함께 오르고, 그 분야의 비용이 계속 늘어나요.',40,bold=True,lh=1.45)]),
  Card([Text('1967년 보몰은 경제를 생산성이 오르는 부문(진보 부문)과 오르지 않는 부문(정체 부문)으로 나눠 이 현상을 설명했어요.'),
        Text('정체 부문의 임금도 진보 부문의 생산성 상승을 따라 올라간다고 봤어요.'),
        Text('출처: W. J. Baumol, American Economic Review 57(3), 415–426 (1967)',26,th.soft,lh=1.4)])])
# 6 구조
S.append([Pill('이렇게 굴러가요'),Head(['공연 비용은 이렇게 올라요']),
  Flow([('생산성','공장은 기계 덕분에 같은 시간에 더 많이 만든다'),('임금','생산성이 오른 부문의 임금이 오른다'),('경쟁','연주자도 더 나은 일자리로 옮겨 갈 수 있다'),('인상','공연 쪽도 임금을 올려야 사람을 붙잡는다'),('결과','생산성은 그대로인데 공연 비용만 오른다')])])
# 7 수입 격차
S.append([Pill('수입 격차'),Head(['표값만으로는 모자라요'],size=72),
  Card([Text('보몰과 보언은 공연 비용이 수입(주로 표값)보다 빠르게 늘어난다고 봤어요. 이 간격은 후원금이나 지원금이 메워야 하는데, 그 돈이 충분히 늘기는 어렵다고 예상했어요.'),
        Text('※ 이후 연구에서는 공연 단체들이 처음 예상보다 잘 적응했다는 평가도 있어요.',30,th.soft,lh=1.5)]),
  Card([AccText('비용은 빨리 늘고 수입은 느리게 늘어, 둘 사이에 틈이 생겨요.',40,True,1.45)],accent=True)])
# 8 다른 분야
S.append([Pill('다른 분야는?'),Head(['공연만의 일이 아니에요'],size=72),
  Card([Text('사람이 직접 하는 일이 중심인 분야, 예를 들어 교육, 의료, 예술의 비용이 계속 오르는 이유를 설명할 때 이 개념이 자주 쓰여요.'),
        Text('반면 컴퓨터처럼 생산성이 빠르게 오르는 물건은 점점 싸져요.')]),
  Card([Text('※ 모든 경제학자가 같은 설명에 동의하는 것은 아니에요. 의료와 교육에도 효율을 높일 여지가 있다는 반론이 있어요.',32,th.soft,lh=1.5)])])
# 9 보몰의 결론
S.append([Pill('보몰의 결론'),Head(['그래도 감당할 수 있어요'],size=72),
  Card([Text('보몰은 2012년 책 『The Cost Disease』에서, 비용 질병은 우리가 돈을 나누어 쓰는 방식에 영향을 줄 뿐, 우리가 살 수 있는 양을 줄이게 하지는 않는다고 주장했어요.'),
        Text('다른 부문의 생산성이 오르면 사회 전체의 소득도 늘기 때문이에요.')]),
  Card([AccText('비용이 오르는 것과 감당하지 못하는 것은 다른 이야기예요.',40,True,1.45)],accent=True)])
# 10 수능 연결
S.append([Pill('수능 지문에서는'),Head([[('2026 수능 40번',True),(' 요약 문제',False)]]),
  Card([Text('주제: 공연예술의 독자성과 재정 문제',42,bold=True,lh=1.4),
        Text('보몰의 비용 질병은 공연이 왜 재정적으로 불안정해지기 쉬운지 이해하게 돕는 배경 개념이에요. 알고 읽으면 “독특한 경험”과 “돈 문제”의 대비가 쉽게 보여요.',40)])])
# 11 흐름
S.append([Pill('지문 흐름'),Head(['이런 주제의 글은 이렇게 흘러가요'],size=66),
  Card([Text('① 공연예술의 독특한 매력: 현장에서 함께하는 경험'),
        Text('② 숨은 문제: 비용은 늘고 수입은 불안정하다'),
        Text('③ 해결의 방향: 지원과 자금이 필요하다'),
        Text('④ 결론: 공연이 오래 이어지려면 지속 가능한 구조가 필요하다'),
        Text('※ 특정 지문의 순서가 아니라, 이 주제의 글에서 흔히 보이는 전개예요.',28,th.soft,lh=1.45)])])
# 12 기출 단어 (CSV 2026-40 원문 확인 단어)
S.append([Pill('기출 단어 · 2026 수능 40번'),Head([[('이 주제의 ',False),('핵심 단어',True)]]),
  Word('distinct','독특한, 뚜렷이 다른','Live theater is distinct from film.'),
  Word('unstable','불안정한','Income from tickets can be unstable.'),
  Word('funding','자금 지원','Many theaters need public funding.'),
  Word('sustain','유지하다, 지탱하다','Funding helps sustain the arts.'),
  Word('sustainable','지속 가능한','They need a sustainable plan.')])
# 13 한 줄 정리
S.append([Pill('한 줄 정리'),Head(['생산성은 그대로인데',[('비용',True),('은 오른다',False)]],size=80),
  Card([Text('더 읽어 보기',32,th.acc,True),
        Text('William J. Baumol, The Cost Disease: Why Computers Get Cheaper and Health Care Doesn\'t (Yale University Press, 2012)',34,bold=True,lh=1.4),
        Text('컴퓨터는 점점 싸지는데 의료는 왜 그렇지 않은지 설명한 보몰의 책이에요.',34,lh=1.45)]),
  Text('저장해 두고, 지문 읽기 전에 다시 보기',34,th.acc,True)])
# 14 퀴즈 ② 읽고 나서
S.append([Pill('미니 퀴즈 · 읽고 나서 풀기'),Head(['비용 질병이 나타나기 쉬운 것은?'],size=62),
  Card([AccText('생산성을 높이기 어렵고, 사람이 직접 하는 일의 비중이 커서 임금이 비용의 큰 몫을 차지하는 활동은?',36,True,1.45)],accent=True),
  Option('1','스마트폰 조립'),Option('2','직접 얼굴을 보고 하는 수업'),Option('3','반도체 생산'),Option('4','인터넷 쇼핑'),
  Text('댓글로 정답 번호를 남겨 보세요.',32,th.acc,True),Upside('정답 ② 직접 얼굴을 보고 하는 수업')])
render(th,S,'output/no03_glass/att','수능 빈출 배경지식',label=f'영어지문 세계관 {NO}')
