# Morgorithm Study
코테를 작살내기위한 스터디 입니다.

- 정기 회의 : 매주 화요일 저녁 20시 30분

- 마감 기한 : 매주 월요일 18시


## 👥 참여자
> [DaegiYeo](https://github.com/daegi0923)
> 
> [BeomsuJeong](https://github.com/jbs0708)
> 
> [BigBeom](https://github.com/BigBeom)

## 💁‍♂️ 스터디 규칙
### 문제 풀이
- 매주 5문제씩 해결(화 ~ 월)(하루에 몰아서 하지않기), 문제 수준은 본인수준 맞춰서 ^_^
- 한 주간 풀어본 문제 중 택하여 한 주에 한명씩 해설
- 회의시간에 문제 정해서 다 같이 안풀어본 문제 풀어보고 접근방법, 풀이 및 피드백 공유


### 리드미 규칙
사용한 알고리즘, 중요 구현 로직 및 설명, 풀이 후기

> 아는 것은 최대한 공유하도록 합시다.
> 코드 리뷰는 창과 방패의 싸움!
> 의견 교환 및 질문은 거침없이

### 커밋 규칙
1. Repository clone
```
git clone https://github.com/daegi0923/morgoStudy.git
```
2. Repository open
- vscode or Pycharm
3. Branch 생성
branch는 주차별로 생성한다.
```
git checkout -b {본인의 깃허브 이름}/{주차명}
```
> ex. git checkout -b daegi0923/1week

4. 문제별 디렉토리 생성 및 코드, README 저장, 
```
{주차}/{플랫폼}_{난이도}_{문제 번호}_{문제명}/{풀이날짜}_{본인이름}
```
- 디렉토리 명 띄어쓰기 없이!
> ex. 1week/BOJ_G4_14500_테트로미노/0205_여대기
> ex. MIN_A_사과먹기게임/0206_여대기
5. Push
```
git add .
git commit -m "{주차명} : {플랫폼}[{문제번호}] {문제명}"
git push origin {생성한 브랜치}
```
- 커밋 메시지도 띄어쓰기 없이!
> ex. git commit -m "1week:BOJ[1759]암호만들기"

6. Pull request 생성
- Pull Request Name : {본인의 깃허브 이름} : [{주차명}]
> ex. daegi0923:[1week]

- Content : 문제명, 시간복잡도
- Label : 플랫폼, 언어
- Assignees : 본인
스터디 회의 후, merge
### 리뷰 규칙
회의 전까지, 타인이 작성한 코드를 보고 평가와 코멘트 plz~

### 풀이문제 및 순서
- 대기->범준->범수 (순환)
1. 1주차(240213) : BOJ_1244_스위치켜고끄기 [문제링크](https://www.acmicpc.net/problem/1244)
2. 2주차(240220) : BOJ_2628_종이자르기 [문제링크](https://www.acmicpc.net/problem/2628)

---
#### 참고한 레포들
- https://github.com/tony9402/baekjoon/tree/main

- https://github.com/Seongho0503/Algo_Study

- https://github.com/SeongukBaek/algoStudy
