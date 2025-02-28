import os
from PIL import Image


def rename_images(folder_path):
    # 폴더 내 모든 파일 가져오기
    files = sorted([f for f in os.listdir(folder_path)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    # 파일 이름 변경
    for i, file_name in enumerate(files):
        # 파일 확장자 분리
        _, ext = os.path.splitext(file_name)
        # 새로운 파일명 생성 (0000, 0001, ...)
        new_name = f"{i:04d}.jpg"
        # 원본 경로와 변경할 경로 생성
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # 파일명 변경
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")


def resize_images(input_folder, output_folder, size=(256, 256)):
    # 출력 폴더 생성 (없으면 자동 생성)
    os.makedirs(output_folder, exist_ok=True)

    # 폴더 내 이미지 파일 처리
    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        try:
            # 이미지 열기
            with Image.open(input_path) as img:
                # RGB로 변환 (일부 PNG는 RGBA 채널이 있어서 변환 필요)
                img = img.convert("RGB")
                # 256x256으로 크기 조정
                img_resized = img.resize(size, Image.LANCZOS)
                # 변환된 이미지 저장
                img_resized.save(output_path)
                print(f"Resized: {file_name} -> {output_path}")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")


# Rename 사용시
# folder_path = "C:\\AI_Study\\YAI\\ToyProject_Real\\Fire\\datasets\\person2fire\\testB"
# rename_images(folder_path)


# Resize 사용시
input_folder = "C:\\AI_Study\\YAI\\ToyProject_Real\\Fire\\datasets\\person2fire\\trainB"   # 원본 이미지 폴더 경로
output_folder = "C:\\AI_Study\\YAI\\ToyProject_Real\\Fire\\datasets\\person2fire\\trainB2"  # 변환된 이미지 저장 폴더
resize_images(input_folder, output_folder)
