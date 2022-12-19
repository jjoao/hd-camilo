
~~~
title: Trabalho Prático 1
author: Henrique
~~~

# Resolução dos [Enunciados](https://github.com/jjoao/hd-camilo/blob/main/Doc/TP/tp1.md) propostos

## 1. Lista das obras de camilo.
Listar as obras de Camilo existentes na pasta `Obra/` do nosso repositório.
Ou seja apresentar a lista dos ficheiros de texto existentes nessa pasta.


#### Código

```python
obras = os.listdir('../Obra'); obras.sort();
```

### Listagem de obras
<details id="list_books">
	<summary>expanda lista</summary>
	
1. Camilo-A_Brasileira_de_Prazins.txt
1. Camilo-A_Gratidao.txt
1. Camilo-A_Infanta_Capelista.txt
1. Camilo-A_Morgada_de_Romariz.txt
1. Camilo-A_enjeitada.txt
1. Camilo-A_filha_do_Acerdiago.txt
1. Camilo-A_filha_do_doutor_negro.txt
1. Camilo-A_mulher_fatal.txt
1. Camilo-A_neta_do_arcediago.txt
1. Camilo-A_queda_de_um_Anjo-Grafia_actualizada.txt
1. Camilo-A_queda_de_um_Anjo-Grafia_da_Epoca.txt
1. Camilo-A_senhora_Rattazzi.txt
1. Camilo-A_velhice_do_Padre_Eterno-Estudo.txt
1. Camilo-A_viuva_do_enforcado.txt
1. Camilo-Agostinho_de_Ceuta-Teatro.txt
1. Camilo-Amor_de_Perdicao.txt
1. Camilo-Amor_de_Salvacao.txt
1. Camilo-Anatema_1.txt
1. Camilo-Aventuras_de_Basilio_Fernandes.txt
1. Camilo-Carlota_Angela.txt
1. Camilo-Cenas_da_Foz.txt
1. Camilo-Coisas_que_so_eu_sei.txt
1. Camilo-Coracao_cabeca_e_estomago.txt
1. Camilo-Doze_casamentos_felizes.txt
1. Camilo-Duas_Horas_de_Leitura.txt
1. Camilo-Esbocos_de_apreciacoes_literarias.txt
1. Camilo-Espinhos_e_flores-Teatro.txt
1. Camilo-Eusebio_Macario.txt
1. Camilo-Gracejos_que_matam.txt
1. Camilo-Justica-Teatro.txt
1. Camilo-Maria_Moises-v1.txt
1. Camilo-Maria_Moises.txt
1. Camilo-Maria_da_Fonte.txt
1. Camilo-Memorias_de_Guilherme_do_Amaral.txt
1. Camilo-Misterios_de_Fafe.txt
1. Camilo-Misterios_de_Lisboa_1.txt
1. Camilo-Misterios_de_Lisboa_2.txt
1. Camilo-Misterios_de_Lisboa_3.txt
1. Camilo-No_Bom_Jesus_do_Monte.txt
1. Camilo-Noites_de_Lamego.txt
1. Camilo-Novelas_do_Minho_1.txt
1. Camilo-Novelas_do_Minho_2.txt
1. Camilo-O_Arrependimento.txt
1. Camilo-O_Comendador.txt
1. Camilo-O_Judeu_1.txt
1. Camilo-O_carrasco_de_Vitor_Hugo.txt
1. Camilo-O_cego_de_Landim.txt
1. Camilo-O_esqueleto-v2.txt
1. Camilo-O_esqueleto.txt
1. Camilo-O_filho_natural.txt
1. Camilo-O_que_fazem_mulheres.txt
1. Camilo-O_regicida.txt
1. Camilo-O_retrato_de_Ricardina-v1.txt
1. Camilo-O_romance_dum_homem_rico.txt
1. Camilo-Onde_esta_a_felicidade.txt
1. Camilo-Poesia_ou_Dinheiro-Teatro.txt
1. Camilo-Purgatorio_e_Paraiso-Teatro.txt
1. Camilo-Teatro-Vol_1.txt
1. Camilo-Teatro-Vol_2.txt
1. Camilo-Um_homem_de_brios.txt
1. Camilo-Um_livro.txt
1. Camilo-Uma_praga_rogada.txt
1. Camilo-Vinganca.txt
1. Camilo-Vinte_horas_de_liteira.txt
1. Camilo-Vulcoes_de_lama.txt
</details>



## 2. Estatísticas sobre as obras de Camilo

Instancio uma classe de _Books_ aonde, usando o **spaCy**, carrego estatísticas (método _stats_) sobre cada obra:
  * As entidades _ents_ separados em:
    - personagens
    - localidades
  * As frases e seu tamanho médio em carácteres e em palavras
  * Os verbos e seus lemmas, compilados em dicionário de frequencias

Então imprimo tabelas e as 2 frases iniciais com tais informações (função _md_)

#### Código

```python
for obra in obras:
	book_path = '../Obra/' + obra
	book = Book(book_path)
	book.stats()
	markdown += md(book)
```

### Listagem de obras

	
### A Brasileira de Prazins
<details id="Camilo-A_Brasileira_de_Prazins.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |  A Brasileira de Prazins  | Camilo-A_Brasileira_de_Prazins.txt   |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> A Brasileira de Prazins, de Camilo Castelo Branco
>
>Fonte:
>CASTELO BRANCO, Camilo.
> A brasileira de Prazins : cenas do Minho.

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      72347 |    3082    |       3894 |   ~  15.3 palavras | 2628       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  317 |      dizer | disseram; dizer; dizia; diria; diziam              |
|  265 |        ter | tem; têm; tinha; ter; tiver                        |
|  160 |      fazer | fazendo; faziam; feitos; fizeram; faz              |
|  155 |        dar | dadas; davam; der; daria; dá                       |
|  124 |      haver | havia; houve; haviam; havido; haver                |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Marta                   80 | Braga                  48 |
| Zeferino                52 | Cerveira               38 |
| Veríssimo               46 | Porto                  25 |
| José Dias               44 | Caldelas               19 |
| Deus                    34 | Póvoa de Lanhoso       12 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| INTRODUÇÃO           |            Caldelas ; Velhaca ; Bom            |
| I                    |            Caldelas ; Velhaca ; Bom            |
| II                   |         Caldelas ; Pernambuco ; Brasil         |
| III                  |      Santo Tirso ; Caldelas ; Pernambuco       |
| IV                   |         Cerveira ; Santo Tirso ; Porto         |
| V                    |         Cerveira ; Porto ; Santo Tirso         |
| VI                   |            Cerveira ; Braga ; Porto            |
| VII                  |            Cerveira ; Braga ; Porto            |
| VIII                 |            Cerveira ; Braga ; Porto            |
| IX                   |            Cerveira ; Braga ; Porto            |
| X                    |            Cerveira ; Braga ; Porto            |
| XI                   |            Braga ; Cerveira ; Porto            |
| XII                  |            Braga ; Cerveira ; Porto            |
| XIII                 |            Braga ; Cerveira ; Porto            |
| XIV                  |            Braga ; Cerveira ; Porto            |
| XV                   |            Braga ; Cerveira ; Porto            |
| XVI                  |            Braga ; Cerveira ; Porto            |
| XVII                 |            Braga ; Cerveira ; Porto            |
| XVIII                |            Braga ; Cerveira ; Porto            |
| XIX                  |            Braga ; Cerveira ; Porto            |
| XX                   |            Braga ; Cerveira ; Porto            |
| CONCLUSÃO            |            Braga ; Cerveira ; Porto            |



</details>

### A Gratidao
<details id="Camilo-A_Gratidao.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |        A Gratidao         | Camilo-A_Gratidao.txt                |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> Camilo Castelo Branco
> A Gratidão

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      17578 |    968     |       1016 |   ~  14.4 palavras | 554        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   80 |      dizer | disseram; dizer; dizia; diziam; diz                |
|   78 |        ter | tem; tinha; ter; tiver; tive                       |
|   73 |      fazer | fazendo; fazeres; faziam; fizeram; faz             |
|   60 |      poder | poderiam; pode; poder; pôde; posso                 |
|   45 |     querer | queres; quer; querendo; quis; queria               |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Rosa                   160 | Porto                   7 |
| D. Júlia                90 | S. Cosme                6 |
| D. Teresa               68 | serra de Valongo        4 |
| D. Berta                17 | S.                      3 |
| Deus                    16 | Candal                  3 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |        S. ; Dezembro ; serra de Valongo        |
| II                   |        S. ; Dezembro ; serra de Valongo        |
| III                  |        S. ; Dezembro ; serra de Valongo        |
| IV                   |        S. ; Dezembro ; serra de Valongo        |
| V                    |         S. ; serra de Valongo ; Porto          |
| VI                   |         S. ; serra de Valongo ; Porto          |
| VII                  |         S. ; serra de Valongo ; Porto          |
| VIII                 |         Porto ; S. ; serra de Valongo          |
| IX                   |         Porto ; S. ; serra de Valongo          |
| X                    |         Porto ; S. ; serra de Valongo          |
| XI                   |         Porto ; S. ; serra de Valongo          |
| XII                  |         Porto ; S. ; serra de Valongo          |
| XIII                 |         Porto ; S. ; serra de Valongo          |
| XIV                  |             Porto ; S. Cosme ; S.              |



</details>

### A Infanta Capelista
<details id="Camilo-A_Infanta_Capelista.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |    A Infanta Capelista    | Camilo-A_Infanta_Capelista.txt       |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> Camilo Castelo Branco
> A Infanta Capelista

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      27675 |    1703    |       1318 |   ~  18.2 palavras | 668        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   83 |      dizer | dirá; disseram; dizer; dizia; diria                |
|   79 |        ter | tem; têm; tinha; ter; tiver                        |
|   73 |      poder | poderiam; pode; podiam; poder; podem               |
|   63 |      saber | saibam; sabe; sabendo; sabia; saiba                |
|   61 |     querer | querer; quer; querendo; querem; quis               |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| V. Exª                  27 | Lisboa                 17 |
| D. Maria José           17 | Portugal                9 |
| Epifânio                15 | Rosenda                 6 |
| Vítor Hugo José Alves   14 | em Portugal             5 |
| Vítor                   14 | Rio de Janeiro          3 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |           Lisboa ; Portugal ; Minho            |
| II                   |           Lisboa ; Portugal ; Minho            |
| III                  |           Lisboa ; Portugal ; Minho            |
| IV                   |          Lisboa ; Portugal ; Rosenda           |
| V                    |          Lisboa ; Portugal ; Rosenda           |
| VI                   |          Lisboa ; Portugal ; Rosenda           |
| VII                  |          Lisboa ; Rosenda ; Portugal           |
| VIII                 |          Lisboa ; Portugal ; Rosenda           |
| IX                   |          Lisboa ; Portugal ; Rosenda           |
| X                    |          Lisboa ; Portugal ; Rosenda           |
| XI                   |          Lisboa ; Portugal ; Rosenda           |



</details>

### A Morgada de Romariz
<details id="Camilo-A_Morgada_de_Romariz.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |   A Morgada de Romariz    | Camilo-A_Morgada_de_Romariz.txt      |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> Camilo Castelo Branco
> A Morgada de Romariz
>    
>    
>     
>
>     
>     
>     A Francisco Teixeira de Queirós,
>     autor da Comédia do Campo, 
>     por Bento Moreno, 
>     saúda com superior admiração e indelével reconhecimento
>     
>     Camilo Castelo Branco
>     
>     
>
>     
>    I

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      14393 |    1029    |        888 |   ~  13.7 palavras | 484        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   61 |        ter | tem; têm; tinha; terei; ter                        |
|   61 |      dizer | disseram; dizer; dizia; diz; diziam                |
|   30 |        dar | daria; dá; dando; dado; deram                      |
|   29 |      fazer | fazendo; faziam; fizeram; faz; fazem               |
|   24 |     querer | queres; querer; quer; querendo; queremos           |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Joaquim                 26 | Barcelos                7 |
| Silvestre               19 | Braga                   6 |
| Bento                   12 | Famalicão               6 |
| Luís Meirinho           10 | Vermoim                 6 |
| Deus                     9 | Lisboa                  5 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |  Santo António ; Braga ; Teatro de S. Geraldo  |
| II                   |  Santo António ; Braga ; Teatro de S. Geraldo  |
| III                  | Lisboa ; Santo António ; Vila Nova de Famalicão |
| IV                   |      Lisboa ; Terra Negra ; Santo António      |
| V                    |      Lisboa ; Terra Negra ; Santo António      |
| VI                   |        Lisboa ; Terra Negra ; Meirinho         |
| VII                  |        Meirinho ; Lisboa ; Terra Negra         |
| VIII                 |        Vermoim ; Meirinho ; Terra Negra        |
| IX                   |        Vermoim ; Meirinho ; Terra Negra        |
| X                    |        Vermoim ; Meirinho ; Terra Negra        |
| XI                   |           Barcelos ; Vermoim ; Braga           |



</details>

### A enjeitada
<details id="Camilo-A_enjeitada.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |        A enjeitada        | Camilo-A_enjeitada.txt               |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> Camilo Castelo Branco
> A enjeitada

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      63880 |    3145    |       3716 |   ~  14.3 palavras | 1990       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  328 |      dizer | dirá; disseram; dizer; dizia; diria                |
|  220 |        ter | tem; têm; terei; tido; tiver                       |
|  165 |        ver | verem; via; verá; veria; viu                       |
|  154 |      saber | saberia; sabe; sabendo; sabia; saberem             |
|  144 |      poder | poderiam; pode; poderem; podiam; poderei           |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Flávia                 170 | Guimarães              27 |
| Ernesto                 83 | França                 24 |
| Carlota                 71 | Paris                  22 |
| Alfredo                 63 | Granadina              18 |
| Deus                    54 | Madrid                 15 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Capítulo I           | Guimarães ; Santa Maria de Pombeiro  Ó ; Portugal |
| Capítulo II          | Guimarães ; Santa Maria de Pombeiro  Ó ; Portugal |
| Capítulo III         |         Guimarães ; França ; Portugal          |
| Capítulo IV          |         Guimarães ; França ; Portugal          |
| Capítulo V           |         Guimarães ; França ; Portugal          |
| Capítulo VI          |         Guimarães ; França ; Portugal          |
| Capítulo VII         |         Guimarães ; França ; Portugal          |
| Capítulo VIII        |           Guimarães ; França ; Braga           |
| Capítulo IX          |           Guimarães ; França ; Braga           |
| Capítulo X           |           Guimarães ; França ; Braga           |
| Capítulo XI          |           Guimarães ; Braga ; França           |
| Capítulo XII         |         Granadina ; Guimarães ; Braga          |
| Capítulo XIII        |         Granadina ; Guimarães ; França         |
| Capítulo XIV         |         Granadina ; Guimarães ; França         |
| Capítulo XV          |         Granadina ; Guimarães ; França         |
| Capítulo XVI         |         Granadina ; Guimarães ; França         |
| Capítulo XVII        |         Granadina ; Guimarães ; França         |
| Capítulo XVIII       |         Granadina ; França ; Guimarães         |
| Capítulo XIX         |         Granadina ; França ; Guimarães         |
| Capítulo XX          |         Granadina ; França ; Guimarães         |
| Capítulo XXI         |         Granadina ; França ; Guimarães         |
| Capítulo XXII        |         Granadina ; França ; Guimarães         |
| Capítulo XXIII       |         Granadina ; França ; Guimarães         |
| Capítulo XXIV        |         Granadina ; França ; Guimarães         |
| Capítulo XXV         |         França ; Granadina ; Guimarães         |
| Capítulo XXVI        |           França ; Paris ; Granadina           |
| Capítulo XXVII       |           França ; Paris ; Guimarães           |
| Capítulo XXVIII      |           França ; Paris ; Guimarães           |
| Capítulo XXIX        |           França ; Guimarães ; Paris           |
| Capítulo XXX         |           França ; Guimarães ; Paris           |
| Conclusão            |           França ; Guimarães ; Paris           |



</details>

### A filha do Acerdiago
<details id="Camilo-A_filha_do_Acerdiago.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |   A filha do Acerdiago    | Camilo-A_filha_do_Acerdiago.txt      |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> Camilo Castelo Branco
> A filha do Arcedíago
>
>
> 
>
>
>Leitores!

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      93117 |    3586    |       5061 |   ~  15.2 palavras | 2769       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  536 |        ter | tem; têm; terei; tenham; tido                      |
|  427 |      dizer | dirá; disseram; dizer; dizia; diria                |
|  304 |     querer | quiseram; queres; querer; quer; querendo           |
|  281 |      saber | saberão; saberia; sabe; sabendo; sabemos           |
|  239 |      fazer | fazeres; feito; fazemos; fazem; feita              |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Rosa                   157 | Porto                  25 |
| Sr. António            105 | Rua das Flores         18 |
| Deus                    63 | Terra                  14 |
| Maria Elisa             49 | Paris                  14 |
| Maria                   41 | França                 13 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Capítulo I           |   Rua das Flores ; Barroso ; cidade do Porto   |
| Capítulo II          |    Rua das Flores ; Barroso ; Recolhimento     |
| Capítulo III         |    Rua das Flores ; Barroso ; Recolhimento     |
| Capítulo IV          |    Rua das Flores ; Recolhimento ; Barroso     |
| Capítulo V           |    Rua das Flores ; Recolhimento ; Barroso     |
| Capítulo VI          |     Recolhimento ; Rua das Flores ; Santo      |
| Capítulo VII         |     Recolhimento ; Rua das Flores ; Santo      |
| Capítulo VIII        |    Rua das Flores ; Recolhimento ; Barroso     |
| Capítulo IX          |    Rua das Flores ; Recolhimento ; Barroso     |
| Capítulo X           |    Rua das Flores ; Recolhimento ; Barroso     |
| Capítulo XI          |    Rua das Flores ; Recolhimento ; Barroso     |
| Capítulo XII         |    Rua das Flores ; Recolhimento ; Barroso     |
| Capítulo XIII        |    Recolhimento ; Rua das Flores ; Barroso     |
| Capítulo XIV         |    Recolhimento ; Rua das Flores ; Barroso     |
| Capítulo XV          |    Recolhimento ; Rua das Flores ; Barroso     |
| Capítulo XVI         |    Recolhimento ; Rua das Flores ; Barroso     |
| Capítulo XVII        |     Recolhimento ; Rua das Flores ; Porto      |
| Capítulo XVIII       |     Recolhimento ; Rua das Flores ; Porto      |
| Capítulo XIX         |     Recolhimento ; Rua das Flores ; Terra      |
| Capítulo XX          |     Recolhimento ; Rua das Flores ; Terra      |
| Capítulo XXI         |     Rua das Flores ; Recolhimento ; Porto      |
| Capítulo XXII        |     Rua das Flores ; Recolhimento ; Porto      |
| Capítulo XXIII       |     Rua das Flores ; Recolhimento ; Porto      |
| Capítulo XXIV        |     Rua das Flores ; Recolhimento ; Porto      |
| Capítulo XXV         |     Rua das Flores ; Recolhimento ; Porto      |
| Capítulo XXVI        |     Rua das Flores ; Porto ; Recolhimento      |
| Capítulo XXVII       |     Porto ; Rua das Flores ; Recolhimento      |
| Capítulo XXVIII      |     Porto ; Rua das Flores ; Recolhimento      |
| Capítulo XXIX        |     Porto ; Rua das Flores ; Recolhimento      |



