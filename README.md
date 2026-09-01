# Smart Burger — prévia de site (conceito)

Prévia de conceito criada por **Jadir Freire** para apresentar uma proposta de site próprio à
Smart Burger. **Não é o site oficial da marca e não possui vínculo com ela.**

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | A página. HTML, CSS e JS num arquivo só; imagens em `img/`. É aqui que se edita. |
| `img/` | As 8 fotos usadas na página. |
| `build/inline.py` | Gera a versão de arquivo único (imagens em base64) em `dist/`. |

Basta abrir `index.html` no navegador — não precisa de servidor, build ou instalação.

### Versão de arquivo único

Para mandar a prévia por e-mail ou WhatsApp, onde uma pasta `img/` separada se perderia:

```bash
python build/inline.py
```

Escreve `dist/index-arquivo-unico.html` (~2,6 MB), que abre com duplo clique em qualquer
lugar. `dist/` é gerado e não entra no versionamento.

## Dependências

Nenhuma biblioteca. Só as fontes do Google Fonts, carregadas por `<link>`:
**Anton** (títulos), **Barlow Condensed** (preços, rótulos) e **Rubik** (texto).
Sem internet as fontes caem para as alternativas declaradas no CSS e o layout continua íntegro.

## Trocar as cores

Tudo passa por variáveis CSS no topo do `<style>`. Mexer aqui repinta a página inteira:

```css
:root{
  --char:#120E0B;    /* fundo, preto quente        */
  --char2:#1C1613;   /* superfícies elevadas       */
  --char3:#271E19;   /* realces                    */
  --line:#3A2C24;    /* bordas e divisórias        */
  --paper:#F6F0E6;   /* texto principal            */
  --dim:#B5A79A;     /* texto secundário           */
  --dim2:#8A7C71;    /* texto de apoio             */
  --mostarda:#F0B429;/* acento 1 — preços, selo    */
  --brasa:#D63B18;   /* acento 2 — botões          */
}
```

Se a marca tiver cores oficiais, substitua `--mostarda` e `--brasa` — o resto se ajusta.

## Estrutura da página

1. Faixa de aviso (prévia não oficial)
2. Cabeçalho fixo + "Pedir agora"
3. Hero com selo giratório de 15 anos
4. Faixa de números (15 anos · 4 unidades · 107 mil seguidores · #9 em Osasco)
5. Os mais pedidos — 4 cards
6. Cardápio completo em ficha de pedido, com abas (Burgers / Entradas / Sobremesas / Bebidas)
7. Combos
8. Prova social
9. Unidades, com link para o sistema de pedidos de cada uma
10. Chamada final + rodapé

As abas do cardápio são o único JavaScript da página (~20 linhas, no fim do arquivo).
São acessíveis por teclado (setas ← →) e usam `role="tablist"` / `aria-selected`.

## Antes de publicar de verdade

- [ ] **Conferir todos os preços** com a casa. Foram lidos do cardápio público de delivery da unidade Osasco em setembro de 2026.
- [ ] **Confirmar autorização de uso das fotos.** São as do próprio cardápio da Smart Burger.
- [ ] **Substituir os depoimentos.** Os três cards estão marcados como *texto de exemplo* — trocar por avaliações reais ou integrar o Google Meu Negócio.
- [ ] Preencher endereço de Alphaville e horários de Carapicuíba, Alphaville e São Francisco (só o de Osasco é público).
- [ ] Preços das bebidas (hoje aparecem como "ver no pedido").
- [ ] Trocar o logotipo `SB` de marcador pelo logo oficial em SVG.
- [ ] **Remover a faixa de aviso** (`<p class="demo">`) e este README quando o site passar a ser oficial.
- [ ] Adicionar Open Graph e favicon para o compartilhamento em redes.

## Links de pedido usados

Os botões apontam para o sistema que a casa já utiliza — nada muda no fluxo da cozinha:

- Osasco — `pedido.anota.ai/loja/smart-burger-1`
- Carapicuíba — `pedido.anota.ai/loja/smart-burger-carapicuba`
- Alphaville — `pedido.anota.ai/loja/smart-burger-carapicuba-1`
- São Francisco — iFood
