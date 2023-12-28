# Data analysis phases:


1 Ask

2 Prepare

3 Process

4 Analyze

5 Share

6 Act


# Database definition:

A collection of data stored in a computer system


# Relational database definition:

A database that contains a series of related tables that can be connected via their relationships

- Primary key: An identifies that references a column in which each value is unique 
- Foreign key: A field within a table that is a primary key in another table
- Metadata is used in database management to help data analysts interpret the contents of the data within the database


# Common types of metadata

- Descriptive
- Structural
- Administrative

Data e hora = metadado administrativo


Os Conjuntos de dados públicos do Google Cloud permitem aos analistas de dados o acesso a conjuntos de dados públicos de alta demanda, e facilitam a descoberta de insights na nuvem. 

A Pesquisa de conjunto de dados pode ajudá-lo a encontrar conjuntos de dados disponíveis on-line com pesquisas de palavras-chave. 

A Kaggle tem uma função de busca de dados abertos que pode ajudá-lo a encontrar conjuntos de dados para praticar.

Finalmente, a BigQuery hospeda mais de 150 conjuntos de dados públicos que você pode acessar e utilizar. 


# Structured query language (SQL)

A language to comunicate to databases

SELECT é a seção de uma consulta que indica quais dados você quer que o SQL retorne a você

FROM é a seção de uma consulta que indica de qual tabela provêm os dados desejados.

WHERE está a seção de uma consulta que indica qualquer filtro que você gostaria de aplicar ao seu conjunto de dados


# Data security

Protecting data from unauthorized access or corruption by adopting safety measures 

## Criptografia
A criptografia usa um algoritmo único para alterar dados e torná-los inutilizáveis por usuários e aplicativos que desconheçam o algoritmo, que é salvo como uma “chave” que pode ser usada para revogar a criptografia. Dessa forma, se você tem a chave, você ainda pode usar os dados em seu formato original.  

## Tokenização
A tokenização, por sua vez, substitui os elementos dos dados que você quer proteger com dados gerados de forma aleatória, conhecidos como “token”. Os dados originais são armazenados em um local separado e atribuídos aos tokens. Para ter acesso aos dados originais completos, o usuário ou o aplicativo precisa ter permissão para usar o dado tokenizado e o mapeamento do token, ou seja, mesmo que o dado tokenizado seja hackeado, o dado original continua seguro em um local separado. 


# Flowchart to cope with incomplete or data with errors

![Flowchart to cope with incomplete data](img_lidar_erros_dados.png)

# Spreadsheet for sample size estimate based on confidence interval
https://docs.google.com/spreadsheets/d/1WrHqkxWo3JnFsbnlF-IY5ZLm6-nQKFGBQuAEraLKg9o/edit?resourcekey=0-VCs_I4_LM2Kkqf5WNU2H3A#gid=0


# Spreadsheet for margin of error estimate
https://docs.google.com/spreadsheets/d/1y3QQhgsSvQFm2QSs15CHER0K7w9zQb25G5twD-G-OKE/edit#gid=77526548

# Dirty data
Data that is incomplete, incorret, or irrelevant to the problem you're trying to solve

# Data engineers
Transform data into a useful format for analysis and give it a reliable infrastructure

# Data warehousing specialists
Develop processes and procedures to effectively store and organize data

# Types of dirty data
- Duplicates
- Outdated
- Incomplete
- Incorrect
- Inconsistent 

# Merger
An agreement that unites two organizations into a single new one


# Data merging
The process of combining two or more datasets into a single dataset

# Compatibility
How well two or more datasets are able to work together

