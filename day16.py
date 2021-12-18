def binToInt(bin):
	return int(''.join(bin), 2)


def GetPackets(code, amt=0, ignorePadding=False, parentsname=''):
	packets = []
	data = code
	while len(set(data)) > 1:
		packet = Packet(data, ignorePadding, name=str(len(packets)), parentsname=parentsname)
		packets.append(packet)
		data = packet.leftoverBits
		if len(packets) == amt:
			break
	return packets, data


hex2bin = {
	'0':'0000',
	'1':'0001',
	'2':'0010',
	'3':'0011',
	'4':'0100',
	'5':'0101',
	'6':'0110',
	'7':'0111',
	'8':'1000',
	'9':'1001',
	'A':'1010',
	'B':'1011',
	'C':'1100',
	'D':'1101',
	'E':'1110',
	'F':'1111'
	}


class Packet:
	_LTIdict = {0:15, 1:11}

	def __init__(self, bits, ignorePadding=False, name = '', parentsname = ''):
		self.bits = bits
		self._ignorePadding = ignorePadding
		self._padding = 0
		self.version = binToInt(self.bits[:3])
		self.type = binToInt(self.bits[3:6])
		self._encodedBits = bits[6:]
		self.subpackets = []
		self.name = parentsname + '-' + name if parentsname != '' else name
		print(self.name)
		self.DecodeBits()
		self.activeBits = self.bits[:self._currLen + self._padding]
		self.leftoverBits = self.bits[self._currLen + self._padding:]
		self.size = len(self.activeBits)

	def DecodeBits(self):
		if self.type == 4:
			getliteral = [self._encodedBits[1:5]]
			cont = self._encodedBits[0]
			cnt = 1
			while cont == '1':
				cont = self._encodedBits[5 * cnt]
				getliteral.append(self._encodedBits[cnt * 5 + 1:cnt * 5 + 6])
				cnt += 1
			self.literal = int(''.join(getliteral), 2)
			self._currLen = 6 + cnt * 5
			print(self.bits[:self._currLen])
			if not self._ignorePadding:
				self._padding = 4 - (self._currLen % 4)
		else:
			self.LTI = int(self._encodedBits[0])
			self._LTIInstLen = self._LTIdict[self.LTI]
			self.LTIInst = binToInt(self._encodedBits[1:self._LTIInstLen + 1])
			self._currLen = 6 + 1 + self._LTIInstLen
			print(self.bits[:self._currLen])
			if self.LTI == 0:
				self._padding = self.LTIInst
				self.subpackets = GetPackets(
						self._encodedBits[self._LTIInstLen + 1:self.LTIInst + self._LTIInstLen + 1],
						ignorePadding=True,
						parentsname=self.name
						)[0]
			else:
				self.subpackets, leftover = GetPackets(self._encodedBits[self._LTIInstLen + 1:], self.LTIInst, True, parentsname=self.name)
				self._padding = sum([packet.size for packet in self.subpackets]) + len(leftover)

	def GetVersions(self):
		if any(self.subpackets):
			return self.version + sum([pack.GetVersions() for pack in self.subpackets])
		return self.version


with open('day16.txt') as f:
	raw = f.read().splitlines()
	raw = [list(e) for e in raw][0]
	inputcode = ''.join([hex2bin[c] for c in raw])
	print(inputcode)
	print(sum([pack.GetVersions() for pack in GetPackets(inputcode)[0]]))
