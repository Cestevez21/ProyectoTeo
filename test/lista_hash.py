from nodo import Nodo
class ListaHash():
  def __init__(self):
    self.first=None
    self.last=None
    self.size=0
  
  def isEmpty(self):
    if self.first==None:
      return True
    return False
  
  def insertar(self,token,name):
    aux = self.first
    a = ''
    while aux:
        if aux.token == token:
            a = aux.token
        aux = aux.next
    if  a == token:
        return True  
    else:
        elementoInsertar=Nodo(token,name)
        if self.isEmpty():
            self.first=self.last=elementoInsertar
        else:
            self.last.next=elementoInsertar
            self.last=elementoInsertar
            self.size += 1

  def eliminar(self, token):
    if self.isEmpty():
      print("Error lista vacia")
      return False
    elif self.size>1:
      if self.first.token==token:
        self.first=self.first.next
        self.size-=1
        return True
      else:
        aux=self.first
        while aux.next:
          if aux.next.token == token:
            aux.next=aux.next.next
            self.size-=1
            return True
          aux=aux.next
    else:
      self.first=None
      self.last=None
      self.size-=1
      return True


  def recorrer(self):
    aux=self.first
    while aux:
      print(aux.token,"-->",aux.name,"| ",end="")
      aux=aux.next

  def funcionHash(self, token, tamaño):
    return token % int(tamaño)