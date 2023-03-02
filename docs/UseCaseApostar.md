::: mermaid
    flowchart LR

    A[Apostador] -->|Fazer uma aposta| B(Seleciona aposta)
    B -->C(Insere o valor da aposta)
    C --> D{Decisão}
    D --> |Fazer aposta| E[Aposta efetuada]
    E--> G[Desconto da carteira]
    D --> |Cancelar aposta| F[Aposta cancelada]
:::