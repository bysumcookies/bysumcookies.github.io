---
layout: bsc
title: 태그
permalink: /tags/
---
<nav class="bsc-breadcrumb"><a href="/">HOME</a> &nbsp;/&nbsp; TAGS</nav>
<header class="bsc-page-heading"><h1>태그</h1><p>태그별 게시글을 찾아보세요.</p></header>
{% assign sorted_tags = site.tags | sort %}
<div class="bsc-post-list">
{% for item in sorted_tags %}
<article class="bsc-entry"><a href="/all/"><h2>{{ item[0] | escape }}</h2><p class="bsc-excerpt">{{ item[1].size }}개 게시글</p></a></article>
{% endfor %}
</div>