</details>

### A filha do doutor negro
<details id="Camilo-A_filha_do_doutor_negro.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |  A filha do doutor negro  | Camilo-A_filha_do_doutor_negro.txt   |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> Camilo Castelo Branco
> A filha do doutor negro
>     
>    
>
>    Prefácio

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      71900 |    3358    |       4951 |   ~  12.1 palavras | 2296       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  312 |      dizer | dirá; disseram; dizer; dizia; diria                |
|  224 |        ter | tem; têm; tido; teria; tiver                       |
|  161 |      poder | poderiam; pode; poderei; pôde; posso               |
|  157 |      saber | saberia; sabe; sabido; sabendo; sabia              |
|  142 |      fazer | fazendo; faziam; feitos; fizeram; faz              |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| João Crisóstomo        159 | Porto                  47 |
| Albertina              146 | Brasil                 31 |
| António da Silveira    122 | Albertina              25 |
| João                    70 | Portugal               25 |
| Negro                   49 | Braga                  16 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Capítulo Primeiro    |          Porto ; Portugal ; Silveira           |
| Capítulo Segundo     |           Porto ; Portugal ; Brasil            |
| Capítulo Terceiro    |           Porto ; Portugal ; Brasil            |
| Capítulo Quarto      |           Brasil ; Porto ; Portugal            |
| Capítulo Quinto      |           Brasil ; Porto ; Portugal            |
| Capítulo Sexto       |           Brasil ; Porto ; Portugal            |
| Capítulo Sétimo      |           Brasil ; Porto ; Portugal            |
| Capítulo Oitavo      |             Brasil ; Porto ; Braga             |
| Capítulo Nono        |             Brasil ; Porto ; Braga             |
| Capítulo Décimo      |             Brasil ; Porto ; Braga             |
| Capítulo Décimo Primeiro |             Brasil ; Porto ; Braga             |
| Capítulo Décimo Segundo |             Brasil ; Porto ; Braga             |
| Capítulo Décimo Terceiro |             Porto ; Brasil ; Braga             |
| Capítulo Décimo Quarto |             Porto ; Brasil ; Braga             |
| Capítulo Décimo Quinto |             Porto ; Brasil ; Braga             |
| Capítulo Décimo Sexto |             Porto ; Brasil ; Braga             |
| Capítulo Décimo Sétimo |             Porto ; Brasil ; Braga             |
| Capítulo Décimo Oitavo |             Porto ; Brasil ; Braga             |
| Capítulo Décimo Nono |             Porto ; Brasil ; Braga             |
| Capítulo Vigésimo    |           Porto ; Brasil ; Portugal            |
| Capítulo Vigésimo Primeiro |           Porto ; Brasil ; Portugal            |
| Capítulo Vigésimo Segundo |           Porto ; Brasil ; Portugal            |
| Capítulo Vigésimo Terceiro |           Porto ; Brasil ; Portugal            |
| Capítulo Vigésimo Quarto |           Porto ; Brasil ; Portugal            |
| Conclusão            |           Porto ; Brasil ; Portugal            |



</details>

### A mulher fatal
<details id="Camilo-A_mulher_fatal.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |      A mulher fatal       | Camilo-A_mulher_fatal.txt            |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      53367 |    2975    |       4209 |   ~  10.5 palavras | 1577       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  207 |      dizer | disseram; dizer; dizia; diria; diziam              |
|  194 |        ter | tem; têm; teriam; tinha; ter                       |
|  144 |        ver | verem; via; veria; viu; viam                       |
|  138 |      saber | saberia; sabe; sabendo; sabemos; sabia             |
|   98 |      haver | haja; havia; haverá; haver; havemos                |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Carlos                 166 | Lisboa                 59 |
| Filomena                42 | Porto                  27 |
| Carlos Pereira          41 | Esteia                 23 |
| Deus                    26 | Virgínia               14 |
| Vossa Excelência        26 | Coimbra                14 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Introdução           |          Invernos ; Subir ; Ingleses           |
| Capítulo I           |  Porto ; Rua da Fábrica ; Colégio da Formiga   |
| Capítulo II          |  Porto ; Rua da Fábrica ; Colégio da Formiga   |
| Capítulo III         |  Porto ; Rua da Fábrica ; Colégio da Formiga   |
| Capítulo IV          |      Porto ; Virgínia ; Quinta das Açudes      |
| Capítulo V           |         Porto ; Virgínia ; Vaca Loura          |
| Capítulo VI          |           Porto ; Esteia ; Virgínia            |
| Capítulo VII         |           Esteia ; Porto ; Virgínia            |
| Capítulo VIII        |            Esteia ; Porto ; Lisboa             |
| Capítulo IX          |            Esteia ; Porto ; Lisboa             |
| Capítulo X           |            Lisboa ; Porto ; Esteia             |
| Capítulo XI          |            Lisboa ; Porto ; Esteia             |
| Conclusão            |            Lisboa ; Porto ; Esteia             |



</details>

### A neta do arcediago
<details id="Camilo-A_neta_do_arcediago.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |    A neta do arcediago    | Camilo-A_neta_do_arcediago.txt       |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Barnco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      68776 |    3105    |       4979 |   ~  11.3 palavras | 1981       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  283 |        ter | tem; têm; terei; tenham; tido                      |
|  214 |      dizer | disseram; dizer; dizia; diria; diziam              |
|  203 |      poder | poderiam; pode; podiam; poderei; poder             |
|  159 |      saber | saberia; sabe; sabes; sabendo; sabia               |
|  157 |      fazer | fazendo; faziam; fazerem; fizeram; faz             |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Luís da Cunha          232 | Mariana                50 |
| Açucena                144 | Lisboa                 33 |
| Luís                   122 | Portugal               22 |
| João da Cunha           80 | Brasil                 18 |
| Deus                    41 | Faro                   16 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Capítulo I           |            Lisboa ; Faro ; Coimbra             |
| Capítulo II          |            Lisboa ; Faro ; Coimbra             |
| Capítulo III         |            Lisboa ; Faro ; Coimbra             |
| Capítulo IV          |            Faro ; Lisboa ; Coimbra             |
| Capítulo V           |            Faro ; Lisboa ; Coimbra             |
| Capítulo VI          |            Faro ; Lisboa ; Coimbra             |
| Capítulo VII         |            Lisboa ; Faro ; Coimbra             |
| Capítulo VIII        |            Lisboa ; Faro ; Coimbra             |
| Capítulo IX          |          Lisboa ; Faro ; Campo Grande          |
| Capítulo X           |          Lisboa ; Faro ; Campo Grande          |
| Capítulo XI          |            Lisboa ; Faro ; Portugal            |
| Capítulo XII         |            Lisboa ; Portugal ; Faro            |
| Capítulo XIII        |            Lisboa ; Portugal ; Faro            |
| Capítulo XIV         |           Lisboa ; Portugal ; Brasil           |
| Capítulo XV          |           Lisboa ; Portugal ; Brasil           |
| Capítulo XVI         |           Lisboa ; Portugal ; Brasil           |
| Capítulo XVII        |           Lisboa ; Portugal ; Brasil           |
| Capítulo XVIII       |           Lisboa ; Portugal ; Brasil           |
| Capítulo XIX         |           Lisboa ; Portugal ; Brasil           |
| Conclusão            |           Lisboa ; Portugal ; Brasil           |



</details>

### A queda de um Anjo-Grafia actualizada
<details id="Camilo-A_queda_de_um_Anjo-Grafia_actualizada.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | A queda de um Anjo-Grafia actualizada | Camilo-A_queda_de_um_Anjo-Grafia_actualizada.txt |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> Camilo Castelo Branco
> A Queda de um Anjo

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      61240 |    2923    |       3879 |   ~  13.2 palavras | 2005       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  290 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  168 |        ter | tem; têm; tinha; terei; ter                        |
|  123 |      haver | haja; houve; houver; havendo; haviam               |
|  122 |     querer | queiram; querer; querermos; quer; queres           |
|  119 |      fazer | fazendo; faziam; fazerem; feitos; faz              |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| V. Exª                 102 | Lisboa                 69 |
| Calisto                 93 | Portugal               17 |
| Calisto Elói            84 | França                 14 |
| sr.                     41 | Miranda                13 |
| Teodora                 38 | Travanca               11 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |         Miranda ; Travanca ; Portugal          |
| II                   |         Miranda ; Portugal ; Travanca          |
| III                  |          Miranda ; Portugal ; Lisboa           |
| IV                   |          Lisboa ; Miranda ; Portugal           |
| V                    |          Lisboa ; Miranda ; Portugal           |
| VI                   |          Lisboa ; Miranda ; Portugal           |
| VII                  |          Lisboa ; Miranda ; Portugal           |
| VIII                 |          Lisboa ; Portugal ; Miranda           |
| IX                   |          Lisboa ; Portugal ; Miranda           |
| X                    |          Lisboa ; Portugal ; Miranda           |
| XI                   |          Lisboa ; Portugal ; Miranda           |
| XII                  |          Lisboa ; Portugal ; Miranda           |
| XIII                 |          Lisboa ; Portugal ; Miranda           |
| XIV                  |          Lisboa ; Portugal ; Miranda           |
| XV                   |          Lisboa ; Portugal ; Miranda           |
| XVI                  |          Lisboa ; Portugal ; Miranda           |
| XVII                 |          Lisboa ; Portugal ; Miranda           |
| XVIII                |          Lisboa ; Portugal ; Miranda           |
| XIX                  |          Lisboa ; Portugal ; Miranda           |
| XX                   |          Lisboa ; Portugal ; Miranda           |
| XXI                  |          Lisboa ; Portugal ; Miranda           |
| XXII                 |          Lisboa ; Portugal ; Miranda           |
| XXIII                |          Lisboa ; Portugal ; Miranda           |
| XXIV                 |           Lisboa ; Portugal ; França           |
| XXV                  |           Lisboa ; Portugal ; França           |
| XXVI                 |           Lisboa ; Portugal ; França           |
| XXVII                |           Lisboa ; Portugal ; França           |
| XXVIII               |           Lisboa ; Portugal ; França           |
| XXIX                 |           Lisboa ; Portugal ; França           |
| XXX                  |          Lisboa ; Portugal ; Miranda           |
| XXXI                 |          Lisboa ; Portugal ; Miranda           |
| XXXII                |          Lisboa ; Portugal ; Miranda           |
| XXXIII               |          Lisboa ; Portugal ; Miranda           |
| XXXIV                |          Lisboa ; Portugal ; Miranda           |
| XXXV                 |          Lisboa ; Portugal ; Miranda           |
| XXXVI                |           Lisboa ; Portugal ; França           |
| FIM                  |           Lisboa ; Portugal ; França           |



</details>

### A queda de um Anjo-Grafia da Epoca
<details id="Camilo-A_queda_de_um_Anjo-Grafia_da_Epoca.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | A queda de um Anjo-Grafia da Epoca | Camilo-A_queda_de_um_Anjo-Grafia_da_Epoca.txt |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      60966 |    3020    |       3938 |   ~  12.9 palavras | 2178       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  287 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  166 |        ter | tem; tinha; terei; ter; tiver                      |
|  118 |      fazer | fazendo; faziam; feitos; fazerem; faz              |
|  104 |     querer | queiram; querer; querermos; quer; queres           |
|  102 |      saber | saibam; sabe; sabia; sabem; soube                  |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Calisto Eloy            88 | Lisboa                 65 |
| Calisto                 87 | elle                   50 |
| sr.                     40 | Portugal               20 |
| Theodora                29 | Iphigenia              20 |
| D. Theodora             21 | França                 14 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| LIVRARIA DE CAMPOS JUNIOR- EDITOR |                                                |
| DEDICATORIA          |             Retia videtur tendere”             |
| I                    |         Miranda ; Travanca ; Portugal          |
| II                   |           Miranda ; Portugal ; elle            |
| III                  |          Miranda ; Portugal ; Lisboa           |
| IV                   |            Lisboa ; Miranda ; elle             |
| V                    |            Lisboa ; Miranda ; elle             |
| VI                   |            Lisboa ; Miranda ; elle             |
| VII                  |            Lisboa ; elle ; Miranda             |
| VIII                 |            Lisboa ; Portugal ; elle            |
| IX                   |            Lisboa ; Portugal ; elle            |
| X                    |            Lisboa ; Portugal ; elle            |
| XI                   |            Lisboa ; Portugal ; elle            |
| XII                  |            Lisboa ; Portugal ; elle            |
| XIII                 |            Lisboa ; Portugal ; elle            |
| XIV                  |            Lisboa ; elle ; Portugal            |
| XV                   |            Lisboa ; elle ; Portugal            |
| INJUSTIÇA!           |            Lisboa ; elle ; Portugal            |
| IMMORALIDADE!        |            Lisboa ; elle ; Portugal            |
| IMMUNDICIE!          |            Lisboa ; elle ; Portugal            |
| INSULTO!             |            Lisboa ; elle ; Portugal            |
| INFERNO!             |            Lisboa ; elle ; Portugal            |
| XVI                  |            Lisboa ; elle ; Portugal            |
| XVII                 |            Lisboa ; elle ; Portugal            |
| XVIII                |            Lisboa ; elle ; Portugal            |
| XIX                  |            Lisboa ; elle ; Portugal            |
| XX                   |            Lisboa ; elle ; Portugal            |
| XXI                  |            Lisboa ; elle ; Portugal            |
| XXII                 |            Lisboa ; elle ; Portugal            |
| XXIII                |            Lisboa ; elle ; Portugal            |
| XXIV                 |            Lisboa ; elle ; Portugal            |
| XXV                  |            Lisboa ; elle ; Portugal            |
| XXVI                 |            Lisboa ; elle ; Portugal            |
| XXVII                |            Lisboa ; elle ; Portugal            |
| XXVIII               |            Lisboa ; elle ; Portugal            |
| XXIX                 |            Lisboa ; elle ; Portugal            |
| XXX                  |            Lisboa ; elle ; Portugal            |
| XXXI                 |            Lisboa ; elle ; Portugal            |
| XXXII                |            Lisboa ; elle ; Portugal            |
| XXXIII               |            Lisboa ; elle ; Portugal            |
| XXXIV                |            Lisboa ; elle ; Portugal            |
| XXXV                 |            Lisboa ; elle ; Portugal            |
| XXXVI                |            Lisboa ; elle ; Portugal            |
| FIM                  |            Lisboa ; elle ; Portugal            |
| INDICE               |            Lisboa ; elle ; Portugal            |
| NOTAS                |            Lisboa ; elle ; Portugal            |



</details>

### A senhora Rattazzi
<details id="Camilo-A_senhora_Rattazzi.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |    A senhora Rattazzi     | Camilo-A_senhora_Rattazzi.txt        |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|       7835 |    511     |        442 |   ~  14.3 palavras | 374        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   32 |      dizer | dizer; dizia; diria; diz; dizemos                  |
|   27 |        ter | tem; tinha; ter; temos; tido                       |
|   18 |      fazer | feitos; fizeram; faz; fazem; fez                   |
|   10 |   escrever | escreve; escreveu; escrever; escrevendo            |
|   10 |     contar | contar; contou; conta                              |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Rattazzi                10 | Portugal               10 |
| Jorge                    5 | princeza                7 |
| Mendes Leal              4 | Coimbra                 5 |
| Campbell                 3 | Lisboa                  4 |
| Burnay                   3 | Inglaterra              4 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| A SENHORA RATTAZZI   |                                                |
| POR                  |                                                |
| CAMILLO CASTELLO BRANCO |                                                |
| NOVA EDIÇÃO          |                                                |
| MAIS INCORRECTA E AUGMENTADA |                                                |
| LIVRARIA INTERNACIONAL |                                                |
| DE                   |                                                |
| ERNESTO CHARDRON, EDITOR |                                                |
| PORTO E BRAGA        |           Portugal ; princeza ; elle           |



</details>

### A velhice do Padre Eterno-Estudo
<details id="Camilo-A_velhice_do_Padre_Eterno-Estudo.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | A velhice do Padre Eterno-Estudo | Camilo-A_velhice_do_Padre_Eterno-Estudo.txt |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> Camilo Castelo Branco
>     (Portugal, 1825-1890)
> A velhice do Padre Eterno
>     (Estudo)
>     
>     
>     Desde que o nervoso poeta iconoclasta Guerra Junqueiro atirou às ventanias tempestuosas da opinião pública vinte e oito sátiras com o rótulo de Velhice do Padre Eterno, as tais ventanias, irrompendo dos odres, começaram a rugir que o poeta é... ateu!

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|       1843 |    145     |        123 |   ~  12.5 palavras | 71         |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|    9 |      poder | pode; podemos; poderia; podendo; pudesse           |
|    5 |        ter | tem; tenho; temos; teve                            |
|    5 |      haver | havia; há; haver                                   |
|    5 |   escrever | escreve; escrevesse; escrever; escreveu            |
|    4 |      saber | sabem; sabe; sei                                   |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Deus                     8 | Via Láctea              2 |
| Voltaire                 4 | Sírio                   2 |
| Padre                    4 | Quereriam               1 |
| Guerra Junqueiro         2 | Havanesas               1 |
| Camilo Castelo Branco      (Portugal    1 | salubérrimas da Estupidez    1 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| DEO                  |                                                |
| EREXIT               |                                                |
| VOLTAIRE             | Havanesas ; salubérrimas da Estupidez ; Abade  |



</details>

### A viuva do enforcado
<details id="Camilo-A_viuva_do_enforcado.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |   A viuva do enforcado    | Camilo-A_viuva_do_enforcado.txt      |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      43393 |    2257    |       2671 |   ~  13.8 palavras | 1420       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  209 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  162 |        ter | tem; têm; terei; tenham; teria                     |
|  123 |      fazer | fazendo; faziam; fazerem; feitos; faz              |
|  119 |     querer | queres; querer; quer; querendo; querem             |
|   90 |         ir | ido; ir; vá; iremos; vamos                         |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Teresa                 100 | Guimarães              29 |
| Guilherme               60 | Espanha                19 |
| Teresa de Jesus         46 | Portugal               16 |
| Joaquim Pereira         34 | Porto                  14 |
| Deus                    29 | Ronfe                  11 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]


##### Capítulos não encontrados.



</details>

