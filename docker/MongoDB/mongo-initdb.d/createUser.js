db = db.getSiblingDB('<database>'),
db.createUser({
    user: "<username>",
    pwd: "<password>",
    roles: ["readWrite"]
});
