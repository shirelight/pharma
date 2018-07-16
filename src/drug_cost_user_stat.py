class Sumdrug():
    def __init__(self, dname):
        self.name = dname
        self.user = set()
        self.total = 0

    def add_val(self, val, pname):
        self.total += val
        self.user.add(pname)

from heapq import heappush, heappop
import sys
def main():
    inpfile = sys.argv[1]
    outfile = sys.argv[2]
    drug_name = {}
    drug_price = []
    with open(inpfile) as infile:
        next(infile)
        for line in infile:
            data = line.split(",")
            pname, dname = data[1]+data[2], data[3]
            if dname not in drug_name:
                drug_name[dname] = Sumdrug(dname)
            drug_name[dname].add_val(int(data[-1]), pname)
    for dname in drug_name:
        heappush(drug_price, [-drug_name[dname].total, dname])
    with open(outfile, "w") as ofile:
        ofile.write("drug_name,num_prescriber,total_cost\n")
        for __ in range(len(drug_name)):
            price, dname = heappop(drug_price)
            ofile.write (dname+","+str(len(drug_name[dname].user))+","+str(-price)+"\n")

main()
