#Перевірити чи отримано очікування значення (юніттести)

actual_submissions = [120, "Hello world", ["Python", "Java Script", "Dart"]]
expected_submissions = [120, "Hello world", ["Python", "C++"]]

for actual_submission, expected_submission in (
    zip(actual_submissions, expected_submissions)
):
    if actual_submission != expected_submission:
        print(
            f"Wrong answer. Actual: {actual_submission}"
            f"Expected: {expected_submission}"
        )