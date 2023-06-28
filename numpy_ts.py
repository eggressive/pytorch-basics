import torch
import numpy as np

# torch to numpy:
a = torch.ones(5)
b = a.numpy()
#print(a)
#print(b)
#print(type(b))

# GPU check (with CPU both a and c will be on CPU):
a.add_(1)
#print(a)
#print(b)

# numpy to torch:
zz = np.ones(5)
#print(zz)
yy = torch.from_numpy(zz) # y and z share the same memory location
#print(yy)
zz = zz + 1
#print(zz)
#print(yy)
# looks like this time the memory location is not shared

# cuda check:
if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones(5, device=device)
    y = torch.ones(5)
    y = y.to(device) # or y = y.cuda()
    z = x + y
    z = z.to("cpu") # or z = z.cpu()
    print(z)
    print(z.numpy())

# requires_grad - gradient calculation (when we have a variable we want to optimize):
g = torch.ones(5, requires_grad=True)
print(g)
