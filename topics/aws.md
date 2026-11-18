---
layout: bsc
title: AWS
permalink: /topics/aws/
---
<nav class="bsc-breadcrumb" aria-label="현재 위치"><a href="/">HOME</a> &nbsp;/&nbsp; <span>AWS</span><span id="bsc-crumb-extra"></span></nav>
<section class="bsc-topic-banner flip-image" aria-label="AWS"><img class="bsc-topic-image" src="/assets/img/banners/v2/aws-1x.webp" alt="" loading="eager"><h1>AWS</h1></section>
{% assign matching = site.posts | where_exp: "post", "post.categories contains 'AWS'" | sort: "date" | reverse %}
<div class="bsc-topic-intro"><p>클라우드 아키텍처와 운영·보안 기술을 체계적으로 정리합니다.</p><span class="bsc-topic-count">{{ matching.size }}개 게시글</span></div>
<nav class="bsc-filters" aria-label="하위 주제 필터"><button class="bsc-filter is-current" type="button" data-topic="">전체</button>
<button class="bsc-filter" type="button" data-topic="Fundamentals & Governance">Fundamentals & Governance</button>
<button class="bsc-filter" type="button" data-topic="Compute & Network">Compute & Network</button>
<button class="bsc-filter" type="button" data-topic="Storage & Data">Storage & Data</button>
<button class="bsc-filter" type="button" data-topic="Security & Architecture">Security & Architecture</button></nav>
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
