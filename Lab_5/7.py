import re

def snake_to_camel(snake):
    pattern = r"(^|_)([a-z])"
    return re.sub(pattern, lambda match: match.group(2).upper(), snake)

snake = "random_text_with_randomly_capitalized_text"
print(snake_to_camel(snake))
