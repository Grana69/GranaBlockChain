class Block:
	def __init__(self,ph,ts):
		self.ph = ph #Hash anterior
		self.ts = ts #Transaccion
		self.cn = str([hash(ts),ph]) #Combinacion hash datos y Hash anterior
		self.bh = hash(self.cn) #Generacion del nuevo hash
	def getPh(self):
		return self.ph
	def getTs(self):
		return self.ts
	def getBh(self):
		return self.bh

ts = "Enviar 10 objetos"
b1 = Block(0,ts)

ts2 = "Enviar 13 Objetos"
b2 = Block(b1.getBh(),ts2)

print "Hash Bloque 1: "
print b1.getBh()
print "Hash Bloque 2: " 
print b2.getBh()