### Agostinho de Ceuta-Teatro
<details id="Camilo-Agostinho_de_Ceuta-Teatro.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | Agostinho de Ceuta-Teatro | Camilo-Agostinho_de_Ceuta-Teatro.txt |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Agostinho de Ceuta

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      21362 |    1072    |       1878 |   ~   8.6 palavras | 789        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   47 |        ter | tem; tinha; terei; temos; tive                     |
|   39 |      haver | havia; havemos; haverão; há                        |
|   30 |       amar | ama; amava; amou; amado; amo                       |
|   28 |        ver | via; viu; vê; vi; verei                            |
|   28 |      saber | sabe; saberão; sei; saber                          |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| D. Manuel               21 | Portugal                9 |
| D. Leonor               16 | hei-de                  3 |
| D. Manuel de Melo       15 | Duque do Cadaval        2 |
| D. Leonor               15 | Hei-de                  2 |
| Afonso VI               14 | castelo de Évora        2 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| FIM                  |  http://groups.google.com/group/digitalsource  |



</details>

### Amor de Perdicao
<details id="Camilo-Amor_de_Perdicao.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |     Amor de Perdicao      | Camilo-Amor_de_Perdicao.txt          |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> Amor de Perdição
>de Camilo Castelo Branco
>
>(Memórias Duma Família)
> Ao
>Ilmo.

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      62716 |    2625    |       4298 |   ~  11.6 palavras | 1648       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  390 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  296 |        ter | tem; têm; tenham; tido; teria                      |
|  165 |      saber | sabe; saberei; sabendo; sabia; saiba               |
|  152 |         ir | iria; ido; for; foram; vá                          |
|  142 |      haver | haja; houve; houver; haviam; haverá                |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Simão                  168 | Mariana                78 |
| Teresa                 151 | Viseu                  54 |
| João da Cruz            53 | Coimbra                35 |
| Simão Botelho           50 | Porto                  29 |
| Baltasar                45 | Lisboa                 23 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| INTRODUÇÃO           | Relação do Porto ; Universidade de Coimbra ; cidade de Lisboa |
| CAPÍTULO I           |            Lisboa ; Viseu ; Coimbra            |
| CAPÍTULO II          |            Coimbra ; Viseu ; Lisboa            |
| CAPÍTULO III         |            Coimbra ; Viseu ; Lisboa            |
| CAPÍTULO IV          |            Viseu ; Coimbra ; Lisboa            |
| CAPÍTULO V           |            Viseu ; Coimbra ; Lisboa            |
| CAPÍTULO VI          |            Viseu ; Coimbra ; Lisboa            |
| CAPÍTULO VII         |            Viseu ; Coimbra ; Lisboa            |
| CAPÍTULO VIII        |            Viseu ; Coimbra ; Lisboa            |
| CAPÍTULO IX          |            Viseu ; Coimbra ; Lisboa            |
| CAPÍTULO X           |            Coimbra ; Viseu ; Lisboa            |
| CAPÍTULO XI          |            Coimbra ; Viseu ; Lisboa            |
| CAPÍTULO XII         |            Viseu ; Coimbra ; Lisboa            |
| CAPÍTULO XIII        |            Viseu ; Coimbra ; Lisboa            |
| CAPÍTULO XIV         |            Viseu ; Coimbra ; Porto             |
| CAPÍTULO XV          |            Viseu ; Coimbra ; Porto             |
| CAPÍTULO XVI         |            Viseu ; Coimbra ; Porto             |
| CAPÍTULO XVII        |            Viseu ; Coimbra ; Porto             |
| CAPÍTULO XVIII       |            Viseu ; Coimbra ; Porto             |
| CAPÍTULO XIX         |            Viseu ; Coimbra ; Porto             |
| CONCLUSÃO            |            Viseu ; Coimbra ; Porto             |
| FIM                  |            Viseu ; Coimbra ; Porto             |



</details>

### Amor de Salvacao
<details id="Camilo-Amor_de_Salvacao.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |     Amor de Salvacao      | Camilo-Amor_de_Salvacao.txt          |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Amor de Salvação

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      59957 |    3258    |       3690 |   ~  13.7 palavras | 1736       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  232 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  158 |        ter | tem; têm; tinha; terei; ter                        |
|  132 |        ver | verem; via; verá; vinham; viu                      |
|  124 |      saber | sabe; sabendo; sabemos; saberem; sabia             |
|  107 |        dar | darem; dadas; davam; daria; dá                     |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Afonso                 200 | Palmira                49 |
| Teodora                 97 | Lisboa                 45 |
| Afonso de Teive         69 | Braga                  21 |
| Deus                    50 | Paris                  21 |
| Eleutério               31 | Ruivães                20 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |            Minho ; Porto ; Coimbra             |
| II                   |             Minho ; Porto ; Lisboa             |
| III                  |             Minho ; Lisboa ; Porto             |
| IV                   |             Minho ; Lisboa ; Porto             |
| V                    |             Braga ; Minho ; Lisboa             |
| VI                   |             Braga ; Lisboa ; Minho             |
| VII                  |            Lisboa ; Braga ; Ruivães            |
| VIII                 |            Lisboa ; Braga ; Ruivães            |
| IX                   |            Lisboa ; Braga ; Ruivães            |
| X                    |            Lisboa ; Braga ; Coimbra            |
| XI                   |            Lisboa ; Braga ; Coimbra            |
| XII                  |            Lisboa ; Braga ; Ruivães            |
| XIII                 |            Lisboa ; Braga ; Ruivães            |
| XIV                  |            Lisboa ; Braga ; Ruivães            |
| XV                   |            Lisboa ; Braga ; Ruivães            |
| XVI                  |            Lisboa ; Braga ; Palmira            |
| XVII                 |            Lisboa ; Palmira ; Braga            |
| XVIII                |            Palmira ; Lisboa ; Braga            |
| XIX                  |            Palmira ; Lisboa ; Braga            |
| XX                   |            Palmira ; Lisboa ; Braga            |
| XXI                  |            Palmira ; Lisboa ; Braga            |
| XXII                 |            Palmira ; Lisboa ; Braga            |
| XXIII                |            Palmira ; Lisboa ; Paris            |
| ??                   |            Palmira ; Lisboa ; Paris            |
| ??                   |            Palmira ; Lisboa ; Paris            |
| ??                   |            Palmira ; Lisboa ; Paris            |
| ??                   |            Palmira ; Lisboa ; Paris            |
| 1                    |            Palmira ; Lisboa ; Paris            |



</details>

### Anatema 1
<details id="Camilo-Anatema_1.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |         Anatema 1         | Camilo-Anatema_1.txt                 |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      18988 |    1083    |       1142 |   ~  13.9 palavras | 524        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   71 |        ter | tem; tinha; ter; temos; terá                       |
|   64 |      dizer | dirá; dizer; dizia; diz; diziam                    |
|   38 |      poder | poderiam; pode; poder; pôde; podem                 |
|   35 |      saber | sabe; sabemos; sabia; sabem; sei                   |
|   30 |      haver | haja; havia; houve; haviam; haverá                 |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Cristóvão da Veiga      20 | Távora                 14 |
| conde de São Vicente    16 | Vila Real               7 |
| Micaela                 15 | Timóteo de Oliveira     7 |
| Dona Inês               13 | Timóteo                 4 |
| Dona Inês da Veiga      12 | Guimarães               3 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Introdução           |                                                |
| Capítulo I - No qual se prova que o autor não tem jeito para escrever romances |                                                |
| Capítulo II - Onde o mestre sapateiro João Rodrigues Cambado aparece a conversar com sua mulher, Jacinta Rosa, e do mais que a seu respeito se disser |                                                |
| Capítulo III - Quem era a cozinheira destes fidalgos, que ditos ficam, e de outras coisas muito para se lerem, e menos para se imitarem. |                                                |
| Capítulo IV - No qual se tratam coisas muito tristes |                                                |
| Capítulo V - Vários sucessos a respeito da fidalguia destes reinos |                                                |
| Capítulo VI - Em que o autor diz o que pensa a respeito das mulheres; pedindo vénia para ousadia tamanha... |                                                |
| Capítulo VII - Que é necessário ler-se para entender o que vier depois. O autor esquece-se do romance algumas vezes |                                                |
| Capítulo VIII - No qual o autor teve pretensões a estilo sublime. De como as más-línguas só dizem às vezes metade do que é. Vê-se que as mulheres pouco adiantaram em civilização e romanticismo desde 1701. E de outras coisas dignas de se lerem a muitos respeitos |                                                |
| Capítulo IX - Metade do qual é para metade dos leitores, e a outra metade para todos |                                                |
| Capítulo X - Prova-se que o reumatismo e o amor são incompativeis. Prova-se que honra e cem mil réis, afora o arrendamento de uns moinhos, também são incompatíveis. De como é preciso abolir estes argumentos jocosos, quando se tratam assuntos sérios. Dizem-se coisas pie dosas de se ouvirem |                                                |
| Capítulo XI - De como ninguém sabe para o que nasceu. Diz-se como a salvação de um cavalo depende de um triângulo. Espirito das matemáticas nos irracionais, e outras coisas tristes. De como Cristóvão da Veiga era um trabuco. Franquezas de uma criada de servir, e outras coisas não menos Maravilhosas |                                                |
| Capítulo XII - Em que o autor tem a honra de apresentar a Sr.a Joaquina da Luz, e pede que a tenham na devida consideração, como do capitulo melhor se verá |                                                |
| Capítulo XIII - Grande capítulo, em que a Sr.a Joaquina da Luz suspeita que o Diabo se metesse no corpo de Dona Inês da Veiga, e as dúvidas do sapateiro a esse respeito. Vê-se o que é um fidalgo se lhe tocam na família, e o que seria dele se por grande vilta nascesse plebeu. Salto prodigioso que o autor dá para trás, e convence-se o leitor que seria pior saltar para diante |                                                |
| Capítulo XIV - Dizem-se coisas interessantes, como por exemplo o encontro de Pedro da Veiga com três falansterianos intempestivos, e outras muitas coisas que não se dizem aqui por causa da surpresa |                                                |
| Capítulo XV - Os mistérios do castelo de Dona Chama, e os de um abade misteriosíssimo |                                                |
| Capítulo XVI - Em que o padre Carlos da Silva inquestionavelmente narra a famosa história, não sabemos por ora de quem, mas com a ajuda de Deus a mais inteligível de todas as histórias. Obra de muita moral e edificação. Temos a anunciar interrupções, que nos não deixam gozar estes contos do princípio ao fim, com aquela fleuma lógica e imperturbável de uma novela inglesa |                                                |
| Capítulo XVII  - O editor destas coisas dá a sua palavra de romancista em como a história do padre Carlos da Silva não será interrompida |                                                |
| Capítulo XVIII - Contam-se passagens que só o Demónio era capaz de adivinhar! |                                                |
| Capítulo XIX - Grande maçada! |                                                |
| Capítulo XX - Vê-se que o editor desta verdadeira história não quis desfalcar a ordem do manuscrito, e por isso deu aqui remate ao lamentoso diário de Antónia Bacelar |                                                |
| Capítulo XXI - Vê-se que o duelo foi sempre uma caricatura em Portugal, e há-de sê-lo sempre enquanto a dor física for mais pungente que a moral. E mais se diz que mestre António sapateiro foi o único que lucrou vinte cruzados nestas águas turvas de tão infaustos |                                                |
| Capítulo XXII - De como mestre António era um refinadíssimo agiota, e destarte cumpre a promessa que nos fizera de fazer-se ladrão. Imaginações que conspiram na cabeça do padre, e levam por diante aquela bernarda moral, à custa de ferro e fogo |                                                |
| Capítulo XXIII - O padre assenta a primeira bateria. Vê-se o que são as vinganças nos caracteres perversos. Antiguidade das cartas anónimas. De como uma tulha é o melhor valhacouto contra corregedores e meirinhos. Descobrem-se três familiares do Santo Ofício, que por força ou por jeito deviam entrar no romance |                                                |
| Capítulo XXIV - Traição e vingança |                                                |
| Capítulo XXV - Que vale a pena de ler-se por ser o último, e por encerrar a acção de mais de meio século, coisa por certo nova e admirável, não só pelo muito que se diz, mas pelo muito mais que se poderia dizer, se o autor quisesse escrever o seu romance em quatro volumes |                                                |
| Introdução           |     Torquate ; Torcato ; Torcato Tasso...      |
| Capítulo I           |     Torquate ; Torcato ; Torcato Tasso...      |
| Capítulo II          |         Vila Real ; Torquate ; Torcato         |
| Capítulo III         |   Timóteo de Oliveira ; Timóteo ; Vila Real    |
| Capítulo IV          |   Timóteo de Oliveira ; Timóteo ; Guimarães    |
| Capítulo V           |   Timóteo de Oliveira ; Vila Real ; Timóteo    |
| Capítulo VI          |    Távora ; Timóteo de Oliveira ; Vila Real    |
| Capítulo VII         |    Távora ; Timóteo de Oliveira ; Vila Real    |
| Capítulo VIII        |    Távora ; Timóteo de Oliveira ; Vila Real    |



</details>

### Aventuras de Basilio Fernandes
<details id="Camilo-Aventuras_de_Basilio_Fernandes.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | Aventuras de Basilio Fernandes | Camilo-Aventuras_de_Basilio_Fernandes.txt |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>Aventuras de 
>Basílio Fernandes Enxertado
>     
>http://groups.google.com/group/digitalsource

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      54860 |    2611    |       3897 |   ~  11.4 palavras | 1780       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  245 |      dizer | dirá; disseram; dizer; dizia; diria                |
|  193 |        ter | tem; têm; tinha; ter; tiver                        |
|  155 |        dar | darem; dadas; davam; darei; der                    |
|  129 |      fazer | fazendo; faziam; feitos; fizeram; faz              |
|  121 |     querer | quiseram; querer; queres; quer; querendo           |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Basílio                236 | Porto                  52 |
| Etelvina               156 | Lisboa                 44 |
| Henrique                77 | Ervedosa               14 |
| José Fernandes          50 | Paris                  12 |
| Henrique Pestana        36 | Enxertado               9 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Capítulo I           |     Senhora Bonifácia ; Porto ; Enxertado      |
| Capítulo II          |     Senhora Bonifácia ; Porto ; Enxertado      |
| Capítulo III         |           Porto ; Ervedosa ; Valbom            |
| Capítulo IV          |      Porto ; Ervedosa ; Senhora Bonifácia      |
| Capítulo V           |      Porto ; Ervedosa ; Senhora Bonifácia      |
| Capítulo VI          |      Porto ; Ervedosa ; Senhora Bonifácia      |
| Capítulo VII         |      Porto ; Ervedosa ; Senhora Bonifácia      |
| Capítulo VIII        |           Porto ; Lisboa ; Ervedosa            |
| Capítulo IX          |           Lisboa ; Porto ; Ervedosa            |
| Capítulo X           |           Lisboa ; Porto ; Ervedosa            |
| Capítulo XI          |           Lisboa ; Porto ; Ervedosa            |
| Capítulo XII         |           Lisboa ; Porto ; Ervedosa            |
| Capítulo XIII        |           Lisboa ; Porto ; Ervedosa            |
| Capítulo XIV         |           Lisboa ; Porto ; Ervedosa            |
| Capítulo XV          |           Lisboa ; Porto ; Ervedosa            |
| Capítulo XVI         |           Lisboa ; Porto ; Ervedosa            |
| Capítulo XVII        |           Lisboa ; Porto ; Ervedosa            |
| Capítulo XVIII       |           Lisboa ; Porto ; Ervedosa            |
| Capítulo XIX         |           Porto ; Lisboa ; Ervedosa            |
| Capítulo XX          |           Porto ; Lisboa ; Ervedosa            |
| Capítulo XXI         |           Porto ; Lisboa ; Ervedosa            |
| Capítulo XXII        |           Porto ; Lisboa ; Ervedosa            |
| Capítulo XXIII       |           Porto ; Lisboa ; Ervedosa            |
| Conclusão            |           Porto ; Lisboa ; Ervedosa            |



</details>

### Carlota Angela
<details id="Camilo-Carlota_Angela.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |      Carlota Angela       | Camilo-Carlota_Angela.txt            |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Carlota Ângela
>
>     
>    Capítulo I

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      58237 |    2815    |       3563 |   ~  13.6 palavras | 1730       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  226 |      dizer | dirá; disseram; dizer; dizia; diria                |
|  159 |      fazer | feitos; feito; fazem; feita; fazerem               |
|  157 |        ter | tem; têm; teria; teremos; tiver                    |
|  145 |      poder | poderiam; pode; podiam; poderei; poder             |
|  120 |     querer | querer; querermos; quer; queres; querendo          |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Carlota                160 | Lisboa                 32 |
| Deus                    66 | Porto                  32 |
| Mendonça                44 | Portugal               17 |
| Carlota Ângela          40 | Brasil                 14 |
| D. Rosália              37 | Reino                  11 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Capítulo I           |        Noutro ; Lisboa ; Rua das Taipas        |
| Capítulo II          |        Lisboa ; Noutro ; Rua das Taipas        |
| Capítulo III         |            Lisboa ; Porto ; Manique            |
| Capítulo IV          |            Lisboa ; Porto ; Manique            |
| Capítulo V           |            Lisboa ; Porto ; Manique            |
| Capítulo VI          |            Lisboa ; Porto ; Brasil             |
| Capítulo VII         |            Lisboa ; Porto ; Brasil             |
| Capítulo VIII        |            Lisboa ; Porto ; Brasil             |
| Capítulo IX          |           Lisboa ; Porto ; Portugal            |
| Capítulo X           |           Lisboa ; Porto ; Portugal            |
| Capítulo XI          |           Lisboa ; Porto ; Portugal            |
| Capítulo XII         |           Lisboa ; Porto ; Portugal            |
| Capítulo XIII        |           Lisboa ; Porto ; Portugal            |
| Capítulo XIV         |           Lisboa ; Porto ; Portugal            |
| Capítulo XV          |           Lisboa ; Porto ; Portugal            |
| Capítulo XVI         |           Lisboa ; Porto ; Portugal            |
| Capítulo XVII        |           Lisboa ; Porto ; Portugal            |
| Capítulo XVIII       |           Lisboa ; Porto ; Portugal            |
| Capítulo XIX         |           Lisboa ; Porto ; Portugal            |
| Conclusão            |           Lisboa ; Porto ; Portugal            |



</details>

