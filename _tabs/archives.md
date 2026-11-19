---
layout: bsc
title: 아카이브
permalink: /archives/
---
<nav class="bsc-breadcrumb"><a href="/">HOME</a> &nbsp;/&nbsp; ARCHIVES</nav>
<header class="bsc-page-heading"><h1>아카이브</h1><p>게시일을 기준으로 정리한 전체 기록입니다.</p></header>
{% assign sorted_posts = site.posts | sort: "date" | reverse %}
<div class="bsc-post-list">
{% for post in sorted_posts %}
<article class="bsc-entry"><a href="{{ post.url | relative_url }}"><span class="bsc-date">{{ post.date | date: "%Y.%m.%d" }}</span><h2>{{ post.title | escape }}</h2></a><span class="bsc-arrow" aria-hidden="true">↗</span></article>
{% endfor %}
</div>
