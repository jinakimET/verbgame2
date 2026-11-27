import sys; sys.path.insert(0,'.')
from engine import *
# 컬러칩 11: Jet Black #0B0B0B · Hot Pink #FF2DA8 · Chartreuse #D4FF3F (핑크 계열)
th=Theme(base='#14050E',blobs=['#FF2DA8','#C21F83','#7A1255'],acc='#D4FF3F',acc_txt='#0B0B0B',soft='#F6D3E7',dim=0.5)
NO='No.4'
S=[]
# 1 표지
S.append([Card([Pill(f'{NO} · 과학·기술'),
  Gap(20),Head(['오타가 진화가',[('될 수',True),(' 있을까?',False)]],size=104),Gap(10),
  Text('복제 실수는 어떻게\n진화의 재료가 될까?',46,bold=True,lh=1.45),
  Gap(24),Stamp('2024 수능 39번 연결',38),Gap(16),
  Text('오늘 읽을 개념\n돌연변이와 적응도 (mutation & fitness)',34,th.soft,lh=1.45)],pad=64)])
# 2 퀴즈 ① 읽기 전
S.append([Pill('미니 퀴즈 · 읽기 전에 맞혀 보기'),Head(['부모에게서 새로 생긴','복사 실수는 몇 개?'],size=62),
  Text('아이는 부모의 DNA를 복사해서 물려받아요. 이때 부모에게도 없던 새 복사 실수(돌연변이)가 아이에게 생겨요. 사람 한 명에게 생기는 새 돌연변이는 몇 개쯤일까요?',36,th.soft),
  Option('1','거의 없다 (0~1개)'),Option('2','수십 개'),Option('3','수만 개'),Option('4','수억 개'),
  Text('정답과 이유는 이 캐러셀 안에 있어요.',32,th.acc,True),Upside('정답 ② 수십 개 (약 60개 안팎)')])
# 3 생각해 볼까요
S.append([Pill('생각해 볼까요'),Head(['책을 베끼다','틀리면?'],size=72),
  Card([Text('인쇄술이 없던 시절에는 책을 손으로 베껴 썼어요. 베끼는 사람이 글자 하나를 잘못 쓰면 오타(misprint, 오식)가 생겨요.'),
        Text('그 필사본을 다시 베끼면 오타도 함께 복사돼요. 오타는 이렇게 다음 책으로 이어져요.')]),
  Card([AccText('생물의 몸을 만드는 설계도도 복사되는 글이에요. 그럼 복사 실수는 어떻게 될까요?',40,True,1.45)],accent=True)])
# 4 DNA 복사
S.append([Pill('복사되는 글 · DNA'),Head([[('DNA도 ',False),('복사',True),('해요',False)]],size=76),
  Card([Text('생물은 DNA라는 긴 글자열에 몸을 만드는 정보를 담고 있어요. 부모는 이 DNA를 복사해서 자손에게 물려줘요.'),
        Text('복사는 아주 정확하지만 완벽하지는 않아요. 글자가 바뀌거나 빠지거나 끼어드는 실수가 가끔 생겨요. 이 실수를 돌연변이(mutation)라고 해요.')]),
  Card([AccText('사람은 한 세대에 새 돌연변이가 평균 60개 안팎 생겨요.',40,True,1.45),
        Text('출처: A. Kong et al., Nature 488, 471–475 (2012)',26,th.acc_txt,lh=1.4)],accent=True)])
# 5 비유 짝짓기
S.append([Pill('비유로 짝짓기'),Head(['오타 비유는 이렇게 맞아요']),
  Card([Text('책 한 권  →  DNA 전체',40,bold=True),
        Text('베껴 쓰기  →  DNA 복사',40,bold=True),
        Text('오타(misprint)  →  돌연변이(mutation)',40,bold=True),
        Text('다음 필사본  →  자손(offspring)',40,bold=True)],gap=20),
  Card([AccText('오타가 다음 책으로 이어지듯, 돌연변이도 자손에게 이어져요.',40,True,1.45)],accent=True)])
