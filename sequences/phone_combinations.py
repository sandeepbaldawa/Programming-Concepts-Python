d = { '1': "1",
      '2': "ABC",
      '3': "DEF",
      '4': "GHI",
      '5': "JKL",
      '6': "MNO",
      '7': "PQRS",
      '8': "TUV",
      '9': "WXYZ",
}

def digstolets(digs):
  if len(digs) == 0:
    yield ''
    return
  first, rest = digs[0], digs[1:]
  for x in d[first]:
      for y in digstolets(rest): yield x + y

print list(digstolets('1234'))
