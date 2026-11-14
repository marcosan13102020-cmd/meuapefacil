/* ===== CONFIGURAÇÃO — preencha os IDs quando tiver ===== */
var CONFIG = {
  whatsapp: '5543988341571',
  pixelId: '',      // ID do Pixel da Meta (ex.: 123456789012345)
  ga4Id: ''         // ID do Google Analytics 4 (ex.: G-XXXXXXX)
};

/* ===== Rastreamento (só carrega se tiver ID) ===== */
(function(){
  if (CONFIG.pixelId) {
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', CONFIG.pixelId); fbq('track', 'PageView');
  }
  if (CONFIG.ga4Id) {
    var s = document.createElement('script'); s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + CONFIG.ga4Id; document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function(){ dataLayer.push(arguments); };
    gtag('js', new Date()); gtag('config', CONFIG.ga4Id);
  }
})();

function registrarLead(origem){
  try { if (window.fbq) fbq('track', 'Lead', {content_name: origem}); } catch(e){}
  try { if (window.gtag) gtag('event', 'generate_lead', {origem: origem}); } catch(e){}
}

/* ===== Origem do visitante (UTM) — vai junto na mensagem ===== */
var origem = (function(){
  try {
    var p = new URLSearchParams(location.search);
    var u = p.get('utm_source');
    if (u) { sessionStorage.setItem('origem', u + (p.get('utm_campaign') ? '/' + p.get('utm_campaign') : '')); }
    return sessionStorage.getItem('origem') || '';
  } catch(e){ return ''; }
})();

function linkWhats(texto){
  var t = texto + (origem ? '\n\n(via site - ' + origem + ')' : '');
  return 'https://wa.me/' + CONFIG.whatsapp + '?text=' + encodeURIComponent(t);
}

/* Todos os botões com data-wa abrem o WhatsApp com a mensagem certa */
document.querySelectorAll('[data-wa]').forEach(function(a){
  a.href = linkWhats(a.getAttribute('data-wa'));
  a.target = '_blank'; a.rel = 'noopener';
  a.addEventListener('click', function(){ registrarLead(a.getAttribute('data-origem') || 'botao'); });
});

/* ===== Descubra sua faixa do MCMV ===== */
var simForm = document.getElementById('sim-form');
if (simForm) {
  simForm.addEventListener('submit', function(e){
    e.preventDefault();
    var bruto = document.getElementById('renda').value.replace(/\./g,'').replace(',', '.');
    var renda = parseFloat(bruto);
    var out = document.getElementById('sim-res');
    if (!renda || renda <= 0) { out.innerHTML = 'Digite a renda bruta mensal da família.'; out.classList.add('on'); return; }
    var faixa, txt;
    if (renda <= 3200) { faixa = 'Faixa 1'; txt = 'Você pode ter direito aos <b>maiores subsídios do programa</b> e às menores taxas de juros.'; }
    else if (renda <= 5000) { faixa = 'Faixa 2'; txt = 'Você pode ter <b>subsídio do governo</b> e juros reduzidos. O valor do desconto depende da renda exata e do imóvel.'; }
    else if (renda <= 9600) { faixa = 'Faixa 3'; txt = 'Não há subsídio direto, mas você financia com <b>juros abaixo do mercado</b> e pode usar o FGTS.'; }
    else if (renda <= 13000) { faixa = 'Faixa 4 (Classe Média)'; txt = 'Você financia com <b>condições especiais do programa</b> e pode usar o FGTS.'; }
    else { faixa = 'acima do limite do programa'; txt = 'Sua renda passa do limite do programa, mas eu te ajudo com o <b>financiamento tradicional</b>.'; }
    var rendaFmt = renda.toLocaleString('pt-BR', {style:'currency', currency:'BRL'});
    out.innerHTML = 'Com renda de <b>' + rendaFmt + '</b>, sua família se enquadra na <b>' + faixa + '</b>. ' + txt +
      '<br><br><a class="btn btn-wa" data-origem="simulador" href="' +
      linkWhats('Olá Marcos! Fiz a simulação no site: renda familiar de ' + rendaFmt + ' (' + faixa + '). Quero saber quanto consigo de subsídio e qual parcela cabe no meu bolso.') +
      '" target="_blank" rel="noopener">Ver meu subsídio e parcela com o Marcos</a>';
    out.classList.add('on');
    registrarLead('simulador_faixa');
  });
}

/* ===== Formulário de contato -> WhatsApp ===== */
var form = document.getElementById('form-lead');
if (form) {
  form.addEventListener('submit', function(e){
    e.preventDefault();
    var nome = form.nome.value.trim();
    var renda = form.renda.value;
    var interesse = form.interesse.value;
    var msg = 'Olá Marcos! Meu nome é ' + nome + '.\nRenda familiar: ' + renda + '\nInteresse: ' + interesse + '\nQuero uma análise gratuita do meu perfil.';
    registrarLead('formulario');
    window.open(linkWhats(msg), '_blank');
  });
}

/* Ano no rodapé */
var ano = document.getElementById('ano'); if (ano) ano.textContent = new Date().getFullYear();
