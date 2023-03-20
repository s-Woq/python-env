import matplotlib.pyplot as plt

def generate_pie_chart(labels,values):

    fig,ax =  plt.subplots()
    ax.pie(values , labels = labels)
    ax.axis("equal")
    plt.savefig("pie.png")
    plt.close()
   
def generate_bar_chart(name,labels, values):
    fig , ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f"./charts/{name}.png")
    plt.close()


generate_bar_chart("peep", ["tobo","juan","mario"],[122,1212,1212])