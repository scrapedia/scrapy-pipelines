db = db.getSiblingDB('test_db'),
db.createUser({
    user: "test_username",
    pwd: "test_password",
    roles: ["readWrite"]
});
