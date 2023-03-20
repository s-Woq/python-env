import readcsv
import charts
import utils2


def run():
    data=readcsv.read_csv("./csv/world_population.csv")
    data=list(filter(lambda item : item["Continent"] == 'South America' , data))

    countries=list(map(lambda x: x['Country/Territory'] , data))
    percentages= list(map(lambda x : x ["World Population Percentage"], data))
    charts.generate_pie_chart(countries,percentages)

    country= input("Type Country: ")
    result=utils2.populaiton_by_country(data, country)

    if len(result) > 0:
        country=result[0]
        print("it got this far")
        labels, values=utils2.get_population(country)
        charts.generate_bar_chart(country["Country/Territory"],values,labels)
    
    labels, values=utils2.get_population(country)

    charts.generate_bar_chart(country["Country/Territory"],values,labels)
if __name__ == "__main__":
    run()
