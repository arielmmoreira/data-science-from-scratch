from collections import Counter, defaultdict
from matplotlib import pyplot as plt

users = [
    {"id": 0, "name": "Hero", "friends": []},
    {"id": 1, "name": "Dunn", "friends": []},
    {"id": 2, "name": "Sue", "friends": []},
    {"id": 3, "name": "Chi", "friends": []},
    {"id": 4, "name": "Thor", "friends": []},
    {"id": 5, "name": "Clive", "friends": []},
    {"id": 6, "name": "Hicks", "friends": []},
    {"id": 7, "name": "Devin", "friends": []},
    {"id": 8, "name": "Kate", "friends": []},
    {"id": 9, "name": "Klein", "friends": []}
]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]


salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)
                        ]


for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


def number_of_friends(user):
    """
    :param user: a dictionary representing an user
    :return: total of user's friend
    """
    return len(user["friends"])


total_connections = sum(number_of_friends(user) for user in users) # 24

num_users = len(users)
avg_connections = total_connections / num_users # 2.4

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_by_id.sort(key=lambda num_friends: num_friends[1], reverse=True)


def get_name(user_id):
    for user in users:
        if user["id"] == user_id:
            return user["name"]


def not_the_same(user, other_user):
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    return all(not_the_same(friend, other_user) for friend in user["friends"])


def friends_of_friend(user):
    return Counter(friend_of_friend["id"]
                   for friend in user["friends"]
                   for friend_of_friend in friend["friends"]
                   if not_the_same(user, friend_of_friend) and not_friends(user, friend_of_friend))


user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


def most_common_interests_with(user):
    return [interested_user_id
            for interest in interests_by_user_id[user["id"]]
            for interested_user_id in user_ids_by_interest[interest]
            if interested_user_id != user["id"]]


salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)


avg_salary_by_bucket = {
    tenure_bucket: round(sum(salaries) / len(salaries), 2)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}


words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split()
                           )

