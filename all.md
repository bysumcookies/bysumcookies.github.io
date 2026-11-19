---
layout: bsc
title: 전체 글
permalink: /all/
---
<nav class="bsc-breadcrumb"><a href="/">HOME</a> &nbsp;/&nbsp; 전체 글</nav>
<header class="bsc-page-heading"><h1>전체 글 보기</h1><p>모든 카테고리의 기록을 최신순으로 확인합니다.</p></header>
{% assign all_posts = site.posts | sort: 'date' | reverse %}
<div class="bsc-post-list bsc-all-list">
{% for post in all_posts %}
{% assign cat = post.categories | first | default: '기타' %}
<article class="bsc-entry" data-tags="{{ post.tags | join: '|' | escape }}"><a href="{{ post.url | relative_url }}"><span class="bsc-date">{% if post.subcategory %}{{ post.subcategory | escape }} · {% endif %}{{ post.date | date: '%Y.%m.%d' }}</span><h2><span class="bsc-prefix">[{{ cat | capitalize | escape }}]</span> {{ post.title | escape }}</h2></a><span class="bsc-side-date">{{ post.date | date: '%Y.%m.%d' }}</span><span class="bsc-arrow" aria-hidden="true">↗</span></article>
{% else %}
<p class="bsc-empty">아직 등록된 게시글이 없습니다. 기존 티스토리 기록을 이전할 예정입니다.</p>
{% endfor %}
</div>

<script>
(() => {
  const tag = new URLSearchParams(location.search).get('tag');
  if (!tag) return;
  const entries = [...document.querySelectorAll('.bsc-all-list .bsc-entry')];
  let visible = 0;
  for (const entry of entries) {
    const matches = (entry.dataset.tags || '').split('|').includes(tag);
    entry.hidden = !matches;
    if (matches) visible++;
  }
  const heading = document.querySelector('.bsc-page-heading p');
  if (heading) heading.textContent = '태그: ' + tag + ' · ' + visible + '개 게시글';
  if (!visible) {
    const empty = document.createElement('p');
    empty.className = 'bsc-empty';
    empty.textContent = '해당 태그의 게시글이 없습니다.';
    document.querySelector('.bsc-all-list')?.append(empty);
  }
})();
</script>
