# use git with credential manager
# git clone https://github.com/example/repo.git --config credential.helper=manager

"""
To set up a Python virtual environment in Visual Studio Code, you can use the following steps:
Open Visual Studio Code and navigate to your Python project.
Open the Command Palette by pressing Ctrl+Shift+P.
Type “Python: Create Environment” in the search bar and select the command.
Choose the type of environment you want to create (Venv or Conda).
Select the location where you want to create the environment.
Enter a name for your environment and press Enter.
Wait for Visual Studio Code to create the environment.
You can also create a new virtual environment directly in Visual Studio by right-clicking on “Python Environments” in Solution Explorer and selecting “Add Environment”
or selecting “Add Environment” from the environments drop-down list on the Python toolbar 1.
"""

# Step 1: Tensors

import torch

# Construct empty tensor:
x = torch.empty(3, 2)

# Construct tensor with random values:
y = torch.rand(6, 2, dtype=torch.float16)

# Construct tensor with 0s:
z = torch.zeros(2, 5, dtype=torch.long)
# Construct tensor with 1s:
p = torch.ones(2, 2)
# Construct tensor from Python list:
l = torch.tensor([2.01, 1.01])

# Tensor operations:
a = torch.rand(2, 2)
b = torch.rand(2, 2)
# addition:
s = a + b  # or
ss = torch.add(a, b)

# in-place addition:
c = torch.rand(2, 2)
d = torch.rand(2, 2)
d.add_(c)  # all elements of d will be added to c

# subtraction:
su = a - b  # or
suu = torch.sub(a, b)

# multiplication:
m = a * b  # or
mm = torch.mul(a, b)
# in-place multiplication:
b.mul_(a)

# division:
dv = a / b  # or
dvv = torch.div(a, b)


# Slice tensors:
xx = torch.rand(5, 3)

# get all rows and 1st column:
# print(xx[:, 0])
# get row 1 and all columns:
# print(xx[1, :])
# get element from row 1 and column 1:
# print(xx[1, 1])
# with single element tensors, use .item() to get the value as a Python number:
# print(xx[1, 1].item())

# Reshape tensors:
yy = torch.rand(4, 4)
print(yy)
# 1 dimension:
xy = yy.view(16) # number of elements must be the same
print(xy)
xy2 = yy.view(-1, 8) # the size -1 is inferred from other dimensions
print(xy2)
print(xy2.size())
