# jina-carousel

「영어지문 세계관」 인스타그램 캐러셀 렌더링 코드와 결과물입니다. 제작 규칙은 [RULES.md](RULES.md)에 있습니다.

## 파일
| 파일 | 내용 |
|---|---|
| `engine.py` | 글라스모피즘 캐러셀 엔진. 글 양에 맞춰 카드 높이가 늘어나고, 여백이 많으면 글씨를 키움 (블록: Pill, Head, Text, Card, Flow, Word, Option, Upside, Stamp) |
| `glass_no01_attention.py` | No.1 공짜 앱의 비밀 (주제 캐러셀 12장). 새 편은 이 파일을 복사해서 내용만 바꾼다 |
| `neo_no01_attention.py` | No.1 수준별 지문 네오 브루탈리즘 캐러셀 11장 |
| `glass_no02_confirmation.py` | No.2 확증 편향의 함정 (주제 캐러셀 15장) |
| `neo_no02_confirmation.py` | No.2 수준별 지문 11장 |
| `glass_no03_baumol.py` | No.3 보몰의 비용 질병 (주제 캐러셀 15장) |
| `neo_no03_baumol.py` | No.3 수준별 지문 11장 |
| `data/suneung_sheet_by_question.csv` | 2024~2027 수능 18~45번 주제와 원문 확인 단어 |
| `output/` | 렌더링 결과 PNG와 캡션 |

## 실행
```bash
apt-get install -y fonts-noto-cjk   # 한글 폰트 (없을 때만)
pip install pillow numpy            # 없을 때만
cd jina-carousel
python3 glass_no01_attention.py
python3 neo_no01_attention.py
```
