f = open("./testChannels_t1c.cfg", "r")
g = open("testNamesOfPredictions.cfg","a")
line = f.readline()
while line:
        #print("Line {}: {}".format(cnt, line.strip()))        
        g.write("prediction_"+ line[50:].replace("/","_"))
        line = f.readline()
       
g.close()
f.close()