# 6 결과는 세 가지
S.append([Pill('돌연변이의 결과'),Head(['대부분은 이렇게 끝나요']),
  Card([Text('해로운 경우',38,th.acc,True),
        Text('몸의 중요한 기능을 망가뜨려요. 오타 때문에 문장 뜻이 이상해지는 것과 비슷해요.'),
        Text('아무 일 없는 경우',38,th.acc,True),
        Text('글자가 바뀌어도 몸에 달라지는 게 없어요. 뜻이 같은 다른 글자로 바뀐 것과 비슷해요.'),
        Text('이로운 경우',38,th.acc,True),
        Text('드물지만 생존에 도움이 되는 변화가 생겨요. 이 경우가 진화의 재료가 돼요.')],gap=16)])
# 7 비유의 한계 ①
S.append([Pill('비유의 한계 ①'),Head(['오타에는 정답이 있어요'],size=72),
  Card([Text('책에는 저자가 쓴 원문이 있어서, 원문과 다르면 틀린 글자가 돼요. 오타는 언제나 오타예요.'),
        Text('그런데 생물에게는 정해진 원문이 없어요. 어떤 글자가 맞고 틀린지 미리 정해져 있지 않아요.')]),
  Card([AccText('같은 변화라도 어떤 환경에서는 손해이고, 어떤 환경에서는 이득일 수 있어요.',40,True,1.45)],accent=True)])
# 8 적응도
S.append([Pill('핵심 개념'),Head([[('적응도',True),('란?',False)]]),
  Card([Text('그 환경에서 살아남아 자손을 얼마나 남기느냐를 나타내는 정도',44,bold=True,lh=1.45)]),
  Card([Text('영어로는 fitness예요. 몸이 튼튼하다는 뜻이 아니라, 주어진 환경에서 자손을 남기는 데 성공하는 정도예요.'),
        Text('돌연변이가 좋은지 나쁜지는 그 변화가 적응도를 높이는지 낮추는지로 정해져요.')])])
# 9 사례 겸상 적혈구
S.append([Pill('사례 ① 낫 모양 적혈구'),Head(['같은 유전자, 다른 환경'],size=72),
  Card([Text('낫 모양 적혈구 유전자는 두 개를 가지면 심한 빈혈을 일으켜요. 그런데 하나만 가진 사람은 말라리아에 심하게 걸리는 일이 적어요.'),
        Text('1954년 앨리슨은 동아프리카 여러 집단을 조사해, 말라리아가 흔한 곳에서 이 유전자도 흔하다는 것을 보였어요.'),
        Text('출처: A. C. Allison, British Medical Journal 1(4857), 290–294 (1954)',26,th.soft,lh=1.4)]),
  Card([AccText('말라리아가 흔한 환경에서는 해로운 유전자가 이득이 되기도 해요.',40,True,1.45)],accent=True)])
# 10 사례 대장균
S.append([Pill('사례 ② 대장균 실험'),Head(['실험실에서 본 진화'],size=72),
  Card([Text('1988년 렌스키 연구팀은 똑같은 대장균 12집단을 키우기 시작했어요. 먹이는 포도당이 부족하고 구연산이 든 환경이었어요.'),
        Text('약 31,500세대 무렵, 한 집단에서 산소가 있을 때도 구연산을 먹이로 쓰는 변이가 나타났어요.'),
        Text('출처: Z. D. Blount, C. Borland, R. Lenski, PNAS 105(23), 7899–7906 (2008)',26,th.soft,lh=1.4)]),
  Card([AccText('환경에 맞는 변화는 오타가 아니라 새 능력이 되었어요.',40,True,1.45)],accent=True)])
