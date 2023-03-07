import fire

def hello(name="World"):
  return "Adiós %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
