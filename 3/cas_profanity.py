bad_words = ['shit', 'fuck', 'ass']
profanity_filter_on = True
sentence = ['How', 'are', 'you', 'shit', 'face', '?']
censored_sentence = ''
censored_list = []
for x in sentence:
	if x in bad_words:
		censored_list.append('*' * len(x))
		censored_sentence = censored_sentence + '*' * len(x) + ' '
	else:
		censored_list.append(x)
		censored_sentence = censored_sentence + x + ' '
print(censored_sentence)
print(censored_list)
