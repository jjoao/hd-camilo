import re
import doctest

"""REVIEW!"""
def expanAbbr(xml):

	"""
	Given a XML string, 
	_substitute <abbr> for its @expan attribute
							<abbr expan="European Union">EU</abbr>
		European Union<orig><abbr expan='European Union'>EU</abbr></orig>

	:param xml: str
	:return: str

	>>> expanAbbr('<abbr expan="European Union">EU</abbr>')
	'European Union<orig><abbr expan="European Union">EU</abbr></orig>'
	>>> expanAbbr('<abbr expan="Ilustríssimo">Ill.<sup>mo</sup></abbr> <abbr expan="Senhor">Snr.</abbr> <abbr expan="Doutor">D.<sup>or</sup></abbr> Domingos')
	'Ilustríssimo<orig><abbr expan="Ilustríssimo">Ill.<sup>mo</sup></abbr></orig> Senhor<orig><abbr expan="Senhor">Snr.</abbr></orig> Doutor<orig><abbr expan="Doutor">D.<sup>or</sup></abbr></orig> Domingos'
	"""

	xml = re.sub(r'(<abbr expan=")([^\"]+)(".*?<\/abbr>)',
				 r'\2<orig>\1\2\3</orig>',xml)

	return xml

doctest.testmod()