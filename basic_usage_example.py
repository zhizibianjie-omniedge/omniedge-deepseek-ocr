#!/usr/bin/env python3
"""
omniedge-deepseek-ocr 基础使用示例
"""

# 导入模块
from deepseek_ocr import DeepSeekOCR, recognize_image

def example_1_basic_usage():
    """示例1：基础使用"""
    print("=== 示例1：基础使用 ===")

    # 方法1：直接传递API密钥
    # ocr = DeepSeekOCR(api_key="your_api_key_here")

    # 方法2：使用环境变量（推荐）
    # export OMNIEDGE_OCR_API_KEY="your_api_key_here"
    # ocr = DeepSeekOCR()  # 自动读取环境变量

    # 这里先用测试密钥演示（会失败，但能看到使用方式）
    try:
        ocr = DeepSeekOCR(api_key="test_key_demo")
        print("✅ OCR客户端创建成功")

        # 识别图片
        text = ocr.recognize("test_pic.png")
        if text:
            print(f"识别结果: {text[:100]}...")
        else:
            print("⚠️  识别失败（需要有效的API密钥）")

    except Exception as e:
        print(f"❌ 错误: {e}")
        print("💡 这是因为使用了测试密钥，需要真实API密钥才能工作")

def example_2_convenience_function():
    """示例2：便捷函数使用"""
    print("\n=== 示例2：便捷函数使用 ===")

    try:
        # 一步识别
        text = recognize_image("test_pic.png", api_key="test_key_demo")
        if text:
            print(f"识别结果: {text[:100]}...")
        else:
            print("⚠️  识别失败（需要有效的API密钥）")

    except Exception as e:
        print(f"❌ 错误: {e}")
        print("💡 这是因为使用了测试密钥，需要真实API密钥才能工作")

def example_3_batch_processing():
    """示例3：批量处理"""
    print("\n=== 示例3：批量处理 ===")

    try:
        ocr = DeepSeekOCR(api_key="test_key_demo")

        # 批量识别
        image_paths = ["test_pic.png", "test_pic.png"]  # 重复文件用于演示
        results = ocr.recognize_batch(image_paths)

        for i, result in enumerate(results):
            if result['success']:
                print(f"✅ 文件{i+1}: {result['text'][:50]}...")
            else:
                print(f"❌ 文件{i+1}: {result['error']}")

    except Exception as e:
        print(f"❌ 错误: {e}")
        print("💡 这是因为使用了测试密钥，需要真实API密钥才能工作")

def example_4_save_results():
    """示例4：保存结果"""
    print("\n=== 示例4：保存结果 ===")

    try:
        ocr = DeepSeekOCR(api_key="test_key_demo")

        # 模拟识别结果
        sample_text = "这是示例识别结果内容..."

        # 保存为文本文件
        success1 = ocr.save_result(sample_text, "result.txt")
        print(f"✅ 保存文本文件: {'成功' if success1 else '失败'}")

        # 保存为JSON文件
        success2 = ocr.save_result(sample_text, "result.json", format="json")
        print(f"✅ 保存JSON文件: {'成功' if success2 else '失败'}")

    except Exception as e:
        print(f"❌ 错误: {e}")

def example_5_custom_prompt():
    """示例5：自定义Prompt"""
    print("\n=== 示例5：自定义Prompt ===")

    try:
        ocr = DeepSeekOCR(api_key="test_key_demo")

        # 不同的prompt示例
        prompts = [
            "OCR",  # 默认
            "请识别图片中的中文文字",
            "请识别表格内容并转换为markdown格式",
            "请提取图片中的所有数字"
        ]

        for i, prompt in enumerate(prompts):
            print(f"📝 Prompt {i+1}: {prompt}")
            # text = ocr.recognize("test_pic.png", prompt=prompt)
            # print(f"   结果: {text[:50] if text else '无'}")
            print("   (需要有效API密钥才能执行)")

    except Exception as e:
        print(f"❌ 错误: {e}")

def show_api_config_methods():
    """显示API密钥配置方法"""
    print("\n=== API密钥配置方法 ===")
    print("方法1：直接传递")
    print("  ocr = DeepSeekOCR(api_key='your_api_key')")
    print()
    print("方法2：环境变量（推荐）")
    print("  export OMNIEDGE_OCR_API_KEY='your_api_key'")
    print("  ocr = DeepSeekOCR()  # 自动读取")
    print()
    print("方法3：配置文件")
    print("  创建 deepseek_ocr_key.txt 文件")
    print("  内容: your_api_key")
    print("  ocr = DeepSeekOCR()  # 自动读取")
    print()
    print("🔑 获取API密钥: https://cloud.siliconflow.cn/account/ak")

def main():
    """运行所有示例"""
    print("🚀 omniedge-deepseek-ocr 基础使用示例")
    print("=" * 50)

    show_api_config_methods()

    example_1_basic_usage()
    example_2_convenience_function()
    example_3_batch_processing()
    example_4_save_results()
    example_5_custom_prompt()

    print("\n" + "=" * 50)
    print("📚 更多信息:")
    print("- PyPI页面: https://pypi.org/project/omniedge-deepseek-ocr/")
    print("- 作者: 智子边界(OmniEdge)")
    print("- 支持格式: PNG, JPG, GIF, BMP, WebP")
    print("\n💡 配置有效API密钥后即可正常使用！")

if __name__ == "__main__":
    main()