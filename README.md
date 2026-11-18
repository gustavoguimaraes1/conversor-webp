# Conversor de Imagens para WebP

Script em **Python** para automatizar a conversão de imagens PNG, JPG, JPEG e SVG para o formato WebP, com foco na otimização de arquivos de imagem utilizados em aplicações web.

O projeto permite processar múltiplas imagens, incluindo arquivos em subdiretórios, preservando a transparência quando aplicável e oferecendo configurações de qualidade e gerenciamento dos arquivos originais.

## Funcionalidades

- Conversão de imagens PNG, JPG, JPEG e SVG para WebP.
- Busca automática e recursiva de imagens.
- Preservação de transparência.
- Configuração da qualidade de compressão.
- Conversão de SVG utilizando CairoSVG.
- Verificação de arquivos WebP existentes para evitar sobrescrita.
- Remoção opcional dos arquivos originais.
- Tratamento de erros durante o processamento.
- Relatório final com a quantidade de conversões e erros.

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal |
| Pillow | Processamento e conversão de imagens |
| CairoSVG | Renderização de arquivos SVG |
| pathlib | Manipulação de diretórios e arquivos |
| BytesIO | Processamento de imagens na memória |

## Instalação

Clone o repositório:

```bash
git clone git@github.com:gustavoguimaraes1/conversor-webp.git
cd conversor-webp
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Linux ou macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install Pillow CairoSVG
```

**Observação:** o CairoSVG também depende de bibliotecas nativas do Cairo, que podem precisar ser instaladas no sistema operacional.

## Como utilizar

Por padrão, o script procura imagens no diretório `public/images`.

Exemplo de estrutura:

```text
conversor-webp/
├── public/
│   └── images/
│       ├── logo.png
│       ├── banner.jpg
│       ├── icon.svg
│       └── produtos/
│           └── produto.jpeg
└── conversor.py
```

Execute o script a partir da raiz do projeto:

```bash
python conversor.py
```

As imagens convertidas serão salvas nos mesmos diretórios dos arquivos originais.

```text
public/images/
├── logo.png
├── logo.webp
├── banner.jpg
├── banner.webp
├── icon.svg
├── icon.webp
└── produtos/
    ├── produto.jpeg
    └── produto.webp
```

## Configurações

As configurações podem ser modificadas diretamente no código:

```python
PASTA = Path("public/images")
EXTENSOES = {".png", ".jpg", ".jpeg", ".svg"}

QUALIDADE = 85
REMOVER_ORIGINAIS = False
```

| Parâmetro | Descrição |
|---|---|
| `PASTA` | Diretório utilizado para localizar as imagens |
| `EXTENSOES` | Formatos de entrada aceitos |
| `QUALIDADE` | Qualidade de compressão WebP, entre 0 e 100 |
| `REMOVER_ORIGINAIS` | Define se os arquivos originais serão excluídos após uma conversão bem-sucedida |

Por padrão, os arquivos originais são preservados. Para removê-los automaticamente após a conversão, altere:

```python
REMOVER_ORIGINAIS = True
```

**Atenção:** essa opção exclui os arquivos originais convertidos. Recomenda-se manter um backup.

## Funcionamento

O processo de conversão segue as seguintes etapas:

1. Verifica a existência do diretório configurado.
2. Localiza os arquivos com extensões compatíveis.
3. Verifica se a versão WebP já existe.
4. Processa a imagem utilizando Pillow.
5. Para arquivos SVG, utiliza CairoSVG para renderização em memória.
6. Ajusta o modo de cor conforme necessário.
7. Salva a imagem convertida no formato WebP.
8. Exibe o resultado do processamento.

### Exemplo de execução

```text
Imagens encontradas: 3

[OK] public/images/logo.png -> public/images/logo.webp
[OK] public/images/banner.jpg -> public/images/banner.webp
[OK] public/images/icon.svg -> public/images/icon.webp

========================================
CONVERSÃO FINALIZADA
========================================
Convertidas: 3
Erros: 0
Qualidade: 85
Remover originais: False
```

## Considerações técnicas

- O script utiliza `method=6` para priorizar o esforço de compressão oferecido pelo codificador WebP do Pillow.
- Imagens SVG são renderizadas com escala 2 antes de serem convertidas.
- Arquivos WebP já existentes não são sobrescritos.
- O processamento é realizado individualmente, permitindo continuar a execução mesmo quando ocorre um erro em determinado arquivo.
- A conversão não garante redução de tamanho em todos os casos, especialmente em imagens que já possuem compressão eficiente.
- O script não altera automaticamente as referências das imagens no código de aplicações web.

## Licença

Consulte o arquivo `LICENSE` disponível neste repositório para verificar os termos de uso e distribuição.

---

Desenvolvido por [Gustavo Guimarães](https://github.com/gustavoguimaraes1), com auxílio de Inteligência Artificial.
