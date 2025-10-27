# omniedge-deepseek-OCR

[![PyPI version](https://img.shields.io/pypi/v/omniedge-deepseek-ocr.svg)](https://pypi.org/project/omniedge-deepseek-ocr/)
[![Python versions](https://img.shields.io/pypi/pyversions/omniedge-deepseek-ocr.svg)](https://pypi.org/project/omniedge-deepseek-ocr/)
[![License](https://img.shields.io/pypi/l/omniedge-deepseek-ocr.svg)](https://pypi.org/project/omniedge-deepseek-ocr/)
[![Downloads](https://img.shields.io/pypi/dm/omniedge-deepseek-ocr.svg)](https://pypi.org/project/omniedge-deepseek-ocr/)

**作者**: 智子边界(OmniEdge)
**版本**: 1.0.0

简单易用的DeepSeek-OCR文字识别模块，专为您提供高效的图片文字识别功能。

## ✨ 特性

- ✅ **简单易用** - 一行代码即可识别图片文字
- ✅ **中文优化** - 专门针对中文OCR场景优化
- ✅ **批量处理** - 支持多张图片批量识别
- ✅ **多种格式** - 支持PNG、JPG、GIF等常见图片格式
- ✅ **灵活配置** - 支持自定义prompt和参数
- ✅ **完善错误处理** - 网络超时重试、格式验证等

## 🚀 快速开始

### 安装

```bash
pip install omniedge-deepseek-ocr
```

### 配置API密钥

**🎁 新用户福利**: 通过下方邀请链接注册，立即获得 **2000万 Tokens** 免费额度！

[🔗 **注册获取免费API密钥**](https://cloud.siliconflow.cn/i/I2WvYDqu)

> 💡 **注册流程**: 访问链接 → 完成注册 → 获得API密钥 → 开始使用

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
from deepseek_ocr import DeepSeekOCR
ocr = DeepSeekOCR(api_key="your_api_key_here")
```

### 基础使用

```python
from deepseek_ocr import DeepSeekOCR

# 创建OCR实例
ocr = DeepSeekOCR()

# 识别图片
text = ocr.recognize("image.png")
print(text)
```

## 📋 使用示例

### 便捷函数使用

```python
from deepseek_ocr import recognize_image

# 直接识别
text = recognize_image("image.png")
print(text)
```

### 批量处理

```python
from deepseek_ocr import DeepSeekOCR

ocr = DeepSeekOCR()
image_paths = ["img1.png", "img2.jpg", "img3.png"]
results = ocr.recognize_batch(image_paths)

for result in results:
    if result["success"]:
        print(f"✅ {result['path']}: {result['text'][:50]}...")
    else:
        print(f"❌ {result['path']}: {result['error']}")
```

### 自定义Prompt

```python
from deepseek_ocr import DeepSeekOCR

ocr = DeepSeekOCR()

# 使用默认prompt
text1 = ocr.recognize("image.png")  # 默认prompt="OCR"

# 使用自定义prompt
text2 = ocr.recognize("image.png", prompt="请识别图片中的中文文字")
text3 = ocr.recognize("image.png", prompt="请识别表格内容并转换为markdown格式")
```

### 保存结果

```python
from deepseek_ocr import DeepSeekOCR

ocr = DeepSeekOCR()
text = ocr.recognize("image.png")

# 保存为文本文件
ocr.save_result(text, "result.txt")

# 保存为JSON文件
ocr.save_result(text, "result.json", format="json")
```

## 🔧 API参考

### DeepSeekOCR类

#### 构造函数
```python
DeepSeekOCR(api_key=None)
```

**参数**:
- `api_key` (str, optional): API密钥，不提供则自动从环境变量或配置文件读取

#### 方法

##### recognize(image_path, prompt="OCR")
识别单张图片中的文字

**参数**:
- `image_path` (str): 图片文件路径
- `prompt` (str): OCR提示词，默认为"OCR"

**返回**:
- `str` or `None`: 识别出的文字内容

##### recognize_batch(image_paths, prompt="OCR")
批量识别多张图片

**参数**:
- `image_paths` (List[str]): 图片文件路径列表
- `prompt` (str): OCR提示词，默认为"OCR"

**返回**:
- `List[Dict]`: 识别结果列表

##### save_result(text, output_path, format="txt")
保存识别结果到文件

**参数**:
- `text` (str): 要保存的文本内容
- `output_path` (str): 输出文件路径
- `format` (str): 文件格式，"txt"或"json"

**返回**:
- `bool`: 保存是否成功

### 便捷函数

##### recognize_image(image_path, api_key=None, prompt="OCR")
便捷的图片识别函数

**参数**:
- `image_path` (str): 图片文件路径
- `api_key` (str, optional): API密钥
- `prompt` (str): OCR提示词，默认为"OCR"

**返回**:
- `str` or `None`: 识别出的文字内容

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

## 🎁 免费额度

新用户通过邀请链接注册即可获得：

- ✅ **2000万 Tokens** 免费额度
- ✅ 无需信用卡验证
- ✅ 立即开通，立即使用

[🔗 **点击注册获取免费额度**](https://cloud.siliconflow.cn/i/I2WvYDqu)

## 🤝 贡献

我们欢迎所有形式的贡献！

### 如何贡献
1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

### 开发环境设置
```bash
# 克隆仓库
git clone https://github.com/zhizibianjie-omniedge/omniedge-deepseek-ocr.git
cd omniedge-deepseek-ocr

# 安装依赖
pip install -r requirements.txt

# 运行测试
python test_module.py
```

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🔗 相关链接

- **PyPI页面**: https://pypi.org/project/omniedge-deepseek-ocr/
- **GitHub仓库**: https://github.com/zhizibianjie-omniedge/omniedge-deepseek-ocr
- **Gitee仓库**: https://gitee.com/omniedge/omniedge-deepseek-ocr
- **API密钥申请**: https://cloud.siliconflow.cn/i/I2WvYDqu
- **问题反馈**: https://github.com/zhizibianjie-omniedge/omniedge-deepseek-ocr/issues

## 📞 支持

如果您在使用过程中遇到问题，请：
1. 查看本文档的常见问题部分
2. 在GitHub上提交Issue
3. 联系智子边界(OmniEdge)团队

---

**简单、高效、准确的OCR识别方案** 🚀

*由智子边界(OmniEdge)团队开发和维护*