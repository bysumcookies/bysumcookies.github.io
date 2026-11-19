# ByteSumCookies

Network · Security · Cloud — 기술 학습과 실습 기록을 정리하는 개인 아카이브입니다.

- Website: https://bysumcookies.github.io
- Jekyll 4.4 (custom `bsc` and `bsc-post` layouts; **no Chirpy theme dependency**)
- GitHub Pages deployment: `.github/workflows/pages-deploy.yml`
- Article editor: Pages CMS (`.pages.yml`)

## 로컬 실행

Ruby와 Bundler를 설치한 다음 저장소 루트에서:

```bash
bundle install
bundle exec jekyll serve
```

브라우저에서 http://127.0.0.1:4000 을 열어 확인합니다.

## 게시글 등록

1. `_posts/YYYY-MM-DD-english-slug.html` 파일을 작성하거나 Pages CMS에서 새 게시글을 만듭니다.
2. 아래와 같은 YAML Front Matter를 포함합니다. 원래 티스토리 날짜가 있다면 **원래 게시일(+0900)** 을 유지합니다.

```yaml
---
layout: bsc-post
title: "글 제목"
date: 2026-07-02 22:59:00 +0900
categories:
  - Network
tags: [Protocol]
subcategory: Protocol
original_url: "https://bytesumcookies.tistory.com/30"
permalink: /posts/protocol-1/
---
```

3. 그 아래에 HTML 본문을 작성합니다. 표는 표준 `<table>`을 사용하고, 페이지 공통 템플릿이 각 표에 가로 스크롤 영역을 자동으로 적용합니다. 표의 고정 `width`, `min-width` 등 인라인 스타일은 가급적 사용하지 않습니다.
4. 이미지 파일은 `assets/img/posts/`에 저장하고 절대 경로(`/assets/img/posts/...`)로 참조합니다. 민감정보가 찍힌 로그와 IP·계정·토큰은 공개 전 검토합니다.
5. CMS에서 저장한 뒤에는 HTML과 Front Matter가 그대로 유지되는지 diff를 확인합니다.

## 구성

| 경로 | 용도 |
| --- | --- |
| `index.html` | 홈페이지 |
| `_layouts/bsc.html` | 공통 헤더·탐색·스타일 |
| `_layouts/bsc-post.html` | 게시글·목차·표 스크롤 |
| `_posts/` | 게시글 원본 |
| `topics/` | 카테고리 페이지 |
| `_tabs/` | About · 태그 · 카테고리 · 아카이브 |
| `assets/img/banners/` | 카테고리별 desktop-1x / desktop-2x / mobile 배너 |
| `assets/img/brand/` | 로고·OG 이미지 |
| `scripts/validate_site.py` | 빌드 후 리소스·게시글 검증 |
| `.pages.yml` | Pages CMS 편집 설정 |

## 빌드·검증

```bash
bundle exec jekyll build
python3 scripts/validate_site.py
bundle exec htmlproofer _site --disable-external
```

PR은 빌드·검증까지만 실행하며, `main`에 반영될 때 GitHub Pages에 배포됩니다.

## 자산 관리

- 파비콘은 동일한 `b.` 디자인으로 SVG / ICO / PNG(32px) / Apple touch 형식만 유지합니다.
- OG 이미지 정본은 `assets/img/brand/og-image.png` 한 개입니다. 생성 스크립트는 `scripts/render_og_preview.py`입니다.
- 배너는 각 카테고리별 데스크톱 1x·2x와 모바일 1개씩 유지합니다. 임시 `v2` 폴더나 사용되지 않는 디자인 파일은 보관하지 않습니다.
- 이전 Chirpy 캐시 해제를 위한 `sw.js`, `sw.min.js`, `refresh.html`은 기존 방문자 보호를 위해 한시적으로 유지합니다.

## 출처와 라이선스

이 저장소는 초기에 Chirpy Starter를 기반으로 생성되었으나, 현재 페이지의 디자인과 빌드 설정은 별도 구성입니다. 기존 코드·자산의 라이선스 의무는 `LICENSE` 및 각 원저작자 고지에 따릅니다.
