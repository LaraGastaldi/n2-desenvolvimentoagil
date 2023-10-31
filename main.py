def encrypt_this(to_encrypt):
  return " ".join(
      [str(ord(x[0])) + x[-1] + x[2:-1] + x[1] for x in to_encrypt.split(" ")])
