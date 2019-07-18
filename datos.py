
class Datos(object):
    def __init__(self):
        #self.datos = {}
        
        self.datos = {
            
            "DataA": {
                "name":"One name",
                "Level": "One",
                "Priority": "Highest"
            },
            "DataB": {
                "name":"One nameB",
                "Level": "Two",
                "Priority": "Low"
            }
        }
        
        self.data_r = {}
        
        self.prioridad = {
            "Highest": 5, "High": 4, "Medium": 3, "Low": 2, "Lowest": 1
        }
        
    def add_data(self, d):
        pr = self.prioridad[d['Priority']]
        self.data_r[pr].append(d)
    
    def show(self):
        for i in [5,4,3,2,1]:
            if i in self.data_r:
                print(self.data_r[i])
        
    def ordena_data(self):
        for k in self.datos:
            d = self.datos[k]
            pr = self.prioridad[d['Priority']]
            if pr not in self.data_r:
                self.data_r[pr] = []
            self.data_r[pr].append({k: d})
            
            
if __name__ == "__main__":
    print('-- Datos --')
    dt = Datos()
    dt.ordena_data()
    dt.show()
    
            
    