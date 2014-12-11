##############################################
#
#  RPYC Player class to be used with OOD Fall
#	2014 RPS Proxy pattern implementation
#
#__author__ = 'matt and tony'
#
##############################################
import rpyc
import MMJRPlayer

class RPYCPlayerService(rpyc.Service):
    #when connection is established
    def on_connect(self):
        print("Connected to server")
    #when connection is terminated
    def on_disconnect(self):
        print("Disconnected from server")
    
    #will create a player variable which is currently None at startup
    def __init__(self):

        self.player = None
        
    #gets name of player
    def exposed_get_name(self,player):
        return player.get_name()

    #calls player to "play" or make move
    def exposed_play(self,player):
        return player.play()

    #notifies player using the incoming message
    def exposed_notify(self,message):
        player.notify(message)
    #I assume this class will get the computer's personal player for tournament
    def exposed_get_player(self):


        #use the particular player on computer
        self.player=MMJRPlayer()
        return 
    
    #Not sure at all what to do
    def exposed_start_player_service(self):
        return None
if __name__ == "__main__" :
    from rpyc.utils.server import ThreadedServer
    server =
ThreadedServer(RPYCPlayerService,port=12345,protocol_config={'allow_public_attrs':True})
    server.start()