### Cenas da Foz
<details id="Camilo-Cenas_da_Foz.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |       Cenas da Foz        | Camilo-Cenas_da_Foz.txt              |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      63160 |    2989    |       4065 |   ~  12.9 palavras | 1673       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  283 |      dizer | dirá; disseram; dizer; dizia; diria                |
|  221 |        ter | tem; têm; terei; teria; teremos                    |
|  165 |      saber | saberão; sabe; sabendo; sabia; saiba               |
|  165 |      fazer | fazendo; faziam; feitos; fizeram; faz              |
|  156 |      poder | poderiam; pode; podiam; poderei; pôde              |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Leocádia               112 | Amarante               15 |
| Vasco                   47 | Lua                    13 |
| Deus                    39 | Foz                    12 |
| Bento de Castro         29 | Lisboa                 11 |
| Francisco de Proença    28 | Porto                  10 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Capítulo I           |      Amarante ; Cabeceiras de Basto ; Foz      |
| Capítulo II          |      Amarante ; Cabeceiras de Basto ; Foz      |
| Capítulo III         |      Céu ; Amarante ; Cabeceiras de Basto      |
| Capítulo IV          |      Céu ; Amarante ; Cabeceiras de Basto      |
| Capítulo V           |             Porto ; Céu ; Amarante             |
| Capítulo VI          |               Porto ; Céu ; Foz                |
| Capítulo VII         |               Porto ; Céu ; Foz                |
| Capítulo VIII        |               Porto ; Foz ; Céu                |
| Capítulo IX          |             Vicência ; Lua ; Porto             |
| Capítulo X           |              Vicência ; Lua ; Foz              |
| Capítulo XI          |              Vicência ; Lua ; Foz              |
| Capítulo XII         |              Vicência ; Lua ; Foz              |
| Capítulo XIII        |           Vicência ; Amarante ; Lua            |
| Capítulo XIV         |           Vicência ; Amarante ; Lua            |
| Capítulo XV          |           Lua ; Vicência ; Amarante            |
| Capítulo XVI         |           Lua ; Vicência ; Amarante            |
| Capítulo XVII        |           Amarante ; Lua ; Vicência            |
| Capítulo XVIII       |           Amarante ; Lua ; Vicência            |
| Capítulo XIX         |           Amarante ; Lua ; Vicência            |
| Capítulo XX          |           Amarante ; Lua ; Vicência            |
| Capítulo I           |              Amarante ; Lua ; Foz              |
| Capítulo II          |              Amarante ; Lua ; Foz              |
| Capítulo III         |              Amarante ; Lua ; Foz              |
| Capítulo IV          |              Amarante ; Lua ; Foz              |
| Capítulo V           |              Amarante ; Lua ; Foz              |
| Capítulo VI          |              Amarante ; Lua ; Foz              |
| Capítulo VII         |              Amarante ; Lua ; Foz              |
| Capítulo VIII        |              Amarante ; Lua ; Foz              |
| Capítulo IX          |              Amarante ; Lua ; Foz              |
| Capítulo X           |              Amarante ; Lua ; Foz              |
| Capítulo XI          |              Amarante ; Lua ; Foz              |
| Capítulo XII         |              Amarante ; Lua ; Foz              |
| Capítulo XIII        |              Amarante ; Lua ; Foz              |
| Capítulo XIV         |              Amarante ; Lua ; Foz              |
| Capítulo XV          |              Amarante ; Lua ; Foz              |
| Capítulo XVI         |              Amarante ; Lua ; Foz              |
| Capítulo XVII        |              Amarante ; Lua ; Foz              |
| Capítulo XVIII       |              Amarante ; Lua ; Foz              |
| Capítulo XIX         |              Amarante ; Lua ; Foz              |



</details>

### Coisas que so eu sei
<details id="Camilo-Coisas_que_so_eu_sei.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |   Coisas que so eu sei    | Camilo-Coisas_que_so_eu_sei.txt      |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      16723 |    1067    |       1204 |   ~  11.4 palavras | 371        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   51 |      saber | sabe; sabia; saberá; souber; sei                   |
|   49 |      poder | poderiam; pode; poder; pôde; posso                 |
|   37 |        ter | tem; tinha; ter; tive; terá                        |
|   35 |      fazer | faziam; fizeram; faz; feito; faria                 |
|   33 |      dizer | dizer; dizia; diz; digo; disse                     |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Carlos                  42 | Lisboa                 12 |
| Laura                   23 | Londres                 8 |
| Vasco                   14 | Henriqueta              7 |
| Vasco de Seabra         12 | Porto                   4 |
| Elisa                    7 | Hás-de                  3 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    | Porto ; Teatro de S. João ; Olha do qu’isso!... |
| II                   | Porto ; Teatro de S. João ; Olha do qu’isso!... |
| III                  |      Porto ; Londres ; Teatro de S. João       |
| IV                   |      Porto ; Londres ; Teatro de S. João       |
| V                    |            Porto ; Lisboa ; Londres            |
| VI                   |            Lisboa ; Londres ; Porto            |
| VII                  |            Lisboa ; Londres ; Porto            |
| VIII                 |            Lisboa ; Londres ; Porto            |
| IX                   |            Lisboa ; Londres ; Porto            |
| X                    |         Lisboa ; Londres ; Henriqueta          |
| FIM                  |         Lisboa ; Londres ; Henriqueta          |



</details>

### Coracao cabeca e estomago
<details id="Camilo-Coracao_cabeca_e_estomago.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | Coracao cabeca e estomago | Camilo-Coracao_cabeca_e_estomago.txt |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Coração, cabeça e estômago

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      55666 |    2953    |       3675 |   ~  12.7 palavras | 1295       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  232 |        ter | tem; têm; tinha; ter; tiver                        |
|  205 |      dizer | disseram; dizer; dizia; diz; diziam                |
|  131 |        ver | verem; via; verá; viam; vê                         |
|  129 |      fazer | fazendo; faziam; feitos; fizeram; faz              |
|  116 |        dar | der; dava; dar; dada; dei                          |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Tomásia                 36 | Porto                  28 |
| Silvestre               23 | Lisboa                 27 |
| Paula                   20 | Lua                     8 |
| Deus                    18 | Brasil                  7 |
| Augusto                 15 | Paris                   7 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |      Lisboa ; Grilo ; Teatro de S. Carlos      |
| II                   |      Lisboa ; Grilo ; Teatro de S. Carlos      |
| III                  |         Lisboa ; Porto Brandão ; Grilo         |
| IV                   |        Lisboa ; Porto Brandão ; Brasil         |
| V                    |         Lisboa ; Paris ; Porto Brandão         |
| I                    |         Lisboa ; Paris ; Porto Brandão         |
| II                   |         Lisboa ; Paris ; Porto Brandão         |
| III                  |         Lisboa ; Paris ; Porto Brandão         |
| IV                   |         Lisboa ; Paris ; Porto Brandão         |
| V                    |         Lisboa ; Paris ; Porto Brandão         |
| VI                   |         Lisboa ; Paris ; Porto Brandão         |
| VII                  |           Lisboa ; Paris ; Santarém            |
| VIII                 |           Lisboa ; Paris ; Santarém            |
| I                    |           Lisboa ; Paris ; Santarém            |
| II                   |           Lisboa ; Paris ; Santarém            |
| III                  |           Lisboa ; Paris ; Santarém            |
| IV                   |           Lisboa ; Paris ; Santarém            |
| V                    |           Lisboa ; Paris ; Santarém            |
| VI                   |           Lisboa ; Paris ; Santarém            |
| VII                  |           Lisboa ; Paris ; Santarém            |
| VIII                 |           Lisboa ; Paris ; Santarém            |
| IX                   |           Lisboa ; Paris ; Santarém            |
| I                    |           Lisboa ; Paris ; Santarém            |
| II                   |             Lisboa ; Porto ; Paris             |
| III                  |             Lisboa ; Porto ; Paris             |
| I                    |             Lisboa ; Porto ; Paris             |
| II                   |             Lisboa ; Porto ; Paris             |
| III                  |             Lisboa ; Porto ; Paris             |
| IV                   |             Lisboa ; Porto ; Paris             |
| V                    |             Lisboa ; Porto ; Paris             |
| VI                   |             Lisboa ; Porto ; Paris             |
| VII                  |             Lisboa ; Porto ; Paris             |
| I                    |             Lisboa ; Porto ; Paris             |
| II                   |             Lisboa ; Porto ; Paris             |
| III                  |             Lisboa ; Porto ; Paris             |
| IV                   |             Lisboa ; Porto ; Paris             |
| V                    |             Lisboa ; Porto ; Paris             |
| VI                   |              Lisboa ; Porto ; Lua              |
| VII                  |              Lisboa ; Porto ; Lua              |
| VIII                 |              Lisboa ; Porto ; Lua              |
| IX                   |              Lisboa ; Porto ; Lua              |
| X                    |              Lisboa ; Porto ; Lua              |



</details>

### Doze casamentos felizes
<details id="Camilo-Doze_casamentos_felizes.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |  Doze casamentos felizes  | Camilo-Doze_casamentos_felizes.txt   |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      56716 |    2762    |       3552 |   ~  13.4 palavras | 1844       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  281 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  193 |        ter | tem; têm; tinha; terei; ter                        |
|  119 |      poder | poderiam; pode; podiam; pôde; posso                |
|  117 |      saber | sabe; sabendo; sabia; saberem; saiba               |
|  112 |      haver | haja; havia; houve; haviam; havemos                |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Inês                    38 | Lisboa                 34 |
| Deus                    35 | Porto                  24 |
| Júlio                   28 | Vila Real              14 |
| Francisco da Cunha      27 | Minho                  11 |
| Maria                   23 | Carolina               11 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |             Patmos ; Terra ; Nilo              |
| II                   |             Porto ; Patmos ; Terra             |
| III                  |             Lisboa ; Porto ; Paris             |
| IV                   |             Lisboa ; Porto ; Paris             |
| V                    |             Lisboa ; Porto ; Paris             |
| I                    |             Lisboa ; Porto ; Paris             |
| II                   |           Lisboa ; Porto ; Guimarães           |
| III                  |           Lisboa ; Guimarães ; Porto           |
| I                    |           Lisboa ; Guimarães ; Porto           |
| II                   |           Lisboa ; Guimarães ; Porto           |
| III                  |           Lisboa ; Guimarães ; Porto           |
| I                    |           Lisboa ; Guimarães ; Porto           |
| II                   |           Lisboa ; Guimarães ; Porto           |
| III                  |           Lisboa ; Guimarães ; Porto           |
| IV                   |           Lisboa ; Guimarães ; Porto           |
| V                    |           Lisboa ; Guimarães ; Porto           |
| VI                   |         Lisboa ; Vila Real ; Guimarães         |
| VII                  |         Lisboa ; Vila Real ; Guimarães         |
| VIII                 |           Lisboa ; Vila Real ; Braga           |
| I                    |           Lisboa ; Vila Real ; Braga           |
| II                   |           Lisboa ; Vila Real ; Braga           |
| III                  |           Lisboa ; Vila Real ; Braga           |
| IV                   |           Lisboa ; Vila Real ; Braga           |
| I                    |           Lisboa ; Vila Real ; Braga           |
|                      |           Lisboa ; Vila Real ; Braga           |
| II                   |           Lisboa ; Vila Real ; Braga           |
| III                  |           Lisboa ; Vila Real ; Braga           |
| IV                   |           Lisboa ; Vila Real ; Braga           |
| V                    |           Lisboa ; Vila Real ; Porto           |
| I                    |           Lisboa ; Vila Real ; Porto           |
| II                   |           Lisboa ; Vila Real ; Porto           |
| III                  |           Lisboa ; Vila Real ; Porto           |
| IV                   |           Lisboa ; Vila Real ; Porto           |
| I                    |           Lisboa ; Vila Real ; Porto           |
| II                   |           Lisboa ; Vila Real ; Porto           |
| III                  |           Lisboa ; Vila Real ; Porto           |
| IV                   |           Lisboa ; Vila Real ; Porto           |
| I                    |           Lisboa ; Vila Real ; Porto           |
| II                   |           Lisboa ; Vila Real ; Porto           |
| III                  |           Lisboa ; Vila Real ; Porto           |
| IV                   |           Lisboa ; Vila Real ; Porto           |
| I                    |           Lisboa ; Porto ; Vila Real           |
| II                   |           Lisboa ; Porto ; Vila Real           |
| III                  |           Lisboa ; Porto ; Vila Real           |
| IV                   |           Lisboa ; Porto ; Vila Real           |
| V                    |           Lisboa ; Porto ; Vila Real           |
| I                    |           Lisboa ; Porto ; Vila Real           |
| I                    |           Lisboa ; Porto ; Vila Real           |
| II                   |           Lisboa ; Porto ; Vila Real           |
| III                  |           Lisboa ; Porto ; Vila Real           |
| IV                   |           Lisboa ; Porto ; Vila Real           |
| V                    |           Lisboa ; Porto ; Vila Real           |



</details>

### Duas Horas de Leitura
<details id="Camilo-Duas_Horas_de_Leitura.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |   Duas Horas de Leitura   | Camilo-Duas_Horas_de_Leitura.txt     |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> Duas Horas de Leitura
>                   de Camilo Castelo Branco
>                                   1857
>
>
>
>
>_sec+NA:
> ind_ ÍNDICE
>
>
>- Dois santos não beatificados em Roma
>- Impressão indelével
>- Sete de Junho de 1849
>- Do Porto a Braga 
>
>
>
>##Conto
>                   DOIS SANTOS NÃO BEATIFICADOS EM ROMA
>
>_sec+N:cap=1

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      38347 |    2059    |       2170 |   ~  13.9 palavras | 879        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  160 |        ter | tem; têm; terei; tenham; teria                     |
|  101 |      dizer | dizíamos; disseram; dizer; dizia; diria            |
|   95 |      saber | saibam; sabe; sabendo; sabemos; sabia              |
|   77 |      fazer | fazendo; faziam; feitos; fizeram; faz              |
|   68 |     querer | querer; queres; quer; queremos; querem             |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Matilde                 35 | Braga                  32 |
| Paulo                   30 | Porto                  20 |
| J. B.                   26 | Roma                    7 |
| Deus                    25 | Lisboa                  7 |
| E. B.                   22 | Vila Real               7 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]


##### Capítulos não encontrados.



</details>

### Esbocos de apreciacoes literarias
<details id="Camilo-Esbocos_de_apreciacoes_literarias.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | Esbocos de apreciacoes literarias | Camilo-Esbocos_de_apreciacoes_literarias.txt |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Esboços de apreciações literárias

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      70883 |    3395    |       4152 |   ~  14.3 palavras | 1903       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  195 |      dizer | dirá; disseram; dizer; dizia; diria                |
|  187 |        ter | tem; têm; terei; tenham; teria                     |
|  144 |      haver | haja; houve; houver; haviam; havermos              |
|  137 |      poder | poderiam; pode; poderem; podiam; pôde              |
|  120 |        dar | darem; davam; darei; daria; dá                     |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Pinto Ribeiro           27 | Lisboa                 26 |
| Jorge                   25 | Porto                  21 |
| Maria                   23 | Portugal               20 |
| Júlio César             22 | Roma                   14 |
| Deus                    21 | Lousada                11 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |                 ansa ; Mancha                  |
| II                   |          Providência ; ansa ; Mancha           |
| III                  |           Porto ; Lisboa ; Mouraria            |
| I                    |           Porto ; Lisboa ; Mouraria            |
| II                   |           Porto ; Lisboa ; Mouraria            |
| III                  |           Porto ; Lisboa ; Mouraria            |
| Aí,                  |           Porto ; Lisboa ; Mouraria            |
| IV                   |           Porto ; Lisboa ; Mouraria            |
| V                    |           Porto ; Lisboa ; Mouraria            |
| I                    |           Porto ; Lisboa ; Mouraria            |
| II                   |            Lousada ; Porto ; Lisboa            |
| I                    |            Lousada ; Porto ; Lisboa            |
| II                   |           Lousada ; Porto ; Portugal           |
| I                    |           Lousada ; Porto ; Portugal           |
| II                   |           Lousada ; Porto ; Portugal           |
| III                  |            Porto ; Lisboa ; Lousada            |
| IV                   |           Porto ; Lisboa ; Portugal            |
| V                    |           Lisboa ; Porto ; Portugal            |
| VI                   |           Porto ; Lisboa ; Portugal            |
| I                    |           Porto ; Lisboa ; Portugal            |
| II                   |           Porto ; Lisboa ; Portugal            |
| III                  |           Porto ; Lisboa ; Portugal            |
| V                    |           Porto ; Lisboa ; Portugal            |
| VI                   |           Lisboa ; Porto ; Portugal            |



</details>

### Espinhos e flores-Teatro
<details id="Camilo-Espinhos_e_flores-Teatro.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | Espinhos e flores-Teatro  | Camilo-Espinhos_e_flores-Teatro.txt  |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Espinhos e Flores

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      11165 |    660     |       1182 |   ~   7.1 palavras | 467        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   41 |        ter | tem; têm; tinha; ter; temos                        |
|   37 |     querer | querer; queres; quer; querem; quis                 |
|   33 |      poder | pode; podem; posso; poderão; possa                 |
|   32 |      haver | havia; haver; haverá; há                           |
|   27 |        vir | vinha; venha; vem; veio; vir                       |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Padre Henrique          22 | Lisboa                  7 |
| Josefina                15 | Maria  Josefina         2 |
| D. Amália               14 | Brasil                  2 |
| Padre                   13 | Tange                   2 |
| Luís                    13 | Toma-lhe                2 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Já?!                 |           Lisboa ; Tange ; Toma-lhe            |



</details>

### Eusebio Macario
<details id="Camilo-Eusebio_Macario.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |      Eusebio Macario      | Camilo-Eusebio_Macario.txt           |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Eusébio Macário
>
>História natural e social no tempo dos Cabrais

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      37023 |    2017    |       1835 |   ~  16.9 palavras | 1142       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  150 |      dizer | disseram; dizer; dizia; diziam; diz                |
|  140 |        ter | tem; têm; tinha; ter; tiver                        |
|  106 |      fazer | fazendo; faziam; fazerem; fizeram; faz             |
|   74 |        dar | darem; davam; darei; daria; dá                     |
|   66 |     querer | querer; quer; querendo; querem; quero              |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Felícia                 77 | Porto                  24 |
| Eusébio Macário         34 | Braga                  10 |
| Custódia                24 | Lisboa                  9 |
| Eusébio                 20 | Rabaçal                 9 |
| José Macário            16 | Montalegre              6 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |  Madre Tecla ; genebra ; frescores de sangue   |
| II                   |       Montalegre ; Madre Tecla ; genebra       |
| III                  |        Montalegre ; Braga ; Madre Tecla        |
| IV                   |           Porto ; Montalegre ; Braga           |
| V                    |           Porto ; Montalegre ; Braga           |
| VI                   |           Porto ; Braga ; Montalegre           |
| e                    |           Porto ; Braga ; Montalegre           |
| VII                  |           Porto ; Braga ; Montalegre           |
| VIII                 |           Porto ; Braga ; Montalegre           |
| IX                   |            Porto ; Braga ; Rabaçal             |
| X                    |            Porto ; Braga ; Rabaçal             |
| XI                   |            Porto ; Braga ; Rabaçal             |



</details>

