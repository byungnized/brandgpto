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

## GitHub Pages — 반드시 설정 (배포가 안 될 때)

1. GitHub 저장소 **Settings** → **Pages**
2. **Build and deployment** → **Source** 를 **`GitHub Actions`** 로 선택 (「Deploy from a branch」가 아님)
3. 저장소 루트에 **`.github/workflows/deploy-pages.yml`** 이 있어야 `main` 푸시마다 자동 배포됨
4. 첫 실행 후 **Actions** 탭에서 워크플로가 초록 체크인지 확인 → 몇 분 뒤 **`https://<사용자>.github.io/<저장소>/`** 접속

## GitHub Pages (`/저장소이름/` 주소)

프로젝트 Pages는 **`https://<사용자>.github.io/<저장소>/`** 에 올라갑니다.  
React Router가 루트(`/`)만 보면 404가 나므로, 번들에 **`basename: "/brandgpto"`** 조건부 로직이 들어 있습니다  
(주소가 `/brandgpto` 또는 `/brandgpto/...`일 때만 적용, 로컬 `/`에서는 비움).

- 열 주소: **https://byungnized.github.io/brandgpto/** 또는 **`/brandgpto` (끝 슬래시 없음)** — `index.html` 상단 스크립트가 `<base href="/brandgpto/">` 를 넣어 에셋 경로가 깨지지 않게 함.
- **`.nojekyll`**: Jekyll 처리 끔 (정적 파일 그대로 서빙).
- **`404.html`**: `index.html`과 동일 복사본 — 잘못된 하위 경로로 들어와도 SPA가 뜨도록.
- 저장소 이름을 바꾸면 `index--9VqvNcB.js` 안의 `brandgpto` 문자열을 새 이름에 맞게 수정해야 합니다.

### Actions는 성공인데 사이트가 안 뜰 때

1. **Settings → Pages** 에서 Source가 **`main` / `(root)`** 인지 확인.  
2. **가장 최근 커밋**이 배포됐는지 Actions에서 해당 run의 commit SHA 확인 (예전 `22deadd`만 보이면 **Re-run all jobs** 하거나 빈 커밋 푸시).  
3. 강력 새로고침(Ctrl+Shift+R) 또는 시크릿 창.

## 파일

- `index.html` — 엔트리 (자산 경로는 `./assets/…` 로 로컬용 수정됨)
- `assets/index--9VqvNcB.js` — 번들
- `assets/index-CA363ckB.css` — 스타일
- `favicon.ico`

Lovable에서 빌드 해시가 바뀌면 `index.html`의 JS/CSS 파일명을 맞추고, 새 파일을 다시 받아야 합니다.
