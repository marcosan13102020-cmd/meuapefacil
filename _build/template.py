"""Gera páginas internas do site com o mesmo cabeçalho e rodapé.
Uso: python3 _build/template.py   (roda a partir da pasta do site)"""
import json, os

WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7a11.6 11.6 0 0 1-4.5-4c-.3-.5-1-1.5-1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.2.5.1.6 0l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.3z"/></svg>'

def page(slug, title, desc, h1_crumb, body, faq=None, extra_schema=None, wa_msg="Olá Marcos! Vim pelo site."):
    url = f"https://meuapefacil.imb.br/{slug}/"
    schemas = [{
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": "https://meuapefacil.imb.br/"},
            {"@type": "ListItem", "position": 2, "name": h1_crumb, "item": url}]}]
    if faq:
        schemas.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    if extra_schema:
        schemas.append(extra_schema)
    schema_html = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    faq_html = ""
    if faq:
        items = "".join(f"<details{' open' if i == 0 else ''}><summary>{q}</summary><p>{a}</p></details>" for i, (q, a) in enumerate(faq))
        faq_html = f'<section style="background:var(--creme)"><div class="wrap" style="max-width:820px"><div class="cabeca center"><span class="tag">Dúvidas frequentes</span><h2>Perguntas comuns</h2></div><div class="faq">{items}</div></div></section>'
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#2d5a3d">
<meta property="og:type" content="article">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Meu Apê Fácil">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://meuapefacil.imb.br/assets/og.jpg">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/style.css">
{schema_html}
</head>
<body>
<header class="topo"><div class="wrap">
  <a class="marca" href="../"><b>Meu Apê Fácil</b><small>Marcos Antônio · Corretor de Imóveis</small></a>
  <nav class="menu">
    <a href="../apartamento-barato-londrina/">Apartamentos</a>
    <a href="../como-comprar-primeiro-apartamento/">Como comprar</a>
    <a href="../#faixas">Quem tem direito</a>
    <a class="btn btn-wa" data-origem="topo_{slug}" data-wa="{wa_msg}">Fale comigo</a>
  </nav>
</div></header>
<main>
<div class="wrap migalha"><a href="../">Início</a> › {h1_crumb}</div>
{body}
{faq_html}
<section class="bloco-verde"><div class="wrap center">
  <h2>Quer saber quanto fica a sua parcela?</h2>
  <p class="lead" style="margin:16px auto 28px">Me chame no WhatsApp com a renda da sua família. Eu faço a simulação com subsídio e FGTS e te mostro as opções que cabem no seu bolso. Sem custo.</p>
  <a class="btn btn-wa" data-origem="cta_{slug}" data-wa="{wa_msg}">{WA_SVG} Fazer minha simulação gratuita</a>
</div></section>
</main>
<footer><div class="wrap">
  <div><b style="font-family:'Playfair Display',serif;font-size:1.3rem">Meu Apê Fácil</b>
  <p style="margin-top:10px">Marcos Antônio · Corretor de Imóveis CRECI-PR 51192<br>Minha Casa Minha Vida em Londrina e região.</p></div>
  <div><b>Contato</b><p style="margin-top:10px"><a data-origem="rodape_{slug}" data-wa="Olá Marcos! Vim pelo site.">WhatsApp (43) 98834-1571</a><br><a href="https://www.instagram.com/meuapefacil_/" target="_blank" rel="noopener">Instagram @meuapefacil_</a></p></div>
  <div><b>Guias</b><p style="margin-top:10px"><a href="../apartamento-barato-londrina/">Apartamento barato em Londrina</a><br><a href="../como-comprar-primeiro-apartamento/">Como comprar o primeiro apartamento</a><br><a href="../residencial-mirantti/">Residencial Mirantti</a></p></div>
  <p class="legal">MK CORRETOR LTDA · CNPJ 50.614.443/0001-40 · © <span id="ano">2026</span>. Valores e condições dos empreendimentos são definidos pelas construtoras e podem mudar sem aviso. Subsídio e financiamento sujeitos à aprovação da Caixa.</p>
</div></footer>
<a class="wa-flut" aria-label="Falar no WhatsApp" data-origem="flutuante_{slug}" data-wa="{wa_msg}">{WA_SVG}</a>
<script src="../assets/app.js" defer></script>
</body>
</html>
"""
    os.makedirs(slug, exist_ok=True)
    open(os.path.join(slug, "index.html"), "w").write(html)
    print("ok", slug)