### Gracejos que matam
<details id="Camilo-Gracejos_que_matam.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |    Gracejos que matam     | Camilo-Gracejos_que_matam.txt        |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      15278 |    1119    |       1080 |   ~  11.8 palavras | 623        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   61 |        ter | tem; têm; tinha; ter; tiver                        |
|   56 |      dizer | disseram; dizer; dizia; diz; digo                  |
|   23 |        ver | verá; via; viam; viu; vi                           |
|   22 |      poder | pode; podem; posso; podendo; possa                 |
|   22 |      fazer | faziam; fizeram; faz; faze; fazem                  |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| João Pacheco            35 | Santa Eulália          15 |
| Irene                   33 | Vizela                 11 |
| Álvaro de Abreu         27 | Porto                   8 |
| José de Almeida         27 | Athey                   6 |
| Álvaro                  22 | Lisboa                  5 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Conclusão            |         Vizela ; Porto ; gentilíssima          |



</details>

### Justica-Teatro
<details id="Camilo-Justica-Teatro.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |      Justica-Teatro       | Camilo-Justica-Teatro.txt            |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Justiça

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      11615 |    697     |       1223 |   ~   7.1 palavras | 507        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   51 |        ter | tem; tinha; ter; temos; tive                       |
|   48 |      poder | pode; poderei; poder; podem; podemos               |
|   36 |     querer | queres; querer; quer; querendo; quero              |
|   30 |      saber | sabe; saberei; sabia; saiba; sabem                 |
|   27 |      dizer | dizer; diz; digo; disse; dizem                     |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| D. Inês                 30 | Porto                  12 |
| Luís                    22 | Lisboa                  4 |
| Inês                    22 | Luís                    2 |
| Luís                    18 | Portugal                2 |
| D. Maria                14 | Brasil                  2 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]


##### Capítulos não encontrados.



</details>

### Maria Moises-v1
<details id="Camilo-Maria_Moises-v1.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |      Maria Moises-v1      | Camilo-Maria_Moises-v1.txt           |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> MARIA MOISÉS
>CAMILO

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      27125 |    1435    |       1326 |   ~  17.2 palavras | 859        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  144 |      dizer | disseram; dizer; dizia; diziam; diz                |
|  121 |        ter | tem; têm; tinha; terei; ter                        |
|   75 |      saber | saibam; sabe; saberei; sabendo; sabia              |
|   57 |         ir | iria; ido; for; ir; vá                             |
|   56 |        ver | verá; via; vistos; viu; vê                         |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Josefa                  29 | Tâmega                 19 |
| Maria Moisés            28 | Santa Eulália          16 |
| Deus                    19 | Brasil                  7 |
| Maria                   18 | Limoeiro                7 |
| João da Lage            15 | Coimbra                 6 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| CAMILO CASTELO BRANCO |        Tâmega ; Santa Eulália ; Brasil         |



</details>

### Maria Moises
<details id="Camilo-Maria_Moises.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |       Maria Moises        | Camilo-Maria_Moises.txt              |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Maria Moisés

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      26453 |    1401    |       1723 |   ~  12.8 palavras | 832        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  146 |      dizer | disseram; dizer; dizia; diziam; diz                |
|  124 |        ter | tem; têm; tinha; terei; ter                        |
|   76 |      saber | saibam; sabe; saberei; sabendo; sabia              |
|   58 |        ver | verá; via; vistos; viu; vê                         |
|   57 |         ir | iria; ido; for; ir; vá                             |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Josefa                  29 | Tâmega                 17 |
| Maria Moisés            22 | Santa Eulália          15 |
| Deus                    20 | Santo                   7 |
| Maria                   19 | Limoeiro                7 |
| António de Queirós      19 | Meneses                 6 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| E CARIDADE?          |                                                |



</details>

### Maria da Fonte
<details id="Camilo-Maria_da_Fonte.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |      Maria da Fonte       | Camilo-Maria_da_Fonte.txt            |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Maria da Fonte

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      70834 |    3165    |       3537 |   ~  17.2 palavras | 2980       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  205 |        ter | tem; têm; tido; teria; teremos                     |
|  147 |      fazer | feitos; feito; fazemos; fazem; feita               |
|  133 |        dar | darem; davam; der; daria; dados                    |
|  132 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  123 |      poder | poderiam; pode; poderei; pôde; posso               |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Sr. Padre Casimiro      58 | Braga                  67 |
| padre Casimiro          57 | Vieira                 43 |
| Deus                    47 | Porto                  31 |
| Padre Casimiro          30 | Minho                  27 |
| D. Miguel               26 | Guimarães              26 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| HABITANTES DE BRAGA! |             Braga ; Vieira ; Porto             |



</details>

### Memorias de Guilherme do Amaral
<details id="Camilo-Memorias_de_Guilherme_do_Amaral.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | Memorias de Guilherme do Amaral | Camilo-Memorias_de_Guilherme_do_Amaral.txt |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Memórias de Guilherme do Amaral
>  
>     
>    Introdução

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      45457 |    2545    |       3775 |   ~   9.7 palavras | 1045       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  158 |        ter | tem; têm; tinha; terei; ter                        |
|  130 |      poder | poderiam; pode; poderem; podiam; poderei           |
|  101 |      saber | sabe; sabendo; sabia; saiba; sabem                 |
|   92 |        ver | via; vistas; viu; vê; vista                        |
|   80 |      dizer | disseram; dizer; dizia; diria; diz                 |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Guilherme               38 | Virgínia               39 |
| Deus                    38 | Porto                  25 |
| Raquel                  30 | Lisboa                  9 |
| Guilherme do Amaral     29 | hei-de                  7 |
| Baltasar                18 | Céu                     7 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |                                                |
| S.                   |                     Hei-de                     |
| II                   |                     Hei-de                     |
| III                  |               Hei-de ; Hircânia                |
| IV                   |            Hei-de ; Hircânia ; Céu             |
| V                    |            Hei-de ; Hircânia ; Céu             |
| VI                   |             Virgínia ; Porto ; Céu             |



</details>

### Misterios de Fafe
<details id="Camilo-Misterios_de_Fafe.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |     Misterios de Fafe     | Camilo-Misterios_de_Fafe.txt         |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      68661 |    3419    |       5308 |   ~  10.7 palavras | 2148       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  292 |      dizer | dirá; disseram; dizer; dizia; diria                |
|  242 |        ter | tem; têm; terei; tenham; teria                     |
|  164 |     querer | queiram; querer; queres; quer; quiseram            |
|  152 |      saber | sabe; sabendo; sabia; saberem; sabemos             |
|  146 |      fazer | fazendo; faziam; fazerem; fizeram; faz             |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Rosa                   150 | Fafe                   86 |
| Caetano                 96 | Porto                  47 |
| Caetano de Ataíde       64 | Lisboa                 35 |
| Francisco               55 | Guimarães              21 |
| D. Gabriela             55 | Coimbra                15 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Capítulo I           |            Fafe ; Guimarães ; Porto            |
| Capítulo II          |            Fafe ; Guimarães ; Porto            |
| Capítulo III         |            Fafe ; Guimarães ; Porto            |
| Capítulo IV          |            Fafe ; Guimarães ; Porto            |
| Capítulo V           |            Fafe ; Porto ; Guimarães            |
| Capítulo VI          |            Fafe ; Porto ; Guimarães            |
| Capítulo VII         |            Fafe ; Porto ; Guimarães            |
| Capítulo VIII        |            Fafe ; Porto ; Guimarães            |
| Capítulo IX          |            Fafe ; Porto ; Guimarães            |
| Capítulo X           |            Fafe ; Porto ; Guimarães            |
| Capítulo XI          |             Fafe ; Porto ; Lisboa              |
| Capítulo XII         |             Fafe ; Porto ; Lisboa              |
| Capítulo XIII        |             Fafe ; Porto ; Lisboa              |
| Capítulo XIV         |             Fafe ; Porto ; Lisboa              |
| Capítulo XV          |             Fafe ; Porto ; Lisboa              |
| Capítulo XVI         |             Fafe ; Porto ; Lisboa              |
| Capítulo XVII        |             Fafe ; Porto ; Lisboa              |
| Capítulo XVIII       |             Fafe ; Porto ; Lisboa              |
| Capítulo XIX         |             Fafe ; Porto ; Lisboa              |
| Capítulo XX          |             Fafe ; Porto ; Lisboa              |
| Capítulo XXI         |             Fafe ; Porto ; Lisboa              |
| Capítulo XXII        |             Fafe ; Porto ; Lisboa              |
| Capítulo XXIII       |             Fafe ; Porto ; Lisboa              |
| Capítulo XXIV        |             Fafe ; Porto ; Lisboa              |
| Capítulo XXV         |             Fafe ; Porto ; Lisboa              |
| Capítulo XXVI        |             Fafe ; Porto ; Lisboa              |
| Capítulo XXVII       |             Fafe ; Porto ; Lisboa              |
| Conclusão            |             Fafe ; Porto ; Lisboa              |



</details>

### Misterios de Lisboa 1
<details id="Camilo-Misterios_de_Lisboa_1.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |   Misterios de Lisboa 1   | Camilo-Misterios_de_Lisboa_1.txt     |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      81791 |    3570    |       5419 |   ~  12.6 palavras | 1701       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  320 |        ter | tem; têm; terei; teres; teria                      |
|  302 |      poder | poderiam; pode; poderei; pôde; posso               |
|  287 |      dizer | dirá; disseram; dizer; dizia; diria                |
|  230 |      saber | saberia; sabe; sabendo; sabia; sabemos             |
|  172 |      fazer | fazendo; faziam; fizeram; faz; feito               |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Vossa Excelência        88 | Lisboa                 31 |
| Deus                    83 | Montezelos             19 |
| conde de Santa Bárbara   48 | Santarém               10 |
| D. Antónia              46 | Portugal                7 |
| Padre Dinis             41 | Tejo                    7 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| 1                    |     Mistérios de Lisboa ; Brasil ; Lisboa      |
| F.                   |     Mistérios de Lisboa ; Brasil ; Lisboa      |
| II                   |     Mistérios de Lisboa ; Lisboa ; Brasil      |
| III                  |     Mistérios de Lisboa ; Lisboa ; Brasil      |
| IV                   |     Lisboa ; Mistérios de Lisboa ; Brasil      |
| A.                   |     Lisboa ; Mistérios de Lisboa ; Brasil      |
| V                    |     Lisboa ; Mistérios de Lisboa ; Brasil      |
| VI                   |     Lisboa ; Mistérios de Lisboa ; Brasil      |
| VII                  |     Lisboa ; Mistérios de Lisboa ; Brasil      |
| VIII                 |     Lisboa ; Mistérios de Lisboa ; Brasil      |
| IX                   |     Lisboa ; Mistérios de Lisboa ; Brasil      |
| X                    |     Lisboa ; Mistérios de Lisboa ; Brasil      |
| XI                   |   Lisboa ; Montezelos ; Mistérios de Lisboa    |
| XII                  |   Lisboa ; Montezelos ; Mistérios de Lisboa    |
| XIII                 |    Montezelos ; Lisboa ; Convento de Nazaré    |
| XIV                  |         Montezelos ; Lisboa ; Santarém         |
| XV                   |         Montezelos ; Lisboa ; Santarém         |
| XVI                  |         Lisboa ; Montezelos ; Santarém         |
| XVII                 |         Lisboa ; Montezelos ; Santarém         |
| XVIII                |         Lisboa ; Montezelos ; Penacova         |
| XIX                  |         Lisboa ; Montezelos ; Penacova         |
| XX                   |         Lisboa ; Montezelos ; Santarém         |
| XXI                  |         Lisboa ; Montezelos ; Santarém         |
| XXII                 |         Lisboa ; Montezelos ; Santarém         |
| XXIII                |         Lisboa ; Montezelos ; Santarém         |
| II                   |         Lisboa ; Montezelos ; Santarém         |
| III                  |         Lisboa ; Montezelos ; Santarém         |



</details>

### Misterios de Lisboa 2
<details id="Camilo-Misterios_de_Lisboa_2.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |   Misterios de Lisboa 2   | Camilo-Misterios_de_Lisboa_2.txt     |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      80270 |    3365    |       5946 |   ~  10.9 palavras | 2057       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  340 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  311 |        ter | tem; têm; tinha; terei; ter                        |
|  203 |      poder | poderiam; pode; podiam; poderei; pôde              |
|  200 |      saber | saberão; sabe; sabendo; sabemos; sabia             |
|  178 |      fazer | fazendo; faziam; feitos; fizeram; faz              |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Deus                    83 | Anacleta               78 |
| Sebastião de Melo       63 | Lisboa                 49 |
| Alberto                 53 | Portugal               20 |
| Eugénia                 53 | Paris                  13 |
| Antónia                 42 | Azarias                11 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| 2                    |                                                |
| IV                   |      Adelaide ; Supus ; Vossa Excelência       |
| V                    |            Adelaide ; Viso ; Lisboa            |
| VI                   |           Portugal ; Roma ; Adelaide           |
| VII                  |           Roma ; Portugal ; Adelaide           |
| VIII                 |           Anacleta ; Roma ; Portugal           |
| IX                   |           Anacleta ; Roma ; Portugal           |
|                      |           Anacleta ; Roma ; Portugal           |
| X                    |           Anacleta ; Roma ; Portugal           |
| XI                   |           Anacleta ; Roma ; Portugal           |
| XII                  |            Anacleta ; Roma ; Lisboa            |
| XIII                 |            Anacleta ; Lisboa ; Roma            |
| XIV                  |            Anacleta ; Lisboa ; Roma            |
| XV                   |          Anacleta ; Lisboa ; Portugal          |
| XVI                  |          Anacleta ; Lisboa ; Portugal          |
| XVII                 |          Anacleta ; Lisboa ; Portugal          |
| II                   |          Anacleta ; Lisboa ; Portugal          |
| III                  |          Anacleta ; Lisboa ; Portugal          |
| IV                   |          Anacleta ; Lisboa ; Portugal          |
| V                    |          Anacleta ; Lisboa ; Portugal          |
| VI                   |          Anacleta ; Lisboa ; Portugal          |
| VII                  |          Anacleta ; Lisboa ; Portugal          |
| VIII                 |          Anacleta ; Lisboa ; Portugal          |
| IX                   |          Anacleta ; Lisboa ; Portugal          |
| X                    |          Anacleta ; Lisboa ; Portugal          |
| XI                   |          Anacleta ; Lisboa ; Portugal          |
| II                   |          Anacleta ; Lisboa ; Portugal          |
| III                  |          Anacleta ; Lisboa ; Portugal          |
| IV                   |          Anacleta ; Lisboa ; Portugal          |



</details>

### Misterios de Lisboa 3
<details id="Camilo-Misterios_de_Lisboa_3.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |   Misterios de Lisboa 3   | Camilo-Misterios_de_Lisboa_3.txt     |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      80910 |    3316    |       6208 |   ~  10.6 palavras | 2177       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  341 |        ter | tem; têm; terei; tido; teria                       |
|  273 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  205 |      poder | poderiam; pode; podiam; poderei; pôde              |
|  171 |     querer | quiseram; querer; queres; quer; querendo           |
|  163 |      fazer | fazendo; faziam; fazerem; fizeram; faz             |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| D. Pedro                87 | Paris                  54 |
| Alberto                 83 | Lisboa                 32 |
| Alberto de Magalhães    66 | Portugal               31 |
| D. Pedro da Silva       64 | França                 23 |
| duquesa de Cliton       54 | Tendes                 16 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| 3                    |                                                |
| V                    |     Paris ; Bélgica ; monástico de Lisboa      |
| VI                   |           Portugal ; Paris ; Bélgica           |
| VII                  |           Portugal ; Lisboa ; Paris            |
| VIII                 |           Portugal ; Lisboa ; Paris            |
| IX                   |           Portugal ; Lisboa ; Paris            |
| X                    |           Portugal ; Lisboa ; Paris            |
| XI                   |           Portugal ; Paris ; Lisboa            |
| XII                  |           Paris ; Portugal ; Lisboa            |
| XIII                 |           Paris ; Portugal ; Lisboa            |
| XIV                  |           Paris ; França ; Portugal            |
| XV                   |            Paris ; Lisboa ; França             |
| XVI                  |            Paris ; Lisboa ; França             |
| XVII                 |            Paris ; Lisboa ; França             |
| XVIII                |           Paris ; Lisboa ; Portugal            |
| XIX                  |           Paris ; Lisboa ; Portugal            |
| XX                   |           Paris ; Lisboa ; Portugal            |
| XXI                  |           Paris ; Lisboa ; Portugal            |
| XXII                 |           Paris ; Lisboa ; Portugal            |
| XXIII                |           Paris ; Lisboa ; Portugal            |
| XXIV                 |           Paris ; Lisboa ; Portugal            |
| XXV                  |           Paris ; Lisboa ; Portugal            |
| XXVI                 |           Paris ; Lisboa ; Portugal            |
| XXVII                |           Paris ; Lisboa ; Portugal            |
| XXVIII               |           Paris ; Lisboa ; Portugal            |
| XXIX                 |           Paris ; Lisboa ; Portugal            |
| XXX                  |           Paris ; Lisboa ; Portugal            |
| XXXI                 |           Paris ; Lisboa ; Portugal            |



</details>

### No Bom Jesus do Monte
<details id="Camilo-No_Bom_Jesus_do_Monte.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |   No Bom Jesus do Monte   | Camilo-No_Bom_Jesus_do_Monte.txt     |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      43963 |    2499    |       3060 |   ~  11.9 palavras | 1358       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  127 |      dizer | dirá; disseram; dizer; dizia; diria                |
|  117 |        ter | tem; têm; tinha; ter; temos                        |
|   92 |        ver | verem; via; viam; vê; viu                          |
|   74 |      saber | saberia; sabe; sabia; saberem; saiba               |
|   71 |      poder | pode; podiam; pôde; podem; podemos                 |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| José Augusto            90 | Porto                  28 |
| Fanny                   34 | Lisboa                 21 |
| Deus                    32 | Bom Jesus              19 |
| Senhor                  13 | Braga                  18 |
| Paulo de Barros         13 | Aldonsa                13 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |                     Largo                      |
| II                   |         Lisboa ; Vila Real ; Bom Jesus         |
| I                    |           Lisboa ; Braga ; Vila Real           |
| II                   |           Braga ; Lisboa ; Bom Jesus           |
| I                    |           Braga ; Lisboa ; Bom Jesus           |
| II                   |            Braga ; Aldonsa ; Lisboa            |
| I                    |            Braga ; Aldonsa ; Lisboa            |
| II                   |            Braga ; Aldonsa ; Lisboa            |
| III                  |            Braga ; Aldonsa ; Lisboa            |
| IV                   |            Braga ; Aldonsa ; Lisboa            |
| I                    |            Braga ; Aldonsa ; Lisboa            |
| II                   |            Braga ; Lisboa ; Aldonsa            |
| III                  |             Braga ; Lisboa ; Porto             |
| IV                   |             Braga ; Porto ; Lisboa             |
| V                    |             Porto ; Braga ; Lisboa             |
| VI                   |             Porto ; Braga ; Lisboa             |
| VII                  |             Porto ; Braga ; Lisboa             |
| VIII                 |             Porto ; Braga ; Lisboa             |
| IX                   |             Porto ; Braga ; Lisboa             |
| I                    |             Porto ; Braga ; Lisboa             |
| II                   |             Porto ; Lisboa ; Braga             |
| III                  |             Porto ; Lisboa ; Braga             |
| I                    |             Porto ; Lisboa ; Braga             |
| II                   |             Porto ; Lisboa ; Braga             |
| III                  |             Porto ; Lisboa ; Braga             |
| I                    |           Porto ; Lisboa ; Bom Jesus           |
| II                   |           Porto ; Lisboa ; Bom Jesus           |
| I                    |           Porto ; Lisboa ; Bom Jesus           |
| II                   |           Porto ; Lisboa ; Bom Jesus           |
| I                    |           Porto ; Lisboa ; Bom Jesus           |
| II                   |           Porto ; Lisboa ; Bom Jesus           |
| III                  |           Porto ; Lisboa ; Bom Jesus           |
| FIM                  |           Porto ; Lisboa ; Bom Jesus           |
| I                    |           Porto ; Lisboa ; Bom Jesus           |
| II                   |           Porto ; Lisboa ; Bom Jesus           |
| III                  |           Porto ; Lisboa ; Bom Jesus           |
| FIM                  |           Porto ; Lisboa ; Bom Jesus           |



