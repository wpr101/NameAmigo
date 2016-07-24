import Mnemonic as m

a = m.Mnemonic(None)

#returns the same word if in the list
#for i in range(10):
	#print(list(a.get_suggestions('dogdog')))

#make a number go to a word, over 2000 creates new words
#print(a.mnemonic_encode(1))

#converts word to number (line in file)
#print(a.mnemonic_decode('test'))

#seed = a.mnemonic_to_seed(mnemonic='moment panther eyebrow pause deposit rice denial shoulder glory #kiss veteran galaxy', passphrase='none')
#print(seed.encode('hex'))


print(a.make_seed())
	
