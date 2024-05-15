import sys 
import Ice
Ice.loadSlice('Printer.ice')
import Example

class Client(Ice.Application):
    def run(self, argv):
        config = "tcp -h localhost -p 5018"
        proxy = self.communicator().stringToProxy("printer1:" + config)
        printer = Example.PrinterPrx.checkedCast(proxy)
    
        if not printer:
            raise RuntimeError('Error Proxy')
    
        printer.write('¡Hola mundo!')
    
        return 0

sys.exit(Client().main(sys.argv))

