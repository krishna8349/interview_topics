def reverse_sentence(sentence):

    words = sentence.split(' ')

    rev_sentence = ' '.join(reversed(words))

    return rev_sentence

sen = "My name is Krishna"
print(reverse_sentence(sen))