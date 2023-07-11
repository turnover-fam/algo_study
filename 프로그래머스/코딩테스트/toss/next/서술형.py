# 1번
# 게시판테이블이 있음
# 인덱스는 어떤걸 걸어야하는지
# 캐시는 어떻게 해야하는지 (댓글이 올라올 때마다 캐시 초기화해야하는데 어떻게 해야하는지?)


### 2번
# a - 주식, 애플, 구글
# b - 구글, 아이폰
# c - 토스
# 애플 주식은 어디에서 살 수 있나요? - 키워드 알람 대상자는 a, b
# 이러한 조건을 만족시킬 수 있는 키워드 알림 대상자를 선정하기 위한 시스템 설계에 대한 고민을 해보세요.

### 3번
# 고객은 하루에 최대 3개까지 선물상자 받을 수 있음
# 확률에 따라 꽝, 랜덤종목으로 1주 지급 (다양하게 존재)
# 한번 오픈한 상자는 다시 사용 못함
# 하루에 받을 수 있는 선물상자 확률이 다름
# 이것에 대한 테이블 설계, 서비스에서 사용할 쿼리도 만들기

### 4번
# 10% 정기예금 가입 이벤트 개최
# 트래픽 몰림
# 계좌개설 버튼을 계속 눌러서 -> 트래픽 몰림 -> 데이터베이스 몰림 -> 서비스 장애
# 장애가 발생한 원인과 해결방법
# 1.모놀리틱 구조
# 2.서버 8대
# 3. 스케일 아웃 가능
# 4. api가 1인 평균 10회
# 5. 로우락이 많이 발생
# 6. 다른 서비스도 응답속도 지연

### 5번 redis cluster 분리하자
# 개인 대출이 기존의 redis cluster를 사용하고 기업 대출은 새롭게 구성되는 redis cluster를 사용하려고 합니다.
# 서버가 중단되는 점검 시간 없이 기업 대출 테스트 서버를 새로운 redis cluster로 이관하려고 할 때 client library를 사용하여 데이터를 문제없이 이관하는 전략을 짜주세요.


