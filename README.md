# seo-guarantee — 검색 성과보장 신청 페이지

인스타그램 스토리 광고가 보내는 랜딩. 원본은 `D:\solset\solcap\playbook\랜딩_신청폼.html`,
여기 `index.html` 은 배포용 사본이다(doctype/head/body + noindex 추가).

- 공개 주소: https://nosol-love2.github.io/seo-guarantee/
- 갱신: 원본 고친 뒤 `index.html` 로 다시 만들고 `git add -A && git commit && git push`

## 아직 비어 있는 것

1. **접수 엔드포인트** — `index.html` 안 `const ENDPOINT = ""`.
   비어 있으면 신청이 화면에만 뜨고 아무 데도 안 남는다. **광고를 켜면 안 되는 상태.**
2. **개인정보 처리 책임자** — 하단 붉은 점선 칸(이름 · 연락처 · 이메일).
3. **사업자 정보** — 거래 구조 확정 후.

## 도메인 붙이기 (구입 후 5분)

1. 도메인 구입 (가비아 · 후이즈 등, `.kr` 연 1만원대)
2. 이 폴더에 CNAME 파일 하나 만들고 푸시
   ```
   echo "example.kr" > CNAME && git add CNAME && git commit -m "domain" && git push
   ```
3. 도메인 관리 페이지에서 DNS 레코드 추가
   - 루트(`example.kr`)로 쓸 경우 — A 레코드 4개
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
   - `www` 나 서브도메인으로 쓸 경우 — CNAME `nosol-love2.github.io`
4. GitHub 저장소 Settings > Pages 에서 Custom domain 확인, **Enforce HTTPS** 체크
   (인증서 발급까지 최대 24시간)

## noindex

`<meta name="robots" content="noindex, nofollow">` 가 걸려 있다.
광고로만 유입되는 테스트 페이지라 검색에 잡힐 필요가 없다. 정식 운영 시 이 줄을 지운다.
