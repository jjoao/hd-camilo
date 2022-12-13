import re
import doctest

"""REVIEW!"""
def regOrig(xml):

	"""
	Given a XML string, 
    _substitute <orig> for its @reg attribute
						  <orig reg='Russian Federation'>Russian Soviet Federative Socialist Republic</orig>
		Russian Federation<orig reg='Russian Federation'>Russian Soviet Federative Socialist Republic</orig>

	:param xml: str
	:return: str

	>>> regOrig('<orig reg="Russian Federation">Russian Soviet Federative Socialist Republic</orig>')
	'Russian Federation<orig reg="Russian Federation">Russian Soviet Federative Socialist Republic</orig>'
	>>> regOrig('— E <orig reg="você"><abbr expan="vossa mercê">vm.<sup>ce</sup></abbr></orig> não acceitou a incumbencia')
	'— E você<orig reg="você"><abbr expan="vossa mercê">vm.<sup>ce</sup></abbr></orig> não acceitou a incumbencia'
	"""

	xml = re.sub(r'(<orig reg=")([^\"]+)(".*?<\/orig>)',
				 r'\2\1\2\3',xml)

	return xml

doctest.testmod()