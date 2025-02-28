import os


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


# 사용할 폴더 경로 입력
folder_path = "C:\\AI_Study\\YAI\\ToyProject_Real\\Electric\\zupythunder_images"
rename_images(folder_path)
