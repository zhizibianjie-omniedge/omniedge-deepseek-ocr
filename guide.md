# omniedge-deepseek-ocr 使用指南

> **作者**: 智子边界(OmniEdge)
> **版本**: 1.0.0
> **PyPI**: https://pypi.org/project/omniedge-deepseek-ocr/

## 📖 简介

omniedge-deepseek-ocr 是一个简单易用的DeepSeek-OCR文字识别模块，专为您提供高效的图片文字识别功能。

## 🚀 快速开始

### 1. 安装包

```bash
pip install omniedge-deepseek-ocr
```

### 2. 配置API密钥

**重要**: 使用前必须配置DeepSeek API密钥！

#### 方法1：环境变量（推荐）
```bash
export OMNIEDGE_OCR_API_KEY="your_api_key_here"
```

#### 方法2：配置文件
在项目目录下创建 `deepseek_ocr_key.txt` 文件：
```
your_api_key_here
```

#### 方法3：代码中直接指定
```python
from omniedge_deepseek_ocr import DeepSeekOCR
ocr = DeepSeekOCR(api_key="your_api_key_here")
```

🔑 **获取API密钥**: https://cloud.siliconflow.cn/account/ak

## 📋 基础使用

### 1. 简单OCR识别

```python
from deepseek_ocr import DeepSeekOCR

# 创建OCR实例
ocr = DeepSeekOCR()

# 识别图片
text = ocr.recognize("image.png")
print(text)
```

### 2. 便捷函数

```python
from deepseek_ocr import recognize_image

# 直接识别
text = recognize_image("image.png")
print(text)
```

## 🔧 高级功能

### 1. 批量处理

```python
from deepseek_ocr import DeepSeekOCR

ocr = DeepSeekOCR()

# 批量识别多张图片
image_paths = ["img1.png", "img2.jpg", "img3.png"]
results = ocr.recognize_batch(image_paths)

for result in results:
    if result["success"]:
        print(f"✅ {result['path']}: {result['text'][:50]}...")
    else:
        print(f"❌ {result['path']}: {result['error']}")
```

### 2. 自定义Prompt

```python
from deepseek_ocr import DeepSeekOCR

ocr = DeepSeekOCR()

# 使用默认prompt
text1 = ocr.recognize("image.png")  # 默认prompt="OCR"

# 使用自定义prompt
text2 = ocr.recognize("image.png", prompt="请识别图片中的中文文字")
text3 = ocr.recognize("image.png", prompt="请识别表格内容并转换为markdown格式")
```

### 3. 保存结果

```python
from deepseek_ocr import DeepSeekOCR

ocr = DeepSeekOCR()
text = ocr.recognize("image.png")

# 保存为文本文件
ocr.save_result(text, "result.txt")

# 保存为JSON文件
ocr.save_result(text, "result.json", format="json")
```

## 🎯 最佳实践

### 推荐的Prompt

经过测试，以下prompt效果最佳：

```python
# 最简单有效
prompt = "OCR"

# 中文识别
prompt = "请识别图片中的中文文字"

# 表格识别
prompt = "请识别表格内容并转换为markdown格式"
```

### 支持的图片格式
- PNG (.png)
- JPEG/JPG (.jpg, .jpeg)
- GIF (.gif)
- BMP (.bmp)
- WebP (.webp)

### 性能优化建议
1. 图片大小建议控制在10MB以内
2. 分辨率建议在300dpi以上
3. 避免过于模糊或有噪点的图片
4. 批量处理时注意API调用频率限制

## ❓ 常见问题

### Q: API调用失败怎么办？
A: 请检查：
1. API密钥是否正确配置
2. 网络连接是否正常
3. 图片格式是否支持
4. 图片文件是否存在
5. API密钥是否有足够的配额

### Q: 识别结果不准确怎么办？
A: 尝试：
1. 使用不同的prompt
2. 提高图片质量和分辨率
3. 确保文字清晰可读
4. 尝试裁剪图片只包含文字部分

### Q: 如何批量处理大量图片？
A: 使用 `recognize_batch()` 方法，注意：
1. 控制并发数量避免超过API限制
2. 添加适当的延迟避免频繁调用
3. 处理失败的图片可以单独重试

### Q: 支持哪些语言？
A: 主要支持中文和英文识别，对中文特别优化。

## 📦 完整示例代码

### 基础完整示例

```python
#!/usr/bin/env python3
"""
omniedge-deepseek-ocr 基础使用示例
"""

import os
from deepseek_ocr import DeepSeekOCR

def main():
    # 配置API密钥
    api_key = os.getenv("OMNIEDGE_OCR_API_KEY")
    if not api_key:
        print("请设置环境变量 OMNIEDGE_OCR_API_KEY")
        return

    # 创建OCR实例
    ocr = DeepSeekOCR()

    # 识别图片
    image_path = "test_pic.png"
    if not os.path.exists(image_path):
        print(f"图片文件不存在: {image_path}")
        return

    try:
        # 执行OCR识别
        text = ocr.recognize(image_path)

        if text:
            print("识别成功!")
            print("识别结果:")
            print("-" * 40)
            print(text)
            print("-" * 40)

            # 保存结果
            ocr.save_result(text, "ocr_result.txt")
            print("结果已保存到: ocr_result.txt")

        else:
            print("识别失败，结果为空")

    except Exception as e:
        print(f"OCR识别出错: {e}")

if __name__ == "__main__":
    main()
```

### 批量处理示例

```python
#!/usr/bin/env python3
"""
批量OCR识别示例
"""

import os
from deepseek_ocr import DeepSeekOCR

def batch_ocr(image_folder):
    """批量识别文件夹中的所有图片"""
    ocr = DeepSeekOCR()

    # 支持的图片格式
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'}

    # 获取所有图片文件
    image_files = []
    for file in os.listdir(image_folder):
        if os.path.splitext(file.lower())[1] in image_extensions:
            image_files.append(os.path.join(image_folder, file))

    print(f"找到 {len(image_files)} 张图片")

    # 批量处理
    results = ocr.recognize_batch(image_files)

    # 处理结果
    success_count = 0
    for result in results:
        if result['success']:
            success_count += 1
            # 保存每个识别结果
            output_name = os.path.splitext(os.path.basename(result['path']))[0] + "_ocr.txt"
            ocr.save_result(result['text'], output_name)
            print(f"✅ {os.path.basename(result['path'])} -> {output_name}")
        else:
            print(f"❌ {os.path.basename(result['path'])}: {result['error']}")

    print(f"\n处理完成: {success_count}/{len(image_files)} 成功")

if __name__ == "__main__":
    batch_ocr("./images")
```

## 📊 测试验证

本目录包含完整的测试示例：

```bash
# 基础使用示例
python basic_usage_example.py

# 真实OCR演示（需要API密钥）
python real_ocr_demo.py
```

## 🔗 相关链接

- **PyPI页面**: https://pypi.org/project/omniedge-deepseek-ocr/
- **API密钥申请**: https://cloud.siliconflow.cn/account/ak
- **作者**: 智子边界(OmniEdge)
- **项目主页**: https://github.com/omniedge/deepseek-ocr

## 📄 许可证

MIT License - 详见 [LICENSE](https://github.com/omniedge/deepseek-ocr/blob/main/LICENSE) 文件

---

**简单、高效、准确的OCR识别方案** 🚀

*由智子边界(OmniEdge)团队开发和维护*