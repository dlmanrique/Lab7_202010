"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
import math
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from datetime import datetime

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    rgraph = g.newGraph(111353,compareByKey)
    catalog = {'reviewGraph':rgraph}    
    return catalog


def addReviewNode (catalog, row):
    """
    Adiciona un nodo para almacenar un libro o usuario 
    """
    if not g.containsVertex(catalog['reviewGraph'], row['SOURCE']):
        g.insertVertex (catalog['reviewGraph'], row['SOURCE'])
    if not g.containsVertex(catalog['reviewGraph'], row['DEST']):
        g.insertVertex (catalog['reviewGraph'], row['DEST'])

def addReviewEdge (catalog, row):
    """
    Adiciona un enlace para almacenar una revisión
    """
    g.addEdge (catalog['reviewGraph'], row['SOURCE'], row['DEST'], row['ARRIVAL_DELAY'])


def countNodesEdges (catalog):
    """
    Retorna la cantidad de nodos y enlaces del grafo de revisiones
    """
    nodes = g.numVertex(catalog['reviewGraph'])
    edges = g.numEdges(catalog['reviewGraph'])

    return nodes,edges

def componentes_conectados(catalog):
    counter = 0
    grafo = catalog['reviewGraph']
    vertices = g.vertices(grafo)
    graph_iter = it.newIterator (vertices)
    m = map.newMap(capacity= 55681,maptype='CHAINING',comparefunction=grafo['comparefunction']) # Se asume que hay 111353 nodos y asi se pone la capacidad de la tabla.
    while (it.hasNext (graph_iter)):
        n = it.next (graph_iter)
        visited_w = map.get(m, n)
        if visited_w == None :
            newDFS_2(grafo,n,m)
            counter += 1
    return counter


# Funciones recicladas

def newDFS_2(grafo, source,revisados):
    """
    Crea una busqueda DFS para un grafo y un vertice origen
    """
    map.put(revisados,source,{'marked':True})
    dfs_2(grafo, source,revisados)
    

def dfs_2 (grafo, v, revisados) :
    adjs = g.adjacents(grafo,v)
    adjs_iter = it.newIterator (adjs)
    while (it.hasNext(adjs_iter)):
        w = it.next (adjs_iter)
        visited_w = map.contains(revisados, w)
        if visited_w == False :
            map.put(revisados, w, {'marked':True})
            dfs_2(grafo, w,revisados)

# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

