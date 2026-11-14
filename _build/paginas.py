import sys; sys.path.insert(0, "_build")
from template import page

# ---------------- APARTAMENTO BARATO EM LONDRINA ----------------
barato = """
<section style="padding-top:28px">
 <div class="wrap" style="max-width:900px">
  <span class="tag">Atualizado em novembro de 2026</span>
  <h1>Apartamento barato em Londrina: onde encontrar e como pagar menos</h1>
  <p class="lead" style="margin-top:16px">Em Londrina, os apartamentos novos mais acessíveis são os lançamentos de 2 quartos que entram no Minha Casa Minha Vida. Com o subsídio do governo e o FGTS, muitas famílias pagam uma parcela parecida com o valor do aluguel.</p>
 </div>
</section>

<section style="padding-top:0">
 <div class="wrap" style="max-width:900px">
  <h2>Quanto custa um apartamento barato em Londrina hoje</h2>
  <p style="margin-top:14px">Os lançamentos econômicos de 2 quartos, com 35 a 46 m², estão saindo entre <b>cerca de R$ 215 mil e R$ 300 mil</b> (referência de novembro de 2026). Esse é o preço de tabela. O que a família realmente paga fica bem abaixo, porque entram três descontos no caminho:</p>
  <div class="grid g3" style="margin-top:24px">
   <div class="card"><div class="num">1</div><h3>Subsídio do governo</h3><p>Famílias com renda de até R$ 5 mil podem receber até R$ 55 mil de desconto, sem devolver.</p></div>
   <div class="card"><div class="num">2</div><h3>Saldo do FGTS</h3><p>Quem tem 3 anos de carteira assinada pode usar o Fundo de Garantia na entrada.</p></div>
   <div class="card"><div class="num">3</div><h3>Entrada parcelada</h3><p>Na compra na planta, a entrada costuma ser dividida em parcelas durante a obra.</p></div>
  </div>
 </div>
</section>

<section style="background:var(--creme)">
 <div class="wrap">
  <div class="cabeca"><span class="tag">Opções que eu atendo</span><h2>Apartamentos acessíveis à venda em Londrina</h2>
  <p class="lead">Lançamentos com condições do Minha Casa Minha Vida. Peça a tabela atualizada e a simulação para a sua renda.</p></div>
  <div class="grid g2">
   <article class="card">
    <span class="tag">Lançamento · Jardim Barcelona</span>
    <h3 style="font-size:1.5rem">Residencial Mirantti</h3>
    <p style="margin:8px 0 14px">2 quartos, 40 e 41 m², com vaga. Zona norte de Londrina. Entrega prevista para dezembro de 2030.</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-verde" href="../residencial-mirantti/">Ver detalhes</a><a class="btn btn-wa" data-origem="barato_mirantti" data-wa="Olá Marcos! Quero a tabela do Residencial Mirantti.">Receber tabela</a></div>
   </article>
   <article class="card">
    <span class="tag">Em obras · Vista Bela</span>
    <h3 style="font-size:1.5rem">Residencial Almada</h3>
    <p style="margin:8px 0 14px">2 quartos, 40 e 42 m², com vaga. Na Av. Giocondo Maturi, zona norte. Entrega prevista para dezembro de 2029.</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-wa" data-origem="barato_almada" data-wa="Olá Marcos! Quero a tabela do Residencial Almada.">Receber tabela</a></div>
   </article>
  </div>
  <p style="margin-top:20px;color:var(--cinza);font-size:.95rem">Procura em outra região de Londrina? Me fale o bairro e a renda da família que eu te passo as opções disponíveis.</p>
 </div>
</section>

<section>
 <div class="wrap" style="max-width:900px">
  <h2>Onde ficam os apartamentos mais baratos de Londrina</h2>
  <p style="margin-top:14px">A maior parte dos lançamentos acessíveis está na <b>zona norte</b> (Vista Bela, Jardim Barcelona, Cilo 3 e região), onde ainda há terrenos maiores e o preço do metro quadrado fica abaixo da média da cidade. Também há opções na zona oeste e na zona sul, em bairros como Jardim Morumbi e Jardim Nova Esperança.</p>
  <h2 style="margin-top:44px">Como pagar menos no seu apartamento</h2>
  <div class="grid" style="margin-top:20px;gap:14px">
   <div class="card"><h3>Compre na planta</h3><p>O preço costuma ser menor do que o de um imóvel pronto, e você tem o período da obra para juntar a entrada.</p></div>
   <div class="card"><h3>Some a renda com mais alguém</h3><p>Casais, irmãos ou pais e filhos podem comprar juntos. A renda maior aumenta o valor financiado, mas pode mudar a faixa do subsídio. Vale simular as duas formas.</p></div>
   <div class="card"><h3>Deixe o nome limpo antes</h3><p>Restrição no CPF trava a aprovação na Caixa. Resolver isso antes acelera tudo.</p></div>
   <div class="card"><h3>Simule antes de visitar</h3><p>Saber quanto você consegue financiar evita perder tempo com imóveis fora do seu orçamento.</p></div>
  </div>
 </div>
</section>

<section class="bloco-verde" id="faixas">
 <div class="wrap"><div class="sim">
  <div><span class="tag">Teste rápido</span><h2>Descubra se você tem direito ao subsídio</h2><p class="lead" style="margin-top:16px">Digite a renda bruta mensal da família e veja na hora em qual faixa do Minha Casa Minha Vida você se encaixa.</p></div>
  <div class="sim-box"><form id="sim-form"><label for="renda">Renda bruta familiar por mês</label><input id="renda" inputmode="decimal" placeholder="Ex.: 3.500" autocomplete="off"><button class="btn btn-verde" style="width:100%;margin-top:14px" type="submit">Ver minha faixa</button></form><div class="resultado" id="sim-res" aria-live="polite"></div></div>
 </div></div>
</section>
"""
page("apartamento-barato-londrina",
     "Apartamento barato em Londrina: opções com subsídio e FGTS (2026) | Meu Apê Fácil",
     "Onde encontrar apartamento barato em Londrina, quanto custa e como pagar menos com o Minha Casa Minha Vida, subsídio de até R$ 55 mil e FGTS. Simulação gratuita.",
     "Apartamento barato em Londrina", barato,
     faq=[
      ("Qual o apartamento mais barato de Londrina?", "Os lançamentos mais acessíveis são apartamentos de 2 quartos com 35 a 46 m², com preço de tabela a partir de cerca de R$ 215 mil (referência de novembro de 2026). Com subsídio e FGTS, o valor que a família paga fica menor."),
      ("Dá para comprar apartamento em Londrina ganhando 2 salários mínimos?", "Em muitos casos, sim. Famílias com renda de até R$ 3.200 estão na Faixa 1 do Minha Casa Minha Vida, que tem os maiores subsídios e as menores taxas de juros. A aprovação depende da análise de crédito da Caixa."),
      ("Apartamento barato é seguro?", "Sim, quando é de construtora com registro e o financiamento é feito pela Caixa. Antes de assinar, confira se o empreendimento tem registro de incorporação e se o contrato é com a construtora."),
      ("Preciso dar entrada?", "Depende do valor do imóvel, do subsídio e do quanto a Caixa aprova. A diferença pode ser paga com FGTS e, na compra na planta, parcelada durante a obra.")],
     wa_msg="Olá Marcos! Vi a página de apartamentos baratos em Londrina e quero saber as opções para a minha renda.")

