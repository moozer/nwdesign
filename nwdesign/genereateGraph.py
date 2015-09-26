from graphOut.l2Graph import l2Graph
from restIO.restReader import restReader


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("rstFilename", help="reStructured text file to use")
    args = parser.parse_args()

    print args.rstFilename
    
    # read data
    r = restReader( args.rstFilename )
    hwList = r.hardwareList
    deviceConns = {}
    for dev in hwList:
        deviceConns[hwList[dev]] = r.getDeviceInfo( dev )

    # output graphs
    g = l2Graph(args.rstFilename)
    g.addDevices( deviceConns )
    g.generate()
    
main()