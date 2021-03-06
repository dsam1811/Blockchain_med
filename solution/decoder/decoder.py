from .deserialize import *
from .BCDataStream import *
import codecs


def decoder(hexstr):
    decode_hex = codecs.getdecoder("hex_codec")
    test = BCDataStream()
    test.write(decode_hex(hexstr)[0])
    tx = parse_Transaction(test)
    values = []

    for txOut in tx['txOut'][1:8]:
        decoded = [x for x in script_GetOp(txOut['scriptPubKey'])]
        values.append(str(decoded[2][1][4:], 'ascii'))
    return '\t'.join(values)
