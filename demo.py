import json

perguntas = [
    {
        "pergunta": "Os Objetivos de Desenvolvimento Sustentável (ODS) foram adotados pela ONU em 2015?",
        "resposta": "Verdadeiro"
    },
    {
        "pergunta": "Existem 20 ODS estabelecidos pela ONU?",
        "resposta": "Falso"
    },
    {
        "pergunta": "O ODS 1 visa erradicar a pobreza em todas as suas formas?",
        "resposta": "Verdadeiro"
    },
    {
        "pergunta": "O ODS 5 promove a igualdade de gênero?",
        "resposta": "Verdadeiro"
    },
    {
        "pergunta": "Os ODS não abordam questões relacionadas à mudança climática?",
        "resposta": "Falso"
    },
    {
        "pergunta": "O ODS 14 trata da vida terrestre?",
        "resposta": "Falso"
    },
    {
        "pergunta": "A educação de qualidade é o foco do ODS 4?",
        "resposta": "Verdadeiro"
    },
    {
        "pergunta": "Os ODS são obrigatórios para todos os países membros da ONU?",
        "resposta": "Falso"
    },
    {
        "pergunta": "O ODS 7 busca assegurar o acesso à energia limpa e acessível?",
        "resposta": "Verdadeiro"
    },
    {
        "pergunta": "O ODS 10 visa reduzir as desigualdades dentro e entre os países?",
        "resposta": "Verdadeiro"
    },
    {
        "pergunta": "Os ODS não incluem metas relacionadas à saúde pública?",
        "resposta": "Falso"
    },
    {
        "pergunta": "O ODS 11 foca em tornar as cidades e comunidades sustentáveis?",
        "resposta": "Verdadeiro"
    },
    {
        "pergunta": "A parceria global para o desenvolvimento sustentável é o objetivo do ODS 17?",
        "resposta": "Verdadeiro"
    },
    {
        "pergunta": "Os ODS substituíram os Objetivos de Desenvolvimento do Milênio (ODM)?",
    "resposta": "Verdadeiro"
    },
    
    {
        "pergunta": "Qual é o principal objetivo do ODS 2?\n        a) Promover a educação de qualidade\n        b) Erradicar a fome e promover a segurança alimentar\n        c) Assegurar o acesso à água potável\n        d) Promover a igualdade de gênero",
        "resposta": "b"
    },
    {
        "pergunta": "Quantas metas específicas acompanham os 17 ODS?\n        a) 100\n        b) 169\n        c) 200\n        d) 150",
        "resposta": "b"
    },
    {
        "pergunta": "O ODS 6 busca?\n        a) Promover trabalho decente e crescimento econômico\n        b) Assegurar a disponibilidade e gestão sustentável da água e saneamento para todos\n        c) Reduzir a desigualdade dentro e entre os países\n        d) Proteger a vida marinha",
        "resposta": "b"
    },
    {
        "pergunta": "Em que ano os ODS foram adotados pelos Estados Membros das Nações Unidas?\n        a) 2000\n        b) 2010\n        c) 2015\n        d) 2020",
        "resposta": "c"
    },
    {
        "pergunta": "O ODS 13 trata de?\n        a) Ação contra a mudança global do clima\n        b) Vida na água\n        c) Vida terrestre\n        d) Consumo e produção responsáveis",
        "resposta": "a"
    },
    {
        "pergunta": "Qual ODS foca em promover sociedades pacíficas e inclusivas?\n        a) ODS 12\n        b) ODS 16\n        c) ODS 8\n        d) ODS 14",
        "resposta": "b"
    },
    {
        "pergunta": "O ODS 9 está relacionado a?\n        a) Indústria, inovação e infraestrutura\n        b) Redução das desigualdades\n        c) Energia limpa e acessível\n        d) Fome zero",
        "resposta": "a"
    },
    {
        "pergunta": "Quantos países adotaram os ODS em 2015?\n        a) 150\n        b) 193\n        c) 175\n        d) 160",
        "resposta": "b"
    },
    {
        "pergunta": "O ODS 12 promove?\n        a) Consumo e produção responsáveis\n        b) Igualdade de gênero\n        c) Educação de qualidade\n        d) Saúde e bem-estar",
        "resposta": "a"
    },
    {
        "pergunta": "Qual ODS visa acabar com a fome, alcançar a segurança alimentar e promover a agricultura sustentável?\n        a) ODS 1\n        b) ODS 2\n        c) ODS 3\n        d) ODS 4",
        "resposta": "b"
    },
    {
        "pergunta": "O ODS 8 busca?\n        a) Promover o crescimento econômico sustentado, inclusivo e sustentável, emprego pleno e produtivo e trabalho decente para todos\n        b) Assegurar a educação inclusiva e equitativa de qualidade\n        c) Reduzir a desigualdade dentro e entre os países\n        d) Proteger, restaurar e promover o uso sustentável dos ecossistemas terrestres",
        "resposta": "a"
    },
    {
        "pergunta": "O ODS 15 trata de?\n        a) Vida terrestre\n        b) Vida na água\n        c) Energia limpa e acessível\n        d) Trabalho decente e crescimento econômico",
        "resposta": "a"
    }

    ,

    {
        "pergunta": "O que são os Objetivos de Desenvolvimento Sustentável (ODS)?",
        "resposta": "Os Objetivos de Desenvolvimento Sustentável (ODS) são uma iniciativa global adotada pela Assembleia Geral das Nações Unidas em 2015, como parte da Agenda 2030 para o Desenvolvimento Sustentável. Eles são compostos por 17 objetivos que buscam abordar os principais desafios globais enfrentados pela humanidade, como a erradicação da pobreza, a proteção do meio ambiente e a promoção da paz e da justiça, com foco na sustentabilidade social, econômica e ambiental. Cada ODS possui metas específicas a serem alcançadas até o ano de 2030, que servem como um guia para ações de governos, empresas, organizações e indivíduos. Os ODS são interconectados e visam promover uma abordagem integrada para o desenvolvimento, reconhecendo que problemas globais como a desigualdade, a mudança climática e a falta de acesso a recursos essenciais estão profundamente interligados."
    },
    {
        "pergunta": "Em que ano os ODS foram adotados pelos Estados Membros das Nações Unidas?",
        "resposta": "Os ODS foram adotados pelos Estados Membros das Nações Unidas em 2015."
    },
    {
        "pergunta": "Quais são os principais desafios para a implementação dos ODS?",
        "resposta": "Os principais desafios para a implementação dos ODS incluem a falta de recursos financeiros, a desigualdade social e econômica, a instabilidade política, a mudança climática, a falta de infraestrutura adequada em algumas regiões e a necessidade de colaboração internacional eficaz entre governos, empresas e sociedade civil."
    },
    {
        "pergunta": "Como os países monitoram o progresso em relação aos ODS?",
        "resposta": "Os países monitoram o progresso em relação aos ODS por meio de indicadores globais definidos pela ONU, com relatórios nacionais e internacionais sobre o avanço de cada meta. O Sistema de Monitoramento e Avaliação acompanha os dados e os resultados, enquanto as metas e indicadores ajudam a medir os avanços de forma comparável entre os países."
    },
    {
        "pergunta": "Qual é o papel das parcerias globais no alcance dos ODS?",
        "resposta": "As parcerias globais desempenham um papel crucial no alcance dos ODS ao unir governos, setor privado, sociedade civil e organizações internacionais para mobilizar recursos, compartilhar conhecimentos e promover ações coordenadas. Elas são essenciais para enfrentar desafios globais de forma colaborativa e eficaz."
    },
    {
        "pergunta": "Como as empresas podem integrar os ODS em suas estratégias de negócio?",
        "resposta": "As empresas podem integrar os ODS em suas estratégias de negócio ao adotar práticas sustentáveis, inovar em produtos e serviços que promovam o bem-estar social e ambiental, reduzir impactos negativos e colaborar com stakeholders para alcançar metas compartilhadas. Isso pode gerar valor para a empresa enquanto contribui para o desenvolvimento sustentável."
    },
    {
        "pergunta": "Como os ODS estão interconectados entre si?",
        "resposta": "Os ODS estão interconectados porque ações em um objetivo podem impactar outros. Por exemplo, combater a pobreza (ODS 1) pode melhorar o acesso à educação (ODS 4), enquanto promover a saúde (ODS 3) pode contribuir para um ambiente sustentável (ODS 13). Eles são abordagens integradas para resolver problemas globais complexos de forma holística."
    },
    {
        "pergunta": "De que forma o progresso em um ODS pode influenciar positivamente outro?",
        "resposta": "O progresso em um ODS pode influenciar positivamente outro ao criar efeitos em cadeia. Por exemplo, melhorar o acesso à educação de qualidade (ODS 4) pode reduzir a pobreza (ODS 1), pois pessoas mais bem educadas tendem a ter melhores oportunidades de emprego e rendimento. Da mesma forma, a promoção de energia limpa (ODS 7) pode ajudar a combater a mudança climática (ODS 13), beneficiando o meio ambiente e a saúde pública."
    },
    {
        "pergunta": "Quais são os possíveis conflitos entre diferentes ODS?",
        "resposta": "Os possíveis conflitos entre diferentes ODS ocorrem quando as ações para alcançar um objetivo podem limitar ou prejudicar o progresso de outro. Isso pode acontecer devido a prioridades concorrentes, alocação limitada de recursos ou impactos negativos indiretos que uma iniciativa em um setor pode gerar em outro. Esses conflitos exigem uma abordagem integrada e planejamento estratégico para equilibrar os objetivos e minimizar impactos adversos."
    },
    {
        "pergunta": "Qual é a relação dos ODS com os direitos humanos?",
        "resposta": "Os ODS e os direitos humanos estão diretamente relacionados, pois ambos visam garantir dignidade, igualdade e bem-estar para todos. Os ODS promovem a realização de direitos fundamentais, como acesso à educação, saúde, trabalho decente e justiça, enquanto os direitos humanos fornecem a base ética e jurídica para a implementação dos objetivos. Juntos, reforçam um desenvolvimento sustentável que não deixe ninguém para trás."
    },
    {
        "pergunta": "Como os ODS consideram a preservação da biodiversidade?",
        "resposta": "Os ODS consideram a preservação da biodiversidade por meio de objetivos específicos como o ODS 14 (Vida na Água) e o ODS 15 (Vida Terrestre). Esses objetivos promovem a proteção dos ecossistemas marinhos e terrestres, o uso sustentável dos recursos naturais, o combate à degradação ambiental e a preservação da fauna e flora, reconhecendo a biodiversidade como essencial para a saúde do planeta e o bem-estar humano."
    },
    {
        "pergunta": "De que forma os ODS promovem a paz e a justiça?",
        "resposta": "Os ODS promovem a paz e a justiça principalmente por meio do ODS 16, que busca construir sociedades pacíficas, justas e inclusivas. Ele enfatiza a necessidade de fortalecer instituições eficazes, reduzir a violência, combater a corrupção, garantir o acesso à justiça e promover o estado de direito. Além disso, outros ODS contribuem indiretamente ao abordar desigualdades, pobreza e exclusão social, que são causas subjacentes de conflitos e instabilidade."
    },
    {
        "pergunta": "Quantas metas específicas acompanham os ODS?",
        "resposta": "Os ODS são acompanhados por 169 metas específicas, que detalham os objetivos e fornecem orientações para sua implementação e monitoramento."
    },
    {
        "pergunta": "Qual é a função dos indicadores nos ODS?",
        "resposta": "Os indicadores nos ODS têm a função de medir e monitorar o progresso na implementação das metas. Eles permitem acompanhar os resultados alcançados, identificar desafios, orientar políticas públicas e garantir a transparência e a prestação de contas em nível local, nacional e global."
    },
    {
        "pergunta": "Como os indicadores ajudam a medir o progresso dos ODS?",
        "resposta": "Os indicadores ajudam a medir o progresso dos ODS ao fornecerem dados específicos, quantificáveis e comparáveis que permitem avaliar o desempenho em relação a cada meta. Eles traduzem os objetivos em métricas concretas, facilitando o monitoramento dos avanços, a identificação de lacunas e a formulação de políticas baseadas em evidências. Além disso, promovem a transparência e permitem ajustes nas estratégias de implementação."
    },
    {
        "pergunta": "Quais são os desafios na coleta de dados para os indicadores dos ODS?",
        "resposta": "Os principais desafios na coleta de dados para os indicadores dos ODS incluem: Falta de capacidade técnica em alguns países para produzir e gerenciar dados confiáveis. Desigualdade na disponibilidade de dados, com lacunas significativas em regiões menos desenvolvidas. Dados desatualizados ou inconsistentes, dificultando análises precisas e comparações globais. Altos custos envolvidos na coleta, processamento e análise de dados. Falta de padronização global, tornando difícil harmonizar métodos e garantir comparabilidade. Desafios éticos e de privacidade na coleta de dados pessoais ou sensíveis. Superar esses desafios exige investimentos em infraestrutura estatística, capacitação técnica e colaboração internacional."
    },
    {
        "pergunta": "Como os indicadores podem ser adaptados às realidades locais?",
        "resposta": "Os indicadores podem ser adaptados às realidades locais por meio de: Contextualização: Ajustar os indicadores globais para refletir as condições socioeconômicas, culturais e ambientais de cada região. Criação de indicadores locais: Desenvolver métricas específicas que complementem os globais, considerando prioridades regionais. Engajamento das partes interessadas: Incluir governos locais, comunidades e organizações na definição de indicadores relevantes. Capacitação e recursos: Investir em infraestrutura e competências locais para coleta e análise de dados. Integração com políticas públicas: Garantir que os indicadores reflitam metas e estratégias já estabelecidas localmente. Essa adaptação torna o monitoramento mais eficaz, alinhando as metas globais às necessidades locais."
    },
    {
        "pergunta": "Quais são as principais fontes de financiamento para os ODS?",
        "resposta": "As principais fontes de financiamento para os ODS incluem: Orçamentos públicos nacionais: Governos alocam recursos para implementar políticas e projetos relacionados aos ODS. Investimentos privados: Empresas e investidores financiam iniciativas sustentáveis, como energia limpa e inovação tecnológica. Organizações internacionais: Instituições como o Banco Mundial e o FMI oferecem empréstimos e subsídios. Ajuda oficial ao desenvolvimento (AOD): Países desenvolvidos fornecem apoio financeiro a nações em desenvolvimento. Parcerias público-privadas (PPP): Colaborações entre governos e setor privado para projetos alinhados aos ODS. Filantropia e ONGs: Fundos provenientes de organizações sem fins lucrativos e doações. Inovação financeira: Mecanismos como títulos verdes e fundos de impacto social mobilizam recursos para objetivos específicos."
    },
    {
        "pergunta": "Como os investimentos privados podem apoiar os ODS?",
        "resposta": "Os investimentos privados podem apoiar os ODS ao: Financiar soluções sustentáveis: Investir em setores como energia renovável, infraestrutura verde, agricultura sustentável e tecnologias inovadoras que promovem o desenvolvimento sustentável. Adotar práticas empresariais responsáveis: Integrar os ODS nas estratégias empresariais, como garantir trabalho decente (ODS 8), promover igualdade de gênero (ODS 5) e minimizar impactos ambientais (ODS 12). Fomentar a inovação: Investir em novas tecnologias que resolvam desafios globais, como mudanças climáticas, saúde e educação. Criar parcerias públicas e privadas: Colaborar com governos e ONGs para implementar soluções de grande escala para os ODS. Responsabilidade social corporativa (RSC): Contribuir para iniciativas sociais, ambientais e educacionais que beneficiem a sociedade."
    }
    ,

       {
        "pergunta": "Qual é o papel das instituições financeiras internacionais no financiamento dos ODS?",
        "resposta": "As instituições financeiras internacionais desempenham um papel crucial no financiamento dos ODS ao: Fornecer empréstimos e subsídios: Oferecem financiamento a países em desenvolvimento para implementar projetos que promovam os ODS, como infraestrutura sustentável, saúde e educação. Facilitar a mobilização de recursos: Ajudam na mobilização de recursos privados e públicos, criando mecanismos como fundos de impacto e investimentos em projetos sustentáveis. Promover políticas financeiras sustentáveis: Apoiam a criação de políticas financeiras que incentivem o financiamento de iniciativas ligadas ao desenvolvimento sustentável. Desenvolver capacidades técnicas e conhecimento: Oferecem assistência técnica e consultoria para ajudar os países a planejar e implementar suas estratégias de desenvolvimento sustentável. Estabelecer parcerias e colaborações: Trabalham em conjunto com governos, setor privado e ONGs para criar soluções financeiras inovadoras e eficazes para atingir os ODS."
    },
    {
        "pergunta": "Como a cooperação internacional contribui para o financiamento dos ODS?",
        "resposta": "A cooperação internacional contribui para o financiamento dos ODS de várias maneiras: Transferência de recursos: Países desenvolvidos fornecem ajuda oficial ao desenvolvimento (AOD) para países em desenvolvimento, contribuindo para projetos ligados aos ODS, como saúde, educação e infraestrutura. Fomento à colaboração multilateral: Organizações internacionais, como a ONU, o Banco Mundial e o FMI, coordenam esforços globais para mobilizar recursos financeiros e técnicos para os ODS. Criação de parcerias: A cooperação internacional promove parcerias público-privadas que viabilizam o financiamento de projetos sustentáveis, compartilhando riscos e benefícios. Desenvolvimento de capacidades: Proporciona assistência técnica e conhecimento, ajudando países em desenvolvimento a criar estruturas financeiras e políticas adequadas para implementar os ODS. Mobilização de investimentos privados: A cooperação internacional pode facilitar o investimento privado, incentivando fundos internacionais a direcionar recursos para áreas prioritárias dos ODS."
    },
    {
        "pergunta": "Como a conscientização pública pode influenciar positivamente os ODS?",
        "resposta": "A conscientização pública pode influenciar positivamente os ODS ao: Estimular a ação individual: Ao entender a importância dos ODS, as pessoas podem adotar comportamentos mais sustentáveis, como consumo responsável, redução de desperdício e apoio a políticas ambientais. Pressionar por políticas públicas: A conscientização gera pressão sobre governos e empresas para implementar e apoiar iniciativas que promovam os ODS. Mobilizar recursos e parcerias: Com maior conhecimento sobre os ODS, indivíduos e organizações podem contribuir financeiramente ou formar parcerias para projetos que atendem aos objetivos. Promover a educação: A conscientização pública pode levar a uma maior demanda por educação de qualidade (ODS 4) e informação sobre os direitos humanos, empoderando as comunidades a participar ativamente no desenvolvimento sustentável. Reduzir desigualdades sociais: Ao aumentar a conscientização sobre questões de igualdade, saúde e pobreza, é possível reduzir a discriminação e promover uma sociedade mais inclusiva."
    },
    {
        "pergunta": "Como as inovações sociais podem apoiar os ODS?",
        "resposta": "As inovações sociais podem apoiar os ODS ao introduzir soluções criativas e eficazes para desafios globais. Elas podem: Resolver problemas sociais e ambientais: Desenvolver novos modelos de negócios, tecnologias ou serviços que atendam a necessidades sociais, como saúde, educação e pobreza, de maneira sustentável. Empoderar comunidades locais: Criar soluções adaptadas às necessidades específicas de populações vulneráveis, promovendo inclusão e igualdade (ODS 10). Melhorar a eficiência e o impacto das políticas públicas: Utilizar abordagens inovadoras para melhorar a implementação dos ODS, como o uso de tecnologias digitais para aumentar a transparência e a participação social. Estímulo à colaboração: Facilitar parcerias entre organizações, governos e empresas para criar soluções mais amplas e impactantes, com foco em resultados duradouros. Promover o desenvolvimento econômico sustentável: Criar novas oportunidades de emprego e modelos de negócios que respeitem os princípios de sustentabilidade e responsabilidade social (ODS 8)."
    }
]
# Usa ensure_ascii=False para manter os caracteres UTF-8
object_json = json.dumps(perguntas, indent=4, ensure_ascii=False)

with open("simples.json", "w", encoding="utf-8") as file:
    file.write(object_json)
