a = '''
What is the National Energy and Climate Plans (EU) all about?

National Energy and Climate Plans (PNEC) were introduced by the Energy and Climate Action Union (EU) Governance Regulation 2018/1999, agreed as part of the Clean Energy for All Europeans package adopted in 2019.

National plans describe how EU countries intend to address:
- energy efficiency
- renewable
- reductions in greenhouse gas emissions
- interconnections
- research and innovation
This approach requires coordination of objectives across government departments and provides a level of planning that will facilitate public and private investment.

The dataset consists of columns: country, subsection, dimension and text (automatically extracted and raw).

Source: https://ec.europa.eu/info/energy-climate-change-environment/implementation-eu-countries/energy-and-climate-governance-and-reporting/national-energy-and-climate-plans_en

'''

b = '''\n\n The present time program aims to answer the following questions:

0 - THE LIST OF COUNTRIES AND THEIR ENGAGEMENTS IN EACH THEME.
1 - Which country is more engaged for each of the themes?
2 - What is the theme with the greatest general engagement in the countries and the percentage of each one?
3 - Country/proposal ratio for energy efficiency.
4 - Country/proposal ratio for decarbonisation.
5 - Country/proposal ratio for energy security.
6 - Country/proposal ratio for Internal market.
7 - Country/proposal ratio for research and innovation.
'''

c = '''\n\n Some technical details:

-This data analysis was produced by combining native Python themes with functions from the Pandas library.
-In some cells we will display NaN - which means empty.
'''

d = '''\n\nAbout developer:

-Hello, my name is Luiz Esquivel, I'm 19 years old and currently I work as a Jr IT Analyst at Ultracom, being essentially co-responsible for the management activities of the mailing (I manage the data of clients and potential clients that we need to contact or have already contact us), I also manage data about customers and potential customers (such as: availability to serve their region with internet/telephrony products; primary credit analysis; primary analysis of data provided by the customer...) .
-I have been a development student since 2019, when I started studying WEB development, migrating to the data area in 2022, as I feel more confident in this area and recognize the importance of data in the lives and projects of companies and people.
-In the data area, my knowledge is centered on Office Package (especially Word and Excel); Business Intelligence methodology and tools (such as PowerBI); Database and its Management Systems (SQL and MySQL); Python focused on data analysis (automation of routines with Python).
'''

def about():
    texto = ""
    texto += a + b + c + d
    txt = texto.split("\n\n ")
    
    for i in txt:
        if input('Do you wish to continue? Y for yes and N for NO:-') == "N": break
        print(i)