</details>

### Noites de Lamego
<details id="Camilo-Noites_de_Lamego.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |     Noites de Lamego      | Camilo-Noites_de_Lamego.txt          |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Noites de Lamego

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      45471 |    2317    |       3472 |   ~  10.6 palavras | 1449       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  196 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  134 |        ter | tem; têm; tinha; ter; tiver                        |
|  102 |        ver | verem; via; verá; viu; vê                          |
|   97 |      fazer | fazendo; faziam; feitos; fizeram; faz              |
|   91 |      saber | sabe; sabido; sabia; sabemos; sabem                |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| D. Luísa                42 | Lisboa                 19 |
| César                   37 | Porto                  14 |
| Helena                  34 | Espanha                12 |
| Guilherme               32 | Portugal               12 |
| João Moreira            29 | Leituga                10 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |                     Retire                     |
| II                   |               Retire ; Festejava               |
| III                  |               Retire ; Festejava               |
| I                    |          Retire ; Festejava ; Lisboa           |
| II                   |          Retire ; Festejava ; Lisboa           |
| III                  |          Retire ; Festejava ; Lisboa           |
| IV                   |          Lisboa ; Retire ; Festejava           |
| V                    |            Lisboa ; Brasil ; Retire            |
| VI                   |        Lisboa ; Brasil ; Rio de Janeiro        |
| VII                  |       Lisboa ; Rio de Janeiro ; Portugal       |
| VIII                 |       Lisboa ; Rio de Janeiro ; Portugal       |
| IX                   |       Lisboa ; Rio de Janeiro ; Portugal       |
| X                    |       Lisboa ; Rio de Janeiro ; Portugal       |
| XI                   |       Lisboa ; Rio de Janeiro ; Portugal       |
| XII                  |       Lisboa ; Rio de Janeiro ; Portugal       |
| XIII                 |       Lisboa ; Rio de Janeiro ; Portugal       |
| XIV                  |       Lisboa ; Rio de Janeiro ; Portugal       |
| I                    |       Lisboa ; Rio de Janeiro ; Portugal       |
| II                   |         Lisboa ; Portugal ; Esposende          |
| III                  |           Lisboa ; Portugal ; Porto            |
| IV                   |           Lisboa ; Porto ; Portugal            |
| V                    |           Lisboa ; Porto ; Portugal            |
| I                    |           Lisboa ; Porto ; Portugal            |
| II                   |           Lisboa ; Porto ; Portugal            |
| III                  |           Lisboa ; Porto ; Portugal            |
| IV                   |           Lisboa ; Porto ; Portugal            |
| V                    |           Lisboa ; Porto ; Portugal            |
| VI                   |           Lisboa ; Porto ; Portugal            |
| I                    |           Lisboa ; Porto ; Portugal            |
| II                   |           Lisboa ; Porto ; Portugal            |
| I                    |           Lisboa ; Porto ; Portugal            |
| II                   |           Lisboa ; Porto ; Portugal            |
| I                    |           Lisboa ; Porto ; Portugal            |
| II                   |           Lisboa ; Portugal ; Porto            |
| I                    |           Lisboa ; Portugal ; Porto            |
| II                   |           Lisboa ; Portugal ; Porto            |
| III                  |           Lisboa ; Portugal ; Porto            |
| IV                   |           Lisboa ; Porto ; Portugal            |
| V                    |           Lisboa ; Porto ; Portugal            |



</details>

### Novelas do Minho 1
<details id="Camilo-Novelas_do_Minho_1.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |    Novelas do Minho 1     | Camilo-Novelas_do_Minho_1.txt        |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      82429 |    3536    |       5110 |   ~  13.7 palavras | 2745       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  399 |      dizer | disseram; dizer; dizia; diria; diziam              |
|  325 |        ter | tem; têm; terei; tenham; teria                     |
|  209 |      fazer | fazendo; faziam; feitos; fizeram; faz              |
|  192 |     querer | queres; querer; quer; querendo; queremos           |
|  180 |      saber | saibam; sabe; sabíamos; saberei; sabendo           |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Teresa                 101 | Guimarães              30 |
| Guilherme               60 | Portugal               22 |
| Deus                    52 | Lisboa                 20 |
| Teresa de Jesus         46 | Espanha                19 |
| Joaquim Pereira         34 | Tâmega                 17 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |       Tâmega ; Santa Eulália ; Limoeiro        |
|                      |       Tâmega ; Santa Eulália ; Limoeiro        |
|                      |       Tâmega ; Santa Eulália ; Limoeiro        |
| II                   |       Tâmega ; Santa Eulália ; Limoeiro        |
|                      |       Tâmega ; Santa Eulália ; Limoeiro        |
|                      |       Tâmega ; Santa Eulália ; Limoeiro        |
|                      |       Tâmega ; Santa Eulália ; Limoeiro        |
|                      |       Tâmega ; Santa Eulália ; Limoeiro        |
|                      |       Tâmega ; Santa Eulália ; Limoeiro        |
|                      |       Tâmega ; Santa Eulália ; Vila Real       |
| III                  |       Tâmega ; Santa Eulália ; Vila Real       |
| e                    |         Guimarães ; Portugal ; Lisboa          |



</details>

### Novelas do Minho 2
<details id="Camilo-Novelas_do_Minho_2.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |    Novelas do Minho 2     | Camilo-Novelas_do_Minho_2.txt        |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>Novelas do Minho
> 
>II

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      78907 |    3844    |       6026 |   ~  11.0 palavras | 2696       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  320 |        ter | tem; têm; terei; tenham; tido                      |
|  287 |      dizer | disseram; dizer; dizia; diz; diziam                |
|  147 |      fazer | fazendo; faziam; feitos; fizeram; faz              |
|  134 |        ver | verá; via; veria; víamos; viam                     |
|  134 |        dar | darem; davam; der; dados; daria                    |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Tomásia                 61 | Braga                  36 |
| Álvaro                  57 | Porto                  33 |
| João Pacheco            35 | Minho                  25 |
| Irene                   34 | Lisboa                 24 |
| Deus                    30 | Brasil                 21 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| II                   |                                                |
| I                    |         Santa Eulália ; Vizela ; Porto         |
| II                   |         Braga ; Santa Eulália ; Minho          |
| III                  |         Braga ; Santa Eulália ; Minho          |
| I                    |         Braga ; Santa Eulália ; Minho          |
| II                   |         Braga ; Santa Eulália ; Minho          |
| III                  |         Braga ; Santa Eulália ; Porto          |
| IV                   |         Braga ; Porto ; Santa Eulália          |
| V                    |         Braga ; Porto ; Santa Eulália          |
| VI                   |         Braga ; Porto ; Santa Eulália          |
| VII                  |         Braga ; Porto ; Santa Eulália          |
| VIII                 |         Braga ; Porto ; Santa Eulália          |
| IX                   |         Braga ; Porto ; Santa Eulália          |
| X                    |         Braga ; Porto ; Santa Eulália          |
| XI                   |         Braga ; Porto ; Santa Eulália          |
| IV                   |         Braga ; Porto ; Santa Eulália          |
| I                    |         Braga ; Porto ; Santa Eulália          |
| II                   |         Braga ; Porto ; Santa Eulália          |
| III                  |         Braga ; Porto ; Santa Eulália          |
| IV                   |         Braga ; Porto ; Santa Eulália          |
| V                    |         Braga ; Porto ; Santa Eulália          |
| VI                   |         Braga ; Porto ; Santa Eulália          |
| VII                  |         Braga ; Porto ; Santa Eulália          |
| VIII                 |         Braga ; Porto ; Santa Eulália          |
| IX                   |         Braga ; Porto ; Santa Eulália          |
| X                    |             Braga ; Porto ; Minho              |
| XI                   |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |
|                      |             Braga ; Porto ; Minho              |



</details>

### O Arrependimento
<details id="Camilo-O_Arrependimento.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |     O Arrependimento      | Camilo-O_Arrependimento.txt          |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|       4778 |    368     |        210 |   ~  19.5 palavras | 114        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   28 |        ter | tinha; ter; tiver; temos; tivesse                  |
|   17 |      fazer | fazendo; faz; feito; fez; feitas                   |
|   13 |      poder | pode; pôde; poder; poderia; poderá                 |
|   12 |        dar | dava; dar; dado; deu                               |
|   10 |     seguir | seguido; seguiu; seguir; seguisse                  |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Emílio da Cunha         32 | Porto                   5 |
| Roberto                 17 | Rio de Janeiro          4 |
| Valentina               14 | Brasil                  3 |
| D. Mafalda               7 | Lisboa                  2 |
| Deus                     4 | Califórnia              2 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]


##### Capítulos não encontrados.



</details>

### O Comendador
<details id="Camilo-O_Comendador.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |       O Comendador        | Camilo-O_Comendador.txt              |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> O Comendador
>    
>    Camilo Castelo Branco
>     (Portugal, 1825 - 1890)
>    
>     
>     É tão fatalmente séria a vida que o sofrê-la, sem misturar a tragédia com a comédia, seria impossível.

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      13791 |    968     |        902 |   ~  12.8 palavras | 426        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   53 |      dizer | dizer; dizia; diz; diziam; digo                    |
|   49 |        ter | tem; têm; tinha; ter; tiver                        |
|   38 |        ver | verá; via; veria; víamos; viu                      |
|   27 |        dar | dados; daria; dá; deram; dado                      |
|   23 |      haver | havia; há; haver                                   |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Belchior                21 | Braga                  24 |
| Bernabé                 16 | Minho                  11 |
| Maria                   14 | Paris                   9 |
| Deus                    12 | Vila do Conde           8 |
| V. Ex                   11 | Porto                   5 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]


##### Capítulos não encontrados.



</details>

### O Judeu 1
<details id="Camilo-O_Judeu_1.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |         O Judeu 1         | Camilo-O_Judeu_1.txt                 |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      57603 |    2784    |       3434 |   ~  14.1 palavras | 2527       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  226 |      dizer | disseram; dizer; dizia; diria; diziam              |
|  174 |        ter | tem; têm; tenham; tido; teria                      |
|  112 |      poder | poderiam; pode; poderem; podiam; pôde              |
|  100 |      fazer | fazendo; faziam; fazerem; fizeram; faz             |
|   94 |      saber | sabe; sabendo; sabia; saiba; soube                 |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Jorge                  213 | Lisboa                 62 |
| Sara                   143 | Portugal               50 |
| D. Francisca            63 | Covilhã                33 |
| Jorge de Barros         47 | Lourença               33 |
| Simão de Sã             43 | Amesterdão             21 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| PARTE PRIMEIRA       |  Lisboa ; Convento da Madre de Deus ; Brasil   |
| NOTA                 |          Lisboa ; Covilhã ; Portugal           |
| SEGUNDA PARTE        |          Lisboa ; Portugal ; Lourença          |



</details>

### O carrasco de Vitor Hugo
<details id="Camilo-O_carrasco_de_Vitor_Hugo.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | O carrasco de Vitor Hugo  | Camilo-O_carrasco_de_Vitor_Hugo.txt  |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> O Carrasco de

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      53393 |    2712    |       3304 |   ~  13.6 palavras | 1723       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  185 |      dizer | dirá; disseram; dizer; dizia; diria                |
|  136 |        ter | tem; têm; tinha; ter; tiver                        |
|  113 |      saber | saibam; sabe; sabendo; sabia; saiba                |
|  107 |      poder | poderiam; pode; podiam; pôde; poder                |
|  102 |      fazer | fazendo; fazermos; faziam; fazerem; fizeram        |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Vítor Hugo              47 | Lisboa                 41 |
| D. Maria José           40 | Portugal               17 |
| D. Maria                37 | Mariana                11 |
| Vossa Excelência        33 | Rosenda                 9 |
| Vítor Hugo José Alves   31 | Rua Nova da Palma       8 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| 1                    | Rua Nova da Palma  II y a ici quelque chose... une fleur... cherchez! ; Lisboa ; Indostão |
| II                   |     Lisboa ; Rua Nova da Palma ; Portugal      |
| III                  |      Rosenda ; Lisboa ; Rua Nova da Palma      |
| IV                   |      Rosenda ; Lisboa ; Rua Nova da Palma      |
| V                    |      Rosenda ; Lisboa ; Rua Nova da Palma      |
| VI                   |          Rosenda ; Lisboa ; Portugal           |
| VII                  |          Rosenda ; Lisboa ; Portugal           |
| VIII                 |          Lisboa ; Rosenda ; Portugal           |
| IX                   |          Lisboa ; Portugal ; Rosenda           |
| X                    |          Lisboa ; Portugal ; Rosenda           |
| XI                   |          Lisboa ; Portugal ; Rosenda           |
| XII                  |          Lisboa ; Portugal ; Rosenda           |
| XIII                 |          Lisboa ; Portugal ; Rosenda           |
| XIV                  |          Lisboa ; Portugal ; Rosenda           |
| XV                   |          Lisboa ; Portugal ; Rosenda           |
| XVI                  |          Lisboa ; Portugal ; Rosenda           |



</details>

### O cego de Landim
<details id="Camilo-O_cego_de_Landim.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |     O cego de Landim      | Camilo-O_cego_de_Landim.txt          |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      11945 |    892     |        700 |   ~  14.7 palavras | 430        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   46 |        ter | tem; têm; tinha; ter; temos                        |
|   31 |      dizer | disseram; dizer; dizia; diz; diziam                |
|   24 |        dar | davam; daria; dá; dando; deram                     |
|   21 |      fazer | faziam; feitos; faz; feito; faria                  |
|   18 |      haver | haja; houve; haver; há; havia                      |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Pinto Monteiro          27 | Rio                    12 |
| Landim                  17 | Porto                  11 |
| Pinto                   15 | Brasil                 10 |
| Narcisa                 13 | Portugal                5 |
| Amaro Faial              8 | Monteiro                5 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| CAPÍTULO    I        | S. Miguel de Seide ; em Portugal ; Completamente |
| CAPÍTULO    II       | S. Miguel de Seide ; em Portugal ; Completamente |
| CAPÍTULO    III      |           Brasil ; Porto ; Portugal            |
| CAPÍTULO    IV       |              Porto ; Brasil ; Rio              |
| CAPÍTULO    V        |              Porto ; Rio ; Brasil              |
| CAPÍTULO     VI      |              Porto ; Rio ; Brasil              |
| CAPÍTULO    VII      |              Porto ; Rio ; Brasil              |
| CAPÍTULO    VIII     |              Rio ; Porto ; Brasil              |
| CAPÍTULO    IX       |              Rio ; Porto ; Brasil              |
| CAPÍTULO    X        |              Rio ; Porto ; Brasil              |
| CAPÍTULO    XI       |              Rio ; Porto ; Brasil              |
| AQUI JAZ             |              Rio ; Porto ; Brasil              |
| ANTÓNIO JOSÉ PINTO MONTEIRO |              Rio ; Porto ; Brasil              |
| NASCEU               |              Rio ; Porto ; Brasil              |
| A 11 DE DEZEMBRO DE 1808 |              Rio ; Porto ; Brasil              |
| FALECEU              |              Rio ; Porto ; Brasil              |
| A 1 DE DEZEMBRO DE 1868 |              Rio ; Porto ; Brasil              |
| TRIBUTO DE GRATIDÃO  |              Rio ; Porto ; Brasil              |
| DE ETERNA SAUDADE    |              Rio ; Porto ; Brasil              |
| QUE LHE DEDICA SUA   |              Rio ; Porto ; Brasil              |
| INCONSOLÁVEL FILHA   |              Rio ; Porto ; Brasil              |
| GUILHERMINA          |              Rio ; Porto ; Brasil              |



</details>

### O esqueleto-v2
<details id="Camilo-O_esqueleto-v2.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |      O esqueleto-v2       | Camilo-O_esqueleto-v2.txt            |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> ﻿The
> Project

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      75154 |    3655    |       6075 |   ~   9.4 palavras | 2737       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  243 |      dizer | disseram; dizer; dizia; diria; diziam              |
|  188 |        ter | tem; tido; teria; teremos; tiver                   |
|  126 |      saber | saberão; saberia; sabe; sabendo; sabemos           |
|  115 |        ver | verem; via; viu; vê; viam                          |
|  113 |      fazer | fazendo; faziam; fazerem; fizeram; faz             |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Beatriz                155 | Nicoláo               112 |
| Raphael                149 | elle                   66 |
| Ricardo                 83 | Nicoláo de Mesquita    64 |
| Martinho Xavier         81 | Lisboa                 54 |
| Margarida               53 | Palmeira               43 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| DE                   |                                                |
| V                    | MARIA PEREIRA--LIVRARIA-EDITORA _Rua ; Antonio Maria ; Rua dos Correeiros |
| I                    |     Porto ; Nicoláo de Mesquita ; Nicoláo      |
| II                   |     Nicoláo de Mesquita ; Nicoláo ; Porto      |
| III                  |     Nicoláo ; Nicoláo de Mesquita ; Porto      |
| IV                   |     Nicoláo ; Nicoláo de Mesquita ; Porto      |
| V                    |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| VI                   |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| VII                  |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| VIII                 |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| IX                   |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| X                    |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XI                   |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XII                  |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XIII                 |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XIV                  |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XV                   |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XVI                  |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| XVII                 |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| XVIII                |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XIX                  |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XX                   |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XXI                  |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XXII                 |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XXIII                |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| XXIV                 |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| XXV                  |      Nicoláo ; elle ; Nicoláo de Mesquita      |
| XXVI                 |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| XXVII                |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| FIM                  |      Nicoláo ; Nicoláo de Mesquita ; elle      |
| DE                   |      Nicoláo ; Nicoláo de Mesquita ; elle      |



</details>

