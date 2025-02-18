from datetime import datetime

students = [
    {
        "name": "Arnol",
        "birthday": "29-11-1990",
        "grades": [8, 7.5, 5.6, 9.8]
    },
    {
        "name": "Bella",
        "birthday": "15-04-1995",
        "grades": [9.2, 6.8, 7.5, 8.1]
    },
    {
        "name": "Carlos",
        "birthday": "08-07-1988",
        "grades": [5.5, 6.2, 7.8, 6.5]
    },
    {
        "name": "Diana",
        "birthday": "22-01-1992",
        "grades": [8.8, 9.1, 8.6, 9.0]
    },
    {
        "name": "Ethan",
        "birthday": "30-09-1993",
        "grades": [7.5, 6.7, 7.8, 8.0]
    },
    {
        "name": "Fiona",
        "birthday": "17-12-1996",
        "grades": [9.5, 9.8, 9.7, 10.0]
    },
    {
        "name": "George",
        "birthday": "03-05-1991",
        "grades": [6.5, 5.9, 7.1, 6.8]
    },
    {
        "name": "Hannah",
        "birthday": "27-06-1994",
        "grades": [8.3, 7.6, 9.2, 8.5]
    }
]


# media

def average(grades):
    return round(sum(grades) / len(grades), 2)

# print(list(map(lambda student: {"name": student["name"], "grades": student["grades"]}, students)))
print(list(map(lambda student: {"name": student["name"], "average": average(student["grades"])}, students)))

# los mejores
print(
    list(
        map(lambda student: 
            student["name"], 
             filter(lambda student: average(student["grades"]) >= 9, students))
        )
    )

# ordernar por fechas de nacimiento
print(sorted(students, key=lambda student: datetime.strptime(student["birthday"], "%d-%m-%Y"), reverse=True))

# clasificacin mas alta
print(list(map(lambda student: max(student["grades"]), students)))