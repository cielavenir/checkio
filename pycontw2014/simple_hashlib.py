checkio=lambda a,b:__import__('hashlib').__dict__[b](a.encode()).hexdigest()

if __name__ == '__main__':
	assert checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
	assert checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
	print('Done')