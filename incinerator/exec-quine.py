import base64
dna='aW1wb3J0IGJhc2U2NApkbmE9JyonCnF1aW5lPWxhbWJkYTpiYXNlNjQuYjY0ZGVjb2RlKGRuYS5lbmNvZGUoJ3V0Zi04JykpLmRlY29kZSgndXRmLTgnKS5yZXBsYWNlKGNocig0MiksZG5hKQ=='
quine=lambda:base64.b64decode(dna.encode('utf-8')).decode('utf-8').replace(chr(42),dna)