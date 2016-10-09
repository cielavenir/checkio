get_cookie=lambda a,b:{e[0]:e[1] for e in [e.split('=') for e in a.split('; ')]}[b]

if __name__ == "__main__":
	assert get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light', 'theme=light'
	assert get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true', 'ffo=true'
	print("Looks like you know everything. It is time for 'Check'!")
