# 📊 Data Catalog Pipeline — Banco Central

Pipeline modular de catalogação automática de metadados de séries temporais financeiras do Banco Central do Brasil (BACEN), com geração de relatórios em linguagem natural via LLM.

> Projeto desenvolvido para simular um fluxo real de ingestão, perfilagem e catalogação de dados — prática central em equipes de Metadados e Data Governance.

---

## 🔍 O que esse projeto faz

1. **Ingere** séries temporais diretamente da API pública do BACEN (sem autenticação)
2. **Extrai metadados automaticamente** de cada série: tipo, nulos, cardinalidade, estatísticas
3. **Gera um relatório em linguagem natural** via LLM (Groq) descrevendo qualidade e padrões dos dados
4. **Exporta o catálogo** estruturado em `.json` e `.md` — prontos para consulta ou integração

---

## 💡 Por que isso importa

Empresas de dados lidam diariamente com centenas de datasets. Catalogar manualmente cada um é lento e propenso a erros. Este pipeline automatiza essa etapa: qualquer dataset novo entra no pipeline e sai com seu catálogo gerado — incluindo uma análise escrita por um modelo de linguagem.

É uma aplicação direta do conceito de **agente de dados**: ingestão → perfilagem → interpretação → documentação.

---

## 🗂️ Estrutura do projeto

```
data-catalog/
├── src/
│   ├── ingestor.py     # Busca séries temporais via API do BACEN
│   ├── profiler.py     # Extrai metadados: tipos, nulos, estatísticas
│   ├── reporter.py     # Chama o LLM (Groq) e gera relatório em linguagem natural
│   └── exporter.py     # Salva o catálogo em JSON e Markdown
├── output/             # Catálogos gerados (criado automaticamente)
├── main.py             # Orquestra o pipeline completo
├── requirements.txt
└── README.md
```

---

## 📈 Séries monitoradas (padrão)

| Série     | Código BACEN | Descrição                  |
|-----------|-------------|----------------------------|
| Selic     | 11          | Taxa básica de juros        |
| IPCA      | 433         | Inflação oficial (IBGE)     |
| Câmbio    | 1           | Dólar comercial (USD/BRL)  |
| IGP-M     | 189         | Inflação do mercado (FGV)  |
| PIB mensal| 4380        | Proxy de atividade econômica|

As séries são configuráveis no `src/ingestor.py` — qualquer código da API do BACEN pode ser adicionado.

---

## 🚀 Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/rubiamassaud/data-catalog-bacen
cd data-catalog-bacen
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure a chave da API do Groq

Crie uma conta gratuita em [console.groq.com](https://console.groq.com) e exporte sua chave:

```bash
export GROQ_API_KEY="sua_chave_aqui"
```

### 4. Execute o pipeline

```bash
python main.py --name "bacen_mercado" --dias 365
```

**Parâmetros disponíveis:**

| Parâmetro | Padrão           | Descrição                            |
|-----------|-----------------|--------------------------------------|
| `--name`  | `bacen_mercado` | Nome do dataset no catálogo          |
| `--dias`  | `365`           | Janela histórica de dados (em dias)  |
| `--output`| `output/`       | Pasta onde os arquivos serão salvos  |

---

## 📄 Exemplo de saída

Após a execução, dois arquivos são gerados na pasta `output/`:

**`bacen_mercado_20260314_143021.json`**
```json
{
  "dataset_name": "bacen_mercado",
  "total_rows": 1842,
  "total_columns": 3,
  "columns": [
    {
      "name": "valor",
      "type": "float64",
      "null_count": 0,
      "null_pct": 0.0,
      "unique_count": 1201,
      "min": 0.0275,
      "max": 13.75,
      "mean": 7.43
    }
  ],
  "llm_report": "O dataset consolida 5 séries temporais do Banco Central..."
}
```

**`bacen_mercado_20260314_143021.md`** — relatório completo em Markdown com tabela de atributos e análise do LLM.

---

## 🛠️ Tecnologias

- **Python 3.10+**
- **Pandas** — manipulação e perfilagem dos dados
- **Requests** — consumo da API REST do BACEN
- **Groq SDK** — integração com LLM (llama3-8b-8192)

---

## 🔗 Fonte dos dados

[API do Banco Central do Brasil](https://dadosabertos.bcb.gov.br/) — dados públicos, sem autenticação, atualizados diariamente.

---

## 👩‍💻 Autora

**Rubia Massaud**
[linkedin.com/in/rubiamassaud](https://linkedin.com/in/rubiamassaud) · [github.com/rubiamassaud](https://github.com/rubiamassaud)
