# 贡献指南

感谢您对 omniedge-deepseek-ocr 项目的关注！我们欢迎所有形式的贡献。

## 🤝 如何贡献

### 报告问题
- 使用 [GitHub Issues](https://github.com/zhizibianjie-omniedge/omniedge-deepseek-ocr/issues) 报告bug
- 提供详细的问题描述和复现步骤
- 包含您的环境信息（Python版本、操作系统等）

### 提交功能请求
- 在 Issues 中描述您希望的功能
- 说明使用场景和预期效果
- 欢迎提供设计建议

### 代码贡献
1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 🛠️ 开发环境设置

### 克隆仓库
```bash
git clone https://github.com/zhizibianjie-omniedge/omniedge-deepseek-ocr.git
cd omniedge-deepseek-ocr
```

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行测试
```bash
python test_module.py
```

## 📝 代码规范

### Python代码风格
- 遵循 PEP 8 规范
- 使用 4 个空格缩进
- 行长度限制在 88 字符

### 提交信息格式
```
<类型>: <简短描述>

详细描述
关联issue: #123
```

类型包括：
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

## 📋 文档贡献

### 改进文档
- 修正错误和不准确的地方
- 添加使用示例
- 翻译文档到其他语言

### 添加示例
- 在 `examples/` 目录下添加示例代码
- 包含详细的使用说明
- 确保示例可以直接运行

## 🧪 测试

### 运行测试
```bash
# 运行所有测试
python -m pytest

# 运行特定测试
python -m pytest tests/test_ocr.py
```

### 添加测试
- 为新功能添加单元测试
- 确保测试覆盖边界情况
- 使用有意义的测试名称

## 📤 发布流程

### 版本号规则
遵循语义化版本控制 (SemVer)：
- `MAJOR.MINOR.PATCH`
- 主版本号：不兼容的API修改
- 次版本号：向下兼容的功能性新增
- 修订号：向下兼容的问题修正

### 发布步骤
1. 更新版本号
2. 更新 CHANGELOG.md
3. 创建 Git 标签
4. 构建并上传到 PyPI

## 💬 沟通渠道

- GitHub Issues: 报告问题和功能请求
- GitHub Discussions: 一般讨论和问答
- Email: contact@omniedge.com

## 📄 许可证

通过贡献代码，您同意您的贡献将在 MIT 许可证下授权。

---

感谢您的贡献！🎉