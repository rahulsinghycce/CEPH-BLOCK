import rados
import rbd



class InitCluster():
     ''' initialise cluster connection'''
     cluster = ''
     def __init__(self):
         pass

     def initialise(self):
         try:
             cluster = rados.Rados(conffile='/root/RBD/config_file')

         except TypeError as e:
             print 'Argument validation error: ', e
             raise e

     def connect(self):

         try:
             cluster.connect()
             return cluster
         except Exception as e:
             print "connection error: ", e
             raise e
         finally:
             print "Connected to the cluster."


     def close(self):
         cluster.close()

def clusterinit():

    try:
        cluster = rados.Rados(conffile='/root/RBD/config_file')

    except TypeError as e:
        print 'Argument validation error: ', e
        raise e

    try:
        cluster.connect()
    except Exception as e:
        print "connection error: ", e
        raise e
    finally:
        print "Connected to the cluster."

    return cluster

class CephVol():

    def __init__(self,size,pool,image_name):
        ''' initialise volume attributes'''
        self.size = size
        self.pool = pool
        self.image_name = image_name

    def create(self):
        '''create ceph volume'''
        cluster = clusterinit()
        try:
            print "\nCreating a context for the 'data' pool"
            if not cluster.pool_exists(self.pool):
                raise RuntimeError('No data pool exists')
            ioctx = cluster.open_ioctx(self.pool)
            try:
                rbd_inst = rbd.RBD()
                size = self.size * 1024**3
                rbd_inst.create(ioctx, self.image_name, size)
            except Exception as e:
                print(e)
            finally:
                ioctx.close()
        finally:
#            cluster.shutdown()
            pass

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='options for creating ceph volume')

    parser.add_argument('--size','-s',action='store',default=1, required=True, type=int, help='size in GB')
    parser.add_argument('--pool','-p',action='store',required=True,help='pool name to be created. Cannot be NULL')
    parser.add_argument('--image-name','-i',action='store',required=True,help='Image name')

    args = parser.parse_args()

    print args.size,args.pool,args.image_name
    try:
        cluster = rados.Rados(conffile='/root/RBD/config_file')

    except TypeError as e:
        print 'Argument validation error: ', e
        raise e

    try:
        cluster.connect()
    except Exception as e:
        print "connection error: ", e
        raise e
    finally:
        print "Connected to the cluster."

    myvol=CephVol(args.size,args.pool,args.image_name)
    myvol.create(cluster)
