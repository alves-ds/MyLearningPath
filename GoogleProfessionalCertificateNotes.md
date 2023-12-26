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



