import sys; sys.path.insert(0,'.')
from engine import *
# 컬러칩 4: Midnight Ink #080F1B · Azure Blue #329DD2 · Vermilion Orange #FF4C2B
th=Theme(base='#080F1B',blobs=['#329DD2','#FF4C2B','#1B4F72'],acc='#329DD2',acc_txt='#080F1B',soft='#C6D4E1',dim=0.5)
NO='No.2'
S=[]
# 1 표지
S.append([Card([Pill(f'{NO} · 심리'),
  Gap(20),Head([[('확증 편향',True),('의 함정',False)]],size=118),Gap(10),
  Text('내 생각과 같은 말만\n유독 잘 들리는 이유는?',46,bold=True,lh=1.45),
  Gap(24),Stamp('2027 수능 29번 연결',38),Gap(16),
  Text('오늘 읽을 개념\n확증 편향 (confirmation bias)',34,th.soft,lh=1.45)],pad=64)])
# 2 퀴즈 ① 읽기 전
S.append([Pill('미니 퀴즈 · 읽기 전에 맞혀 보기'),Head(['이미 믿는 생각과 다른','증거를 만나면 보통…'],size=66),
  Text('연구에서 사람들에게 더 흔하게 나타난 반응은 무엇일까요?',36,th.soft),
  Option('1','증거를 보고 곧바로 생각을 바꾼다'),
  Option('2','믿음에 맞는 증거는 더 믿고, 맞지 않는 증거는 의심한다'),
  Option('3','증거를 읽지 않고 그냥 넘긴다'),
  Option('4','양쪽 증거를 똑같이 평가한다'),
  Text('정답과 이유는 이 캐러셀 안에 있어요.',32,th.acc,True),Upside('정답 ② 믿음에 맞는 증거를 더 믿는다')])
# 3 생각해 볼까요
S.append([Pill('생각해 볼까요'),Head(['내 생각과 같은 말만','귀에 쏙 들어온 적 있나요?'],size=66),
  Card([Text('예를 들어 어떤 사람을 “별로야”라고 한번 마음먹으면, 그 사람의 실수는 크게 보이고 잘한 일은 눈에 잘 안 들어와요.'),
        Text('반대로 좋아하는 사람이 하는 말은 근거가 부족해도 그럴듯하게 들리죠.')]),
  Card([AccText('한번 가진 생각은, 그 생각을 지켜 주는 정보에 먼저 손을 뻗게 해요. 이 경향에는 이름이 있어요.',40,True,1.45)],accent=True)])
# 4 웬슨 ①
S.append([Pill('실험 ① 웬슨의 2-4-6'),Head([[('규칙을 ',False),('알아맞혀 보세요',True)]],size=72),
  Card([Text('1960년 심리학자 피터 웬슨은 참가자에게 숫자 세 개 “2, 4, 6”을 보여 주고, 이 숫자들이 어떤 규칙을 따른다고 알려 줬어요.'),
        Text('참가자는 직접 숫자 세 개를 말해 보고, 규칙에 맞는지 아닌지 답을 들으며 규칙을 알아맞혀야 했어요.')]),
  Card([AccText('많은 참가자가 “2씩 커진다”고 생각하고, 예를 들면 8-10-12처럼 자기 생각에 맞는 숫자만 시험해 봤어요.',38,True,1.45)],accent=True)])
# 5 웬슨 ②
S.append([Pill('실험 ① 결과'),Head(['진짜 규칙은 더 단순했어요'],size=72),
  Card([Text('진짜 규칙은 “숫자가 점점 커지기만 하면 된다”였어요. 1-2-3도, 5-60-700도 정답이에요.'),
        Text('“2씩 커진다”는 생각을 제대로 시험하려면 일부러 틀릴 만한 숫자를 내 봐야 해요. 그런데 많은 사람들은 자기 생각이 맞다는 답만 계속 모으려 했어요.'),
        Text('출처: P. C. Wason, Quarterly Journal of Experimental Psychology (1960)',26,th.soft,lh=1.4)]),
  Card([AccText('내 생각이 맞다는 증거만 모으면, 틀린 생각도 계속 맞아 보여요.',40,True,1.45)],accent=True)])
# 6 로드·로스·레퍼
S.append([Pill('실험 ② 사형제 논쟁'),Head(['같은 연구, 다른 평가'],size=72),
  Card([Text('1979년 로드, 로스, 레퍼는 사형제에 찬성하는 대학생과 반대하는 대학생에게, 서로 반대 결론을 내는 연구 두 편을 읽게 했어요.'),
        Text('두 집단 모두 자기 입장과 맞는 연구는 더 설득력 있다고, 맞지 않는 연구는 덜 설득력 있다고 평가했고, 처음 입장이 더 강해졌다고 답했어요.')]),
  Card([Text('※ 이후 연구에서는 같은 결과가 항상 나오지는 않았어요. 사람들이 늘 이렇게 판단한다는 뜻이 아니라, 이런 경향이 나타날 수 있다는 뜻으로 읽어요.',32,th.soft,lh=1.5)])])
