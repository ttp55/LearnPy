# @Time : 2024/12/25 14:52
# @Author : WZG
# --coding:utf-8--
from development import model
import torch

def convert():
    # 加载 PyTorch 模型
    model_path = "E://model/resnet18_38_0.021147585306924.pth"
    modelL = model.MyModel()
    modelL.load_state_dict(torch.load(model_path))
    modelL.eval()
    # 生成一个示例输入
    dummy_input = torch.randn(10, 3, 224, 224)
    # 将模型转换为 ONNX 格式
    torch.onnx.export(model, dummy_input, "model/resnet18.onnx", verbose=True)


if __name__ == '__main__':
    convert()