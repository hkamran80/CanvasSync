"""
A dummy module that does no encryption.
"""

def encrypt(message):
    return message.encode('utf-8')

def decrypt(message, password):
    return message
