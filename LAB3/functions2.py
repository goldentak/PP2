movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def overfive(movie):
    return movie["imdb"] > 5.5
print(overfive(movies[0]))
print(overfive(movies[7]))


#2
def movieList(movie):
    toPrint = []
    for i in movie:
        if i["imdb"] > 5.5:
            toPrint.append(i)
    
    return toPrint
print(movieList(movies))

#3
def sameCategory(category):
    names = []
    for i in movies:
        if i["category"] == category:
            names.append(i["name"])
    return names
print(sameCategory("Thriller"))

#4
def avgScore():
    avg = 0
    for i in movies:
        avg += i["imdb"]
    return avg / len(movies)
print(avgScore())

#5
def avgCategory(category):
    avg = 0
    s = 0
    for i in movies:
        if i["category"] == category:
            avg += i['imdb']
            s += 1
    return avg / s
print(avgCategory("Thriller"))