# Site de apresentação (GitHub Pages)

Esta pasta contém a página de apresentação do curso para a **Secretaria Municipal de Meio
Ambiente**, publicável no GitHub Pages.

## Como publicar

1. Crie o repositório no GitHub e envie este projeto.
2. No repositório, abra **Settings → Pages**.
3. Em **Source**, escolha **Deploy from a branch**.
4. Selecione a branch **main** e a pasta **/docs**.
5. Salve. O GitHub exibirá o endereço, algo como:
   `https://marquezbertin.github.io/Curso-Tecnologia-Dados-Gestao-Ambiental/`

> O site não usa backend, banco de dados nem dependências externas. Ele funciona apenas com
> `index.html`, `styles.css`, `script.js` e `favicon.svg`.

## Como atualizar

| O que mudar | Onde |
|---|---|
| Textos da apresentação | `index.html` |
| Cores, tipografia e layout | `styles.css` |
| Menu mobile, animações e contadores | `script.js` |
| Links para o repositório | procure pelo domínio `github.com/Marquezbertin` no `index.html` |
| Contato | procure por `mailto:` no `index.html` |

## Antes de apresentar

- [ ] Troque o link do repositório se o nome for diferente.
- [ ] Confira o e-mail de contato.
- [ ] Abra no celular para testar o menu.
- [ ] Imprima ou gere PDF da página (o CSS tem estilo de impressão).
- [ ] Confira se os links para os documentos do GitHub abrem.

## Estrutura

```
docs/
├── index.html      página única com todas as seções
├── styles.css      identidade visual e responsividade
├── script.js       menu, navegação ativa, animações e contadores
├── favicon.svg     ícone do site
└── README.md       este arquivo
```

## Acessibilidade

- Navegação por teclado e link "pular para o conteúdo".
- Contraste mínimo 4,5:1.
- `prefers-reduced-motion` respeitado.
- Textos alternativos e rótulos ARIA.
- Layout responsivo de 320 px a telas grandes.
