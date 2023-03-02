::: mermaid
    flowchart LR

    A[Ator] -->|Fazer uma aposta| B(Seleciona aposta)
    B -->C(Inser o valor da aposta)
    C --> D{Decisão}
    D --> |Fazer aposta| E[Aposta efetuada]
    D --> |Cancelar aposta| F[Aposta cancelada]
:::