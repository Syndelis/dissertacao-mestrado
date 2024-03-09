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

- [x] No início do capítulo 3 [Trabalhos Relacionados], incluir o quadro comparativo;
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

- 4.4.3 [Distribuição do software]:
    - Falar sobre AppImages construídas em contêiner;
        - ```
        ./t: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found (required by ./t)
        ```

- Trabalhos futuros:
    - Feedback de alunos;
    - "Solução: Uma ideia é oferecer a possibilidade de agrupar um grupo de nós e as ligações entre eles em um submodelo. Os submodelos seriam combinados para formar o modelo completo.";

- [x] Fazer tabela descrevendo os tipos de nós da representação visual desenvolvida.
