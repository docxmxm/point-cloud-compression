def load_ply_data(filename):
  '''
  load data from ply file.
  '''
  f = open(filename)
  #1.read all points
  points = []
  for line in f:
    #only x,y,z
    wordslist = line.split(' ')
    try:
      x, y, z = float(wordslist[0]),float(wordslist[1]),float(wordslist[2])
    except ValueError:
      continue
    points.append([x,y,z])
  points = np.array(points)
  points = points.astype(np.int32)#np.uint8
  # print(filename,'\n','length:',points.shape)
  f.close()

  return points
