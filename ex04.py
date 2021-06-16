
ID = input('IDを入力してください:')
Pass = input('Passを入力してください:')

trueID = 'yoshino'
truePass = 'yt1974'

def check():
	if ID == trueID and Pass == truePass:
		print('OK')
	else:
		print('IDかパスワードが違います')

check()

