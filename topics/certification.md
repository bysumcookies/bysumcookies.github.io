---
layout: page
title: CERTIFICATION
permalink: /topics/certification/
icon: fas fa-folder-open
---

{% assign posts_in_category = site.posts | where_exp: "post", "post.categories contains 'Certification'" %}
<div id="category-summary"><p>이 카테고리의 학습 기록과 프로젝트를 모아둔 공간입니다.</p></div>
{% if posts_in_category.size > 0 %}
<div id="topic-list">
{% for post in posts_in_category %}
  <article class="topic-article" data-fields="{{ post.categories | join: ' ' | escape }} {{ post.tags | join: ' ' | escape }}">
    <h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
    <small>{{ post.date | date: '%Y.%m.%d' }}</small>
  </article>
{% endfor %}
</div>
<p id="topic-empty" hidden>해당 세부 주제의 게시글이 아직 없습니다.</p>
{% else %}
<p>아직 이 카테고리에 게시글이 없습니다. 기존 티스토리 글을 순차적으로 이전할 예정입니다.</p>
{% endif %}
<style>.topic-article{padding:18px 0;border-bottom:1px solid var(--main-border-color)}.topic-article h3{font-size:1.08rem;margin:0 0 6px}.topic-article small{opacity:.65}</style>
<script>
(function(){
  const term=new URLSearchParams(location.search).get('topic');
  if(!term)return;
  const list=document.querySelectorAll('.topic-article');
  if(!list.length)return;
  let visible=0;
  list.forEach(el=>{const matched=el.dataset.fields.toLowerCase().includes(term.toLowerCase());el.hidden=!matched;if(matched)visible++;});
  const notice=document.getElementById('topic-empty');
  if(notice)notice.hidden=visible!==0;
  const summary=document.getElementById('category-summary');
  if(summary){const e=document.createElement('p');e.textContent='선택한 주제: '+term;summary.append(e);}
})();
</script>
