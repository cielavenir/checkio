import base64
def i_love_python():
	return base64.b64decode('SSBsb3ZlIFB5dGhvbiE=')

if __name__=='__main__':
	print(i_love_python())