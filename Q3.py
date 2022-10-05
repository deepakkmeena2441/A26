class user:
    def __init__(self,id,bal):
        self.user_id=id
        self.balance=bal

    def __add__(self,other):   #student.___add___(ram,lakhan)   ram.__Add__(lakhan)
            total_id=self.user_id +other.user_id 
            total_bal=self.balance +other.balance
            syam=user(total_id,total_bal)
            return syam
    def __str__(self):
        return(str(self.user_id)+ ":" +str(self.balance))
    


                              

    
ram=user(101,2000)
lakhan=user(102,1000)
print(ram)
print(lakhan)
syam=ram+lakhan

print(syam)      # syam.__str__()