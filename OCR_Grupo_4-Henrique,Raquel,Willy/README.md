# Scripts & Modules

![example usage](readme_img_01.png example usage)

## `ppxml.py`

Pretty prints xml passed to it, input:
	* as a python module
	* as arguments either a valid filepath to xml file 
	or valid xml as quoted string
	* as valid xml strings from `stdin`

## `tagReplacer.py`

Replace/strips XML tags, 
`<>` should not be written
@atributes can be written in form `'a href="./source/"'`
it defaults to replacing everytag with '' effectively stripping
can selectively change tags if given a pair of tags, 
or selectively strip a tag if given a single one.
_Self Closing_ tags must be explicitly marked by a boolean flag
>it cannot replace self_closing with regular tag, nor vise-versa
>can replace for instance `<br />` with `<lb />`<>`
input:
	* as a python module, expecting valid SGML str
	optionally taking 
		- tag_to_be_replaced, 
		- replacer, 
		- bool_is_self_closing
	* as command line arguments 
		- either a valid filepath to xml file 
		or valid xml as quoted string. 
		>Optionally folllowed by:
		- tag_to_be_replaced, 
		- replacer
		~~bool~~
	* as valid xml strings from `stdin`, 
	stripping all tags on the output

## `substDict.py`

make dictionary substitutions on strings,
has a written in dictionary, 
but seeks first on `./sources/dictSubst.json`
input:
	* as a python module, accepting text 
	and optionally a substitution dictionary
	* as command line arguments 
		- either a valid filepath to xml file 
		or valid xml as quoted string
	* as valid xml strings from `stdin`

## `expanAbbr.py` & `regOrig.py`

takes @`attributes` into the text per se, 
wraps everything in `<orig>` if not already
