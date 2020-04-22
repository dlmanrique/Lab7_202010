import unittest
import config
from DataStructures import edge as e
from DataStructures import listiterator as it
from ADT import graph as g
from ADT import queue as q
from ADT import list as lt


class GraphTest (unittest.TestCase):

    def setUp (self):
        pass



    def tearDown (self):
        pass

    def comparenames (self, searchname, element):
        return (searchname == element['key'])

    def comparelst (self, searchname, element):
        return (searchname == element)


    def test_newEdge (self):
        edge = e.newEdge (1,1,1)
        print (edge)


    def test_edgeMethods (self):
        edge = e.newEdge ('Bogota','Cali')

        print (e.either(edge))
        print (e.other(edge, e.either(edge)))
        print (e.weight(edge))


    def test_insertVertex (self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')

        self.assertEqual (g.numVertex(graph), 7)
        lst = g.vertices (graph)
        self.assertEqual (lt.size (lst), 7)

    def test_removeVertex(self):
        graph = g.newGraph(7,self.comparenames)
        
        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')

        

        g.removeVertex(graph,'Bogota')
        g.removeVertex(graph,'Cali')

        n=g.containsVertex(graph, 'Bogota')
        o=g.containsVertex(graph, 'Cali')

        self.assertEqual(False,n)
        self.assertEqual(False,o)

    def test_numVertex(self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        n=g.numVertex(graph)
        lst = g.vertices (graph)
        self.assertEqual (lt.size (lst), n)
        
    def test_numEdges(self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')

        g.addEdge (graph, 'Bogota', 'Yopal')
        g.addEdge (graph, 'Bogota', 'Cali')

        n=g.numEdges(graph)
        lst = g.edges (graph)
        self.assertEqual (lt.size (lst), n)

    def test_addEdges (self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')

        g.addEdge (graph, 'Bogota', 'Yopal')
        g.addEdge (graph, 'Bogota', 'Medellin')
        g.addEdge (graph, 'Bogota', 'Pasto')
        g.addEdge (graph, 'Bogota', 'Cali')
        g.addEdge (graph, 'Yopal', 'Medellin')
        g.addEdge (graph, 'Medellin', 'Pasto')
        g.addEdge (graph, 'Cali', 'Pasto')
        g.addEdge (graph, 'Cali', 'Barranquilla')
        g.addEdge (graph, 'Barranquilla','Manizales')
        g.addEdge (graph, 'Pasto','Manizales')

        self.assertEqual (g.numEdges(graph), 10)
        self.assertEqual (g.numVertex(graph), 7)

        lst = g.vertices (graph)
        self.assertEqual (lt.size (lst), 7)

        lst = g.edges (graph)
        self.assertEqual (lt.size (lst), 10)

        degree = g.degree (graph, 'Bogota')
        self.assertEqual (degree, 4)

        edge = g.getEdge (graph, 'Bogota', 'Medellin')

        lst = g.adjacents (graph, 'Bogota')
        self.assertEqual (lt.size (lst), 4)
    
    def test_adjacents(self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')

        g.addEdge (graph, 'Bogota', 'Yopal')
        g.addEdge (graph, 'Bogota', 'Medellin')
        g.addEdge (graph, 'Bogota', 'Pasto')
        g.addEdge (graph, 'Bogota', 'Cali')
        g.addEdge (graph, 'Yopal', 'Medellin')
        g.addEdge (graph, 'Medellin', 'Pasto')
        g.addEdge (graph, 'Cali', 'Pasto')
        g.addEdge (graph, 'Cali', 'Barranquilla')
        g.addEdge (graph, 'Barranquilla','Manizales')
        g.addEdge (graph, 'Pasto','Manizales')

        lst=g.adjacents(graph,'Bogota')
        self.assertEqual(lt.size(lst),4)
    
    def test_containsVertex(self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        v1 = g.containsVertex(graph,'Cali')
        self.assertEqual (True, v1)
        v2=g.containsVertex(graph,'Tunja')
        self.assertEqual(False,v2)


if __name__ == "__main__":
    unittest.main()