# 11 비유의 한계 ②
S.append([Pill('비유의 한계 ②'),Head(['고치는 사람이 없어요'],size=72),
  Card([Text('책은 오타를 발견한 사람이 고쳐 쓸 수 있어요. 하지만 자연에는 고쳐 주는 사람이 없어요.'),
        Text('너무 해로운 변화(fatal, 치명적인)는 자손을 남기기 전에 사라지고, 살아남아 자손을 많이 남기는 변화는 점점 흔해져요.')]),
  Card([AccText('자연이 고치는 게 아니라, 자손을 더 남기는 쪽이 더 많이 남아요.',40,True,1.45)],accent=True)])
# 12 구조
S.append([Pill('이렇게 굴러가요'),Head(['오타가 진화가 되는 길']),
  Flow([('실수','DNA를 복사하다 돌연변이가 생긴다'),('다양성','같은 종 안에 조금씩 다른 개체가 생긴다'),('환경','어떤 변화는 이 환경에서 유리하고 어떤 변화는 불리하다'),('적응도','유리한 개체가 자손을 더 많이 남긴다'),('결과','유리한 변화가 다음 세대에 점점 흔해진다')])])
# 13 수능 연결
S.append([Pill('수능 지문에서는'),Head([[('2024 수능 39번',True),(' 문장 삽입',False)]]),
  Card([Text('주제: 돌연변이와 오식의 비유, 그리고 그 비유의 한계',42,bold=True,lh=1.4),
        Text('오타 비유가 어디까지 맞고 어디서부터 어긋나는지 알고 읽으면, 문장이 들어갈 자리를 찾기 쉬워요.',40)])])
# 14 흐름
S.append([Pill('지문 흐름'),Head(['이런 주제의 글은 이렇게 흘러가요'],size=66),
  Card([Text('① 비유 소개: 돌연변이는 복사 과정의 오타와 같다'),
        Text('② 비유가 맞는 점: 실수는 다음으로 이어진다'),
        Text('③ 그러나 한계: 오타와 달리 생물에는 정해진 정답이 없다'),
        Text('④ 결론: 변화의 좋고 나쁨은 환경 속 적응도로 정해진다')])])
# 15 기출 단어 (CSV 2024-39 원문 확인 단어)
S.append([Pill('기출 단어 · 2024 수능 39번'),Head([[('이 주제의 ',False),('핵심 단어',True)]]),
  Word('misprint','오식, 오타','A misprint can change the meaning.'),
  Word('mutation','돌연변이','A mutation is a copying error in DNA.'),
  Word('analogy','유사, 비유','The analogy has its limits.'),
  Word('fatal','치명적인','Some changes are fatal to the animal.'),
  Word('offspring','자손','Parents pass genes to their offspring.'),
  Word('fitness','적응도','Fitness depends on the environment.')])
# 16 한 줄 정리
S.append([Pill('한 줄 정리'),Head(['오타의 좋고 나쁨은',[('환경',True),('이 정해요',False)]],size=80),
  Card([Text('더 읽어 보기',32,th.acc,True),
        Text('Charles Darwin, On the Origin of Species (1859)',34,bold=True,lh=1.4),
        Text('변이와 자연선택으로 생물이 달라진다고 처음 체계적으로 설명한 책이에요.',34,lh=1.45)]),
  Text('저장해 두고, 지문 읽기 전에 다시 보기',34,th.acc,True)])
# 17 퀴즈 ② 읽고 나서
S.append([Pill('미니 퀴즈 · 읽고 나서 풀기'),Head(['적응도를 정하는 것은?'],size=66),
  Card([AccText('어떤 돌연변이가 생물에게 유리한지는 무엇으로 정해질까요?',38,True,1.45)],accent=True),
  Option('1','돌연변이가 생긴 글자의 수'),Option('2','몸이 얼마나 튼튼한가'),Option('3','그 환경에서 자손을 얼마나 남기는가'),Option('4','저자가 정한 원문과 얼마나 같은가'),
  Text('댓글로 정답 번호를 남겨 보세요.',32,th.acc,True),Upside('정답 ③ 그 환경에서 자손을 얼마나 남기는가')])
render(th,S,'output/no04_glass/att','수능 빈출 배경지식',label=f'영어지문 세계관 {NO}')
