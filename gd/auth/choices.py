# -*- coding: utf-8 -*-
#
# Copyright (C) 2011  Governo do Estado do Rio Grande do Sul
#
#   Author: Lincoln de Sousa <lincoln@gg.rs.gov.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This module holds all of the choices used by the `forms.SignupForm'
class to avoid messing up that module, things were done here in a
separated place.
"""

GENDER = (
    (u'', _(u'--')),
    (u'm', _(u'Male')),
    (u'f', _(u'Female')),
    (u'o', _(u'Other')),
)


AGE = [(u'', u'--')] + [
    (i, i) for i in (
        _(u'80 years old or more'),
        _(u'75 to 79'),
        _(u'70 to 74'),
        _(u'65 to 69'),
        _(u'60 to 64'),
        _(u'55 to 59'),
        _(u'50 to 54'),
        _(u'45 to 49'),
        _(u'40 to 44'),
        _(u'35 to 39'),
        _(u'30 to 34'),
        _(u'25 to 29'),
        _(u'20 to 24'),
        _(u'15 to 19'),
        _(u'10 to 14'),
        _(u'5 to 9'),
        _(u'0 to 4'),
    )
]


STATES = [('', '--')] + [
    (i, i) for i in (
        u'AC', u'AL', u'AM', u'AP', u'BA', u'CE', u'DF', u'ES',
        u'GO', u'MA', u'MG', u'MS', u'MT', u'PA', u'PB', u'PE',
        u'PI', u'PR', u'RJ', u'RN', u'RO', u'RR', u'RS', u'SC',
        u'SE', u'SP', u'TO')
]


FULL_STATES = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AP', u'Amapá'),
    ('AM', u'Amazonas'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MT', u'Mato Grosso'),
    ('MS', u'Mato Grosso do Sul'),
    ('MG', u'Minas Gerais'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PR', u'Paraná'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RS', u'Rio Grande do Sul'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('SC', u'Santa Catarina'),
    ('SP', u'São Paulo'),
    ('SE', u'Sergipe'),
    ('TO', u'Tocantins'),
)

CITIES = [('', '--')] + [
    (i, i) for i in (
        u'Acegua',
        u'Afonso Rodrigues',
        u'Água Santa',
        u'Águas Claras',
        u'Agudo',
        u'Ajuricaba',
        u'Albardão',
        u'Alecrim',
        u'Alegrete',
        u'Alegria',
        u'Alfredo Brenner',
        u'Almirante Tamandare',
        u'Alpestre',
        u'Alto Alegre',
        u'Alto Da União',
        u'Alto Feliz',
        u'Alto Paredão',
        u'Alto Recreio',
        u'Alto Uruguai',
        u'Alvorada',
        u'Amaral Ferrador',
        u'Ametista Do Sul',
        u'André Da Rocha',
        u'Anta Gorda',
        u'Antônio Kerpel',
        u'Antônio Prado',
        u'Arambare',
        u'Ararica',
        u'Aratiba',
        u'Arco Verde',
        u'Arco-iris',
        u'Arroio Canoas',
        u'Arroio Do Meio',
        u'Arroio Do Padre',
        u'Arroio Do Sal',
        u'Arroio Do So',
        u'Arroio Do Tigre',
        u'Arroio Dos Ratos',
        u'Arroio Grande',
        u'Arvore So',
        u'Arvorezinha',
        u'Atafona',
        u'Atiacu',
        u'Augusto Pestana',
        u'Aurea',
        u'Avelino Paranhos',
        u'Azevedo Sodre',
        u'Bacupari',
        u'Bage',
        u'Baliza',
        u'Balneario Pinhal',
        u'Banhado Do Colegio',
        u'Barão',
        u'Barão De Cotegipe',
        u'Barão Do Triunfo',
        u'Barra Do Guarita',
        u'Barra Do Ouro',
        u'Barra Do Quarai',
        u'Barra Do Ribeiro',
        u'Barra Do Rio Azul',
        u'Barra Funda',
        u'Barracão',
        u'Barreirinho',
        u'Barreiro',
        u'Barro Preto',
        u'Barro Vermelho',
        u'Barros Cassal',
        u'Basilio',
        u'Bela Vista',
        u'Beluno',
        u'Benjamin Constant Do Sul',
        u'Bento Gonçalves',
        u'Bexiga',
        u'Boa Esperanca',
        u'Boa Vista',
        u'Boa Vista Das Missões',
        u'Boa Vista Do Burica',
        u'Boa Vista Do Cadeado',
        u'Boa Vista Do Incra',
        u'Boa Vista Do Sul',
        u'Boca Do Monte',
        u'Boi Preto',
        u'Bojuru',
        u'Bom Jardim',
        u'Bom Jesus',
        u'Bom Principio',
        u'Bom Progresso',
        u'Bom Retiro',
        u'Bom Retiro Do Guaiba',
        u'Bom Retiro Do Sul',
        u'Bonito',
        u'Boqueirão',
        u'Boqueirão Do Leão',
        u'Borore',
        u'Bossoroca',
        u'Botucarai',
        u'Braga',
        u'Brochier',
        u'Buriti',
        u'Butia',
        u'Butias',
        u'Cacapava Do Sul',
        u'Cacequi',
        u'Cachoeira Do Sul',
        u'Cachoeirinha',
        u'Cacique Doble',
        u'Cadorna',
        u'Caibate',
        u'Caicara',
        u'Camaqua',
        u'Camargo',
        u'Cambara Do Sul',
        u'Camobi',
        u'Campestre Baixo',
        u'Campestre Da Serra',
        u'Campina Das Missões',
        u'Campina Redonda',
        u'Campinas',
        u'Campinas Do Sul',
        u'Campo Bom',
        u'Campo Branco',
        u'Campo Do Meio',
        u'Campo Novo',
        u'Campo Santo',
        u'Campo Seco',
        u'Campo Vicente',
        u'Campos Borges',
        u'Candelaria',
        u'Candido Freire',
        u'Candido Godoi',
        u'Candiota',
        u'Canela',
        u'Cangucu',
        u'Canhembora',
        u'Canoas',
        u'Canudos',
        u'Capane',
        u'Capão Bonito',
        u'Capão Comprido',
        u'Capão Da Canoa',
        u'Capão Da Porteira',
        u'Capão Do Cedro',
        u'Capão Do Cipo',
        u'Capão Do Leão',
        u'Capela De Santana',
        u'Capela Velha',
        u'Capinzal',
        u'Capitão',
        u'Capivari Do Sul',
        u'Capivarita',
        u'Capo-ere',
        u'Capoeira Grande',
        u'Caraa',
        u'Caraja Seival',
        u'Carazinho',
        u'Carlos Barbosa',
        u'Carlos Gomes',
        u'Carovi',
        u'Casca',
        u'Cascata',
        u'Caseiros',
        u'Castelinho',
        u'Catuipe',
        u'Cavajureta',
        u'Cavera',
        u'Caxias Do Sul',
        u'Cazuza Ferreira',
        u'Cedro Marcado',
        u'Centenario',
        u'Centro Linha Brasil',
        u'Cerrito',
        u'Cerrito Alegre',
        u'Cerrito Do Ouro Ou Vila Do Cerrito',
        u'Cerro Alto',
        u'Cerro Branco',
        u'Cerro Claro',
        u'Cerro Do Martins',
        u'Cerro Do Roque',
        u'Cerro Grande',
        u'Cerro Grande Do Sul',
        u'Cerro Largo',
        u'Chapada',
        u'Charqueadas',
        u'Charrua',
        u'Chiapetta',
        u'Chicoloma',
        u'Chimarrão',
        u'Chorão',
        u'Chui',
        u'Chuvisca',
        u'Cidreira',
        u'Cinquentenario',
        u'Ciriaco',
        u'Clara',
        u'Clemente Argolo',
        u'Coimbra',
        u'Colinas',
        u'Colônia Das Almas',
        u'Colônia Medeiros',
        u'Colônia Municipal',
        u'Colônia Nova',
        u'Colônia São João',
        u'Colônia Z-null',
        u'Coloninha',
        u'Colorado',
        u'Comandai',
        u'Condor',
        u'Consolata',
        u'Constantina',
        u'Coqueiro Baixo',
        u'Coqueiros Do Sul',
        u'Cordilheira',
        u'Coroados',
        u'Coronel Barros',
        u'Coronel Bicaco',
        u'Coronel Finzito',
        u'Coronel Pilar',
        u'Coronel Teixeira',
        u'Cortado',
        u'Costa Da Cadeia',
        u'Costão',
        u'Cotipora',
        u'Coxilha',
        u'Coxilha Grande',
        u'Cr-null',
        u'Crissiumal',
        u'Cristal',
        u'Cristal Do Sul',
        u'Criuva',
        u'Cruz Alta',
        u'Cruz Altense',
        u'Cruzeiro',
        u'Cruzeiro Do Sul',
        u'Curral Alto',
        u'Curumim',
        u'Daltro Filho',
        u'Dario Lassance',
        u'David Canabarro',
        u'Delfina',
        u'Deodoro',
        u'Deposito',
        u'Derrubadas',
        u'Dezesseis De Novembro',
        u'Dilermando De Aguiar',
        u'Divino',
        u'Dois Irmãos',
        u'Dois Irmãos Das Missões',
        u'Dois Lajeados',
        u'Dom Diogo',
        u'Dom Feliciano',
        u'Dom Pedrito',
        u'Dom Pedro De Alcantara',
        u'Dona Francisca',
        u'Dona Otilia',
        u'Dourado',
        u'Doutor Bozano',
        u'Doutor Edgardo Pereira Velho',
        u'Doutor Mauricio Cardoso',
        u'Doutor Ricardo',
        u'Eldorado Do Sul',
        u'Eletra',
        u'Encantado',
        u'Encruzilhada',
        u'Encruzilhada Do Sul',
        u'Engenho Velho',
        u'Entre Rios Do Sul',
        u'Entre-ijuis',
        u'Entrepelado',
        u'Erebango',
        u'Erechim',
        u'Ernestina',
        u'Ernesto Alves',
        u'Erval Grande',
        u'Erval Seco',
        u'Erveiras',
        u'Esmeralda',
        u'Esperanca Do Sul',
        u'Espigão',
        u'Espigão Alto',
        u'Espinilho Grande',
        u'Espirito Santo',
        u'Espumoso',
        u'Esquina Araujo',
        u'Esquina Bom Sucesso',
        u'Esquina Gaucha',
        u'Esquina Ipiranga',
        u'Esquina Piratini',
        u'Estacão',
        u'Estancia Grande',
        u'Estancia Velha',
        u'Esteio',
        u'Esteira',
        u'Estreito',
        u'Estrela',
        u'Estrela Velha',
        u'Eugenio De Castro',
        u'Evangelista',
        u'Fagundes Varela',
        u'Fão',
        u'Faria Lemos',
        u'Farinhas',
        u'Farrapos',
        u'Farroupilha',
        u'Faxinal',
        u'Faxinal Do Soturno',
        u'Faxinalzinho',
        u'Fazenda Fialho',
        u'Fazenda Souza',
        u'Fazenda Vilanova',
        u'Feliz',
        u'Ferreira',
        u'Flores Da Cunha',
        u'Floresta',
        u'Floriano Peixoto',
        u'Florida',
        u'Fontoura Xavier',
        u'Formigueiro',
        u'Formosa',
        u'Forninho',
        u'Forquetinha',
        u'Fortaleza Dos Valos',
        u'Frederico Westphalen',
        u'Frei Sebastião',
        u'Freire',
        u'Garibaldi',
        u'Garibaldina',
        u'Garruchos',
        u'Gaurama',
        u'General Camara',
        u'Gentil',
        u'Getulio Vargas',
        u'Girua',
        u'Gloria',
        u'Glorinha',
        u'Goio-en',
        u'Gramado',
        u'Gramado Dos Loureiros',
        u'Gramado São Pedro',
        u'Gramado Xavier',
        u'Gravatai',
        u'Guabiju',
        u'Guaiba',
        u'Guajuviras',
        u'Guapore',
        u'Guarani Das Missões',
        u'Guassupi',
        u'Harmonia',
        u'Herval',
        u'Herveiras',
        u'Hidraulica',
        u'Horizontina',
        u'Hulha Negra',
        u'Humaita',
        u'Ibarama',
        u'Ibare',
        u'Ibiaca',
        u'Ibiraiaras',
        u'Ibirapuita',
        u'Ibiruba',
        u'Igrejinha',
        u'Ijucapirama',
        u'Ijui',
        u'Ilha Dos Marinheiros',
        u'Ilopolis',
        u'Imbe',
        u'Imigrante',
        u'Independencia',
        u'Inhacora',
        u'Ipe',
        u'Ipiranga',
        u'Ipiranga Do Sul',
        u'Ipuacu',
        u'Irai',
        u'Irui',
        u'Itaara',
        u'Itacolomi',
        u'Itacurubi',
        u'Itai',
        u'Itaimbezinho',
        u'Itão',
        u'Itapua',
        u'Itapuca',
        u'Itaqui',
        u'Itati',
        u'Itatiba Do Sul',
        u'Itauba',
        u'Ituim',
        u'Ivai',
        u'Ivora',
        u'Ivoti',
        u'Jaboticaba',
        u'Jacuípezinho',
        u'Jacutinga',
        u'Jáguarão',
        u'Jáguarete',
        u'Jáguari',
        u'Jansen',
        u'Jaquirana',
        u'Jari',
        u'Jazidas Ou Capela São Vicente',
        u'João Arregui',
        u'João Rodrigues',
        u'Joca Tavares',
        u'Joia',
        u'José Otavio',
        u'Jua',
        u'Júlio De Castilhos',
        u'Lagoa Bonita',
        u'Lagoa Dos Três Cantos',
        u'Lagoa Vermelha',
        u'Lagoão',
        u'Lajeado',
        u'Lajeado Bonito',
        u'Lajeado Cerne',
        u'Lajeado Do Bugre',
        u'Lajeado Grande',
        u'Lara',
        u'Laranjeira',
        u'Lava-pes',
        u'Lavras Do Sul',
        u'Leonel Rocha',
        u'Liberato Salzano',
        u'Lindolfo Collor',
        u'Linha Comprida',
        u'Linha Nova',
        u'Linha Vitória',
        u'Loreto',
        u'Macambara',
        u'Machadinho',
        u'Magisterio',
        u'Mampituba',
        u'Manchinha',
        u'Mangueiras',
        u'Manoel Viana',
        u'Maquine',
        u'Marata',
        u'Marau',
        u'Marcelino Ramos',
        u'Marcorama',
        u'Mariana Pimentel',
        u'Mariano Moro',
        u'Mariante',
        u'Mariapolis',
        u'Marques De Souza',
        u'Mata',
        u'Matarazzo',
        u'Mato Castelhano',
        u'Mato Grande',
        u'Mato Leitão',
        u'Mato Queimado',
        u'Maua',
        u'Maximiliano De Almeida',
        u'Medianeira',
        u'Minas Do Leão',
        u'Miráguai',
        u'Miráguaia',
        u'Mirim',
        u'Montauri',
        u'Monte Alegre',
        u'Monte Alegre Dos Campos',
        u'Monte Alverne',
        u'Monte Belo Do Sul',
        u'Monte Bonito',
        u'Montenegro',
        u'Mormaco',
        u'Morrinhos',
        u'Morrinhos Do Sul',
        u'Morro Alto',
        u'Morro Azul',
        u'Morro Redondo',
        u'Morro Reuter',
        u'Morungava',
        u'Mostardas',
        u'Mucum',
        u'Muitos Capoes',
        u'Muliterno',
        u'Não-me-toque',
        u'Nazare',
        u'Nicolau Vergueiro',
        u'Nonoai',
        u'Nossa Senhora Aparecida',
        u'Nossa Senhora Da Conceição',
        u'Nova Alvorada',
        u'Nova Araca',
        u'Nova Bassano',
        u'Nova Boa Vista',
        u'Nova Brescia',
        u'Nova Candelaria',
        u'Nova Esperanca Do Sul',
        u'Nova Hartz',
        u'Nova Milano',
        u'Nova Padua',
        u'Nova Palma',
        u'Nova Petropolis',
        u'Nova Prata',
        u'Nova Ramada',
        u'Nova Roma Do Sul',
        u'Nova Santa Rita',
        u'Nova Sardenha',
        u'Novo Barreiro',
        u'Novo Cabrais',
        u'Novo Hamburgo',
        u'Novo Horizonte',
        u'Novo Machado',
        u'Novo Planalto',
        u'Novo Tiradentes',
        u'Oliva',
        u'Oralina',
        u'Osorio',
        u'Osvaldo Cruz',
        u'Osvaldo Kroeff',
        u'Otavio Rocha',
        u'Pacheca',
        u'Padilha',
        u'Padre Gonzales',
        u'Paim Filho',
        u'Palmares Do Sul',
        u'Palmas',
        u'Palmeira Das Missões',
        u'Palmitinho',
        u'Pampeiro',
        u'Panambi',
        u'Pantano Grande',
        u'Parai',
        u'Paraíso Do Sul',
        u'Pareci Novo',
        u'Parobe',
        u'Passa Sete',
        u'Passinhos',
        u'Passo Burmann',
        u'Passo Da Areia',
        u'Passo Da Caveira',
        u'Passo Das Pedras',
        u'Passo Do Adão',
        u'Passo Do Sabão',
        u'Passo Do Sobrado',
        u'Passo Fundo',
        u'Passo Novo',
        u'Passo Raso',
        u'Paulo Bento',
        u'Pavão',
        u'Paverama',
        u'Pedras Altas',
        u'Pedreiras',
        u'Pedro Garcia',
        u'Pedro Osorio',
        u'Pedro Paiva',
        u'Pejucara',
        u'Pelotas',
        u'Picada Café',
        u'Pinhal',
        u'Pinhal Alto',
        u'Pinhal Da Serra',
        u'Pinhal Grande',
        u'Pinhalzinho',
        u'Pinheirinho Do Vale',
        u'Pinheiro Machado',
        u'Pinheiro Marcado',
        u'Pinto Bandeira',
        u'Pirai',
        u'Pirapo',
        u'Piratini',
        u'Pitanga',
        u'Planalto',
        u'Plano Alto',
        u'Poço Das Antas',
        u'Poligono Do Erval',
        u'Polo Petroquimico De Triunfo',
        u'Pontão',
        u'Ponte Preta',
        u'Portão',
        u'Porto Alegre',
        u'Porto Batista',
        u'Porto Lucena',
        u'Porto Maua',
        u'Porto Vera Cruz',
        u'Porto Xavier',
        u'Pouso Novo',
        u'Povo Novo',
        u'Povoado Tozzo',
        u'Pranchada',
        u'Pratos',
        u'Presidente Lucena',
        u'Progresso',
        u'Protasio Alves',
        u'Pulador',
        u'Putinga',
        u'Quarai',
        u'Quaraim',
        u'Quatro Irmãos',
        u'Quevedos',
        u'Quilombo',
        u'Quinta',
        u'Quintão',
        u'Quinze De Novembro',
        u'Quiteria',
        u'Rancho Velho',
        u'Redentora',
        u'Refugiado',
        u'Relvado',
        u'Restinga Seca',
        u'Rincão De São Pedro',
        u'Rincão Del Rei',
        u'Rincão Do Cristovão Pereira',
        u'Rincão Do Meio',
        u'Rincão Do Segredo',
        u'Rincão Doce',
        u'Rincão Dos Kroeff',
        u'Rincão Dos Mendes',
        u'Rincão Vermelho',
        u'Rio Azul',
        u'Rio Branco',
        u'Rio Da Ilha',
        u'Rio Dos Indios',
        u'Rio Grande',
        u'Rio Pardinho',
        u'Rio Pardo',
        u'Rio Telha',
        u'Rio Tigre',
        u'Rio Toldo',
        u'Riozinho',
        u'Roca Sales',
        u'Rodeio Bonito',
        u'Rolador',
        u'Rolante',
        u'Rolantinho Da Figueira',
        u'Ronda Alta',
        u'Rondinha',
        u'Roque Gonzales',
        u'Rosario',
        u'Rosario Do Sul',
        u'Sagrada Familia',
        u'Saica',
        u'Saldanha Marinho',
        u'Saltinho',
        u'Salto',
        u'Salto Do Jacuípe',
        u'Salvador Das Missões',
        u'Salvador Do Sul',
        u'Sananduva',
        u'Sant Auta',
        u'Santa Barbara',
        u'Santa Barbara Do Sul',
        u'Santa Catarina',
        u'Santa Cecilia',
        u'Santa Clara Do Ingai',
        u'Santa Clara Do Sul',
        u'Santa Cristina',
        u'Santa Cruz',
        u'Santa Cruz Da Concórdia',
        u'Santa Cruz Do Sul',
        u'Santa Flora',
        u'Santa Ines',
        u'Santa Izabel Do Sul',
        u'Santa Lucia',
        u'Santa Lucia Do Piai',
        u'Santa Luiza',
        u'Santa Luzia',
        u'Santa Maria',
        u'Santa Maria Do Herval',
        u'Santa Rita Do Sul',
        u'Santa Rosa',
        u'Santa Silvana',
        u'Santa Teresinha',
        u'Santa Tereza',
        u'Santa Vitória Do Palmar',
        u'Santana',
        u'Santana Da Boa Vista',
        u'Santana Do Livramento',
        u'Santiago',
        u'Santo Amaro Do Sul',
        u'Santo Angelo',
        u'Santo Antônio',
        u'Santo Antônio Da Patrulha',
        u'Santo Antônio Das Missões',
        u'Santo Antônio De Castro',
        u'Santo Antônio Do Bom Retiro',
        u'Santo Antônio Do Palma',
        u'Santo Antônio Do Planalto',
        u'Santo Augusto',
        u'Santo Cristo',
        u'Santo Expedito Do Sul',
        u'Santo Inacio',
        u'São Bento',
        u'São Bom Jesus',
        u'São Borja',
        u'São Carlos',
        u'São Domingos Do Sul',
        u'São Francisco',
        u'São Francisco De Assis',
        u'São Francisco De Paula',
        u'São Gabriel',
        u'São Jeronimo',
        u'São João',
        u'São João Batista',
        u'São João Bosco',
        u'São João Da Urtiga',
        u'São João Do Polesine',
        u'São Jorge',
        u'São José',
        u'São José Da Gloria',
        u'São José Das Missões',
        u'São José De Castro',
        u'São José Do Centro',
        u'São José Do Herval',
        u'São José Do Hortencio',
        u'São José Do Inhacora',
        u'São José Do Norte',
        u'São José Do Ouro',
        u'São José Dos Ausentes',
        u'São Leopoldo',
        u'São Lourenco Das Missões',
        u'São Lourenco Do Sul',
        u'São Luis Rei',
        u'São Luiz',
        u'São Luiz Gonzaga',
        u'São Manuel',
        u'São Marcos',
        u'São Martinho',
        u'São Martinho Da Serra',
        u'São Miguel',
        u'São Miguel Das Missões',
        u'São Nicolau',
        u'São Paulo',
        u'São Paulo Das Missões',
        u'São Pedro',
        u'São Pedro Da Serra',
        u'São Pedro Do Butia',
        u'São Pedro Do Iraxim',
        u'São Pedro Do Sul',
        u'São Roque',
        u'São Sebastião',
        u'São Sebastião Do Cai',
        u'São Sepe',
        u'São Simão',
        u'São Valentim',
        u'São Valentim Do Sul',
        u'São Valério Do Sul',
        u'São Vendelino',
        u'São Vicente Do Sul',
        u'Sapiranga',
        u'Sapucaia Do Sul',
        u'Sarandi',
        u'Scharlau',
        u'Seberi',
        u'Seca',
        u'Sede Aurora',
        u'Sede Nova',
        u'Segredo',
        u'Seival',
        u'Selbach',
        u'Senador Salgado Filho',
        u'Sentinela Do Sul',
        u'Serafim Schmidt',
        u'Serafina Correa',
        u'Serio',
        u'Serra Dos Gregorios',
        u'Serrinha',
        u'Sertão',
        u'Sertão Santana',
        u'Sertãozinho',
        u'Sete De Setembro',
        u'Sete Lagoas',
        u'Severiano De Almeida',
        u'Silva Jardim',
        u'Silveira',
        u'Silveira Martins',
        u'Sinimbu',
        u'Sirio',
        u'Sítio Gabriel',
        u'Sobradinho',
        u'Soledade',
        u'Souza Ramos',
        u'Suspiro',
        u'Tabai',
        u'Tabajara',
        u'Taim',
        u'Tainhas',
        u'Tamandua',
        u'Tanque',
        u'Tapejara',
        u'Tapera',
        u'Tapes',
        u'Taquara',
        u'Taquari',
        u'Taquarichim',
        u'Taquarucu Do Sul',
        u'Tavares',
        u'Tenente Portela',
        u'Terra De Areia',
        u'Tesouras',
        u'Teutonia',
        u'Tiaraju',
        u'Timbauva',
        u'Tiradentes Do Sul',
        u'Toropi',
        u'Toroqua',
        u'Torquato Severo',
        u'Torres',
        u'Torrinhas',
        u'Touro Passo',
        u'Tramandai',
        u'Travesseiro',
        u'Trentin',
        u'Três Arroios',
        u'Três Barras',
        u'Três Cachoeiras',
        u'Três Coroas',
        u'Três De Maio',
        u'Três Forquilhas',
        u'Três Palmeiras',
        u'Três Passos',
        u'Três Vendas',
        u'Trindade Do Sul',
        u'Triunfo',
        u'Tronqueiras',
        u'Tucunduva',
        u'Tuiuti',
        u'Tunas',
        u'Tunel Verde',
        u'Tupanci Do Sul',
        u'Tupancireta',
        u'Tupancy Ou Vila Block',
        u'Tupandi',
        u'Tupantuba',
        u'Tuparendi',
        u'Tupi Silveira',
        u'Tupinamba',
        u'Turucu',
        u'Turvinho',
        u'Ubiretama',
        u'Umbu',
        u'União Da Serra',
        u'Unistalda',
        u'Uruguaiana',
        u'Vacacai',
        u'Vacaria',
        u'Valdastico',
        u'Vale Do Rio Cai',
        u'Vale Do Sol',
        u'Vale Real',
        u'Vale Veneto',
        u'Vale Verde',
        u'Vanini',
        u'Venancio Aires',
        u'Vera Cruz',
        u'Veranópolis',
        u'Vertentes',
        u'Vespasiano Correa',
        u'Viadutos',
        u'Viamão',
        u'Vicente Dutra',
        u'Victor Graeff',
        u'Vila Bender',
        u'Vila Cruz',
        u'Vila Flores',
        u'Vila Langaro',
        u'Vila Laranjeira',
        u'Vila Maria',
        u'Vila Nova Do Sul',
        u'Vila Rica',
        u'Vila Seca',
        u'Vila Turvo',
        u'Vista Alegre',
        u'Vista Alegre Do Prata',
        u'Vista Gaucha',
        u'Vitória',
        u'Vitória Das Missões',
        u'Volta Alegre',
        u'Volta Fechada',
        u'Volta Grande',
        u'Xadrez',
        u'Xangri-la',
        u'Xingu',
    )
]
