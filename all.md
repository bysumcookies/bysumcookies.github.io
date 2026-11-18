---
layout: page
title: 전체 글
permalink: /all/
icon: fas fa-list
---

<p>모든 카테고리의 게시글을 최신 날짜순으로 모았습니다.</p>

{% assign ordered_posts = site.posts | sort: 'date' | reverse %}
{% if ordered_posts.size > 0 %}
<div class="bsc-all-posts">
{% for post in ordered_posts %}
<article class="bsc-all-post">
  <div class="bsc-post-meta">{{ post.date | date: '%Y.%m.%d' }} · {{ post.categories | join: ' / ' }}</div>
  <h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
</article>
{% endfor %}
</div>
{% else %}
<p>아직 등록된 게시글이 없습니다.</p>
{% endif %}

<style>
.bsc-all-post{padding:18px 0;border-bottom:1px solid var(--main-border-color,#ddd)}
.bsc-all-post h3{font-size:1.05rem;margin:7px 0 0;line-height:1.5}
.bsc-post-meta{font-size:.76rem;opacity:.67}
</style>