# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:45:37 2021

@author: louison
"""

from datetime import datetime
from pymongo import MongoClient



if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    hypermarche_db = client['Market']
    Produits = hypermarche_db['Produits']


    prod = {"Produit": "steak",
            "Reference": 'S_12',
            "Prix" : 10,
            "tags": ["mongodb", "python", "pymongo"],
            
            }

    prod1 = {"Produit": "lait",
            "Reference": 'L_12',
            "Prix" : 1,
            "tags": ["mongodb", "python", "pymongo"],
            
            }

    prod2 = {"Produit": "cookies",
            "Reference": 'C_12',
            "Prix" : 2,
            "tags": ["mongodb", "python", "pymongo"],
            
            }

    produit =[prod, prod1, prod2]  

    collection_with_newFields = Produits.aggregate(
        [
            {
                "$addFields":
                    {
                    "_id": None,
                    "totalReactions": {"$sum": "$reactions"}
                    }
            }
        ]
    )
    for agg in collection_with_newFields:
        print(agg)

    print(Produits)
    
    
    
    
    
if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    hypermarche_db = client['Market']
    Commande = hypermarche_db['Commande']


    comm = {"numero_comm": 1,
            "date": datetime.utcnow(),
            "list":['S_12', 13],
            "tags": ["mongodb", "python", "pymongo"],
            
            }

    comm1 = {"numero_comm": 2,
            "date": datetime.utcnow(),
            "list":['L_12', 35],
            "tags": ["mongodb", "python", "pymongo"],
            
            }

    comm2 = {"numero_comm": 3,
            "date": datetime.utcnow(),
            "list":['C_12', 22],
            "tags": ["mongodb", "python", "pymongo"],
            
            }

    commande =[comm, comm1, comm2]  



    print(Commande)   
    


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    hypermarche_db = client['Market']
    Caisse = hypermarche_db['Caisse']


    caisse = {"caisse_id": 1,
            "commande": ['C_12', 18],
            }
    caisse1 = {"caisse_id": 1,
            "commande": ['L_12', 7],
            }
    caisse2 = {"caisse_id": 1,
            "commande": ['L_12', 23],               
            }
    
    Caisse_N=[caisse, caisse1, caisse2]
    
    #caisse.insert(Produits) --> test

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    hypermarche_db = client['Market']
    Stock = hypermarche_db['Stock']
    
    Stock_total={"Stock_total": [prod, 43, prod1, 32, prod2, 76]}
    
    print(Produits)
    