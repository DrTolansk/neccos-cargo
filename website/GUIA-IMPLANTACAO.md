# NECCOS Cargo — estrutura e publicação do site

**Site no ar:** https://neccos-cargo.joasmaciel588.workers.dev

## Pilha tecnológica
- HTML5, CSS3 responsivo e JavaScript nativo sem framework;
- Layout adaptável a celular e computador, navegação por âncoras e menu mobile;
- Links WhatsApp e `mailto:`;
- Recursos visuais WebP, JPG e PNG;
- Hospedagem gratuita na **Cloudflare Workers — Static Assets**, implantação por upload de arquivos.

## Estrutura real do pacote
```text
/
├── index.html
├── robots.txt
├── LEIA-ME.txt
└── assets/
    ├── banner-neccos.webp
    ├── compartilhamento.jpg
    ├── favicon.png
    ├── frete-e-cargas.webp
    ├── logo-horizontal.webp
    ├── marca-completa.webp
    └── operacao-logistica.webp
```

## Arquivos disponíveis neste GitHub
- [index.html](index.html) — HTML, CSS e JavaScript reais utilizados no site, com os caminhos relativos para imagens versionadas no próprio repositório;
- [Inventário das imagens](assets/README.md) — nomes, papéis e localização dos recursos;
- [Apresentação para parceiros](../APRESENTACAO-PARCEIROS.pdf) — PDF institucional versionado.

As sete imagens binárias estão agora incluídas em [`assets/`](assets/) no repositório, e o HTML utiliza caminhos relativos. Assim, a pasta `website/` contém os arquivos necessários para publicar uma cópia estática independente do site.

## Atualizar o site
1. Editar HTML e/ou recursos em uma cópia do pacote completo.
2. Acessar Cloudflare > Workers & Pages > projeto `neccos-cargo`.
3. Criar nova implantação de ativos estáticos para o **mesmo** Worker.
4. Conferir versão mobile, desktop, menu, imagens e botões.

**Importante:** não foi configurado deploy automático entre GitHub e Cloudflare. Alterar o código aqui **não modifica automaticamente o site publicado**.

## Domínio e e-mails
O domínio `neccoscargo.com.br` ainda não está registrado. Os cinco endereços de e-mail exibidos no site ainda não estão ativos; é necessário registrar domínio, configurar DNS e provedor e testar antes de divulgar.

## Segurança
Não publicar senhas, dados de motoristas, contratos privados, tabelas de preços ou credenciais.