# 7 핵심 개념
S.append([Pill('핵심 개념'),Head([[('확증 편향',True),('이란?',False)]]),
  Card([Text('자기가 이미 가진 믿음이나 가설에 유리한 방향으로 증거를 찾고, 해석하고, 기억하는 경향을 말해요.',40,bold=True,lh=1.45)]),
  Card([Text('심리학자 니커슨은 1998년 논문에서, 이 편향이 여러 모습으로 널리 나타난다고 정리했어요.'),
        Text('찾기: 내 생각을 뒷받침할 정보부터 찾아요.',38,th.acc,True),
        Text('해석하기: 같은 정보도 내 편으로 읽어요.',38,th.acc,True),
        Text('기억하기: 내 생각에 맞는 내용을 더 잘 기억해요.',38,th.acc,True)])])
# 8 구조
S.append([Pill('이렇게 굴러가요'),Head(['믿음은 이렇게 더 강해져요']),
  Flow([('믿음','“이게 맞을 거야”라는 생각이 생긴다'),('찾기','그 생각을 지켜 줄 정보부터 찾는다'),('해석','같은 정보도 내 편으로 읽는다'),('기억','맞지 않는 내용은 쉽게 잊는다'),('결과','믿음이 시험받지 않은 채 더 강해진다')])])
# 9 줄이는 방법
S.append([Pill('그럼 어떻게 줄일까'),Head(['반대 가능성을 생각해 보기'],size=72),
  Card([Text('1984년 로드, 레퍼, 프레스턴은 “가능한 한 공정하고 편견 없이 판단하세요”라고만 말하는 것보다, “반대가 맞다면 어떨지 생각해 보세요”라고 시키는 쪽이 편향을 더 줄였다고 보고했어요.')]),
  Card([AccText('내 생각이 틀렸다면 어떤 증거가 나올지, 먼저 떠올려 보기.',40,True,1.45)],accent=True),
  Text('써 보기: 정답이 ③이라고 생각했다면, 다른 선택지가 정답이 될 이유를 한 번 찾아보세요.',34,th.soft)])
# 10 수능 연결
S.append([Pill('수능 지문에서는'),Head([[('2027 수능 29번',True),(' 어법 문제',False)]]),
  Card([Text('주제: 믿음을 재검토하는 사고',42,bold=True,lh=1.4),
        Text('확증 편향은 “믿음을 다시 살펴보기가 왜 어려운가”를 설명해 주는 배경 개념이에요. 알고 읽으면 글쓴이가 왜 재검토를 강조하는지 짐작하기 쉬워요.',40)])])
# 10-2 흐름
S.append([Pill('지문 흐름'),Head(['이런 주제의 글은 이렇게 흘러가요'],size=66),
  Card([Text('① 겉으로 보이는 모습: 내 믿음은 당연히 옳게 느껴진다'),
        Text('② 숨은 문제: 믿음을 지켜 주는 정보만 받아들이기 쉽다'),
        Text('③ 제안: 믿음을 의식적으로 다시 살펴봐야 한다'),
        Text('④ 방법: 반대 증거를 일부러 찾아본다'),
        Text('※ 특정 지문의 순서가 아니라, 이 주제의 글에서 흔히 보이는 전개예요.',28,th.soft,lh=1.45)])])
# 11 기출 단어 (CSV 2027-29 원문 확인 단어)
S.append([Pill('기출 단어 · 2027 수능 29번'),Head([[('이 주제의 ',False),('핵심 단어',True)]]),
  Word('reexamine','재검토하다','We should reexamine our beliefs from time to time.'),
  Word('tempting','솔깃한, 마음이 끌리는','It is tempting to trust only what agrees with us.'),
  Word('consistent','일관된, ~와 일치하는','Her answer is consistent with what she believes.'),
  Word('evidence','증거','Look at the evidence before you decide.'),
  Word('critically','비판적으로','Read the passage critically.')])
# 12 한 줄 정리
S.append([Pill('한 줄 정리'),Head(['내 생각이 틀릴 증거를',[('먼저',True),(' 찾아보기',False)]],size=80),
  Card([Text('더 읽어 보기',32,th.acc,True),
        Text('줄리아 갈렙, 『스카우트 마인드셋』 (와이즈베리, 2022 · 원제 The Scout Mindset, 2021)',36,bold=True,lh=1.4),
        Text('내 생각을 지키려는 마음이 아니라, 사실을 있는 그대로 보려는 척후병의 마음으로 생각하는 법을 다룬 책이에요.',34,lh=1.45)]),
  Text('저장해 두고, 지문 읽기 전에 다시 보기',34,th.acc,True)])
# 13 퀴즈 ② 읽고 나서
S.append([Pill('미니 퀴즈 · 읽고 나서 풀기'),Head(['생각을 제대로 시험하려면?'],size=66),
  Card([AccText('숫자 규칙이 “2씩 커진다”일 것 같다고 생각했어요. 이 생각이 틀렸는지 확인하려면 어떤 숫자를 내 봐야 할까요?',36,True,1.45)],accent=True),
  Option('1','8-10-12'),Option('2','10-12-14'),Option('3','20-22-24'),Option('4','1-2-3'),
  Text('댓글로 정답 번호를 남겨 보세요.',32,th.acc,True),Upside('정답 ④ 1-2-3')])
render(th,S,'output/no02_glass/att','수능 빈출 배경지식',label=f'영어지문 세계관 {NO}')
