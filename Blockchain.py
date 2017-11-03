import hashlib
class Block:
	def __init__(self,ph,ts):
		self.ph = ph #Hash anterior
		self.ts = ts #Transaccion #aqui se pueden agregar los datos necesarios
		self.bh = "" #Hash a calcular
	def __str__(self):
		return self.bh
	def Calcular(self):
		self.bh = self.cSha256(str([self.cSha256(self.ts),self.ph]))
	def vCalcular(self):
		return self.cSha256(str([self.cSha256(self.ts),self.ph]))
	def getPh(self):
		return self.ph
	def getTs(self):
		return self.ts
	def getBh(self):
		return self.bh
	def cHash(self,cadena):
		return hash(cadena);
	def cSha256(self,cadena):
		return hashlib.sha256(cadena).hexdigest()

class CadenaDeBloques:
	def __init__(self):
		self.cadena = [self.primerBloque()]
	def primerBloque(self):
		bl = Block(0,"Primer Bloque")
		bl.Calcular()
		return bl
	def getUltimoBloque(self):
		return self.cadena[len(self.cadena) -1 ]
	def setNuevoBloque(self,bloque):
		bloque.ph = self.getUltimoBloque().bh
		bloque.Calcular()
		self.cadena.append(bloque)
	def validarCadena(self):
		for i in range(1, len(self.cadena)):
			if self.cadena[i].getBh() != self.cadena[i].vCalcular():
				return False
			if self.cadena[i].getPh() != self.cadena[i-1].getBh():
				return False
		return True
	def imprimirCadena(self):
		print "\nCadena de bloques:\n"
		for item in self.cadena:
			print "Transaccion: %s" % item.ts
			print "Hash: %s" % item.bh
			print "Hash Anterior: %s\n \n " % item.ph

bs = CadenaDeBloques()
bs.setNuevoBloque(Block(0,"Enviar 11 objetos"))
bs.setNuevoBloque(Block(1,"Enviar 13 objetos"))
bs.imprimirCadena()
print bs.validarCadena()
bs.cadena[1].ts = "Enviar 12 objetos"
print bs.validarCadena()