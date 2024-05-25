from django import template

register = template.Library()

censored_words = ['article', 'news']

@register.filter()
def censor(value):
    for word in censored_words:
        value = value.replace(word[1:], '*' * len(word))

    return value
