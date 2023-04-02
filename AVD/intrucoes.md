# Algumas instruções para sobreviver ao windows...

## Melhorar Unicode no windows

No sentido de Selecionar Unicode UTF-8 em (quase) todos os sítios:

```
- Control Panel           // painel de controle
  - Relogio e região
    - Região
      - (selecionar a tab "Administação" )
        - botão (Alterar região do sistema)
          - [V] Beta: Utilizar Unicode UTF-8 para suporte de idiomas no mundo
```

... pode ser preciso reiniciar o computador

## instalar programas com winget

Alguma actualização opcionais...

- winget install microsoft.powershell.preview
- winget install microsoft.windowsterminal.preview

### instalar Perl

- winget install strawberryperl.strawberryperl

### instalar git

- winget install git.git

#### Opcionalmente

instalar um comando `gh` para operações sobre github

- winget install github.cli

ou instalar github desktop

- winget install github.githubdesktop

## Linguakit 

### Descarregar o Linguakit

escolher uma pasta onde o linguakit possa ficar (Exemplo: `Documents`)

- git clone  https://github.com/JJoao/Linguakit
   
#### alternativamente... 

também é possível descarregar o linguakit usando o github-desktop: 
```
 [instalar repo]
   →[a partir de URL]
      → https://github.com/JJoao/Linguakit
```

ou ainda

- gh repo clone jjoao/linguakit


### instalar o Lingakit

- cd linguakit
- gmake deps
- gmake install-win

## Alguns utilitários

- FIXME

## No command.com

### alterar consola (`command.com`) para unicode utf8:

em consolas antigas pode ser útil

- chcp 65001    //// utf8 na consola
