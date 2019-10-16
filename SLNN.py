import matplotlib.pyplot as plt
import numpy as np
import neurolab as nl 

text = np.loadtxt('doc.txt')
data = text[:, 0:2]
labels = text[:, 2:]

plt.scatter(data[:, 0], data[:, 1])
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.title('Input data') 
plt.show()
plt.close()

dim1_min, dim1_max = data[:, 0].min() , data[:, 0].max()
dim2_min, dim2_max = data[:, 1].min() , data[:, 1].max()
num_output = labels.shape[1]

dim1 = [dim1_min, dim1_max]
dim2 = [dim2_min, dim2_max]

snn = nl.net.newp([dim1, dim2], num_output)

error_progress = snn.train(data, labels, epochs = 100, show = 20, lr = 0.03)
plt.plot(error_progress)
plt.xlabel('epochs')
plt.ylabel('Training error')
plt.title('Training error progression')
plt.grid()

print('Testing data:\n')
testing_data = [[1.5, 3.4], [2.3, 1.9], [7.0, 1.3]]
for i in testing_data:
    print(i, '==>', snn.sim([i])[0])


#Multi-Layer Neural Network
# y = 3x^2 + 5

min_vals = -20
max_vals = 20
num_points = 140

x = np.linspace(min_vals, max_vals, num_points)
y = 3*np.square(x)+5
#Normalise data points (Pre-Processing)
y /= np.linalg.norm(y)

data = x.reshape(num_points, 1)
labels = y.reshape(num_points, 1)

plt.scatter(data, labels)
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.title('Data points')
plt.show()

#Train neural net
nlnn = nl.net.newff([[min_vals, max_vals]], [10,6,1])
nlnn.trainf = nl.train.train_gd
error_progress2 = nlnn.train(data, labels, epochs=2000, show=100, lr=0.01)
plt.plot(error_progress2)
plt.xlabel('epochs')
plt.ylabel('Training error')
plt.title('Training error progression')
plt.grid()

#Test data
output = nlnn.sim(data)
y_pred = output.reshape(num_points)
#Predicted output vs actual values
x_dense = np.linspace(min_vals, max_vals, num_points*2)
y_dense_pred = nlnn.sim(x_dense.reshape(x_dense.size,1)).reshape(x_dense.size)

plt.plot(x_dense, y_dense_pred, '-', x,y, '.', x, y_pred, 'p')
plt.title('Actual vs Predicted')
#Training data further will lead to convergence of the curves
#In DL models more pre-processing needed in real life.
#Optimise results by tweaking paramteres












