# Algumas instruções para sobreviver ao windows...

## Unicode

No sentido de Selecionar Unicode UTF-8 em (quase) todos os sítios:

- Control Panel
  - Relogio e região
    - Região
      - (selecionar a tab "Administação" )
        - botão (Alterar região do sistema)
          - [V] Beta: Utilizar Unicode UTF-8 para suporte de idiomas no mundo

... pode ser preciso reiniciar o computador

## instalar programas com winget

Alguma actualização opcionais...

- winget install microsoft.powershell.preview
- winget install microsoft.windowsterminal.preview


- winget install strawberryperl.strawberryperl
- winget install github.cli

- gh repo clone sitiususc/linguakit
ou
- gh repo clone jjoao/linguakit
- cd linguakit
- gmake deps
- gmake install-win

## Alguns utilitários

- winget install burntsushi.ripgrep.gnu

## No command.com

### alterar consola para unicode utf8:

- chcp 65001    //// utf8 na consola
