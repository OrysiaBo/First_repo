#Валідувіати опис ( не більше 120 символів)

max_description_value = 10

response_body = {
    "course_name": "Math",
    "description": (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    ),
}
print((response_body["description"]))
print(len(response_body["description"]))

if len(response_body["description"]) >= 10:
    print("the description is too long.")
