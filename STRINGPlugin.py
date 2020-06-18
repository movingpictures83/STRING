import sys
import pypathway
from pypathway import STRING

class STRINGPlugin:
   def input(self, inputfile):
      self.query = inputfile[inputfile.rfind('/')+1:]

   def run(self):
      self.results = STRING().search("trpA")

   def output(self, outputfile):
      outfile = open(outputfile, 'w')
      for reaction in set(self.results):
         outfile.write("***************************************\n")
         outfile.write(str(reaction))
         outfile.write("\n***************************************\n")
