def primary():
  # print("Keep it logically awesome.")
  # print("Hello there!")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[-1])

if __name__== "__main__":
  primary()
