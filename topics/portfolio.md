---
layout: bsc
title: PORTFOLIO
permalink: /topics/portfolio/
---
<nav class="bsc-breadcrumb" aria-label="현재 위치"><a href="/">HOME</a> &nbsp;/&nbsp; <span>PORTFOLIO</span><span id="bsc-crumb-extra"></span></nav>
<section class="bsc-topic-banner" aria-label="PORTFOLIO"><img class="bsc-topic-image" src="/assets/img/banners/v2/portfolio-1x.webp" alt="" loading="eager"><h1>PORTFOLIO</h1></section>
{% assign matching = site.posts | where_exp: "post", "post.categories contains 'Portfolio'" | sort: "date" | reverse %}
<div class="bsc-topic-intro"><p>직접 구축하고 관찰한 프로젝트의 과정과 결과물입니다.</p><span class="bsc-topic-count">{{ matching.size }}개 게시글</span></div>
<nav class="bsc-filters" aria-label="하위 주제 필터"><button class="bsc-filter is-current" type="button" data-topic="">전체</button>
<button class="bsc-filter" type="button" data-topic="SOC Project">SOC Project</button>
<button class="bsc-filter" type="button" data-topic="Site Development">Site Development</button></nav>
<div class="bsc-post-list" id="bsc-topic-posts">
{% for post in matching %}
<article class="bsc-entry" data-fields="{{ post.categories | join: ' ' | escape }} {{ post.tags | join: ' ' | escape }} {{ post.subcategory | escape }}"><a href="{{ post.url | relative_url }}"><span class="bsc-date">{{ post.date | date: '%Y.%m.%d' }}{% if post.subcategory %} · {{ post.subcategory | escape }}{% endif %}</span><h2>{{ post.title | escape }}</h2><p class="bsc-excerpt">{{ post.excerpt | strip_html | normalize_whitespace | truncate: 135 | escape }}</p></a><span class="bsc-arrow" aria-hidden="true">↗</span></article>
{% endfor %}
<p class="bsc-empty" id="bsc-topic-empty"{% if matching.size > 0 %} hidden{% endif %}>아직 이 주제에 등록된 게시글이 없습니다.</p></div>
<script>
(()=>{
const entries=[...document.querySelectorAll('#bsc-topic-posts .bsc-entry')];
const buttons=[...document.querySelectorAll('.bsc-filter')];
const empty=document.querySelector('#bsc-topic-empty');
const extra=document.querySelector('#bsc-crumb-extra');
function apply(topic){let count=0;entries.forEach(e=>{const ok=!topic||e.dataset.fields.toLowerCase().includes(topic.toLowerCase());e.hidden=!ok;if(ok)count++});empty.hidden=count!==0;buttons.forEach(b=>b.classList.toggle('is-current',b.dataset.topic===topic));extra.textContent=topic?' / '+topic:'';}
buttons.forEach(b=>b.addEventListener('click',()=>{const topic=b.dataset.topic;const url=new URL(location.href);if(topic)url.searchParams.set('topic',topic);else url.searchParams.delete('topic');history.replaceState({},'',url);apply(topic)}));
apply(new URLSearchParams(location.search).get('topic')||'');
})();
</script>
