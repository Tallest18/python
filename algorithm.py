
db = [
    {"name": "Alice", "rank": "manager"},
    {"name": "Bob", "rank": "employee"},
]

def add_user(name, rank):
    db.append({"name": name, "rank": rank})

def get_users():
    [print(u) for u in db]

def update_rank(name, new_rank):
    for u in db:
        if u["name"] == name:
            u["rank"] = new_rank
            
def nuke_users(name):
    global db
    db = [u for u in db if u["name"] != name]

add_user("max", "intern")
update_rank("Alice", "CTO")
nuke_users("Bob")
print(db)