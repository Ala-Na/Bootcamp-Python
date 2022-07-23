from __future__ import division
from vector import Vector

def main():
    print('\nSubject tests')
    print('---')

    # Column vector of shape n * 1
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print('Vector 1:', v1)
    print('Vector 1 tranposed:', v1.T())

    v2 = v1 * 5
    print('Vector 1 * 5:', v2)
    # Expected output:
    # Vector([[0.0], [5.0], [10.0], [15.0]])

    print("")

    # Row vector of shape 1 * n
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print('Vector 1:', v1)
    print('Vector 1 tranposed:', v1.T())

    v2 = v1 * 5
    print('Vector 1 * 5:', v2)
    # Expected output
    # Vector([[0.0, 5.0, 10.0, 15.0]])

    print("")

    v2 = v1 / 2.0
    print('Vector 1 / 2.0:', v2)
    # Expected output
    # Vector([[0.0], [0.5], [1.0], [1.5]])

    #v1 / 0.0
    # Expected ouput
    # ZeroDivisionError: division by zero.

    #2.0 / v1
    # Expected output:
    # NotImplementedError: Division of a scalar by a Vector is not defined here.

    print("")

    # Column vector of shape (n, 1)
    print("Shape of n * 1:", Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
    # Expected output
    # (4,1)
    print("Values of n * 1:", Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    # Expected output
    # [[0.0], [1.0], [2.0], [3.0]]
    # Row vector of shape (1, n)
    print("Shape of 1 * n:", Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
    # Expected output
    # (1,4)
    print("Values of 1 * n:", Vector([[0.0, 1.0, 2.0, 3.0]]).values)
    # Expected output
    # [[0.0, 1.0, 2.0, 3.0]]

    print("")

    # Example 1:
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print("Vector 1 :", v1)
    print("Vector 1 shape:", v1.shape)
    # Expected output:
    (4,1)
    print("Tranposed:", v1.T())
    # Expected output:
    # Vector([[0.0, 1.0, 2.0, 3.0]])
    print("Transposed shape:", v1.T().shape)
    # Expected output:
    # (1,4)

    print("")

    # Example 2:
    v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print("Vector 1 :", v2)
    print("Vector 2 shape:", v2.shape)
    # Expected output:
    # (1,4)
    print("Tranposed:", v2.T())
    # Expected output:
    # Vector([[0.0], [1.0], [2.0], [3.0]])
    print("Transposed shape:", v2.T().shape)
    # Expected output:
    # (4,1)

    print("")

    # Example 1:
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print('Vector 1:', v1)
    print("Vector 2:", v2)
    print('Dot product vector 1 by vector 2:', v1.dot(v2))
    # Expected output:
    # 18.0

    print("")
    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    print('Vector 3:', v3)
    print("Vector 4:", v4)
    print('Dot product vector 3 by vector 4:', v3.dot(v4))
    # Expected output:
    # 13.0
    # /!\ 14.0 and not 13.0 as subject because 1*2 + 4*3 = 14

    print("")
    print(repr(v1))
    # Need to call repr function and not just v1 as suggested by subject
    # Expected output: to see what __repr__() should do
    # [[0.0, 1.0, 2.0, 3.0]]
    print(v1)
    # Expected output: to see what __str__() should do
    # [[0.0, 1.0, 2.0, 3.0]]

if __name__ == "__main__":
    main()
