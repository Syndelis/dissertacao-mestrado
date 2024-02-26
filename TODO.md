- Enviar o software para avaliação de usabilidade para pessoas interessadas:
    - Alunos da última turma de modelagem;
        - Re-implementar alguns modelos de TPs usando o software?;
    - Montar um formulário com algumas perguntas diretas sobre o software;
        - Facilidade de uso (1 a 3 estrelas);
        - Encontrou algum bug no software? (Sim/Não);
            - Se sim, descreva-o;
        - Encontrou alguma limitação durante a construção de algum modelo? (Sim/Não);
            - Se sim, qual modelo? Código?
        - Facilidade de instalação;
        - Sugestão de melhorias;

- [x] Mover seção 4.2.1 [Programação Visual] para a primeira seção do "Referencial Teórico";
    - Acrescentar na seção que existem trabalhos (outros na seção 3) com propostas semelhantes;

- [x] Na introdução:
    - Diferencial: nessa dissertação foi desenvolvido uma nova forma de representação de modelos baseado em editor de nós (exemplos da seção 4.2.1 [Programação Visual]) e a criação de uma representação intermediária extensível, *humanamente legível* e de fácil tradução de/para o código-alvo;
        - Objetivo: simplicidade, naturalidade;

- No início do capítulo 3 [Trabalhos Relacionados], incluir o quadro comparativo;
    - Exemplo:
    
    | Softwares | Distribuição do software | Representação de modelos suportados | Acesso ao código gerado | Simulação Interativa |
    | --- | --- | --- | --- | --- |
    | ODE-Designer | ... | ... | ... | ... |

- Na 4.3 [Implementação e Tecnologias utilizadas]:
    - Comentar que começamos em C++, mudamos para Rust. Motivos:
        - Confiabilidade (não crashar por motivos aleatórios);
        - Segurança (menos brechas de ataque / acesso ilegal, etc.);
        - Facilidade e portabilidade do desenvolvimento;
            - Poucas coisas dependem de um sistema Unix no software atual; (na verdade, nenhuma!)
            - Programação paralela menos propensa a introdução de erros motivados por condições de corrida (*borrow checker*);
        - Dificuldade de conciliar (interop) as duas linguagens (C++ e Rust);
        - Crescimento do ecossistema com a maior disponibilização de bibliotecas para os mais variados propósitos (IoT, Graphics, Web, Frontend);
    - Atualizar seção com novas bibliotecas, remover não-mais utilizadas;
    - Incluir UML geral sobre a organização do software;

- [x] Na 4.1.2 [Representação de expressões]
    - [x] Falar sobre a árvore de expressões;
        - "Todo modelo construído no software é representado na memória utilizando uma árvore de expressões."
    - Importância da representação em árvore:
        - Representação hierárquica do modelo (melhor organização das informações);
        - Facilita a propagação de modificações. Exemplo: troca sinal de um termo, remoção de um termo  (explicar embaixo);
        - [x] Todas as informações sobre o modelo podem ser obtidas percorrendo a árvore facilitando a construção das equações do código; 
        - [x] Permite que novos modelos sejam definidos utilizando a estrutura atual. Exemplo: EDP, AC, Modelos Estocásticos baseados em Gillespie.

- 4.4.3 [Distribuição do software]:
    - Falar sobre AppImages construídas em contêiner;
        - ```
        ./t: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found (required by ./t)
        ```

- [x] 4.2 [Geração de Código e Simulação Interativa]:
    - "O código gerado para a exportação e simulação das EDOs baseia-se na substituição de *strings* em *templates*. O código de Python utiliza a biblioteca `scipy` para simular o conjunto de equações e a biblioteca `matplotlib` para plotar o resultado."

    - O código em Python resolve numericamente o modelo utilizando a função solve_ivp da biblioteca scipy (Colocar link para a página da biblioteca);
    - Exemplo de código em Python no anexo da dissertação.

- Trabalhos futuros:
    - Feedback de alunos;
    - "Solução: Uma ideia é oferecer a possibilidade de agrupar um grupo de nós e as ligações entre eles em um submodelo. Os submodelos seriam combinados para formar o modelo completo.";

- [x] Fazer tabela descrevendo os tipos de nós da representação visual desenvolvida.
