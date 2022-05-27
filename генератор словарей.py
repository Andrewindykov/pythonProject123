m={'хорошо':'4', "удовлетворительно":'8', "Отлично ":6}
a={key.upper(): int(value) for key, value in m.items()}
print(a)