### O esqueleto
<details id="Camilo-O_esqueleto.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |        O esqueleto        | Camilo-O_esqueleto.txt               |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      69671 |    3391    |       6421 |   ~   8.9 palavras | 2495       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  265 |      dizer | disseram; dizer; dizia; diria; diziam              |
|  190 |        ter | tem; têm; tido; teria; teremos                     |
|  151 |        ver | verem; via; viu; vê; viam                          |
|  137 |      saber | saberão; saberia; sabe; sabendo; sabemos           |
|  137 |      poder | pode; poderem; podiam; poderei; pôde               |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Rafael                 189 | Lisboa                 58 |
| Beatriz                177 | Palmeira               52 |
| Nicolau                156 | Porto                  27 |
| Nicolau de Mesquita     96 | Paris                  21 |
| Ricardo                 90 | França                 18 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| PREFÁCIO             |         Porto ; Palmeira ; Vila Pouca          |
| A BEIRA-MAR          |           Lisboa ; Palmeira ; Porto            |
| CONCLUSÃO            |           Lisboa ; Palmeira ; Porto            |



</details>

### O filho natural
<details id="Camilo-O_filho_natural.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |      O filho natural      | Camilo-O_filho_natural.txt           |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      23565 |    1468    |       1545 |   ~  12.8 palavras | 801        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  103 |        ter | tem; têm; tinha; ter; temos                        |
|   86 |      dizer | dizer; dizia; diz; diziam; digo                    |
|   54 |      fazer | faziam; faz; feito; fazemos; faria                 |
|   45 |     querer | querer; quer; querem; quis; quero                  |
|   40 |        ver | via; viam; viu; vi; veja                           |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Tomásia                 61 | Lisboa                 12 |
| Álvaro                  34 | Agilde                  9 |
| Vasco                   22 | Pedraça                 9 |
| Vasco Pereira           13 | Minho                   8 |
| Pedraça                 10 | Basto                   7 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]


##### Capítulos não encontrados.



</details>

### O que fazem mulheres
<details id="Camilo-O_que_fazem_mulheres.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |   O que fazem mulheres    | Camilo-O_que_fazem_mulheres.txt      |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>
>
>O que fazem mulheres

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      50453 |    2638    |       3611 |   ~  11.5 palavras | 1256       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  233 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  175 |        ter | tem; teremos; têm; tinha; terei                    |
|  140 |      fazer | fazendo; faziam; feitos; fizeram; faz              |
|  114 |      saber | saberia; sabe; sabes; sabendo; sabia               |
|  113 |     querer | querer; queres; quer; querendo; querem             |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| D. Angélica             53 | Ludovina               82 |
| Ludovina                47 | Celorico               15 |
| António de Almeida      41 | Porto                  14 |
| Melchior                30 | Celorico de Basto      13 |
| Melchior Pimenta        30 | Lua                    10 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Capítulo avulso      |                 Fazem Mulheres                 |
| Capítulo I           |                 Fazem Mulheres                 |
| Capítulo II          |                 Fazem Mulheres                 |
| Capítulo III         |                 Fazem Mulheres                 |
| Capítulo IV          |                 Fazem Mulheres                 |
| Capítulo V           |                 Fazem Mulheres                 |
| Capítulo VI          |                 Fazem Mulheres                 |
| Capítulo VII         |                 Fazem Mulheres                 |
| Capítulo VIII        |                 Fazem Mulheres                 |
| Capítulo IX          |                 Fazem Mulheres                 |
| Capítulo X           |                 Fazem Mulheres                 |
| Capítulo XI          |                 Fazem Mulheres                 |
| Capítulo XII         |                 Fazem Mulheres                 |
| Capítulo XIII        |                 Fazem Mulheres                 |
| Capítulo XIV         |                 Fazem Mulheres                 |
| Capítulo XV          |                 Fazem Mulheres                 |
| Capítulo XVI         |                 Fazem Mulheres                 |
| Capítulo XVII        |                 Fazem Mulheres                 |
| Conclusão            |           Fazem Mulheres ; Cadinhos            |
| Capítulo Avulso      |       França ; Fazem Mulheres ; Cadinhos       |
| Capítulo I           |             Porto ; França ; Paris             |
| Capítulo II          |           Porto ; França ; Ludovina            |
| Capítulo III         |           Porto ; Ludovina ; França            |
| Capítulo IV          |           Ludovina ; Porto ; França            |
| Capítulo V           |             Ludovina ; Lua ; Porto             |
| Capítulo VI          |             Ludovina ; Lua ; Porto             |
| Capítulo VII         |             Ludovina ; Lua ; Porto             |
| Capítulo VIII        |             Ludovina ; Lua ; Porto             |
| Capítulo IX          |             Ludovina ; Lua ; Porto             |
| Capítulo X           |             Ludovina ; Lua ; Porto             |
| Capítulo XI          |             Ludovina ; Porto ; Lua             |
| Capítulo XII         |             Ludovina ; Porto ; Lua             |
| Capítulo XIII        |             Ludovina ; Porto ; Lua             |
| Capítulo XIV         |             Ludovina ; Porto ; Lua             |
| Capítulo XV          |             Ludovina ; Porto ; Lua             |
| Capítulo XVI         |             Ludovina ; Porto ; Lua             |
| Capítulo XVII        |          Ludovina ; Porto ; Celorico           |
| Conclusão            |          Ludovina ; Celorico ; Porto           |



</details>

### O regicida
<details id="Camilo-O_regicida.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |        O regicida         | Camilo-O_regicida.txt                |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      63611 |    3028    |       3537 |   ~  15.2 palavras | 2868       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  194 |      dizer | disseram; dizer; dizia; dize; diria                |
|  187 |        ter | tem; têm; terei; tenham; tido                      |
|  142 |      saber | sabe; saberei; sabendo; sabia; sabemos             |
|  134 |      fazer | fazendo; faziam; feitos; fizeram; faz              |
|  112 |        dar | dadas; davam; darei; der; daria                    |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Domingos Leite         226 | Lisboa                 72 |
| D. João IV              76 | Madrid                 55 |
| Maria Isabel            76 | Portugal               42 |
| Roque da Cunha          61 | Espanha                29 |
| Maria                   39 | Estado                 27 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Capítulo I           |         Lisboa ; Guimarães ; Portugal          |
| Capítulo II          |         Lisboa ; Portugal ; Guimarães          |
| Capítulo III         |         Lisboa ; Portugal ; Guimarães          |
| Capítulo IV          |          Lisboa ; Portugal ; Limoeiro          |
| Capítulo V           |      Lisboa ; Paço da Ribeira ; Portugal       |
| Capítulo VI          |      Lisboa ; Paço da Ribeira ; Portugal       |
| Capítulo VII         |      Lisboa ; Paço da Ribeira ; Portugal       |
| Capítulo VIII        |      Lisboa ; Portugal ; Paço da Ribeira       |
| Capítulo IX          |           Lisboa ; Portugal ; Madrid           |
| Capítulo X           |           Lisboa ; Madrid ; Portugal           |
| Capítulo XI          |           Lisboa ; Madrid ; Portugal           |
| Capítulo XII         |           Lisboa ; Madrid ; Portugal           |
| Capítulo XIII        |           Madrid ; Lisboa ; Portugal           |
| Capítulo XIV         |           Madrid ; Lisboa ; Portugal           |
| Capítulo XV          |           Lisboa ; Madrid ; Portugal           |
| Capítulo XVI         |           Lisboa ; Madrid ; Portugal           |
| Capítulo XVII        |           Lisboa ; Madrid ; Portugal           |
| Capítulo XVIII       |           Lisboa ; Madrid ; Portugal           |
| Capítulo XIX         |           Lisboa ; Madrid ; Portugal           |
| Capítulo XX          |           Lisboa ; Madrid ; Portugal           |
| Capítulo XXI         |           Lisboa ; Madrid ; Portugal           |
| Conclusão            |           Lisboa ; Madrid ; Portugal           |



</details>

### O retrato de Ricardina-v1
<details id="Camilo-O_retrato_de_Ricardina-v1.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | O retrato de Ricardina-v1 | Camilo-O_retrato_de_Ricardina-v1.txt |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> O RETRATO DE RICARDINA
>Camilo Castelo Branco
>
>ÍNDICE
>A quem ler
>I – O abade de Espinho
>II – Um amigo!
>III – Reacções
>IV – Bernardo Moniz
>V – Mãe e filha
>VI – Agonias
>VII – O que ela pedia a Jesus
>VIII – O bem-fazer da morte
>IX –
> Até que enfim!
>X – A sorte
>XI –

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      65068 |    3130    |       4058 |   ~  12.7 palavras | 2105       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  321 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  218 |        ter | tem; têm; tinha; terei; ter                        |
|  161 |      saber | sabe; sabes; sabendo; sabemos; sabia               |
|  143 |     querer | queiram; querer; queres; quer; querendo            |
|  127 |      fazer | fazendo; faziam; feitos; fizeram; faz              |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Ricardina              124 | Coimbra                36 |
| Bernardo                81 | Viseu                  26 |
| Alexandre               64 | Espinho                23 |
| Bernardo Moniz          60 | Lisboa                 18 |
| Norberto                49 | Espanha                15 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |     Espinho ; diocese de Viseu ; Astúrias      |
| *                    |      Espinho ; Coimbra ; diocese de Viseu      |
| II                   |      Espinho ; Coimbra ; diocese de Viseu      |
| III                  |           Espinho ; Coimbra ; Viseu            |
| IV                   |           Coimbra ; Espinho ; Lisboa           |
| V                    |           Coimbra ; Espinho ; Lisboa           |
| VI                   |           Coimbra ; Espinho ; Lisboa           |
| VII                  |           Espinho ; Coimbra ; Lisboa           |
| VIII                 |           Espinho ; Coimbra ; Lisboa           |
| IX                   |           Espinho ; Coimbra ; Lamego           |
| X                    |           Coimbra ; Espinho ; Lamego           |
| XI                   |           Coimbra ; Espinho ; Lamego           |
| XII                  |           Coimbra ; Espinho ; Viseu            |
| XIII                 |           Coimbra ; Espinho ; Viseu            |
| XIV                  |           Coimbra ; Espinho ; Viseu            |
| XV                   |           Coimbra ; Espinho ; Viseu            |
| XVI                  |           Coimbra ; Espinho ; Viseu            |
| XVII                 |           Coimbra ; Viseu ; Espinho            |
| XVIII                |           Coimbra ; Viseu ; Espinho            |
| XIX                  |           Coimbra ; Viseu ; Espinho            |
| XX                   |           Coimbra ; Viseu ; Espinho            |
| XXI                  |           Coimbra ; Viseu ; Espinho            |
| XXII                 |           Coimbra ; Viseu ; Espinho            |
| XXIII                |           Coimbra ; Viseu ; Espinho            |
| XXIV                 |           Coimbra ; Viseu ; Espinho            |
| XXV                  |           Coimbra ; Viseu ; Espinho            |
| XXVI                 |           Coimbra ; Viseu ; Espinho            |
| XXVII                |           Coimbra ; Viseu ; Espinho            |
| XXVIII               |           Coimbra ; Viseu ; Espinho            |



</details>

### O romance dum homem rico
<details id="Camilo-O_romance_dum_homem_rico.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | O romance dum homem rico  | Camilo-O_romance_dum_homem_rico.txt  |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      66692 |    3094    |       3653 |   ~  15.3 palavras | 2036       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  375 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  235 |        ter | tem; têm; terei; tido; teria                       |
|  142 |        ver | verem; via; verá; vinham; viu                      |
|  125 |      poder | pode; podiam; poderei; poder; podem                |
|  123 |        dar | davam; darei; der; daria; dá                       |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Álvaro                 253 | Lisboa                 70 |
| Leonor                 164 | Olivais                22 |
| Maria da Glória        122 | Eufêmia                21 |
| Deus                    68 | Vila do Conde          17 |
| Maria                   52 | Álvaro                 12 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |            Eufêmia ; Lisboa ; Macau            |
| II                   |            Eufêmia ; Lisboa ; Macau            |
| III                  |            Eufêmia ; Lisboa ; Macau            |
| IV                   |            Lisboa ; Eufêmia ; Macau            |
| V                    |            Lisboa ; Eufêmia ; Macau            |
| VI                   |            Lisboa ; Eufêmia ; Macau            |
| VII                  |            Lisboa ; Eufêmia ; Macau            |
| VIII                 |        Lisboa ; Eufêmia ; Vila do Conde        |
| IX                   |        Lisboa ; Vila do Conde ; Eufêmia        |
| X                    |        Lisboa ; Vila do Conde ; Eufêmia        |
| XI                   |        Lisboa ; Vila do Conde ; Eufêmia        |
| XII                  |        Lisboa ; Vila do Conde ; Eufêmia        |
| XIII                 |        Lisboa ; Vila do Conde ; Eufêmia        |
| XIV                  |        Lisboa ; Vila do Conde ; Eufêmia        |
| XV                   |        Lisboa ; Vila do Conde ; Olivais        |
| XVI                  |        Lisboa ; Vila do Conde ; Olivais        |
| XVII                 |        Lisboa ; Vila do Conde ; Olivais        |
| XVIII                |        Lisboa ; Vila do Conde ; Olivais        |
| XIX                  |        Lisboa ; Vila do Conde ; Olivais        |
| XX                   |        Lisboa ; Vila do Conde ; Olivais        |
| FIM                  |        Lisboa ; Vila do Conde ; Olivais        |



</details>

### Onde esta a felicidade
<details id="Camilo-Onde_esta_a_felicidade.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |  Onde esta a felicidade   | Camilo-Onde_esta_a_felicidade.txt    |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      94748 |    3847    |       6292 |   ~  12.2 palavras | 2195       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  458 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  409 |        ter | tem; têm; terei; tido; teria                       |
|  286 |     querer | querer; queres; quer; querido; querendo            |
|  251 |      fazer | fazendo; faziam; feitos; fizeram; faz              |
|  244 |      poder | poderiam; pode; podiam; poderei; poder             |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Augusta                133 | Augusta                60 |
| Guilherme              109 | Porto                  38 |
| Amaral                  91 | Rua dos Arménios       28 |
| Francisco               50 | Lisboa                 19 |
| Guilherme do Amaral     44 | Estás                  12 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| II                   |             Lisboa ; Porto ; Viseu             |
| III                  |             Lisboa ; Porto ; Viseu             |
| IV                   |             Lisboa ; Porto ; Viseu             |
| V                    |             Porto ; Lisboa ; Viseu             |
| VI                   |       Porto ; Lisboa ; Rua dos Arménios        |
| VII                  |       Porto ; Lisboa ; Rua dos Arménios        |
| VIII                 |       Porto ; Lisboa ; Rua dos Arménios        |
| IX                   |       Porto ; Augusta ; Rua dos Arménios       |
| X                    |       Porto ; Augusta ; Rua dos Arménios       |
| XI                   |       Porto ; Augusta ; Rua dos Arménios       |
| XII                  |       Porto ; Augusta ; Rua dos Arménios       |
| XIII                 |       Augusta ; Porto ; Rua dos Arménios       |
| XIV                  |       Augusta ; Porto ; Rua dos Arménios       |
| XV                   |       Augusta ; Porto ; Rua dos Arménios       |
| XVI                  |       Augusta ; Porto ; Rua dos Arménios       |
| XVII                 |       Augusta ; Porto ; Rua dos Arménios       |
| XVIII                |       Augusta ; Porto ; Rua dos Arménios       |
| XIX                  |       Augusta ; Porto ; Rua dos Arménios       |
| XX                   |       Augusta ; Porto ; Rua dos Arménios       |
| XXI                  |       Augusta ; Porto ; Rua dos Arménios       |
| XXII                 |       Augusta ; Porto ; Rua dos Arménios       |
| XXIII                |       Augusta ; Porto ; Rua dos Arménios       |
| XXIV                 |       Augusta ; Porto ; Rua dos Arménios       |
| XXV                  |       Augusta ; Porto ; Rua dos Arménios       |
| XXVI                 |       Augusta ; Porto ; Rua dos Arménios       |
| XXVII                |       Augusta ; Porto ; Rua dos Arménios       |
| XXVIII               |       Augusta ; Porto ; Rua dos Arménios       |
| XXIX                 |       Augusta ; Porto ; Rua dos Arménios       |
| XXX                  |       Augusta ; Porto ; Rua dos Arménios       |



</details>

### Poesia ou Dinheiro-Teatro
<details id="Camilo-Poesia_ou_Dinheiro-Teatro.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | Poesia ou Dinheiro-Teatro | Camilo-Poesia_ou_Dinheiro-Teatro.txt |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>Poesia ou Dinheiro?

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      10209 |    592     |       1080 |   ~   6.9 palavras | 272        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   56 |        ter | tem; têm; tinha; terei; ter                        |
|   33 |      poder | pode; poder; posso; podemos; poderia               |
|   29 |     querer | querer; queres; quer; quis; quero                  |
|   26 |      fazer | fazendo; faz; feito; faria; fez                    |
|   23 |      dizer | dizer; dizia; diz; digo; disse                     |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Carlos                  13 | Henriqueta              8 |
| Júlio                   12 | Brasil                  2 |
| V. Exª                   9 | Júlio                   2 |
| Manuel Alves             8 | Escreveste              1 |
| Júlio Correia            6 | Leste                   1 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]


##### Capítulos não encontrados.



</details>

### Purgatorio e Paraiso-Teatro
<details id="Camilo-Purgatorio_e_Paraiso-Teatro.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo | Purgatorio e Paraiso-Teatro | Camilo-Purgatorio_e_Paraiso-Teatro.txt |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>Purgatório e Paraíso
>Drama em 3 actos

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      15164 |    837     |       1581 |   ~   7.2 palavras | 626        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   71 |        ter | tem; têm; tinha; terei; ter                        |
|   55 |      saber | sabe; sabendo; sabia; soube; sabido                |
|   53 |      dizer | dizer; diria; diz; digo; disse                     |
|   49 |     querer | queres; quer; querendo; querem; quis               |
|   34 |      poder | pode; podiam; podem; posso; poderá                 |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Luísa                   34 | Lisboa                 11 |
| Jorge                   22 | Évora                   6 |
| Alfredo                 16 | Mascarenhas             3 |
| D. Emília               14 | Benfica                 2 |
| D.                      11 | Luanda                  2 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| PURGATÓRIO E PARAÍSO |                 Lisboa ; Porto                 |



</details>

### Teatro-Vol 1
<details id="Camilo-Teatro-Vol_1.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |       Teatro-Vol 1        | Camilo-Teatro-Vol_1.txt              |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      54600 |    2303    |       5206 |   ~   7.9 palavras | 2020       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  170 |        ter | tem; têm; tinha; terei; ter                        |
|   99 |      saber | saberão; sabe; sabemos; sabia; saiba               |
|   92 |      dizer | dirá; disseram; dizer; dizia; diria                |
|   89 |      haver | haja; houve; houver; haverá; havido                |
|   87 |        ser | seja; era; fosse; serei; foram                     |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| D. Guiomar              51 | Portugal               14 |
| Deus                    27 | Lisboa                  7 |
| D. Guterres             26 | Porto                   5 |
| Ezequiel                24 | hei-de                  5 |
| Mestre Gil              22 | Soror                   3 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| FIM                  |       Carcereiro ; Portugal ; Inquiridor       |
| FIM                  |       Carcereiro ; Portugal ; Inquiridor       |
| EDIÇÕES DAS DUAS PEÇAS |       Carcereiro ; Portugal ; Inquiridor       |
| AGOSTINHO DE CEUTA   |         Carcereiro ; Portugal ; Lisboa         |
| O MARQUÊS DE TORRES-NOVAS |         Carcereiro ; Lisboa ; Portugal         |



