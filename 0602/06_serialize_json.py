import json

obj1 = {'abc': (1,2,3),123: 'qwerty'}


s = json.dumps((obj1))
print(s)

obj2 = json.loads(s)

print(obj2)

print(obj1 == obj2)

print('''''blacl''''''''')
blackjack_hand = (8,'Q')
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)

print(blackjack_hand == decoded_hand)


print(type(blackjack_hand))
print(type(decoded_hand))

print(blackjack_hand == tuple(decoded_hand))