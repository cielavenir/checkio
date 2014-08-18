import base64
i_love_python=lambda:base64.b64decode('SSBsb3ZlIFB5dGhvbiE=').decode('utf-8')
if __name__=='__main__': assert i_love_python()=='I love Python!'