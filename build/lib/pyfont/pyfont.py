#-------------------------------------#
#Created by George Leonard 26/04/18
#-------------------------------------#
class pyfont:
    def __init__():
        print("Welcome to the font converter, all credit for fonts go to https://coolsymbol.com/cool-fancy-text-generator.html")

    def convert(text, fonttype):
        """---------------------------------------------------------------------------------------"""
        """SOURCE FOR FONTS IS https://coolsymbol.com/cool-fancy-text-generator.html"""
        bubble = {"a":"ⓐ","b":"ⓑ","c":"ⓒ","d":"ⓓ","e":"ⓔ","f":"ⓕ","g":"ⓖ","h":"ⓗ","i":"ⓘ","j":"ⓙ","k":"ⓚ","l":"ⓛ","m":"ⓜ","n":"ⓝ","o":"ⓞ","p":"ⓟ","q":"ⓠ","r":"ⓡ","s":"ⓢ","t":"ⓣ","u":"ⓤ","v":"ⓥ","w":"ⓦ","x":"ⓧ","y":"ⓨ","z":"ⓩ", " ": " ", ",":",",".":"."}
        doublestruck = {"a":"𝕒","b":"𝕓","c":"𝕔","d":"𝕕","e":"𝕖","f":"𝕗","g":"𝕘","h":"𝕙","i":"𝕚","j":"𝕛","k":"𝕜","l":"𝕝","m":"𝕞","n":"𝕟","o":"𝕠","p":"𝕡","q":"𝕢","r":"𝕣","s":"𝕤","t":"𝕥","u":"𝕦","v":"𝕧","w":"𝕨","x":"𝕩","y":"𝕪","z":"𝕫", " ": " ", ",":",",".":"."}
        boldscript = {"a":"𝓪","b":"𝓫","c":"𝓬","d":"𝓭","e":"𝓮","f":"𝓯","g":"𝓰","h":"𝓱","i":"𝓲","j":"𝓳","k":"𝓴","l":"𝓵","m":"𝓶","n":"𝓷","o":"𝓸","p":"𝓹","q":"𝓺","r":"𝓻","s":"𝓼","t":"𝓽","u":"𝓾","v":"𝓿","w":"𝔀","x":"𝔁","y":"𝔂","z":"𝔃", " ": " ", ",":",",".":"."}
        sorcerer = {"a":"ǟ","b":"ɮ","c":"ƈ","d":"ɖ","e":"ɛ","f":"ʄ","g":"ɢ","h":"ɦ","i":"ɨ","j":"ʝ","k":"ӄ","l":"ʟ","m":"ʍ","n":"ռ","o":"օ","p":"ք","q":"զ","r":"ʀ","s":"ֆ","t":"ȶ","u":"ʊ","v":"ʋ","w":"ա","x":"Ӽ","y":"ʏ","z":"ʐ", " ": " ", ",":",",".":"."}
        strikethrough = {"a":"a̶","b":"b̶","c":"c̶","d":"d̶","e":"e̶","f":"f̶","g":"g̶","h":"h̶","i":"i̶","j":"j̶","k":"k̶","l":"l̶","m":"m̶","n":"n̶","o":"o̶","p":"p̶","q":"q̶","r":"r̶","s":"s̶","t":"t̶","u":"u̶","v":"v̶","w":"w̶","x":"x̶","y":"y̶","z":"z̶", " ": " ", ",":",",".":"."}
        currency = {'a': '₳', 'b': '฿', 'c': '₵', 'd': 'Đ', 'e': 'Ɇ', 'f': '₣', 'g': '₲', 'h': 'Ⱨ', 'i': 'ł', 'j': 'J', 'k': '₭', 'l': 'Ⱡ', 'm': '₥', 'n': '₦', 'o': 'Ø', 'p': '₱', 'q': 'Q', 'r': 'Ɽ', 's': '₴',
        't': '₮', 'u': 'Ʉ', 'v': 'V', 'w': '₩', 'x': 'Ӿ', 'y': 'Ɏ', 'z': 'Ⱬ', " ": " ", ",":",",".":"."}
        magic = {'a': 'Ꭺ', 'b': 'b', 'c': 'Ꮯ', 'd': 'Ꭰ', 'e': 'Ꭼ', 'f': 'f', 'g': 'Ꮆ', 'h': 'h', 'i': 'Ꭵ', 'j': 'j', 'k': 'Ꮶ', 'l': 'Ꮮ', 'm': 'm', 'n': 'Ꮑ', 'o': 'Ꮎ', 'p': 'Ꮲ', 'q': 'q', 'r': 'Ꮢ', 's': 's', 't': 'Ꮖ', 'u': 'u', 'v': 'Ꮙ', 'w': 'Ꮃ', 'x': 'x', 'y': 'Ꮍ', 'z': 'Ꮓ', " ": " ", ",":",",".":"."}
        knight = {'a': 'Ḁ', 'b': 'ḃ', 'c': 'ḉ', 'd': 'Ḋ', 'e': 'ḕ', 'f': 'ḟ', 'g': 'Ḡ', 'h': 'ḧ', 'i': 'ḭ', 'j': 'j', 'k': 'Ḳ', 'l': 'Ḷ', 'm': 'ṁ', 'n': 'Ṇ', 'o': 'ṏ', 'p': 'Ṗ', 'q': 'q', 'r': 'ṙ', 's': 'Ṡ', 't': 'Ṯ', 'u': 'ṳ', 'v': 'Ṽ', 'w': 'ẇ', 'x': 'Ẍ', 'y': 'ẏ', 'z': 'Ẓ', " ": " ", ",":",",".":"."}
        """---------------------------------------------------------------------------------------"""

        newtext = []

        text = text.lower()
        for char in text:
            if fonttype == "bubble":
                char = bubble[char]
            if fonttype == "doublestruck":
                char = doublestruck[char]
            if fonttype == "boldscript":
                char = boldscript[char]
            if fonttype == "sorcerer":
                char = sorcerer[char]
            if fonttype == "strikethrough":
                char = strikethrough[char]
            if fonttype == "knight":
                char = knight[char]
            if fonttype == "magic":
                char = magic[char]
            if fonttype == "currency":
                char = currency[char]
            newtext.append(char)
        newtext = "".join(newtext)
        return newtext
        print(newtext)