# ---------------- COMO COMPRAR O PRIMEIRO APARTAMENTO ----------------
passos = [
 ("Descubra quanto a sua família ganha por mês", "Some a renda bruta de quem vai comprar junto. Ela define a sua faixa no Minha Casa Minha Vida, o subsídio e quanto a Caixa pode financiar."),
 ("Confira o seu CPF", "Nome com restrição (SPC, Serasa) costuma travar a aprovação. Consulte de graça no app da Serasa e, se houver dívida, negocie antes."),
 ("Separe os documentos", "Com tudo em mãos, a análise anda mais rápido. A lista completa está logo abaixo."),
 ("Faça a simulação", "A simulação mostra o subsídio, o valor financiado, a entrada e a parcela. Eu faço com você, sem custo."),
 ("Escolha o apartamento", "Com o valor aprovado, você escolhe entre os imóveis que cabem no orçamento, na região que prefere."),
 ("Aprovação de crédito na Caixa", "A Caixa analisa renda, documentos e CPF. Eu monto e acompanho o processo até a aprovação."),
 ("Assinatura do contrato", "Você assina o contrato de compra com a construtora e o contrato de financiamento com a Caixa."),
 ("Entrega das chaves", "Na compra na planta, você recebe as chaves quando a obra termina. Nos imóveis prontos, logo após o registro."),
]
passos_html = "".join(f'<div class="card" style="display:flex;gap:18px;align-items:flex-start"><div class="passo"><div class="n">{i}</div></div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (t, d) in enumerate(passos, 1))
comprar = f"""
<section style="padding-top:28px">
 <div class="wrap" style="max-width:900px">
  <span class="tag">Guia completo · 2026</span>
  <h1>Como comprar o seu primeiro apartamento: passo a passo</h1>
  <p class="lead" style="margin-top:16px">Comprar o primeiro imóvel parece complicado, mas segue sempre o mesmo caminho. Neste guia você vê cada etapa, os documentos que precisa e os erros que mais atrasam a aprovação.</p>
 </div>
</section>
<section style="padding-top:0">
 <div class="wrap" style="max-width:900px">
  <h2>As 8 etapas para comprar o primeiro apartamento</h2>
  <div class="grid" style="margin-top:24px;gap:14px">{passos_html}</div>
 </div>
</section>
<section style="background:var(--creme)">
 <div class="wrap" style="max-width:900px">
  <h2>Documentos para financiar pela Caixa</h2>
  <div class="grid g2" style="margin-top:24px">
   <div class="card"><h3>Pessoais</h3><p>RG e CPF (ou CNH)<br>Certidão de nascimento ou casamento<br>Comprovante de endereço recente</p></div>
   <div class="card"><h3>Renda com carteira assinada</h3><p>Últimos 3 holerites<br>Carteira de trabalho (digital serve)<br>Extrato do FGTS</p></div>
   <div class="card"><h3>Renda como autônomo ou MEI</h3><p>Extratos bancários dos últimos meses<br>Declaração do Imposto de Renda, se tiver<br>Declaração do MEI (DASN), se for MEI</p></div>
   <div class="card"><h3>Quem compra junto</h3><p>Os mesmos documentos para cada pessoa que vai somar renda na compra.</p></div>
  </div>
  <p style="margin-top:16px;color:var(--cinza);font-size:.92rem">A Caixa pode pedir outros documentos conforme o caso. Eu confiro a lista certa para a sua situação antes de enviar.</p>
 </div>
</section>
<section>
 <div class="wrap" style="max-width:900px">
  <h2>Erros que mais atrasam a compra</h2>
  <div class="grid" style="margin-top:20px;gap:14px">
   <div class="card"><h3>Visitar imóvel antes de simular</h3><p>Você pode se apaixonar por um apartamento que não cabe no valor aprovado. Simule primeiro.</p></div>
   <div class="card"><h3>Fazer dívida durante o processo</h3><p>Financiar carro ou parcelar compras grandes muda a análise de crédito e pode reduzir o valor aprovado.</p></div>
   <div class="card"><h3>Esconder renda ou informação</h3><p>A Caixa confere tudo. Informação diferente nos documentos faz o processo voltar para o começo.</p></div>
   <div class="card"><h3>Esquecer os custos da compra</h3><p>Existem custos de cartório e ITBI. Em muitos lançamentos do programa, a construtora ajuda com esses valores. Pergunte sempre antes de fechar.</p></div>
  </div>
 </div>
</section>
"""
page("como-comprar-primeiro-apartamento",
     "Como comprar o primeiro apartamento: passo a passo e documentos (2026) | Meu Apê Fácil",
     "Guia simples para comprar o primeiro apartamento: as 8 etapas, os documentos para financiar pela Caixa, como usar o FGTS e os erros que atrasam a aprovação.",
     "Como comprar o primeiro apartamento", comprar,
     faq=[
      ("Qual a renda mínima para comprar um apartamento?", "Não existe um valor mínimo fixo. O que define é quanto a parcela representa da renda: em geral, a Caixa aprova parcelas de até cerca de 30% da renda familiar. Com o subsídio do Minha Casa Minha Vida, famílias com renda a partir de cerca de 2 salários mínimos conseguem comprar."),
      ("Quanto tempo demora para comprar o primeiro apartamento?", "Com a documentação organizada, a aprovação na Caixa costuma levar algumas semanas. Na compra na planta, a entrega das chaves acontece quando a obra termina."),
      ("Posso comprar com nome sujo?", "Com restrição no CPF, a Caixa normalmente não aprova o financiamento. O caminho é negociar a dívida e esperar a baixa no sistema antes de dar entrada no processo."),
      ("Precisa pagar o corretor?", "Na compra de lançamentos, a comissão do corretor é paga pela construtora. A análise, a simulação e o acompanhamento são gratuitos para o comprador.")],
     wa_msg="Olá Marcos! Li o guia de como comprar o primeiro apartamento e quero ajuda com o meu caso.")
