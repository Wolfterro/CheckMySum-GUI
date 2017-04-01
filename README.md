# CheckMySum GUI
## Um simples visualizador de checksum em PyQt4!

### Descrição:

###### Este é um simples programa escrito em Python e que utiliza o PyQt4 para a criação de uma interface gráfica para o usuário.

###### Este programa é capaz de computar alguns dos mais comuns tipos de algoritmos de hash disponíveis na biblioteca 'hashlib' da linguagem Python.

###### No programa, você poderá escolher um dos algoritmos disponíveis (md5, sha1, sha224, sha256, sha384, sha512) e o arquivo que será computado. Você também pode optar por mostrar a hash com letras maiúsculas, por padrão o resultado é exibido com letras minúsculas.

###### Você também poderá criar um arquivo de hash para o arquivo que você escolher analisar. Basta escolher um arquivo para ser criado ou um arquivo já existente e o programa, por padrão, irá acrescentar a hash no arquivo escolhido ou irá substituí-lo, se assim optar por esta opção.

###### O botão 'Copiar' irá copiar a hash gerada no campo ao lado do botão e irá armazená-la na área de transferência (clipboard) do seu sistema

###### Eu criei este programa para ser utilizado no Windows mas poderá rodá-lo muito bem em outros sistemas operacionais (like GNU/Linux, BSD e OSX), contanto que tenha o Python 2 e o PyQt4 instalados.

###### Este programa é baseado em outro programa meu, [CheckMySum](https://github.com/Wolfterro/CheckMySum). O programa original é voltado apenas para interfaces de linha de comando.

######

![CheckMySum GUI](http://i.imgur.com/HJ3gcr6.png)

### Requerimentos:

#### Compilando:
- Python 2.7
- PyQt4 para Python 2.7
- PyInstaller
- Microsoft Visual C++ 2010 Redistributable (Windows apenas)

##### Para compilar este programa no Windows, apenas execute o arquivo 'build.bat'.
##### Para compilar este programa no Linux, apenas execute o arquivo 'build.sh'.
##### **OBS**: O PyInstaller deve ser reconhecido como comando interno no Prompt de Comando do Windows ou no shell que você estiver utilizando no GNU/Linux ou em outros sistemas operacionais UNIX-like.

#### Executando diretamente:

##### Você pode executar este programa diretamente do código-fonte se você não quiser compilar ou caso não tenha o PyInstaller:

    python2 src/CheckMySumGUI.py

### Download:

##### **OBS**: Arquivos binários não requerem que você possua o Python ou o PyQt4 instalados!
#### ***Binário (Windows):*** https://github.com/Wolfterro/CheckMySum-GUI/releases/tag/v1.0.0-Windows
#### ***Código-fonte:*** https://github.com/Wolfterro/CheckMySum-GUI/archive/master.zip
