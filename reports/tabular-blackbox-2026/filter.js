<script>
(function(){
  const cards=[...document.querySelectorAll('.paper-card')];
  const q=document.getElementById('paper-search'), cat=document.getElementById('paper-category'), pri=document.getElementById('paper-priority'), count=document.getElementById('paper-count');
  if(!q||!cat||!pri) return;
  function apply(){
    const needle=q.value.trim().toLowerCase(); let shown=0;
    for(const c of cards){
      const okQ=!needle || c.innerText.toLowerCase().includes(needle);
      const okC=!cat.value || c.dataset.category===cat.value;
      const okP=!pri.value || c.dataset.priority===pri.value;
      const ok=okQ&&okC&&okP; c.style.display=ok?'':'none'; if(ok) shown++;
    }
    count.textContent=shown+' / '+cards.length+' papers';
  }
  q.addEventListener('input',apply); cat.addEventListener('change',apply); pri.addEventListener('change',apply); apply();
})();
</script>
