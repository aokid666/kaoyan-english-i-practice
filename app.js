const listEl=document.querySelector('#list'),detailEl=document.querySelector('#detail');
let entries=[], selected='';
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const paras=s=>esc(s||'').replace(/【待译部分】([\s\S]*?)【待译部分结束】/g,'<mark class="marked">【待译部分】$1【待译部分结束】</mark>');
function render(){
  const q=document.querySelector('#query').value.trim().toLowerCase(),t=document.querySelector('#type').value;
  const shown=entries.filter(e=>(!t||e.kind.includes(t))&&(!q||[e.date,e.title,e.kind,e.translation?.topic,e.partA?.topic].join(' ').toLowerCase().includes(q)));
  document.querySelector('#results').textContent=`显示 ${shown.length} / ${entries.length} 组`;
  listEl.innerHTML=shown.map(e=>`<button class="entry-card ${e.id===selected?'active':''}" data-id="${esc(e.id)}"><span class="entry-date">${esc(e.date)}${e.number>1?' · 第'+e.number+'组':''}</span><span class="entry-title">${esc(e.title)}</span><span class="entry-tags">${esc(e.kind)} · ${esc(e.partA?.topic||'资料待补')}</span></button>`).join('')||'<p class="empty">没有匹配的题目。</p>';
  if(!shown.some(e=>e.id===selected))selected=shown[0]?.id||'';
  listEl.querySelectorAll('button').forEach(b=>b.onclick=()=>{selected=b.dataset.id;render();if(innerWidth<821)detailEl.scrollIntoView({behavior:'smooth',block:'start'})});
  const e=entries.find(x=>x.id===selected);
  if(!e){detailEl.innerHTML='<p class="empty">请选择一组题目。</p>';return}
  const full=e.translation?.text&&e.partA?.text&&e.partB?.directions;
  detailEl.innerHTML=`<div class="detail-head"><span class="overline">PRACTICE SET · ${esc(e.id)}</span><h2>${esc(e.date)}${e.number>1?' · 第'+e.number+'组':''}</h2><span class="pill">原创模拟</span><span class="pill">${esc(e.kind)}</span></div>
    ${e.provenance?`<p class="notice">${esc(e.provenance)}</p>`:!full?'<p class="notice">这组较早的记录只有可核对的题面摘要；仍缺少的原题或图片会明确标出。</p>':''}
    <section><h3>01 / 翻译</h3>${e.translation?.provenance?`<p class="source">${esc(e.translation.provenance)}</p>`:''}<p class="question">${paras(e.translation?.text||e.translation?.summary||'题面待补')}</p>${e.translation?.source?`<p class="source">来源：<a href="${esc(e.translation.url)}" target="_blank" rel="noopener noreferrer">${esc(e.translation.source)}</a></p>`:''}</section>
    <section><h3>02 / 小作文 · Part A</h3>${e.partA?.provenance?`<p class="source">${esc(e.partA.provenance)}</p>`:''}<p class="question">${paras(e.partA?.text||e.partA?.summary||'题面待补')}</p></section>
    <section><h3>03 / 大作文 · Part B</h3>${e.partB?.provenance?`<p class="source">${esc(e.partB.provenance)}</p>`:''}<p class="question">${paras(e.partB?.directions||e.partB?.summary||'题面待补')}</p>${e.partB?.image?`<figure class="figure"><img src="${esc(e.partB.image)}" alt="本组大作文题图" loading="lazy"><figcaption>大作文原始题图</figcaption></figure>`:''}${e.partB?.table?`<p class="question">${esc(e.partB.table)}</p>`:''}</section>`;
  listEl.querySelectorAll('button').forEach(b=>b.classList.toggle('active',b.dataset.id===selected));
}
fetch('./entries.json').then(r=>{if(!r.ok)throw Error(r.status);return r.json()}).then(data=>{entries=data.sort((a,b)=>b.id.localeCompare(a.id));document.querySelector('#count').textContent=entries.length;selected=new URLSearchParams(location.search).get('id')||entries[0]?.id;render()}).catch(()=>{detailEl.innerHTML='<p class="notice">题目数据暂时无法读取，请稍后重试。</p>'});
document.querySelector('#query').addEventListener('input',render);
document.querySelector('#type').addEventListener('change',render);
