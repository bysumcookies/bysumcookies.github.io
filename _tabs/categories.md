---
layout: bsc
title: 카테고리
permalink: /categories/
---
<nav class="bsc-breadcrumb"><a href="/">HOME</a> &nbsp;/&nbsp; CATEGORIES</nav>
<header class="bsc-page-heading"><h1>카테고리</h1><p>기술 기록을 주제별로 찾아보세요.</p></header>
<div class="bsc-post-list">
{% assign topics = "Network,Security,AWS,Portfolio,Certification" | split: "," %}
{% for topic in topics %}
{% assign key = topic | downcase %}
{% assign count = 0 %}
{% for post in site.posts %}{% if post.categories contains topic %}{% assign count = count | plus: 1 %}{% endif %}{% endfor %}
<article class="bsc-entry"><a href="/topics/{{ key }}/"><h2>{{ topic }}</h2><p class="bsc-excerpt">{{ count }}개 게시글</p></a><span class="bsc-arrow" aria-hidden="true">↗</span></article>
{% endfor %}
</div>
