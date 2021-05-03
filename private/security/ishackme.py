from private.config.config import ecoleconf, anneeconf, speconf

sql = ['admin', 'test', '=', '!', '%', '--', '\'', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
xss = ['<', 'script', '--', '/', '=', '%', '#', '&', '*', '!']
tel = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']

def ishackme_(input_, dic):
	ishackme = False
	hack_ = sql if dic == 'sql' else tel if dic == 'tel' else xss

	if hack_ == 'tel':
		for i in range(len(str(input_))):
			if input_[i] not in hack_ :
				ishackme = True

	else :
		for hack in hack_:
			if hack in input_:
				ishackme = True

	return ishackme


def ishackme(username = '', email = '', nom = '', prenom = '', ecole = '', 	annee = '', phone = '', specialite = ''):
	ishackme = False

	for forms in (email, nom, prenom, ecole, annee, specialite):
		if ishackme_(forms, 'xss'):
			ishackme = True

	if email != '':
		if '@' not in email:
			ishackme = True

	if annee != '':
		if annee not in anneeconf:
			ishackme = True

	if ecole != '':
		if ecole not in ecoleconf :
			ishackme = True

	if specialite != '':
		if specialite not in speconf:
			ishackme = True

	if ishackme_(username, 'sql') :
		ishackme = True

	if phone != '':
		if ishackme_(phone, 'tel'):
			ishackme = True

	return ishackme
