'''
Example adjacency matrix:
   1   2   3   4   5   6
1  0   15  0   7   10  0
2  15  0   9   11  0   9
3  0   9   0   0   12  7
4  7   11  0   0   8   14
5  10  0   12  8   0   8
6  0   9   7   14  8   0

Basic format of Prim's:
1) set first vertice (i.e. 1)
2) find shortest path between 1st vertex & another vertex
3) add new vertex to MST
4) find shortest path between 2 vertices & a 3rd vertice
5) repeat until all vertices have been found
for example: 1 -> 4 (7), 4 -> 5 (8), 5 -> 6 (8), 6 -> 3 (7), 3 -> 2 (9)

One important initial step is to ensure your matrix of vertices is sorted by corresponding edge-length in order to make finding
the new vertex pair with the smallest edge-length simple on the next pass.

Additionally, while implementing Prim's in O(n^2) time is simple, the most difficult part IMO is reducing that to O(ElogV) 
since it requires slightly more nuance & for me involved a fair amount of debugging in the nested loop. In fact, the way I've
implemented it may not be 100% efficient, but I'm choosing to leave time-complexity analysis for when I review this algorithm.

The implementation of the adjacency matric could probably be improved greatly (decidedly not space-efficient & using numpy
is the standard way to implement an AM), but since it's not really the point of this exercise, I'm choosing not to do so (:.

The best part of Prim's algorithm, IMO, is that no matter what your starting vertex is in the tree, your total edge weight
will always be the same!

My code for this algorithm could definitely be cleaner & I would like to re-visit it to prepare for future studying,
but it should still have an acceptable time complexitiy (O(ElogV), where 'E' is the # of edges & 'V' the # of vertices)
since it contains 2 nested loops, but the number of vertices shrinks with each iteration of the loop, resulting in logarithmic growth.
'''

def main():
    matrix = {(1,2): 15, (1,4): 7, (1,5): 10,
                (2,1): 15, (2,3): 9, (2,4): 11, (2,6): 9,
                (3,2): 9, (3,5): 12, (3,6): 7,
                (4,1): 7, (4,2): 11, (4,5): 8, (4,6): 14,
                (5,1): 10, (5,3): 12, (5,4): 8, (5,6): 8,
                (6,2): 9, (6,3): 7, (6,4): 14, (6,5): 8}
    
    # create a sorted list of the matrix's vertex pairs & add the initial node to the MST
    sortedMatrix = sorted(matrix, key=matrix.get)
    mstMatrix = [1]
    totalWeight = 0

    while sortedMatrix != []:
        length = len(sortedMatrix)
        # take the vertex pair of the sorted queue & remove any pairs that have either vertices as 2nd vertex
        # then re-sort the matrix
        i = 0
        currentVertices = sortedMatrix[i]
        while currentVertices[0] not in mstMatrix:
            # search the sorted queue until a pair of vertices whose 1st vertex is in the MST is found
            currentVertices = sortedMatrix[i]
            i += 1
        if mstMatrix == []:
            mstMatrix.append(currentVertices[0])
        # add the 2nd vertex in the pair to the MST & get it's edge-length
        mstMatrix.append(currentVertices[1])
        print(matrix.get(currentVertices))
        # add the edge-length to the total edge weight of the MST
        totalWeight += matrix.get(currentVertices)

        i = 0
        while i < length:
            # go through each element in the sorted matrix & remove any keys w a matching 2nd vertex in both matrices
            if (sortedMatrix[i][1] == currentVertices[0]) or (sortedMatrix[i][1] == currentVertices[1]):
                matrix.pop(sortedMatrix[i])
                sortedMatrix.remove(sortedMatrix[i])
                length -= 1
            else:
                i += 1
    
    print(mstMatrix, totalWeight)

main()
