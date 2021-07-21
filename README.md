# Propriedades de Transporte em Sistemas com Baixa dimensionalidade

<div style="text-align: justify">

<p>
A <em>Teoria de localização de Anderson,</em> em referência a <a class="gat" href="https://pt.wikipedia.org/wiki/Philip_Warren_Anderson" title="P.W. Anderson" data-cat="related-question">P.W. Anderson</a>, é uma fenomenologia que trata de efeitos de desordem na função de onda eletrônica. O modelo criado por <em> Anderson</em> permitia estudar transições entre os estados metálicos e isolantes da matéria. O modelo de Anderson trata de elétrons se movendo sobre a influência de um potencial aleatório. Este modelo mostrou que a natureza dos estados eletrônicos apresenta uma dependência grande com o grau de desordem do potencial: <br>
Um sistema com potencial com alto grau de desordem apresenta estados eletrônicos ficam "represados" são exponencialmente localizados e o material torna-se isolante. Quando o potencial apresenta uma fraca desordem os estados eletrônicos são extendidos e o material torna-se metálico. 
</p><br>
<p>
Uma forma de estudar esses sistemas é calcular quantidades que medem o grau de localização de autoestados do <a class="gat" href="https://pt.wikipedia.org/wiki/Sistema_hamiltoniano" title="sistema hamiltoniano" data-cat="related-question">hamiltoniano</a> do sistema como a participação: <em>número de sítios que efetivamente participam do estado eletrônico.</em> Um modelo esquemático que representa o sistema é:
</p>
</div>

<p align="center">
<br>
<img src="img/canalSimples.png"/>
<br>
</p>

um conjunto de N átomos, cada átomo interage com o seu vizinho, apresentando uma *energia de hopping* T.

## O hamiltoniano do sistema:

<div align='center'>
<img src="img/hamiltonian.svg">
</div>

em que  <img src="img/e_i.svg"> é a energia potencial oriunda do potencial de ionização e 
T é o termo cinético e N é o tamanho da cadeia. A interação entre sítios ocorre apenas entre os primeiros vizinhos. A representação matricial do operador hamiltoniano é:

<div align='center'>
<img src="img/matrixHamiltonian.svg">
</div>

## Fenômenos de Localização:

Nós queremos encontrar os autoestados do hamiltoniano e estudar a dinâmica dos autoestados a partir do operador de evolução temporal do sistema e calcular a participação <img src="img/x_i.svg"> a partir da expressão:

<div align='center'>
<img src="img/part.svg">
</div>


Estamos interessados em estudar esse sistema considerando a série 
<img src="img/e_i.svg"> é uma série que obedece o seguinte parâmetro de desordem:

<div align='center'>
<img src="img/autocorr.svg">
</div>

em que <img src="img/y_i.svg"> é um número aleatório uniformemente distribuido no intervalo 
<img src="img/intervalo.svg"> e A é um parâmetro de ajuste. Adicionarei um repositório com o código do cálculo da correlação dda sequência <img src="img/y_i.svg"> com uma explicação mais detalhada da sequência

## Manipulando os arquivos:

O arquivo ```part_x_N.py``` relaciona a participação <img src="img/x_i.svg"> do sistema com o tamanho <img src="img/N.svg"> da cadeia de átomos. A relação é realizada para cada grau <img src="img/A.svg"> de desordem.
Para executar o arquivo python baixe os arquivos, ```requirements.txt``` e ```part_x_N.py```, abra o terminal crie um ambiente virtual e use o comando:

```
python3 -m pip install -r requirements.txt
```

em seguida é só rodar o código part_x_N.py com o comando:

```
python3 part_x_N.py
```
Um gráfico pode ser gerado no python, no entando, para fins de organização, gerei arquivos .dat para que pudéssemos gerar o gráfico no *XmGrace*

<p align="center">
<img width="460" height="300" src="img/xmgrace.gif">
</p>

[Momento da Física](https://www.instagram.com/momentodafisica/)