</details>

### Teatro-Vol 2
<details id="Camilo-Teatro-Vol_2.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |       Teatro-Vol 2        | Camilo-Teatro-Vol_2.txt              |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      48104 |    2024    |       5074 |   ~   7.1 palavras | 1869       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  220 |        ter | tem; têm; tinha; terei; ter                        |
|  151 |     querer | querer; queres; quer; querendo; querem             |
|  148 |      poder | pode; podiam; poderei; poder; podem                |
|  123 |      saber | sabe; saberei; sabendo; sabia; saiba               |
|  122 |      dizer | dizer; dizia; diria; diz; digo                     |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Luís                    35 | Lisboa                 18 |
| V. Exª                  34 | Porto                  13 |
| Luísa                   34 | Henriqueta              9 |
| D. Inês                 30 | Brasil                  6 |
| Deus                    24 | Évora                   6 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Já?!                 |        Mascarenhas ; Lisboa ; Boleeiro         |



</details>

### Um homem de brios
<details id="Camilo-Um_homem_de_brios.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |     Um homem de brios     | Camilo-Um_homem_de_brios.txt         |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      71768 |    3370    |       4449 |   ~  13.3 palavras | 1775       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  294 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  257 |      poder | poderiam; pode; podiam; poderei; poder             |
|  238 |      fazer | fazendo; faziam; fazerem; fizeram; faz             |
|  225 |      saber | saberia; sabe; sabendo; sabia; saberem             |
|  224 |        ter | tem; têm; terei; tenham; teria                     |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Amaral                 143 | Lisboa                 51 |
| Guilherme               84 | Augusta                51 |
| Augusta                 67 | Porto                  33 |
| Vossa Excelência        63 | Amares                 17 |
| Guilherme do Amaral     57 | Rua dos Arménios       17 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| Capítulo I           |       Lisboa ; Porto ; Rua dos Arménios        |
| Capítulo II          |       Lisboa ; Porto ; Rua dos Arménios        |
| Capítulo III         |       Lisboa ; Rua dos Arménios ; Porto        |
| Capítulo IV          |       Lisboa ; Rua dos Arménios ; Porto        |
| Capítulo V           |       Lisboa ; Rua dos Arménios ; Porto        |
| Capítulo VI          |       Lisboa ; Porto ; Rua dos Arménios        |
| Capítulo VII         |       Lisboa ; Rua dos Arménios ; Porto        |
| Capítulo VIII        |       Lisboa ; Porto ; Rua dos Arménios        |
| Capítulo IX          |       Lisboa ; Porto ; Rua dos Arménios        |
| Capítulo X           |       Lisboa ; Porto ; Rua dos Arménios        |
| Capítulo XI          |       Lisboa ; Porto ; Rua dos Arménios        |
| Capítulo XII         |       Lisboa ; Porto ; Rua dos Arménios        |
| Capítulo XIII        |       Lisboa ; Porto ; Rua dos Arménios        |
| Capítulo XIV         |            Lisboa ; Porto ; Augusta            |
| Capítulo XV          |            Lisboa ; Porto ; Augusta            |
| Capítulo XVI         |            Lisboa ; Porto ; Augusta            |
| Capítulo XVII        |            Lisboa ; Porto ; Augusta            |
| Capítulo XVIII       |            Lisboa ; Porto ; Augusta            |
| Capítulo XIX         |            Lisboa ; Porto ; Augusta            |
| Capítulo XX          |            Lisboa ; Porto ; Augusta            |
| Capítulo XXI         |            Lisboa ; Porto ; Augusta            |
| Capítulo XXII        |            Lisboa ; Porto ; Augusta            |
| Capítulo XXIII       |            Lisboa ; Augusta ; Porto            |
| Conclusão            |            Lisboa ; Augusta ; Porto            |



</details>

### Um livro
<details id="Camilo-Um_livro.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |         Um livro          | Camilo-Um_livro.txt                  |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      49608 |    2214    |       2613 |   ~  13.9 palavras | 630        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  129 |        ter | tem; têm; tinha; ter; temos                        |
|  109 |        ver | via; viam; vê; viu; vi                             |
|  108 |      poder | pode; podiam; pôde; podem; posso                   |
|   97 |      dizer | disseram; dizer; dizia; diria; diz                 |
|   79 |      haver | havia; houve; há; haveria; haver                   |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Deus                    40 | Lua                     9 |
| Senhor                   5 | Tejo                    5 |
| Quero                    4 | Sol                     3 |
| torva                    4 | Hás-de                  3 |
| Lucinda                  4 | Lisboa                  2 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| DE                   |       Lisboa ; Morgado de Fafe ; Coimbra       |
| I                    |       Lisboa ; Morgado de Fafe ; Coimbra       |
| II                   |              Lua ; Tejo ; Lisboa               |
| III                  |              Tejo ; Lua ; Lisboa               |
| IV                   |              Tejo ; Lua ; Lisboa               |
| V                    |              Tejo ; Lua ; Lisboa               |
| VI                   |              Lua ; Tejo ; Lisboa               |
| VII                  |              Lua ; Tejo ; Lisboa               |
| VIII                 |              Lua ; Tejo ; Lisboa               |
| IX                   |              Lua ; Tejo ; Lisboa               |
| X                    |              Lua ; Tejo ; Lisboa               |
| XI                   |              Lua ; Tejo ; Lisboa               |
| XII                  |              Lua ; Tejo ; Lisboa               |
| XIII                 |              Lua ; Tejo ; Lisboa               |
| XIV                  |              Lua ; Tejo ; Lisboa               |
| XV                   |              Lua ; Tejo ; Lisboa               |
| XVI                  |              Lua ; Tejo ; Lisboa               |
| XVII                 |              Lua ; Tejo ; Lisboa               |
| XVIII                |              Lua ; Tejo ; Lisboa               |
| XIX                  |              Lua ; Tejo ; Lisboa               |
| XX                   |              Lua ; Tejo ; Lisboa               |
| XXI                  |              Lua ; Tejo ; Lisboa               |
| XXII                 |              Lua ; Tejo ; Lisboa               |
| XXIII                |              Lua ; Tejo ; Lisboa               |
| XXIV                 |              Lua ; Tejo ; Lisboa               |
| XXV                  |              Lua ; Tejo ; Hás-de               |
| I                    |              Lua ; Tejo ; Hás-de               |
| II                   |              Lua ; Tejo ; Hás-de               |
| III                  |              Lua ; Tejo ; Hás-de               |
| IV                   |              Lua ; Tejo ; Hás-de               |
| V                    |              Lua ; Tejo ; Hás-de               |
| VI                   |              Lua ; Tejo ; Hás-de               |
| VII                  |              Lua ; Tejo ; Hás-de               |
| VIII                 |              Lua ; Tejo ; Hás-de               |
| IX                   |              Lua ; Tejo ; Hás-de               |
| X                    |              Lua ; Tejo ; Hás-de               |
| XI                   |              Lua ; Tejo ; Hás-de               |
| XII                  |              Lua ; Tejo ; Hás-de               |
| XIII                 |              Lua ; Tejo ; Hás-de               |
| XIV                  |              Lua ; Tejo ; Hás-de               |
| XV                   |              Lua ; Tejo ; Hás-de               |
| XVI                  |              Lua ; Tejo ; Hás-de               |
| XVII                 |              Lua ; Tejo ; Hás-de               |
| FIM                  |              Lua ; Tejo ; Hás-de               |



</details>

### Uma praga rogada
<details id="Camilo-Uma_praga_rogada.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |     Uma praga rogada      | Camilo-Uma_praga_rogada.txt          |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|       7073 |    537     |        428 |   ~  13.8 palavras | 174        |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|   22 |        ter | tinha; terei; ter; tive; tivesse                   |
|   19 |      poder | pode; pôde; poder; podem; podemos                  |
|   19 |      fazer | faz; fizera; fez; fazer; faça                      |
|   16 |        ver | via; viu; vê; vendo; visto                         |
|   15 |      haver | havia; há; houve                                   |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Bernardo                26 | Viseu                   3 |
| Eulália                 13 | Lucena                  1 |
| João Leite              12 | salto de tigre          1 |
| Paulo Botelho           11 | Eulália                 1 |
| Francisco de Lucena     10 | Supunha                 1 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |                     Viseu                      |
| II                   |                     Viseu                      |
| III                  |                     Viseu                      |
| IV                   |                 Viseu ; Lucena                 |
| V                    |                 Viseu ; Lucena                 |
| VI                   |            Viseu ; Lucena ; Eulália            |
| VII                  |            Viseu ; Lucena ; Eulália            |
| VIII                 |            Eulália ; Viseu ; Lucena            |
| IX                   |            Eulália ; Viseu ; Lucena            |
| X                    |            Eulália ; Viseu ; Lucena            |
| XI                   |            Eulália ; Viseu ; Lucena            |
| XII                  |            Eulália ; Viseu ; Lucena            |
| XIII                 |            Eulália ; Viseu ; Lucena            |
| XIV                  |            Eulália ; Viseu ; Lucena            |
| XV                   |            Eulália ; Viseu ; Lucena            |
| CONCLUSÃO            |            Viseu ; Eulália ; Lucena            |
| REMATE               |            Viseu ; Eulália ; Lucena            |
| FIM                  |            Viseu ; Eulália ; Lucena            |



</details>

### Vinganca
<details id="Camilo-Vinganca.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |         Vinganca          | Camilo-Vinganca.txt                  |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco
>
>Vingança
>
>
>Selecção e notas de Alexandre Cabral

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      60744 |    2829    |       3370 |   ~  15.0 palavras | 1731       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  352 |      dizer | disseram; dizer; dizia; diria; diz                 |
|  235 |        ter | tem; têm; tido; teria; tiver                       |
|  200 |      fazer | fazendo; faziam; fazerem; fizeram; faz             |
|  155 |      poder | pode; poderem; podiam; poderei; poder              |
|  150 |     querer | quiseram; querer; queres; quer; queiram            |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Vossa Excelência        69 | Lisboa                 43 |
| Roberto                 67 | barão da Penha         43 |
| Isaura                  52 | Porto                  41 |
| Bernardo da Veiga       47 | Isaura                 28 |
| Roberto Soares          44 | Portugal               19 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |         Lisboa ; Rossio ; em Portugal          |
| II                   |         Lisboa ; Rossio ; em Portugal          |
| III                  |        Porto ; Lisboa ; barão da Penha         |
| IV                   |        Porto ; Lisboa ; barão da Penha         |
| V                    |        Porto ; Lisboa ; barão da Penha         |
| VI                   |           Porto ; Lisboa ; Portugal            |
| VII                  |           Porto ; Lisboa ; Portugal            |
| VIII                 |           Porto ; Lisboa ; Portugal            |
| IX                   |       Porto ; Portugal ; barão da Penha        |
| X                    |       Porto ; Portugal ; barão da Penha        |
| XI                   |       Porto ; Portugal ; barão da Penha        |
| XII                  |       Porto ; barão da Penha ; Portugal        |
| XIII                 |        Porto ; barão da Penha ; Lisboa         |
| XIV                  |        Porto ; barão da Penha ; Lisboa         |
| XV                   |        Porto ; barão da Penha ; Lisboa         |
| XVI                  |        Lisboa ; Porto ; barão da Penha         |
| XVII                 |        Lisboa ; Porto ; barão da Penha         |
| XVIII                |        Lisboa ; barão da Penha ; Porto         |
| XIX                  |        Lisboa ; barão da Penha ; Porto         |
| XX                   |        Lisboa ; barão da Penha ; Porto         |
| XXI                  |        Lisboa ; barão da Penha ; Porto         |
| XXII                 |        Lisboa ; barão da Penha ; Porto         |
| XXIII                |        Lisboa ; barão da Penha ; Porto         |
| XX1V                 |        barão da Penha ; Lisboa ; Porto         |



</details>

### Vinte horas de liteira
<details id="Camilo-Vinte_horas_de_liteira.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |  Vinte horas de liteira   | Camilo-Vinte_horas_de_liteira.txt    |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> 
> Camilo Castelo Branco

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      66223 |    3148    |       3534 |   ~  15.7 palavras | 1769       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  221 |        ter | tem; têm; tenham; tido; teria                      |
|  214 |      dizer | disseram; dizer; dizia; diz; diziam                |
|  147 |      haver | haja; houve; haviam; haverá; haver                 |
|  137 |      fazer | fazendo; faziam; fazerem; fizeram; faz             |
|  126 |      saber | sabe; sabíamos; sabendo; sabia; saberem            |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| António Joaquim         76 | Brasil                 32 |
| Teresa                  38 | Porto                  29 |
| Deus                    33 | Braga                  22 |
| Francisco Elisiário     28 | Lisboa                 16 |
| Adriana                 23 | Portugal               15 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| INTRODUÇÃO           |             Minho ; Braga ; Daqui              |
| CAPÍTULO I           |             Braga ; Minho ; Daqui              |
| CAPÍTULO II          |             Braga ; Minho ; Daqui              |
| CAPÍTULO III         |             Braga ; Minho ; Brasil             |
| CAPÍTULO IV          |             Braga ; França ; Minho             |
| CAPÍTULO V           |             Braga ; França ; Minho             |
| AQUI JAZ             |             Braga ; França ; Minho             |
| MARIA GOMES,         |             Braga ; França ; Minho             |
| NASCIDA NESTA FREGUESIA EM 1760, |             Braga ; França ; Minho             |
| SUA FILHA ROSALINDA  |             Braga ; França ; Minho             |
| MANDOU ERIGIR        |             Braga ; França ; Minho             |
| ESTA CRUZ SOBRE A SUA LOUSA |             Braga ; França ; Minho             |
| CAPÍTULO VI          |             Braga ; França ; Minho             |
| CAPÍTULO VII         |          Braga ; França ; Felicidade           |
| CAPÍTULO VIII        |            Braga ; Brasil ; França             |
| CAPÍTULO IX          |            Brasil ; Braga ; França             |
| CAPÍTULO X           |           Brasil ; Braga ; Portugal            |
| CAPÍTULO XI          |           Brasil ; Braga ; Portugal            |
| CAPÍTULO XII         |           Brasil ; Braga ; Portugal            |
| CAPÍTULO XIII        |           Brasil ; Braga ; Portugal            |
| CAPÍTULO XIV         |           Brasil ; Braga ; Portugal            |
| CAPÍTULO XV          |           Braga ; Brasil ; Portugal            |
| CAPÍTULO XVI         |           Braga ; Brasil ; Portugal            |
| CAPÍTULO XVII        |           Braga ; Brasil ; Portugal            |
| CAPÍTULO XVIII       |             Braga ; Brasil ; Porto             |
| CAPÍTULO XIX         |             Braga ; Brasil ; Porto             |
| CAPÍTULO XX          |             Braga ; Brasil ; Porto             |
| CAPÍTULO XXI         |             Braga ; Brasil ; Porto             |
| CAPÍTULO XXII        |             Braga ; Brasil ; Porto             |
| CAPÍTULO XXIII       |             Porto ; Braga ; Brasil             |
| CAPÍTULO XXIV        |             Porto ; Braga ; Brasil             |
| CAPÍTULO XXV         |             Porto ; Braga ; Brasil             |
| EPÍLOGO              |             Brasil ; Porto ; Braga             |



</details>

### Vulcoes de lama
<details id="Camilo-Vulcoes_de_lama.txt">
	<summary>expanda para detalhes</summary>

#### metadata

|   Autor |          Título           | Ficheiro                             |
| -------:|:-------------------------:|:------------------------------------ |
|  Camilo |      Vulcoes de lama      | Camilo-Vulcoes_de_lama.txt           |

#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]
> Camilo Castelo Branco
>
>Vulcões de Lama
>
>
>
>Razão do título
> Todavia, há aí na casca do planeta paixões humanas cujo símile não o dá o Vesúvio, o Hecla nem o Etna.

#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]

|  nº tokens | nº verbos  | nº frases  | tamanho de frases  | nº ents    |
| ---------- | ---------- | ---------- | ------------------ | ---------- |
|      41841 |    2354    |       1977 |   ~  18.0 palavras | 1211       |

#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]

| freq |      lemma | ex. não ordenado de flexões                        |
| ----:| ----------:|:-------------------------------------------------- |
|  144 |        ter | tem; têm; tinha; terei; ter                        |
|  112 |      dizer | dirá; dizer; dizia; diria; diz                     |
|  100 |      poder | pode; podiam; poderei; poder; pôde                 |
|   83 |      fazer | fazendo; faziam; fizeram; faz; feito               |
|   73 |        ver | via; vinham; viam; vê; viu                         |


#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]

|     top 5 Personagens      |     top 5 Localidades     |
|:-------------------------- |:------------------------- |
| Balbina                 49 | Porto                  18 |
| Deus                    42 | Canastreiro            13 |
| Frei Joaquim            21 | Fermedo                11 |
| Roberto                 20 | Toqueriné              10 |
| Artur                   18 | Espinho                10 |

#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]

| Capítulo             |               top 3 Localidades                |
|:-------------------- |:---------------------------------------------- |
| I                    |            Porto ; Fermedo ; Arouca            |
| II                   |          Canastreiro ; Porto ; Arouca          |
| III                  |          Canastreiro ; Porto ; Arouca          |
| IV                   |        Canastreiro ; Porto ; Toqueriné         |
| V                    |          Porto ; Canastreiro ; Arouca          |
| VI                   |          Porto ; Canastreiro ; Arouca          |
| VII                  |         Porto ; Canastreiro ; Melitão          |
| VIII                 |        Porto ; Canastreiro ; Toqueriné         |
| IX                   |         Porto ; Canastreiro ; Fermedo          |



</details>




## Considerações finais

Dada a diferença na padronização da formatação das obras na pasta `./Obra`,
seria interessante o pré-processamento destes para melhorar análises textuais.


Cabe salientar que me detive na qualidade da saída de Amor de Perdição, 
posto que teria algumas sugestões de alteração no texto as quais estão em
`./proposta.sh`. _Outputs_ como a **A Brasileira de Prazin** e **A enjeitada** 
parecem bem formadas, mas outras como _A senhora Rattazzi_ ou _Anatema 1_ falham 
seja por detectarem **ents** que não se encaixam nos conceitos, seja porque os
capítulos são errôneamente atribuídos.

Reforço então a sugestão de padronização de estilo para que análises automáticas
resultem mais refinadas.

