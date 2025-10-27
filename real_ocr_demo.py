#!/usr/bin/env python3
"""
真实OCR演示 - 展示完整的OCR工作流程
"""

import os
import json
from deepseek_ocr import DeepSeekOCR

def demo_real_workflow():
    """演示真实的OCR工作流程"""
    print("🎯 真实OCR工作流程演示")
    print("=" * 40)

    # 步骤1：检查API密钥配置
    print("📝 步骤1：检查API密钥配置...")
    api_key = os.getenv("OMNIEDGE_OCR_API_KEY")
    if api_key:
        print("✅ 环境变量中找到API密钥")
        ocr = DeepSeekOCR()
    else:
        print("⚠️  未找到环境变量API密钥，请手动配置")
        print("   方式1: export OMNIEDGE_OCR_API_KEY='your_key'")
        print("   方式2: ocr = DeepSeekOCR(api_key='your_key')")
        print("   方式3: 创建deepseek_ocr_key.txt文件")
        return False

    # 步骤2：检查图片文件
    print("\n📝 步骤2：检查测试图片...")
    if os.path.exists("test_pic.png"):
        print("✅ 找到测试图片: test_pic.png")
    else:
        print("❌ 未找到测试图片")
        return False

    # 步骤3：执行OCR识别
    print("\n📝 步骤3：执行OCR识别...")
    try:
        # 使用默认prompt "OCR"
        print("   使用默认prompt: 'OCR'")
        text = ocr.recognize("test_pic.png")

        if text:
            print(f"✅ 识别成功，共识别 {len(text)} 个字符")
            print(f"📄 识别结果预览: {text[:200]}...")

            # 步骤4：保存结果
            print("\n📝 步骤4：保存识别结果...")

            # 保存为文本文件
            if ocr.save_result(text, "ocr_result.txt"):
                print("✅ 文本文件保存成功: ocr_result.txt")

            # 保存为JSON文件
            if ocr.save_result(text, "ocr_result.json", format="json"):
                print("✅ JSON文件保存成功: ocr_result.json")

            # 步骤5：显示详细结果
            print("\n📝 步骤5：识别结果详情...")
            print("=" * 40)
            print(text)
            print("=" * 40)

            return True
        else:
            print("❌ 识别失败，结果为空")
            return False

    except Exception as e:
        print(f"❌ OCR识别出错: {e}")
        return False

def demo_different_prompts():
    """演示不同prompt的效果"""
    print("\n🎯 不同Prompt效果演示")
    print("=" * 40)

    # 获取API密钥
    api_key = os.getenv("OMNIEDGE_OCR_API_KEY")
    if not api_key:
        print("⚠️  需要配置API密钥才能进行此演示")
        return

    ocr = DeepSeekOCR()

    # 不同的prompt示例
    prompts = [
        ("OCR", "默认OCR识别"),
        ("请识别图片中的所有中文文字", "专注中文识别"),
        ("请识别图片中的所有英文文字", "专注英文识别"),
        ("请识别表格内容并保持格式", "表格识别"),
    ]

    for prompt, description in prompts:
        print(f"\n📝 {description}")
        print(f"   Prompt: {prompt}")
        try:
            text = ocr.recognize("test_pic.png", prompt=prompt)
            if text:
                preview = text[:100] + "..." if len(text) > 100 else text
                print(f"   ✅ 结果: {preview}")
            else:
                print("   ⚠️  识别结果为空")
        except Exception as e:
            print(f"   ❌ 错误: {e}")

def demo_batch_processing():
    """演示批量处理"""
    print("\n🎯 批量处理演示")
    print("=" * 40)

    # 获取API密钥
    api_key = os.getenv("OMNIEDGE_OCR_API_KEY")
    if not api_key:
        print("⚠️  需要配置API密钥才能进行此演示")
        return

    ocr = DeepSeekOCR()

    # 准备多个图片（这里用同一张图片演示）
    image_paths = ["test_pic.png"] * 3  # 模拟3张图片

    print(f"📝 批量处理 {len(image_paths)} 张图片...")
    results = ocr.recognize_batch(image_paths)

    print("\n📊 批量处理结果:")
    for i, result in enumerate(results):
        status = "✅ 成功" if result['success'] else "❌ 失败"
        print(f"   图片{i+1}: {status}")
        if result['success']:
            preview = result['text'][:50] + "..." if result['text'] and len(result['text']) > 50 else result['text']
            print(f"      预览: {preview}")
        else:
            print(f"      错误: {result['error']}")

def show_configuration_guide():
    """显示配置指南"""
    print("\n🎯 API密钥配置指南")
    print("=" * 40)

    print("📋 方法1：环境变量（推荐）")
    print("   export OMNIEDGE_OCR_API_KEY='your_api_key_here'")
    print("   ocr = DeepSeekOCR()  # 自动读取")
    print()

    print("📋 方法2：代码中直接传递")
    print("   ocr = DeepSeekOCR(api_key='your_api_key_here')")
    print()

    print("📋 方法3：配置文件")
    print("   创建 deepseek_ocr_key.txt 文件")
    print("   内容: your_api_key_here")
    print("   ocr = DeepSeekOCR()  # 自动读取")
    print()

    print("🔑 获取API密钥:")
    print("   访问: https://cloud.siliconflow.cn/account/ak")
    print("   注册并获取您的DeepSeek API密钥")

def main():
    """主函数"""
    print("🚀 omniedge-deepseek-ocr 真实使用演示")
    print("=" * 50)

    # 显示配置指南
    show_configuration_guide()

    # 检查是否有API密钥
    api_key = os.getenv("OMNIEDGE_OCR_API_KEY")
    if api_key:
        print(f"\n✅ 检测到API密钥: {api_key[:10]}...{api_key[-10:]}")
        print("开始真实OCR演示...\n")

        # 运行真实演示
        success = demo_real_workflow()

        if success:
            # 其他演示
            demo_different_prompts()
            demo_batch_processing()

    else:
        print("\n⚠️  未检测到API密钥")
        print("请按照上面的指南配置API密钥后重新运行演示")
        print("\n📝 即使没有API密钥，您仍然可以:")
        print("   1. 查看基础使用示例 (python basic_usage_example.py)")
        print("   2. 了解API配置方法")
        print("   3. 查看保存结果功能演示")

if __name__ == "__main__":
    main()