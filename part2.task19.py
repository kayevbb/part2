def moon_weight():
	weight = int(input('Сколько ты весишь? '))
	moon_w = weight * 0.165
	i = 0
	while i <= 15:
		resalt = moon_w + i
		year = 2019 + i
		i += 1
		print('Ваш вес {} году {} кг'.format(year, resalt))

moon_weight()