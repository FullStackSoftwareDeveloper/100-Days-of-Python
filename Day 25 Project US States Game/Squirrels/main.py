import pandas

data = pandas.read_csv("squirrel_data.csv")

var1 = len(data[data["Primary Fur Color"] == "Gray"])
var2 = len(data[data["Primary Fur Color"] == "Cinnamon"])
var3 = len(data[data["Primary Fur Color"] == "Black"])

squirrels = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [var1, var2, var3],
}

df = pandas.DataFrame(squirrels)
df.to_csv("squirrels_count.csv")