# Tips to format and clean data:
[Guide to excel]([https://www.example.com](https://support.microsoft.com/en-us/office/top-ten-ways-to-clean-your-data-2844b620-677c-47a7-ac3e-c2e157d1db19)https://support.microsoft.com/en-us/office/top-ten-ways-to-clean-your-data-2844b620-677c-47a7-ac3e-c2e157d1db19)
[Guide to Google workspace](https://support.google.com/a/users/answer/9604139?hl=en#zippy=)


# Conditional formatting
A spreadsheet tool that changes how cells appear when values meet specific conditions

# Remove duplicates
A tool that automatically searches for and eliminates duplicate entries from a spreadsheet

# Function
A set of instructions that performs a specific calculation using the data in a spreadsheet

# Specific functions in Excel
## COUNTIF
Return the number of cells that match a specified value

## TRIM
A function that removes leading, trailing, and repeated spaces in data

## VLOOKUP
A function that searches for a certain value in a column to return a corresponding piece of information

# Links with tips about automatization in data cleaning processes 
[Towards Data Science’s automatização da análise de dados científicos](https://towardsdatascience.com/automating-scientific-data-analysis-part-1-c9979cd0817e)
[MIT news automatizando a análise de big-data](https://news.mit.edu/2016/automating-big-data-analysis-1021)
[TechnologyAdvice's 10 das melhores opções para software de automação do fluxo de trabalho](https://technologyadvice.com/blog/information-technology/top-10-workflow-automation-software/)


# Pivot table
A data summarization tool that is used in data processing


# Data mapping
The process of matching fields from one data source to another

# Differences between Spreadsheets and SQL

| Spreadsheets | SQL |
| ----------- | ----------- |
| Generated with a program | A language used to interact with database programs |
| Access to the data you input | Can pull information from different sources in the database |
| Stored locally | Stored across a database |
| Small datasets | Larger datasets |
| Working independently | Tracks changes across teams |
| Built-in functionalities | Used across multiple programs | 


# Typecasting
Converting data of a type to another


Obter dados de uma tabela usando instruções SELECT.

Deduplicar dados usando comandos como DISTINCTe COUNT + WHERE.

Manipular dados de string com TRIM(), SUBSTR, e LENGTH.

Criar/eliminar tabelas com CREATE TABLE e DROP TABLE.

Alterar os tipos de dados com CAST.


# Verification
A process to confirm that a data-cleaning effort was well-executed and the resulting data is accurate and reliable. 

# Changelog 
A file containing a chronologically ordered list of modification made to a project


# See the big picture when verifying data-cleaning
1 Consider the business problem

2 Consider the goal

3 Consider the data


# Identificar problemas mais comuns e corrijí-los:

- Origem dos erros. Você usou as ferramentas e funções certas para encontrar a origem dos erros no seu conjunto de dados?

- Dados nulos. Você procurou por NULOS com filtros e formatação condicional?

- Palavras digitadas incorretamente. Você localizou todas as palavras com erro de digitação?

- Números digitados incorretamente. Você verificou se os dados numéricos foram digitados corretamente?

- Caracteres e espaços extras. Você excluiu os caracteres ou espaços extras com a função TRIM?

- Duplicatas. Você excluiu as duplicatas nas planilhas ou SQL com as funções Remove duplicates ou DISTINCT, respectivamente?

- Tipos de dados incompatíveis. Você verificou se os dados numéricos, de datas e strings foram convertidos corretamente?

- Strings desorganizadas (inconsistentes). Você verificou se todas as strings são consistentes e pertinentes?

- Formatos de dados desorganizados (inconsistentes). Você formatou as datas de forma consistente no conjunto de dados?

- Identificações (colunas) variáveis incorretas. Você nomeou suas colunas de forma adequada?

- Dados truncados. Você verificou se há dados ausentes ou truncados que exigem correção?

- Lógica nos negócios. Com base em seu conhecimento nos negócios, você verificou se os dados são coerentes? 


# How to access version control in different tools:

| Planilhas Google | Microsoft Excel | BigQuery | 
| ----------- | ----------- | ----------- |
| 1. Clique com o botão direito na célula e selecione "Exibir histórico de edição". 2. Clique nas setas para a esquerda (<) ou direita (>) para ir para frente ou para trás no histórico, conforme necessário | 1. Se o recurso de Controlar Alterações estiver habilitado na planilha: clique em "Revisão". 2. Em Controlar alterações, clique na opção "Aceitar/Rejeitar alterações" para aceitar ou rejeitar as mudanças feitas | Abra uma versão anterior (sem voltar para ela) e compare-a à versão atual para ver o que mudou |

# Todas as mudanças de cada categoria devem ser agrupadas juntas. Os tipos de alterações se classificam, normalmente, em uma das categorias abaixo:

- Adicionado: novos recursos incorporados

- Alterado: mudanças na funcionalidade já existente

- Obsoleto: recursos prestes a serem removidos

- Removido: recursos que foram removidos

- Corrigido: correções de erros

- Segurança: mitigação de vulnerabilidades

# Example of changelog (in markdown):

# Changelog
This file contains the notable changes to the project

Version 1.0.0 (02-23-2019)
## New
    - Added column classifiers (Date, Time, PerUnitCost, TotalCost, etc. )
    - Added Column “AveCost” to track average item cost

## Changes 
    - Changed date format to MM-DD-YYYY
    - Removal of whitespace (cosmetic)

## Fixes
    - Fixed misalignment in Column "TotalCost" where some rows did not match with correct dates
    - Fixed SUM to run over entire column instead of partial


# Common data errors
- Human error in data entry
- Flawed processes
- System issues

# Functions to a fast data cleaning:
| Function | Sintaxe (Google sheets) | Microsoft Excel | Main use |
| ----------- | ----------- | ----------- | ----------- |
| IMPORTRANGE | =IMPORTRANGE(spreadsheet_url, range_string) | Colar link (copiar os dados primeiro) | Importa (cola) dados de uma planilha para outra e os mantém atualizados automaticamente| 
| QUERY | Sintaxe: =QUERY(Planilha e Intervalo, "Select *") | Dados > De outras fontes > Da consulta Microsoft | Permite que instruções falsas do SQL (do tipo SQL) ou um assistente importem os dados | 
| FILTER | =FILTER(intervalo, condição1 [condição2, ...]) | Filtrar(condições por coluna) | Exibe somente os dados que atendem às condições especificadas |


# Phases of analysis 
1 Organize data

2 Format and adjust data

3 Get input from others

4 Transform data


# Data validation options:
- Add dropdown lists with predetermined options
- Create custom checkboxes
- Protect structured data and formulas

[Regras de conversão em SQL](https://cloud.google.com/bigquery/docs/reference/standard-sql/conversion_rules)


# Data aggregation
The process of gathering data from multiple sourcer in order to combine it into a single summarized collection


# Subquery
A query within another query


# Join
A SQL clause that is used to combine rows from two or more tables based on a related column

# Types of Join:
- Inner = returns records with matching values in both tables
- Left = return all the records from the left table and only the matching records from the right table
- Right = return all records from the right table and only the matching records from the left
- Full outer = combines right and left join to return all matching records in both tables



![Join types](join_types.png)


# Aliasing
When you temporarily name a table or column in your query to make it easier to read and write. 


