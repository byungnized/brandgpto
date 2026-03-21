# BrandGPTO (static export)

Lovable에서보낸 React/Vite 빌드 정적 파일입니다.

## 커스텀 수정 (2026-03)

- `assets/index--9VqvNcB.js` — 문구·GEO 비교 표(행/열 전환)·모니터링 사례 블록(`HE`, 번들 내 Toast용 `WE`와 충돌 방지) 등 반영.
- 동일 수정을 다시 적용하려면 `python do_patch.py` (원본 백업: `index--9VqvNcB.js.bak` 최초 1회 생성).

## 로컬에서 보기

루트 경로로 서빙해야 합니다 (`file://` 로 열면 ES 모듈이 막힐 수 있음).

```bash
cd brandgpto
npx --yes serve .
```

또는:

```bash
python -m http.server 8080
```

브라우저에서 `http://localhost:3000` (serve 기본) 또는 `http://localhost:8080` 접속.

## 파일

- `index.html` — 엔트리 (자산 경로는 `./assets/…` 로 로컬용 수정됨)
- `assets/index--9VqvNcB.js` — 번들
- `assets/index-CA363ckB.css` — 스타일
- `favicon.ico`

Lovable에서 빌드 해시가 바뀌면 `index.html`의 JS/CSS 파일명을 맞추고, 새 파일을 다시 받아야 합니다.
