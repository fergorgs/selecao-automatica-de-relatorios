# Seleção automática de relatórios por termo chave
Scripts utilizados durante a etapa de selação automática de relatórios post-mortem com base em termos chave relacionados a "defeito de software"

Parte do Trabalho de Conclusão de Curso apresentado para obtenção do título de especialista em Engenharia de Software – 2026

**Título:** Por que defeitos de software alcançam produção? Melhorias nos processos de teste adotados pela indústria

**Autor:** Fernando Gorgulho Fayet

## Utilização
### Instalação
`$ pip install`

### Execução
1. Atualize o nome do provedor no campo `provider`, no script de `key_selector.py`
2. Atualize os termos de busca com os termos desejados no campo `search_terms`, no script de `key_selector.py`
3. Atualize a lista de URLs a serem triadas no campo `urls_to_scan`, no script de `key_selector.py`.
    - *Nota: Para relatórios da Azure, o conteúdo dos relatórios deve ser armazenados localmente num arquivo de texto `.txt`, e a URL deve ser o caminho local do arquivo*
4. Execute o script com o comando
    - `$ python key_selector.py`
