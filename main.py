import torch
n_cudas = torch.cuda.device_count()
print(n_cudas)
for i in range(n_cudas):
    print(torch.cuda.get_device_name(i))